import json
from urllib.parse import quote

import requests

from common.log import logUtils as log
from common import generalUtils
from objects import glob
from constants import exceptions

from helpers import config
conf = config.config("config.ini")
server_domain = conf.config["server"]["server-domain"]

#def osuApiRequest(request, params, getFirst=True):
def osuApiRequest(request, params, getFirst=True, checkpp=False):
	"""
	Send a request to osu!api.

	request -- request type, string (es: get_beatmaps)
	params -- GET parameters, without api key or trailing ?/& (es: h=a5b99395a42bd55bc5eb1d2411cbdf8b&limit=10)
	return -- dictionary with json response if success, None if failed or empty response.
	"""
	# Make sure osuapi is enabled
	if not generalUtils.stringToBool(glob.conf.config["osuapi"]["enable"]):
		log.warning("osu!api is disabled")
		return None

	# Api request
	resp = None
	try:
		finalURL = "{}/api/{}?k={}&{}".format(glob.conf.config["osuapi"]["apiurl"], request, glob.conf.config["osuapi"]["apikey"], params)
		log.debug(finalURL)
		resp = requests.get(finalURL, timeout=5).text
		data = json.loads(resp)

		log.debug("len(data) = {} | request + param = {}?k={}&{}".format(len(data), request, glob.conf.config["osuapi"]["apikey"], params))
		#커스텀 비트맵 추가 or 반초 조회 실패
		#반초보다 긁어오는게 없어서 오류남
		#외부에서 osuApiRequest() 요청할 때, pp조회 인자를 하나 파서 기본값 false 박아두고, 와부에서 true 박으면 아래 코드 실행되게 if문 짜기
		#했는데 에러남 ㅅㄱ (!last 명령어)
		#위에 주석 지우기 귀찮다 히히
		#if (checkpp and len(data) <= 0) or data == []:
		if (checkpp and len(data) <= 0):
			log.error("osuapiHelper.py | lets pp oppai? 조회중 반초 요청 실패, Redstar에서 검색")
			finalURL2 = "https://{}/api/v1/{}?{}".format(server_domain, request, params)
			log.info(finalURL2)
			data = json.loads(requests.get(finalURL2, timeout=5).text)
			if data is None:
				data = []

		if data == []:
			finalURL2 = "https://{}/api/v1/{}?{}".format(server_domain, request, params)
			log.info(finalURL2)
			data = json.loads(requests.get(finalURL2, timeout=5).text)
			if data is None:
				data = []

		if getFirst:
			if len(data) >= 1:
				resp = data[0]
			else:
				resp = None
		else:
			resp = data
	finally:
		glob.dog.increment(glob.DATADOG_PREFIX+".osu_api.requests")
		log.debug(str(resp).encode("utf-8"))
		return resp

def getOsuFileFromName(fileName):
	"""
	Send a request to osu! servers to download a .osu file from file name
	Used to update beatmaps

	fileName -- .osu file name to download
	return -- .osu file content if success, None if failed
	"""
	# Make sure osuapi is enabled
	if not generalUtils.stringToBool(glob.conf.config["osuapi"]["enable"]):
		log.warning("osuapi is disabled")
		return None

	response = None
	requestHeaders = {"User-Agent": f"RedstarOSU's lets.py (python request) | https://old.{server_domain}"}
	try:
		URL = "https://b.{}/web/maps/{}".format(server_domain, quote(fileName))
		log.info(f"lets/helpers/osuapiHelper.py/ getOsuFileFromName(fileName) | URL = {URL}")
		req = requests.get(URL, headers=requestHeaders, timeout=30)
		req.encoding = "utf-8"
		response = req.content

		if req.status_code != 200:
			URL = "{}/web/maps/{}".format(glob.conf.config["osuapi"]["apiurl"], quote(fileName))
			log.error(f"b.{server_domain}/web/maps 에러")
			log.info(f"lets/helpers/osuapiHelper.py/ getOsuFileFromName(fileName) | URL = {URL}")
			req = requests.get(URL, headers=requestHeaders, timeout=30)
			req.encoding = "utf-8"
			response = req.content
	finally:
		glob.dog.increment(glob.DATADOG_PREFIX+".osu_api.osu_file_requests")
		return response

def getOsuFileFromID(beatmapID):
	"""
	Send a request to osu! servers to download a .osu file from beatmap ID
	Used to get .osu files for oppai

	beatmapID -- ID of beatmap (not beatmapset) to download
	return -- .osu file content if success, None if failed
	"""
	# Make sure osuapi is enabled
	if not generalUtils.stringToBool(glob.conf.config["osuapi"]["enable"]):
		log.warning("osuapi is disabled")
		return None

	response = None
	requestHeaders = {"User-Agent": f"RedstarOSU's lets.py (python request) | https://old.{server_domain}"}
	try:
		URL = "{}/osu/{}".format(glob.conf.config["osuapi"]["apiurl"], beatmapID)
		log.info(f"lets/helpers/osuapiHelper.py/ getOsuFileFromID(beatmapID) | URL = {URL}")
		req = requests.get(URL, headers=requestHeaders, timeout=20)
		response = req.content
		if response == b'':
			URL = f"https://b.{server_domain}/osu/{beatmapID}"
			log.warning(f"lets/helpers/osuapiHelper.py/ getOsuFileFromID(beatmapID) | URL = {URL}")
			req = requests.get(URL, headers=requestHeaders, timeout=20)
			response = req.content
	finally:
		glob.dog.increment(glob.DATADOG_PREFIX+".osu_api.osu_file_requests")
		return response