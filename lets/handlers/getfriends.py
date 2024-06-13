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


MODULE_NAME = "get_friends"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for /web/osu-getfriends.php

	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self):
		statusCode = 400
		data = {"message": "unknown error"}
		try:
			# Check arguments
			if not requestsManager.checkArguments(self.request.arguments, ["u", "h"]):
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# Get user ID
			username = self.get_argument("u")
			userID = userUtils.getID(username)
			password = self.get_arguments("h")

			getFriends = []
			getFriends = glob.db.fetchAll("SELECT user2 FROM users_relationships WHERE user1 = %s", [userID])
			log.info("Requested getFriends by {}, id = {}".format(username, userID))

			result = ""
			ro = ""
			for i in getFriends:
				result += f"{i['user2']}\n"
				ro += f"{i['user2']} "
			log.info(ro)

			#submitModularHandler.py line 168
			#rx_stats 테이블 ranked_score_std -값일시 수정
			#현재 STD rx만 지원함
			from urllib.parse import urlencode
			import requests

			is_minus_std = glob.db.fetch("SELECT id, username, total_score_std, ranked_score_std, pp_std FROM rx_stats WHERE id = %s AND ranked_score_std < 0", [userID])
			if is_minus_std != None:
				log.warning("(로그인 직후) {}, {}의 계정에서 rx_stats 테이블속 ranked_score_std 값이 음수임을 확인함. {}".format(userID, username, is_minus_std["ranked_score_std"]))
				total_ranked_std = glob.db.fetch('SELECT SUM(score) as total FROM scores_relax WHERE userid = %s', [userID])
				
				glob.db.fetch("UPDATE rx_stats SET ranked_score_std = %s WHERE id = %s", [total_ranked_std["total"], userID])
				log.warning("(로그인 직후) {}, {}의 계정에서 rx_stats 테이블 업데이트 완료. {}".format(userID, username, total_ranked_std["total"]))

				annmsg = "Fixed your ranked_score_std (Relax) value being negative.  " + str(is_minus_std["ranked_score_std"]) + " --> " + str(total_ranked_std["total"])
				params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": username, "msg": annmsg})
				requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
				log.warning("(로그인 직후) 인게임 DM전송 완료")

			is_minus_std2 = glob.db.fetch("SELECT id, username, total_score_std, ranked_score_std, pp_std FROM ap_stats WHERE id = %s AND ranked_score_std < 0", [userID])
			if is_minus_std2 != None:
				log.warning("(로그인 직후) {}, {}의 계정에서 ap_stats 테이블속 ranked_score_std 값이 음수임을 확인함. {}".format(userID, username, is_minus_std["ranked_score_std"]))
				total_ranked_std = glob.db.fetch('SELECT SUM(score) as total FROM scores_ap WHERE userid = %s', [userID])
				
				glob.db.fetch("UPDATE ap_stats SET ranked_score_std = %s WHERE id = %s", [total_ranked_std["total"], userID])
				log.warning("(로그인 직후) {}, {}의 계정에서 ap_stats 테이블 업데이트 완료. {}".format(userID, username, total_ranked_std["total"]))

				annmsg = "Fixed your ranked_score_std (Autopilot) value being negative.  " + str(is_minus_std["ranked_score_std"]) + " --> " + str(total_ranked_std["total"])
				params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": username, "msg": annmsg})
				requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
				log.warning("(로그인 직후) 인게임 DM전송 완료")

		except Exception as e:
			log.error(e)

		finally:
			self.write(result)
