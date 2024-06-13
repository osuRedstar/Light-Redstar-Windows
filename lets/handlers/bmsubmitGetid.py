import json
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

import requests


MODULE_NAME = "bmsubmitGetid"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for /web/osu-osz2-bmsubmit-getid.php

	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self):
		statusCode = 400
		data = {"message": "unknown error"}
		try:
			# Check arguments
			if not requestsManager.checkArguments(self.request.arguments, ["u", "h", "s", "b", "z", "vv"]):
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# Get user ID
			username = self.get_argument("u")
			userID = userUtils.getID(username)

			log.info("Requested bmsubmitGetid by {}, id = {}".format(username, userID))

			redstar_last_bids = glob.db.fetchAll("SELECT beatmap_id FROM beatmaps WHERE beatmap_id < 0 AND beatmap_id > -1000000 ORDER BY beatmap_id LIMIT 3")
			data = requests.get("https://osu.ppy.sh/web/osu-osz2-bmsubmit-getid.php?b=0,0,0", headers={"User-Agent": "osu!"}).text
			lines = data.split('\n')
			lines[2] = f"{redstar_last_bids[2]['beatmap_id']},{redstar_last_bids[1]['beatmap_id']},{redstar_last_bids[0]['beatmap_id']}"
			lines[4] = "821059401241"
			data = '\n'.join(lines)

		except Exception as e:
			log.error(e)

		finally:
			self.write(data)