import json
from urllib.parse import urlencode

import requests
import tornado.gen
import tornado.web

from common.log import logUtils as log
from common.web import requestsManager
from objects import glob


class handler(requestsManager.asyncRequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.engine
	def asyncGet(self):
		self.set_header("Content-Type", "application/json")
		try:
			ss = [i["url"] for i in glob.db.fetchAll("SELECT url FROM seasonal WHERE is_current = 1")]
			self.write(json.dumps(ss, indent=2)) if ss else self.write(json.dumps(requests.get("https://osu.ppy.sh/web/osu-getseasonal.php").json(), indent=2))
		except Exception as e:
			log.error("check-seasonal failed: {}".format(e))
			self.write("")