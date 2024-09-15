import json
import tornado.gen
import tornado.web

from common.log import logUtils as log
from common.ripple import userUtils
from common.web import requestsManager
from constants import exceptions
from objects import glob
from common.sentry import sentry
import re
from common import generalUtils
import requests

MODULE_NAME = "get_beatmapinfo"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for /web/osu-getbeatmapinfo.php
	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	@sentry.captureTornado
	def asyncGet(self):
		return
	def asyncPost(self):
		try:
			# Check arguments
			if not requestsManager.checkArguments(self.request.arguments, ["u", "h"]):
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# GET parameters
			username = self.get_argument("u")
			password = self.get_argument("h")

			# Login and ban check
			userID = userUtils.getID(username)
			if userID == 0: return
			elif not userUtils.checkLogin(userID, password, self.getRequestIP()):
				return self.set_status(403)

			Bancho_u = glob.conf.config["osuapi"]["bancho_username"]
			Bancho_p = glob.conf.config["osuapi"]["bancho_password"]
			Bancho_p_hashed = generalUtils.stringMd5(Bancho_p)

			data = json.loads(self.request.body)
			cho = requests.get(f"https://osu.ppy.sh/web/osu-getbeatmapinfo.php?u={username}&h={password}", headers={"User-Agent": "osu!"}, json=data).content
			if not cho:
				cho = requests.get(f"https://osu.ppy.sh/web/osu-getbeatmapinfo.php?u={Bancho_u}&h={Bancho_p_hashed}", headers={"User-Agent": "osu!"}, json=data).content
			if cho:
				for d in cho.decode("utf-8").strip("\n").split("\n"):
					d = d.split("|")
					for m in range(4):
						r = glob.db.fetch('''
							SELECT play_mode, mods, accuracy, 300_count, 100_count, 50_count, misses_count
							FROM scores WHERE userid = %s AND beatmap_md5 = %s AND completed = 3 AND play_mode = %s ORDER BY pp DESC LIMIT 1
						''', [userID, d[3], m])
						d[5+m] = generalUtils.getRank(r["play_mode"], r["mods"], r["accuracy"],r["300_count"], r["100_count"], r["50_count"], r["misses_count"]) if r else "N"
					log.info("|".join(d))
					self.write("|".join(d) + "\n")

			#반초 요청으로 변경함
			""" result = []
			for num, filename in enumerate(data["Filenames"]):
				log.info(f"Check {filename}")
				try: #mediaserver's functions.py
					parentheses = filename.count(" (")
					if parentheses == 1:
						# 정규식 패턴, 일반적인 경우
						pattern = r"^(.+) - (.+) \(([^)]+)\) \[([^]]+)\]\.osu$"
						match = re.match(pattern, filename)

						artist = match.group(1)
						title = match.group(2)
						creator = match.group(3)
						version = match.group(4)
					elif parentheses == 0:
						# 정규식 패턴, 제작자 누락된 경우
						pattern = r"^(.+) - (.+) \[([^]]+)\]\.osu$"
						match = re.match(pattern, filename)

						artist = match.group(1)
						title = match.group(2)
						creator = match.group(3)
						version = match.group(4)
					else:
						# 정규식 패턴, 괄호가 하나 더 있어서 에러방지
						pattern = r"^(.+) - (.+) (\([^()]+\)) \(([^()]+)\) \[([^]]+)\]\.osu$"
						match = re.match(pattern, filename)

						artist = match.group(1)
						title = f"{match.group(2)} {match.group(3)}"
						creator = match.group(4)
						version = match.group(5)
				except:
					artist = None
					title = None
					creator = None
					version = None
					log.error("osu filename에서 artist, title, creator, version 추출중 에러")

				# filename에 / 가 들어가면 에러남 (http 요청시 / 가 사라짐)
				sql = '''
					SELECT b.id, b.parent_set_id, b.file_md5, b.diff_name, s.ranked_status
					FROM cheesegull.beatmaps AS b
					JOIN cheesegull.sets AS s ON b.parent_set_id = s.id
					WHERE s.artist = %s AND s.title = %s AND s.creator = %s AND b.diff_name = %s
				'''
				info = glob.db.fetch(sql, [artist, title, creator, version])
				if info is None:
					#특수문자 등등 조회 안되는거 짤라서 조회
					log.warning(f"filename 조회 실패! | 단어별로 짤라서 찾아봄 | {filename}")

					artist_sp = artist.split()
					title_sp = title.split()
					creator_sp = creator.split()
					version_sp = version.split()

					sql_part = '''
						SELECT b.id, b.parent_set_id, b.file_md5, b.diff_name, s.ranked_status
						FROM cheesegull.beatmaps AS b
						JOIN cheesegull.sets AS s ON b.parent_set_id = s.id
						WHERE TRUE
					'''
					param_part = []
					for i, v in enumerate(artist_sp):
						sql_part += " AND s.artist LIKE %s"
						if len(artist_sp) == 1: param_part.append(v)
						elif i == 0 and i != len(artist_sp) - 1: param_part.append(f"{v}%")
						elif i == len(artist_sp) - 1: param_part.append(f"%{v}")
						else: param_part.append(f"%{v}%")
					for i, v in enumerate(title_sp):
						sql_part += " AND s.title LIKE %s"
						if len(title_sp) == 1: param_part.append(v)
						elif i == 0 and i != len(title_sp) - 1: param_part.append(f"{v}%")
						elif i == len(title_sp) - 1: param_part.append(f"%{v}")
						else: param_part.append(f"%{v}%")
					for i, v in enumerate(creator_sp):
						sql_part += " AND s.creator LIKE %s"
						if len(creator_sp) == 1: param_part.append(v)
						elif i == 0 and i != len(creator_sp) - 1: param_part.append(f"{v}%")
						elif i == len(creator_sp) - 1: param_part.append(f"%{v}")
						else: param_part.append(f"%{v}%")
					for i, v in enumerate(version_sp):
						sql_part += " AND b.diff_name LIKE %s"
						if len(version_sp) == 1: param_part.append(v)
						elif i == 0: param_part.append(f"{v}%")
						elif i == len(version_sp) - 1: param_part.append(f"%{v}")
						else: param_part.append(f"%{v}%")
					info = glob.db.fetch(sql_part, param_part)

				if info:
					rank = []
					for m in range(4):
						r = glob.db.fetch('''
							SELECT play_mode, mods, accuracy, 300_count, 100_count, 50_count, misses_count
							FROM scores WHERE userid = %s AND beatmap_md5 = %s AND completed = 3 AND play_mode = %s ORDER BY pp DESC LIMIT 1
						''', [userID, info['file_md5'], m])
						if r is None: rank.append("N")
						else: rank.append(generalUtils.getRank(r["play_mode"], r["mods"], r["accuracy"],r["300_count"], r["100_count"], r["50_count"], r["misses_count"]))
				else: result.append(f"{num}|{-1}|{-1}|beatmap_md5|{-1}|N|N|N|N"); continue
				result.append(f"{num}|{info['id']}|{info['parent_set_id']}|{info['file_md5']}|{info['ranked_status']}|{rank[0]}|{rank[1]}|{rank[2]}|{rank[3]}")

			# '|'를 기준으로 파싱하고 두 번째 숫자를 기준으로 정렬
			result = sorted(result, key=lambda x: int(x.split('|')[1]))
			for r in result: self.write(f"{r}\n") """
		except exceptions.invalidArgumentsException:
			return
		except Exception as e:
			log.error(e)
			self.set_status(500)
			self.write(e)