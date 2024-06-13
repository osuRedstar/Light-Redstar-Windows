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


MODULE_NAME = "getBeatmapTopic"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for /web/osu-get-beatmap-topic.php

	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self):
		statusCode = 400
		data = {"message": "unknown error"}
		try:
			#s=0 & vv=2
			# Check arguments
			if not requestsManager.checkArguments(self.request.arguments, ["u", "h", "s", "vv"]):
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# Get user ID
			username = self.get_argument("u")
			userID = userUtils.getID(username)

			log.info("Requested getBeatmapTopic by {}, id = {}".format(username, userID))

			data = "Is submit 2 ???"

		except Exception as e:
			log.error(e)

		finally:
			self.write(data)