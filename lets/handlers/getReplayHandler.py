import os
import sys
import traceback

import tornado.gen
import tornado.web
from raven.contrib.tornado import SentryMixin

from common.log import logUtils as log
from common.ripple import userUtils
from common.web import requestsManager
from constants import exceptions
from objects import glob
from common.sentry import sentry

MODULE_NAME = "get_replay"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for osu-getreplay.php
	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self):
		try:
			# OOF
			#UsingRelax = False

			# Get request ip
			ip = self.getRequestIP()

			# Check arguments
			if not requestsManager.checkArguments(self.request.arguments, ["c", "h", "c"]):
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# Get arguments
			username = self.get_argument("u")
			password = self.get_argument("h")
			replayID = self.get_argument("c")

			# Login check
			userID = userUtils.getID(username)
			if userID == 0:
				raise exceptions.loginFailedException(MODULE_NAME, userID)
			if not userUtils.checkLogin(userID, password, ip):
				raise exceptions.loginFailedException(MODULE_NAME, username)
			if userUtils.check2FA(userID, ip):
				raise exceptions.need2FAException(MODULE_NAME, username, ip)

			###########################
			UsingStatus = glob.db.fetch("SELECT current_status FROM users_stats WHERE id = %s", [userID])
			log.chat("{} is {} (rx or vn or ap)".format(username, UsingStatus["current_status"]))

			if UsingStatus["current_status"] == "on Relax":
				UsingStatusMsg = "RELAX"
				replayData = glob.db.fetch("SELECT scores_relax.*, users.username AS uname FROM scores_relax LEFT JOIN users ON scores_relax.userid = users.id WHERE scores_relax.id = %s", [replayID])
				fileName = "{}_relax/replay_rx_{}.osr".format(glob.conf.config["server"]["replayspath"], replayID)
			elif UsingStatus["current_status"] == "on AP":
				UsingStatusMsg = "AUTOPILOT"
				replayData = glob.db.fetch("SELECT scores_ap.*, users.username AS uname FROM scores_ap LEFT JOIN users ON scores_ap.userid = users.id WHERE scores_ap.id = %s", [replayID])
				fileName = "{}_ap/replay_ap_{}.osr".format(glob.conf.config["server"]["replayspath"], replayID)
			else:
				UsingStatusMsg = "VANILLA"
				replayData = glob.db.fetch("SELECT scores.*, users.username AS uname FROM scores LEFT JOIN users ON scores.userid = users.id WHERE scores.id = %s", [replayID])
				fileName = "{}/replay_vn_{}.osr".format(glob.conf.config["server"]["replayspath"], replayID)

			# Increment 'replays watched by others' if needed
			if replayData is not None:
				if username != replayData["uname"]:
					userUtils.incrementReplaysWatched(replayData["userid"], replayData["play_mode"])

			# Serve replay
			log.info("[{}] Serving {}".format(UsingStatusMsg, fileName))

			if os.path.isfile(fileName):
				with open(fileName, "rb") as f:
					fileContent = f.read()
				self.write(fileContent)

			else:
				log.warning("Replay {} doesn't exist".format(replayID))
				self.write("")
		except exceptions.invalidArgumentsException:
			pass
		except exceptions.need2FAException:
			pass
		except exceptions.loginFailedException:
			pass