import struct
import datetime
import json
import io
import sys
import traceback

import tornado.gen
import tornado.web
from raven.contrib.tornado import SentryMixin

from objects import beatmap
from common.constants import gameModes
from common.log import logUtils as log
from common.web import requestsManager
from constants import exceptions
from helpers import osuapiHelper
from objects import glob
from common.sentry import sentry

from common.ripple import userUtils



MODULE_NAME = "replayParserHandler"
class handler(requestsManager.asyncRequestHandler):
    """
    Handler for /web/replayparser

    """
    @tornado.web.asynchronous
    @tornado.gen.engine
    @sentry.captureTornado
    def asyncGet(self):
        html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Replay Parser</title>

    <meta property="og:title" content="RedstarOSU's lets server Replay Parser">
    <meta property="og:description" content="퓊픠">
    <meta property="og:image" content="https://redstar.moe/favicon.ico">
    <meta property="og:url" content="https://old.redstar.moe/web/replayparser">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Replay Parser">
    <meta property="og:locale" content="ko_KR">

    <style>
        .submit, .file {
            border: 0;
            margin: 20px auto;
            text-align: center;
            border: 2px solid #2ecc71;
            padding: 14px 40px;
            outline: none;
            border-radius: 24px;
            transition: 0.25s;
            cursor: pointer;
        }
        .submit:hover, .file:hover {
            background: #2ecc71;
        }
    </style>
</head>
<body style="background: #00FFFF;">
    <form id="formBox" class="box" action="" method="post" enctype="multipart/form-data" style="text-align: center;">
        <label for="file">osr 파일 선택:</label>
        <input class="file" type="file" name="score" accept=".osr">
        <button class="submit" type="submit">업로드</button>
    </form>

    <script>
        //비디오 Resize
        const formResize = document.getElementById("formBox")
        function rs() {
            let width = innerWidth
            let height = innerHeight
            console.log(width, height, `${height / 2.5}px`)
            
            formResize.style.marginTop = `${height / 2.5}px`
        }
        rs()
        window.addEventListener("resize", rs)
    </script>
</body>
</html>
        """
        self.write(html)

    def asyncPost(self):
        dl = True if type(self.get_argument("dl", default=False)) != bool else False
        try:
            scoreDataEnc = self.request.files["score"][0]["body"]
            log.info(f'Parsing Replay File!{" For Download File" if dl else ""} | {self.request.files["score"][0]["filename"]}')

            def dotTicksToUnix(dotnet_ticks):
                base = datetime.datetime(1, 1, 1)
                delta = datetime.timedelta(microseconds=dotnet_ticks/10)
                timestamp = base + delta
                return int(timestamp.timestamp())

            def readULEB128(data):
                result = 0
                shift = 0
                while True:
                    byte = data.read(1)
                    if not byte:
                        raise ValueError("Unexpected end of data while reading ULEB128")
                    byte = ord(byte)
                    result |= (byte & 0x7F) << shift
                    shift += 7
                    if not byte & 0x80:
                        break
                return result

            def unpackString(data):
                indicator = data.read(1)
                if indicator == b"\x00":
                    return ""
                elif indicator == b"\x0b":
                    length = readULEB128(data)
                    return data.read(length).decode('utf-8')
                else:
                    raise ValueError("Invalid string indicator")

            def unpackReplayData(data):
                data = io.BytesIO(data)  # BytesIO 객체 생성
                play_mode = struct.unpack("<B", data.read(1))[0]
                version = struct.unpack("<I", data.read(4))[0]
                beatmap_md5 = unpackString(data)
                username = unpackString(data)
                replay_md5 = unpackString(data)
                count_300 = struct.unpack("<H", data.read(2))[0]
                count_100 = struct.unpack("<H", data.read(2))[0]
                count_50 = struct.unpack("<H", data.read(2))[0]
                gekis_count = struct.unpack("<H", data.read(2))[0]
                katus_count = struct.unpack("<H", data.read(2))[0]
                misses_count = struct.unpack("<H", data.read(2))[0]
                score = struct.unpack("<I", data.read(4))[0]
                max_combo = struct.unpack("<H", data.read(2))[0]
                full_combo = struct.unpack("<B", data.read(1))[0]
                mods = struct.unpack("<I", data.read(4))[0]
                life_bar_graph = unpackString(data)
                time = dotTicksToUnix(struct.unpack("<Q", data.read(8))[0])
                rawReplay = data.read(struct.unpack("<I", data.read(4))[0])
                id = struct.unpack("<Q", data.read(8))[0]

                if dl: return rawReplay
                return json.dumps(
                    {
                        "dlLink": "https://" + self.request.host + self.request.uri + "?dl",
                        "id": id,
                        "play_mode": play_mode,
                        "version": version,
                        "beatmap_md5": beatmap_md5,
                        "username": username,
                        "replay_md5": replay_md5,
                        "300_count": count_300,
                        "100_count": count_100,
                        "50_count": count_50,
                        "gekis_count": gekis_count,
                        "katus_count": katus_count,
                        "misses_count": misses_count,
                        "score": score,
                        "max_combo": max_combo,
                        "full_combo": full_combo,
                        "mods": mods,
                        "life_bar_graph": life_bar_graph,
                        "time": time,
                        "rawReplay": str(rawReplay)
                    }, indent=2
                )

            scoreData = unpackReplayData(scoreDataEnc)
        
        except Exception as e:
            log.error(e)
        finally:
            if dl:
                self.set_header('Content-Type', self.request.files["score"][0]["content_type"])
                self.write(scoreData)
            else:
                self.set_header("Content-Type", "application/json")
                self.write(scoreData)