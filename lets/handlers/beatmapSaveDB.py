import os
import subprocess
import json
import tornado.gen
import tornado.web
import threading

from objects import beatmap
from common.log import logUtils as log
from common.ripple import userUtils
from common.web import requestsManager
from constants import exceptions
from helpers import mapsHelper
from objects import glob
from common.constants import mods
from common.sentry import sentry
from constants import rankedStatuses
import requests
import time

MODULE_NAME = "savedb"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for /letsapi/v1/savedb
	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self):
		server_domain = glob.conf.config["server"]["server-domain"]
		requestHeaders = {"User-Agent": f"RedstarOSU's lets.py (python request) | https://old.{server_domain}"}
		md5 = self.get_argument("md5", None)
		bsid = int(self.get_argument("s", 0))
		q = f"h={md5}" if md5 else f"s={bsid}"
		if not md5 and not bsid: return self.write("md5 or bsid not detected!")

		isExist = {}
		for i in glob.db.fetchAll("SELECT id, rankedby, beatmap_id, beatmap_md5, ranked, ranked_status_freezed FROM beatmaps WHERE beatmap_md5 = %s or beatmapset_id = %s", [md5, bsid]):
			isExist[i["beatmap_md5"]] = {"id": i["id"], "rankedby": i["rankedby"], "ranked": i["ranked"], "ranked_status_freezed": i["ranked_status_freezed"]}

		res = [None] * 4
		def get_main_data():
			threads = []
			def osuApiRequest(q): res[int(q[-1])] = requests.get(f"{glob.conf.config['osuapi']['apiurl']}/api/get_beatmaps?k={glob.conf.config['osuapi']['apikey']}&{q}", timeout=5).json()
			for m in range(4): t = threading.Thread(target=osuApiRequest, args=[f"{q}&a=1&m={m}"]); t.start(); threads.append(t)
			for t in threads: t.join() #모든 쓰레드가 끝날 때까지 대기
			for d in res: #응답을 순서대로 확인
				if d: return d
		mainData = get_main_data()
		
		thrs = []; convertRankedStatus = {-2: rankedStatuses.PENDING, -1: rankedStatuses.PENDING, 0: rankedStatuses.PENDING, 1: rankedStatuses.RANKED, 2: rankedStatuses.APPROVED, 3: rankedStatuses.QUALIFIED, 4: rankedStatuses.LOVED}
		columns = [
			"id", "rankedby", "beatmap_id", "beatmapset_id", "beatmap_md5", "song_name", "file_name",
			"ar", "od", "mode", "difficulty_std", "difficulty_taiko", "difficulty_ctb", "difficulty_mania",
			"max_combo", "hit_length", "bpm", "ranked", "latest_update", "ranked_status_freezed", "pp_100", "pp_99", "pp_98", "pp_95"
		]
		for i, d in enumerate(mainData):
			def save(i, d):
				osu = requests.get(f"https://osu.ppy.sh/osu/{d['beatmap_id']}", timeout=3)
				if osu.status_code != 200 or not osu: log.error(f"{osu.status_code} | 반초에서 .osu 다운 실패"); osu = requests.get(f"https://b.redstar.moe/osu/{d['beatmap_id']}", headers=requestHeaders, timeout=3)
				if osu.status_code == 200 and osu.content:
					with open(mapsHelper.cachedMapPath(d["beatmap_id"]), "wb") as f: f.write(osu.content)

				pps = [0] * 4
				def fixPath(cmd): return cmd.replace("/", "\\") if os.name == "nt" else cmd
				for j, acc in enumerate([100, 99, 98, 95]):
					cmd = fixPath(f'pp/oppai-ng/oppai {mapsHelper.cachedMapPath(d["beatmap_id"])} {acc}% -ojson')
					pps[j] = json.loads(subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("utf-8", errors="ignore")).get("pp", 0)
				params = [
					isExist[d["file_md5"]]["id"] if d["file_md5"] in isExist else None,
					isExist[d["file_md5"]]["rankedby"] if d["file_md5"] in isExist else "Bancho",
					int(d["beatmap_id"]),
					int(d["beatmapset_id"]),
					d["file_md5"],
					f'{d["artist"]} - {d["title"]} [{d["version"]}]'.encode("utf-8", "ignore").decode("utf-8"),
					f'{d["artist"]} - {d["title"]} ({d["creator"]}) [{d["version"]}].osu'.replace("\\", ""),
					float(d["diff_approach"]),
					float(d["diff_overall"]),
					int(d["mode"]),
					float(res[0][i].get("difficultyrating", 0)) if res[0] else 0,
					float(res[1][i].get("difficultyrating", 0)) if res[1] else 0,
					float(next((x for x in (res[2][i].get("difficultyrating"), res[2][i].get("diff_aim")) if x), 0)) if res[2] else 0,
					float(res[3][i].get("difficultyrating", 0)) if res[3] else 0,
					int(d["max_combo"]) if d["max_combo"] else 0,
					int(d["hit_length"]),
					int(float(d["bpm"])) if d["bpm"] else -1,
					isExist[d["file_md5"]]["ranked"] if d["file_md5"] in isExist else convertRankedStatus.get(int(d["approved"]), rankedStatuses.UNKNOWN),
					int(time.time()),
					isExist[d["file_md5"]]["ranked_status_freezed"] if d["file_md5"] in isExist else 2 if convertRankedStatus.get(int(d["approved"]), rankedStatuses.UNKNOWN) in (2, 3, 5) else 0
				] + pps
				glob.db.execute(
					f"INSERT INTO beatmaps ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
					f"ON DUPLICATE KEY UPDATE {', '.join([f'{c} = VALUES({c})' for c in columns])}", params
				)
				fileNameShort = params[6][:32]+"..." if len(params[6]) > 32 else params[6][:-4]
				log.info(f"Saved beatmap {fileNameShort} ({params[4]})")
			t = threading.Thread(target=save, args=[i, d]); t.start(); thrs.append(t)
		for t in thrs: t.join()
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(mainData, indent=2, ensure_ascii=False))