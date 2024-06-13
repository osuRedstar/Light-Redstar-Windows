import os

from common import generalUtils
from common.log import logUtils as log
from constants import exceptions
from helpers import osuapiHelper
from objects import glob

from helpers import config
conf = config.config("config.ini")
server_domain = conf.config["server"]["server-domain"]

def isBeatmap(fileName=None, content=None):
    if fileName is not None:
        with open(fileName, "rb") as f:
            firstLine = f.readline().decode("utf-8-sig").strip()
    elif content is not None:
        try:
            firstLine = content.decode("utf-8-sig").split("\n")[0].strip()
        except IndexError:
            return False
    else:
        raise ValueError("Either `fileName` or `content` must be provided.")
    return firstLine.lower().startswith("osu file format v")

def cacheMap(mapFile, _beatmap):
    # Check if we have to download the .osu file
    download = False
    if not os.path.isfile(mapFile):
        # .osu file doesn't exist. We must download it
        download = True
    else:
        # File exists, check md5
        if generalUtils.fileMd5(mapFile) != _beatmap.fileMD5 or not isBeatmap(mapFile):
            # MD5 don't match, redownload .osu file
            import requests
            param = {'k': glob.conf.config["osuapi"]["apikey"], 'h': generalUtils.fileMd5(mapFile)}
            response = requests.get('https://osu.ppy.sh/api/get_beatmaps', params=param)
            bancho_md5 = response.json()
            param = {'k': glob.conf.config["osuapi"]["apikey"], 'h': _beatmap.fileMD5}
            response = requests.get('https://osu.ppy.sh/api/get_beatmaps', params=param)
            bancho_md5_2 = response.json()
            param = {'h': _beatmap.fileMD5}
            response = requests.get(f'https://{server_domain}/api/v1/get_beatmaps', params=param)
            redstar_md5 = response.json()

            if bancho_md5 != [] and bancho_md5_2 != [] or redstar_md5 == []:
                download = True
    
    # Download .osu file if needed
    if download:
        #log.debug("maps ~> Downloading {} osu file".format(_beatmap.beatmapID))
        log.info("maps ~> Downloading {} osu file".format(_beatmap.beatmapID))

        # Get .osu file from osu servers
        fileContent = osuapiHelper.getOsuFileFromID(_beatmap.beatmapID)

        # Make sure osu servers returned something
        if fileContent is None or not isBeatmap(content=fileContent):
            raise exceptions.osuApiFailException("maps")

        # Delete old .osu file if it exists
        if os.path.isfile(mapFile):
            os.remove(mapFile)

        # Save .osu file
        with open(mapFile, "wb+") as f:
            f.write(fileContent)
    else:
        # Map file is already in folder
        log.debug("maps ~> Beatmap found in cache!")

def cachedMapPath(beatmap_id):
    return "{}/{}.osu".format(glob.conf.config["server"]["beatmapspath"], beatmap_id)
