import os
import datetime

from common import generalUtils
from constants import exceptions, dataTypes
from helpers import binaryHelper, generalHelper
from objects import glob

def buildFullReplay(scoreID=None, scoreData=None, rawReplay=None):
    if all(v is None for v in (scoreID, scoreData)) or all(v is not None for v in (scoreID, scoreData)):
        raise AttributeError("Either scoreID or scoreData must be provided, not neither or both")

    if scoreData is None:
        scoreData = glob.db.fetch(
            "SELECT scores_relax.*, users.username FROM scores_relax LEFT JOIN users ON scores_relax.userid = users.id "
            "WHERE scores_relax.id = %s",
            [scoreID]
        )
    else:
        scoreID = scoreData["id"]
    if scoreData is None or scoreID is None:
        raise exceptions.scoreNotFoundError()

    if rawReplay is None:
        # Make sure raw replay exists
        fileName = "{}_relax/replay_rx_{}.osr".format(glob.conf.config["server"]["replayspath"], scoreID)
        if not os.path.isfile(fileName):
            raise FileNotFoundError()

        # Read raw replay
        with open(fileName, "rb") as f:
            rawReplay = f.read()

    # Calculate missing replay data
    rank = generalUtils.getRank(int(scoreData["play_mode"]), int(scoreData["mods"]), int(scoreData["accuracy"]),
                                int(scoreData["300_count"]), int(scoreData["100_count"]), int(scoreData["50_count"]),
                                int(scoreData["misses_count"]))
    magicHash = generalUtils.stringMd5(
        "{}p{}o{}o{}t{}a{}r{}e{}y{}o{}u{}{}{}".format(int(scoreData["100_count"]) + int(scoreData["300_count"]),
                                                      scoreData["50_count"], scoreData["gekis_count"],
                                                      scoreData["katus_count"], scoreData["misses_count"],
                                                      scoreData["beatmap_md5"], scoreData["max_combo"],
                                                      "True" if int(scoreData["full_combo"]) == 1 else "False",
                                                      scoreData["username"], scoreData["score"], rank,
                                                      scoreData["mods"], "True"))
    # Add headers (convert to full replay)
    fullReplay = binaryHelper.binaryWrite([
        [scoreData["play_mode"], dataTypes.byte],
        [20150414, dataTypes.uInt32],
        [scoreData["beatmap_md5"], dataTypes.string],
        [scoreData["username"], dataTypes.string],
        [magicHash, dataTypes.string],
        [scoreData["300_count"], dataTypes.uInt16],
        [scoreData["100_count"], dataTypes.uInt16],
        [scoreData["50_count"], dataTypes.uInt16],
        [scoreData["gekis_count"], dataTypes.uInt16],
        [scoreData["katus_count"], dataTypes.uInt16],
        [scoreData["misses_count"], dataTypes.uInt16],
        [scoreData["score"], dataTypes.uInt32],
        [scoreData["max_combo"], dataTypes.uInt16],
        [scoreData["full_combo"], dataTypes.byte],
        [scoreData["mods"], dataTypes.uInt32],
        [0, dataTypes.byte],
        [generalHelper.toDotTicks(int(scoreData["time"])), dataTypes.uInt64],
        [rawReplay, dataTypes.rawReplay],
        [0, dataTypes.uInt32],
        [scoreData['id'], dataTypes.uInt64],
    ])

    # Return full replay
    return fullReplay

def returnReplayFileName(scoreID=None, scoreData=None):
    if all(v is None for v in (scoreID, scoreData)) or all(v is not None for v in (scoreID, scoreData)):
        raise AttributeError("Either scoreID or scoreData must be provided, not neither or both")

    if scoreData is None:
        scoreData = glob.db.fetch(
            "SELECT scores_relax.*, users.username FROM scores_relax LEFT JOIN users ON scores_relax.userid = users.id "
            "WHERE scores_relax.id = %s",
            [scoreID]
        )
    else:
        scoreID = scoreData["id"]
    if scoreData is None or scoreID is None:
        raise exceptions.scoreNotFoundError()

    username = scoreData["username"]
    beatmapName = glob.db.fetch("SELECT song_name FROM beatmaps WHERE beatmap_md5 = %s", [scoreData["beatmap_md5"]])
    #date = datetime.datetime.fromtimestamp(int(scoreData["time"])) - datetime.timedelta(microseconds = int(scoreData["time"])/10)
    date = datetime.datetime.fromtimestamp(int(scoreData["time"]))
    fileName = "{} - {} ({})".format(username, beatmapName["song_name"], date.strftime("%Y-%m-%d"))

    return fileName