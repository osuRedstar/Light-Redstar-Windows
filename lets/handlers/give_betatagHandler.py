import os
import sys
import traceback
import string
import time
import hashlib

import tornado.gen
import tornado.web

from common.log import logUtils as log
from common.ripple import userUtils
from common.ripple import passwordUtils
from common.web import requestsManager
from common import generalUtils
from objects import glob
from common.sentry import sentry
import time

MODULE_NAME = "give_betatagHandler"
class handler(requestsManager.asyncRequestHandler):
	"""
	give-betatag http
	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	def asyncGet(self, userID):
		#ap_stats Table 추가
		time.sleep(3)
		try:
			rx_stats = glob.db.fetch("SELECT * FROM rx_stats WHERE id = %s", [userID])
			glob.db.execute("INSERT INTO ap_stats VALUES {}".format(tuple(rx_stats.values())))
			msg = "ap_stats Table Insert Success!!\n\n"
		except:
			ap_userinfo = glob.db.fetch("SELECT * FROM ap_stats WHERE id = %s", [userID])
			if not ap_userinfo:
				msg = "ap_stats Table Insert Fail!!\nPlease report This to Admin\n\n"
			else:
				msg = "ap_stats Table already have\n\n"

		#betatag
		username = glob.db.fetch("SELECT username FROM users WHERE id = %s", [userID])["username"]
		beta_badge_id = glob.db.fetch("SELECT id FROM badges WHERE name = %s", ['Beta Tester'])["id"]

		have_beta_badge = glob.db.fetch("SELECT id, user, badge FROM user_badges WHERE user = %s AND badge = %s", [userID, beta_badge_id])
		if not have_beta_badge:
			glob.db.execute("INSERT INTO user_badges (user, badge) VALUES (%s, %s)", [userID, beta_badge_id])
			msg += f"Success | {username} ({userID}) given Beta Tester ({beta_badge_id})"
			log.debug(msg)
			return self.write(msg)
		else:
			msg += f"Refused | {username} ({userID}) already have Beta Tester ({beta_badge_id}) badge"
			log.warning(msg)
			return self.write(msg)