import base64
import collections
import json
import sys
import threading
import traceback
from urllib.parse import urlencode
import math

import requests
import tornado.gen
import tornado.web

import secret.achievements.utils
from common import generalUtils
from common.constants import gameModes
from common.constants import mods
from common.log import logUtils as log
from common.ripple import userUtils, scoreUtils
from common.web import requestsManager
from constants import exceptions
from constants import rankedStatuses
from constants.exceptions import ppCalcException
from helpers import aeshelper
from helpers import replayHelper
from helpers import replayHelperRelax
from helpers import replayHelperAutopilot
from helpers import leaderboardHelper
from helpers import leaderboardHelperRelax
from helpers import leaderboardHelperAutopilot
from helpers.generalHelper import zingonify
from objects import beatmap
from objects import glob
from objects import score
from objects import scoreRelax
from objects import scoreAutopilot
from objects import scoreboard
from objects import scoreboardRelax
from objects import scoreboardAutopilot
from objects.charts import BeatmapChart, OverallChart
from secret import butterCake

import string
import random

from helpers import config
conf = config.config("config.ini")
server_domain = conf.config["server"]["server-domain"]

MODULE_NAME = "submit_modular"
class handler(requestsManager.asyncRequestHandler):
	"""
	Handler for /web/osu-submit-modular.php
	"""
	@tornado.web.asynchronous
	@tornado.gen.engine
	#@sentry.captureTornado
	def asyncPost(self):
		newCharts = self.request.uri == "/web/osu-submit-modular-selector.php"
		try:
			# Resend the score in case of unhandled exceptions
			keepSending = True

			# Get request ip
			ip = self.getRequestIP()

			# Print arguments
			if glob.debug:
				requestsManager.printArguments(self)

			# Check arguments
			if not requestsManager.checkArguments(self.request.arguments, ["score", "iv", "pass"]):
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# TODO: Maintenance check

			# Get parameters and IP
			scoreDataEnc = self.get_argument("score")
			iv = self.get_argument("iv")
			password = self.get_argument("pass")
			isX = self.get_argument("x")
			ip = self.getRequestIP()

			# Get bmk and bml (notepad hack check)
			if "bmk" in self.request.arguments and "bml" in self.request.arguments:
				bmk = self.get_argument("bmk")
				bml = self.get_argument("bml")
			else:
				bmk = None
				bml = None

			# Get right AES Key
			if "osuver" in self.request.arguments:
				aeskey = "osu!-scoreburgr---------{}".format(self.get_argument("osuver"))
			else:
				aeskey = "h89f2-890h2h89b34g-h80g134n90133"

			# Get score data
			log.debug("Decrypting score data...")
			scoreData = aeshelper.decryptRinjdael(aeskey, iv, scoreDataEnc, True).split(":")
			if len(scoreData) < 16 or len(scoreData[0]) != 32:
				return
			username = scoreData[1].strip()

			# Login and ban check
			userID = userUtils.getID(username)
			# User exists check
			if userID == 0:
				raise exceptions.loginFailedException(MODULE_NAME, userID)
				
			 # Score submission lock check
			lock_key = "lets:score_submission_lock:{}:{}:{}".format(userID, scoreData[0], int(scoreData[9]))
			if glob.redis.get(lock_key) is not None:
				# The same score score is being submitted and it's taking a lot
				log.warning("Score submission blocked because there's a submission lock in place ({})".format(lock_key))
				return
 
			# Set score submission lock
			log.debug("Setting score submission lock {}".format(lock_key))
			glob.redis.set(lock_key, "1", 120)
 
				
			# Bancho session/username-pass combo check
			if not userUtils.checkLogin(userID, password, ip):
				raise exceptions.loginFailedException(MODULE_NAME, username)
			# 2FA Check
			if userUtils.check2FA(userID, ip):
				raise exceptions.need2FAException(MODULE_NAME, userID, ip)
			# Generic bancho session check
			#if not userUtils.checkBanchoSession(userID):
				# TODO: Ban (see except exceptions.noBanchoSessionException block)
			#	raise exceptions.noBanchoSessionException(MODULE_NAME, username, ip)
			# Ban check
			if userUtils.isBanned(userID):
				raise exceptions.userBannedException(MODULE_NAME, username)
			# Data length check
			if len(scoreData) < 16:
				raise exceptions.invalidArgumentsException(MODULE_NAME)

			# Get restricted
			restricted = userUtils.isRestricted(userID)

			# Get variables for relax
			used_mods = int(scoreData[13])
			UsingRelax = used_mods & 128
			UsingAutopilot = used_mods & 8192

			# Create score object and set its data
			log.info("{} | {} has submitted a score on {}...".format(ip, username, scoreData[0]))
			if UsingRelax:
				s = scoreRelax.score()
			elif UsingAutopilot:
				s = scoreAutopilot.score()
			else:
				s = score.score()
			s.setDataFromScoreData(scoreData)
			s.playerUserID = userID


			if s.completed == -1:
				# Duplicated score
				log.warning("Duplicated score detected, this is normal right after restarting the server")
				return

			# Set score stuff missing in score data
			s.playerUserID = userID

			# Get beatmap info
			beatmapInfo = beatmap.beatmap()
			beatmapInfo.setDataFromDB(s.fileMd5)

			def sendautobanmail():
				log.rap(999, f"has Auto banned {username} ({userID}) | ip = {ip}", True, "lets.py | submitModularHandler.py")

				AuthKey = "" 
				for i in range(16) :
					AuthKey += random.choice(string.ascii_letters + string.digits) # 랜덤한 문자열 하나 선택

				glob.redis.set(f"RealistikPanel:AutoBanMailAuthKey:{userID}", AuthKey, 300)

				r = requests.post(f"https://admin.{server_domain}/sendautobanmail", params={"uid": userID}, headers={"AuthKey": AuthKey, "beatmapInfo": json.dumps({"beatmapInfo": f"{beatmapInfo.songName} {f'+{scoreUtils.readableMods(used_mods)}' if used_mods != 0 else ''} ({round(s.accuracy * 100, 2)}%) {round(s.pp, 2)}pp", "bid": beatmapInfo.beatmapID}, ensure_ascii=False)})
				log.info(f"AutoBanMail = {r.text}")

			#gm = gameModes.getGameModeForDB(s.gameMode)
			gm = gameModes.getGamemodeFull(s.gameMode)
			#(users|rx)_beatmap_playcount 테이블 값 추가, 수정 코드
			if beatmapInfo.beatmapID is not 0:
				if UsingRelax:
					beatmapPlaycount_rx = glob.db.fetch("SELECT id, user_id, beatmap_id, game_mode, playcount FROM rx_beatmap_playcount WHERE user_id = %s AND beatmap_id = %s and game_mode = %s", [userID, beatmapInfo.beatmapID, s.gameMode])
					
					#생성
					if beatmapPlaycount_rx == None:
						glob.db.fetch("INSERT INTO rx_beatmap_playcount (id, user_id, beatmap_id, game_mode, playcount) VALUE (%s, %s, %s, %s, %s)", ["NULL", userID, beatmapInfo.beatmapID, s.gameMode, 1])
						log.chat("RX | {} | INSERT rx_beatmap_playcount 테이블 | userID = {}, BeatmapID = {}".format(gm, userID, beatmapInfo.beatmapID))
						ispass = 1
					#수정
					else:
						plcaID = beatmapPlaycount_rx["id"]
						plca = beatmapPlaycount_rx["playcount"] + 1

						glob.db.fetch("UPDATE rx_beatmap_playcount SET playcount = %s WHERE id = %s", [plca, plcaID])
						log.chat("RX | {} | UPDATE rx_beatmap_playcount 테이블 | userID = {}, BeatmapID = {}".format(gm, userID, beatmapInfo.beatmapID))
				elif UsingAutopilot:
					beatmapPlaycount_ap = glob.db.fetch("SELECT id, user_id, beatmap_id, game_mode, playcount FROM ap_beatmap_playcount WHERE user_id = %s AND beatmap_id = %s and game_mode = %s", [userID, beatmapInfo.beatmapID, s.gameMode])
					
					#생성
					if beatmapPlaycount_ap == None:
						glob.db.fetch("INSERT INTO ap_beatmap_playcount (id, user_id, beatmap_id, game_mode, playcount) VALUE (%s, %s, %s, %s, %s)", ["NULL", userID, beatmapInfo.beatmapID, s.gameMode, 1])
						log.chat("RX | {} | INSERT ap_beatmap_playcount 테이블 | userID = {}, BeatmapID = {}".format(gm, userID, beatmapInfo.beatmapID))
						ispass = 1
					#수정
					else:
						plcaID = beatmapPlaycount_ap["id"]
						plca = beatmapPlaycount_ap["playcount"] + 1

						glob.db.fetch("UPDATE ap_beatmap_playcount SET playcount = %s WHERE id = %s", [plca, plcaID])
						log.chat("RX | {} | UPDATE ap_beatmap_playcount 테이블 | userID = {}, BeatmapID = {}".format(gm, userID, beatmapInfo.beatmapID))	
				else:
					beatmapPlaycount_vn = glob.db.fetch("SELECT id, user_id, beatmap_id, game_mode, playcount FROM users_beatmap_playcount WHERE user_id = %s AND beatmap_id = %s and game_mode = %s", [userID, beatmapInfo.beatmapID, s.gameMode])
					
					#생성
					if beatmapPlaycount_vn == None:
						glob.db.fetch("INSERT INTO users_beatmap_playcount (id, user_id, beatmap_id, game_mode, playcount) VALUE (%s, %s, %s, %s, %s)", ["NULL", userID, beatmapInfo.beatmapID, s.gameMode, 1])
						log.chat("VN | {} | INSERT users_beatmap_playcount 테이블 | userID = {}, BeatmapID = {}".format(gm, userID, beatmapInfo.beatmapID))
						ispass = 1
					#수정
					else:
						plcaID = beatmapPlaycount_vn["id"]
						plca = beatmapPlaycount_vn["playcount"] + 1

						glob.db.fetch("UPDATE users_beatmap_playcount SET playcount = %s WHERE id = %s", [plca, plcaID])
						log.chat("VN | {} | UPDATE users_beatmap_playcount 테이블 | userID = {}, BeatmapID = {}".format(gm, userID, beatmapInfo.beatmapID))
			else:
				log.warning("BeatmapID = {}, users|ap|rx_beatmap_playcount".format(beatmapInfo.beatmapID))

			# Make sure the beatmap is submitted and updated
			#if beatmapInfo.rankedStatus == rankedStatuses.NOT_SUBMITTED or beatmapInfo.rankedStatus == rankedStatuses.NEED_UPDATE or beatmapInfo.rankedStatus == rankedStatuses.UNKNOWN:
			#	log.debug("Beatmap is not submitted/outdated/unknown. Score submission aborted.")
			#	return

			# Check if the ranked status is allowed
			if beatmapInfo.rankedStatus not in glob.conf.extra["_allowed_beatmap_rank"]:
				log.debug("Beatmap's rankstatus is not allowed to be submitted. Score submission aborted.")
				return


			#getfriends.py line 51
			#rx_stats 테이블 ranked_score_std -값일시 수정
			#현재 STD rx만 지원함
			if UsingRelax:
				is_minus_std = glob.db.fetch("SELECT id, username, total_score_std, ranked_score_std, pp_std FROM rx_stats WHERE id = %s AND ranked_score_std < 0", [userID])
				if is_minus_std != None:
					log.warning("{}, {}의 계정에서 rx_stats 테이블속 ranked_score_std 값이 음수임을 확인함. {}".format(userID, username, is_minus_std["ranked_score_std"]))
					total_ranked_std = glob.db.fetch('SELECT SUM(score) as total FROM scores_relax WHERE userid = %s', [userID])
					
					glob.db.fetch("UPDATE rx_stats SET ranked_score_std = %s WHERE id = %s", [total_ranked_std["total"], userID])
					log.warning("{}, {}의 계정에서 rx_stats 테이블 업데이트 완료. {}".format(userID, username, total_ranked_std["total"]))

					annmsg = "Fixed your ranked_score_std (Relax) value being negative.  " + str(is_minus_std["ranked_score_std"]) + " --> " + str(total_ranked_std["total"])
					params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": username, "msg": annmsg})
					requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
					log.warning("인게임 DM전송 완료")
			elif UsingAutopilot:
				is_minus_std = glob.db.fetch("SELECT id, username, total_score_std, ranked_score_std, pp_std FROM ap_stats WHERE id = %s AND ranked_score_std < 0", [userID])
				if is_minus_std != None:
					log.warning("{}, {}의 계정에서 ap_stats 테이블속 ranked_score_std 값이 음수임을 확인함. {}".format(userID, username, is_minus_std["ranked_score_std"]))
					total_ranked_std = glob.db.fetch('SELECT SUM(score) as total FROM scores_ap WHERE userid = %s', [userID])
					
					glob.db.fetch("UPDATE ap_stats SET ranked_score_std = %s WHERE id = %s", [total_ranked_std["total"], userID])
					log.warning("{}, {}의 계정에서 ap_stats 테이블 업데이트 완료. {}".format(userID, username, total_ranked_std["total"]))

					annmsg = "Fixed your ranked_score_std (Autopilot) value being negative.  " + str(is_minus_std["ranked_score_std"]) + " --> " + str(total_ranked_std["total"])
					params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": username, "msg": annmsg})
					requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
					log.warning("인게임 DM전송 완료")

			# Calculate PP
			length = 0
			if s.passed:
				length = userUtils.getBeatmapTime(beatmapInfo.beatmapID)
			else:
				length = math.ceil(int(self.get_argument("ft")) / 1000)

			if UsingRelax: 	
				userUtils.incrementPlaytimeRX(userID, s.gameMode, length)
			elif UsingAutopilot:
				userUtils.incrementPlaytimeAP(userID, s.gameMode, length)
			else:
				userUtils.incrementPlaytime(userID, s.gameMode, length)
			midPPCalcException = None
			try:
				#럽드감지는 lets/common/ripple/userUtils.py에도 있음
				#럽드 확인 & 4번 퀄파 (랭크 되기전 임시 랭크)
				isLoved = glob.db.fetch("SELECT ranked FROM beatmaps WHERE beatmap_id = %s", [beatmapInfo.beatmapID])
				log.chat("pp계산 전 럽드, 퀄파확인 Beatmap_id = {}, (loved = 5, 4번 qualified = 4), result = {}".format(beatmapInfo.beatmapID, isLoved["ranked"]))
				if isLoved["ranked"] == 5 or isLoved["ranked"] == 4:
					#s.pp = 0
					log.chat("럽드 or 퀄파 확인 완료! (pp는 DB에 등록은 됨) {}".format(isLoved["ranked"]))

				s.calculatePP()
			except Exception as e:
				# Intercept ALL exceptions and bypass them.
				# We want to save scores even in case PP calc fails
				# due to some rippoppai bugs.
				# I know this is bad, but who cares since I'll rewrite
				# the scores server again.
				log.error("Caught an exception in pp calculation, re-raising after saving score in db")
				s.pp = 0
				midPPCalcException = e


			# Restrict obvious cheaters
			#특정 userID Restricted 방지
			noRestrictedUsers = [1000, 1001, 1014]
			#Debian(1000), Im Not Debian(1001), anireN Fanboy(1014)
			if userID not in noRestrictedUsers:
				if UsingRelax: 
					if (glob.conf.extra["lets"]["submit"]["max-std-rx-pp"] >= 0 and s.pp >= glob.conf.extra["lets"]["submit"]["max-std-rx-pp"] and s.gameMode == gameModes.STD) and not restricted:
						#userUtils.restrict(userID)
						userUtils.ban(userID)
						userUtils.appendNotes(userID, "RX | Restricted (Banned) due to too high pp gain ({}pp) | bid = {}".format(s.pp, beatmapInfo.beatmapID))
						log.warning("RX | **{}** ({}) has been restricted (Banned) due to too high pp gain **({}pp)** | bid = {}".format(username, userID, s.pp, beatmapInfo.beatmapID), "cm")

						sendautobanmail()
				elif UsingAutopilot: 
					if (glob.conf.extra["lets"]["submit"]["max-std-ap-pp"] >= 0 and s.pp >= glob.conf.extra["lets"]["submit"]["max-std-ap-pp"] and s.gameMode == gameModes.STD) and not restricted:
						#userUtils.restrict(userID)
						userUtils.ban(userID)
						userUtils.appendNotes(userID, "AP | Restricted (Banned) due to too high pp gain ({}pp) | bid = {}".format(s.pp, beatmapInfo.beatmapID))
						log.warning("AP | **{}** ({}) has been restricted (Banned) due to too high pp gain **({}pp)** | bid = {}".format(username, userID, s.pp, beatmapInfo.beatmapID), "cm")

						sendautobanmail()
				else:
					#if (s.pp >= 800 and s.gameMode == gameModes.STD) and not restricted:
					if (s.pp >= glob.conf.extra["lets"]["submit"]["max-std-pp"] and s.gameMode == gameModes.STD) and not restricted:
						#userUtils.restrict(userID)
						userUtils.ban(userID)
						userUtils.appendNotes(userID, "VN | Restricted (Banned) due to too high pp gain ({}pp) | bid = {}".format(s.pp, beatmapInfo.beatmapID))
						log.warning("VN | **{}** ({}) has been restricted (Banned) due to too high pp gain **({}pp)** | bid = {}".format(username, userID, s.pp, beatmapInfo.beatmapID), "cm")

						sendautobanmail()

			# Check notepad hack
			if bmk is None and bml is None:
				# No bmk and bml params passed, edited or super old client
				#log.warning("{} ({}) most likely submitted a score from an edited client or a super old client".format(username, userID), "cm")
				pass
			elif bmk != bml and not restricted:
				# bmk and bml passed and they are different, restrict the user
				userUtils.restrict(userID)
				userUtils.appendNotes(userID, "Restricted due to notepad hack")
				log.warning("**{}** ({}) has been restricted due to notepad hack".format(username, userID), "cm")
				sendautobanmail()
				return
			
			#543번째 줄 에러 방지
			oldPersonalBest = None

			# Right before submitting the score, get the personal best score object (we need it for charts)
			#TODO: 나중에 rx, ap없애보고 잘 동작하나 실험해 보기
			if s.passed and s.oldPersonalBest > 0:
				if UsingRelax:
					oldPersonalBestRank = glob.personalBestCacheRX.get(userID, s.fileMd5)
					if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db through a scoreboard object
						oldScoreboard = scoreboardRelax.scoreboardRelax(username, s.gameMode, beatmapInfo, False)
						#oldScoreboard.setPersonalBest()

						oldScoreboard.setPersonalBestRank()

						oldPersonalBestRank = max(oldScoreboard.personalBestRank, 0)
						oldPersonalBest = scoreRelax.score(s.oldPersonalBest, oldPersonalBestRank)
					else:
					# We have an older personal best. Get its rank (try to get it from cache first)
						oldPersonalBestRank = glob.personalBestCacheRX.get(userID, s.fileMd5)
						if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db through a scoreboard object
							oldScoreboard = scoreboardRelax.scoreboardRelax(username, s.gameMode, beatmapInfo, False)
							#oldScoreboard.setPersonalBest()

							oldScoreboard.setPersonalBestRank()

							oldPersonalBestRank = max(oldScoreboard.personalBestRank, 0)
							oldPersonalBest = scoreRelax.score(s.oldPersonalBest, oldPersonalBestRank)
				elif UsingAutopilot:
					oldPersonalBestRank = glob.personalBestCacheAP.get(userID, s.fileMd5)
					if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db through a scoreboard object
						oldScoreboard = scoreboardAutopilot.scoreboardAutopilot(username, s.gameMode, beatmapInfo, False)
						#oldScoreboard.setPersonalBest()

						oldScoreboard.setPersonalBestRank()

						oldPersonalBestRank = max(oldScoreboard.personalBestRank, 0)
						oldPersonalBest = scoreAutopilot.score(s.oldPersonalBest, oldPersonalBestRank)
					else:
					# We have an older personal best. Get its rank (try to get it from cache first)
						oldPersonalBestRank = glob.personalBestCacheAP.get(userID, s.fileMd5)
						if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db through a scoreboard object
							oldScoreboard = scoreboardAutopilot.scoreboardAutopilot(username, s.gameMode, beatmapInfo, False)
							#oldScoreboard.setPersonalBest()

							oldScoreboard.setPersonalBestRank()

							oldPersonalBestRank = max(oldScoreboard.personalBestRank, 0)
							oldPersonalBest = scoreAutopilot.score(s.oldPersonalBest, oldPersonalBestRank)
				else:
					oldPersonalBestRank = glob.personalBestCache.get(userID, s.fileMd5)
					if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db through a scoreboard object
						oldScoreboard = scoreboard.scoreboard(username, s.gameMode, beatmapInfo, False)
						#oldScoreboard.setPersonalBest()

						oldScoreboard.setPersonalBestRank()

						oldPersonalBestRank = max(oldScoreboard.personalBestRank, 0)
						oldPersonalBest = score.score(s.oldPersonalBest, oldPersonalBestRank)
					else:
					# We have an older personal best. Get its rank (try to get it from cache first)
						oldPersonalBestRank = glob.personalBestCache.get(userID, s.fileMd5)
						if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db through a scoreboard object
							oldScoreboard = scoreboard.scoreboard(username, s.gameMode, beatmapInfo, False)
							#oldScoreboard.setPersonalBest()

							oldScoreboard.setPersonalBestRank()

							oldPersonalBestRank = max(oldScoreboard.personalBestRank, 0)
							oldPersonalBest = score.score(s.oldPersonalBest, oldPersonalBestRank)
			else:
				oldPersonalBestRank = 0
				oldPersonalBest = None
			
			""" #users_beatmap_playcount 추가?
			if UsingRelax:
				RxBeatmapPlaycount = glob.db.fetch("SELECT user_id, beatmap_id, game_mode FROM rx_beatmap_playcount WHERE user_id=%s AND beatmap_id=%s", [userID, beatmapInfo.beatmapID])
				if RxBeatmapPlaycount["user_id"] == userID and RxBeatmapPlaycount["beatmap_id"] == beatmapInfo.beatmapID:
					 """
			""" #users_beatmap_playcount 추가?
			if UsingAutopilot:
				ApBeatmapPlaycount = glob.db.fetch("SELECT user_id, beatmap_id, game_mode FROM ap_beatmap_playcount WHERE user_id=%s AND beatmap_id=%s", [userID, beatmapInfo.beatmapID])
				if ApBeatmapPlaycount["user_id"] == userID and ApBeatmapPlaycount["beatmap_id"] == beatmapInfo.beatmapID:
					 """

			# Save score in db
			s.saveScoreInDB()
				
			# Remove lock as we have the score in the database at this point
			# and we can perform duplicates check through MySQL
			log.debug("Resetting score lock key {}".format(lock_key))
			glob.redis.delete(lock_key)
			
			# Client anti-cheat flags
			'''ignoreFlags = 4
			if glob.debug:
				# ignore multiple client flags if we are in debug mode
				ignoreFlags |= 8
			haxFlags = (len(scoreData[17])-len(scoreData[17].strip())) & ~ignoreFlags
			if haxFlags != 0 and not restricted:
				userHelper.restrict(userID)
				userHelper.appendNotes(userID, "-- Restricted due to clientside anti cheat flag ({}) (cheated score id: {}) | bid = {}".format(haxFlags, s.scoreID, beatmapInfo.beatmapID))
				log.warning("**{}** ({}) has been restricted due clientside anti cheat flag **({})** | bid = {}".format(username, userID, haxFlags, beatmapInfo.beatmapID), "cm")'''

			# สวัสดีฮะ ผมเต้เอ็กเซนไฟไหม้
			if s.score < 0 or s.score > (2 ** 63) - 1:
				userUtils.ban(userID)
				userUtils.appendNotes(userID, "Banned due to negative score (score submitter) | bid = {}".format(beatmapInfo.beatmapID))
				sendautobanmail()

			# Make sure the score is not memed
			if s.gameMode == gameModes.MANIA and s.score > 1000000:
				userUtils.ban(userID)
				userUtils.appendNotes(userID, "Banned due to mania score > 1000000 (score submitter) | bid = {}".format(beatmapInfo.beatmapID))
				sendautobanmail()

			# Ci metto la faccia, ci metto la testa e ci metto il mio cuore
			if ((s.mods & mods.DOUBLETIME) > 0 and (s.mods & mods.HALFTIME) > 0) \
					or ((s.mods & mods.HARDROCK) > 0 and (s.mods & mods.EASY) > 0)\
					or ((s.mods & mods.SUDDENDEATH) > 0 and (s.mods & mods.NOFAIL) > 0):
				userUtils.ban(userID)
				userUtils.appendNotes(userID, "Impossible mod combination {} (score submitter) | bid = {}".format(s.mods, beatmapInfo.beatmapID))
				sendautobanmail()

			# NOTE: Process logging was removed from the client starting from 20180322
			if s.completed == 3 and "pl" in self.request.arguments:
				butterCake.bake(self, s)
				
			# Save replay for all passed scores
			# Make sure the score has an id as well (duplicated?, query error?)
			if s.passed and s.scoreID > 0:
				if UsingRelax:
					# Save the replay if it was provided
					#log.debug("Saving replay ({})...".format(s.scoreID))
					log.chat("Saving replay ({})...".format(s.scoreID))
					replay = self.request.files["score"][0]["body"]
					with open("{}_relax/replay_rx_{}.osr".format(glob.conf.config["server"]["replayspath"], s.scoreID), "wb") as f:
						f.write(replay)
					
					# Send to cono ALL passed replays, even non high-scores
					if glob.conf.config["cono"]["enable"]:
						# We run this in a separate thread to avoid slowing down scores submission,
						# as cono needs a full replay
						threading.Thread(target=lambda: glob.redis.publish(
							"cono:analyze", json.dumps({
								"score_id": s.scoreID,
								"beatmap_id": beatmapInfo.beatmapID,
								"user_id": s.playerUserID,
								"game_mode": s.gameMode,
								"pp": s.pp,
								"replay_data": base64.b64encode(
									replayHelperRelax.buildFullReplay(
										s.scoreID,
										rawReplay=self.request.files["score"][0]["body"]
									)
								).decode(),
							})
						)).start()
					else:
						# Restrict if no replay was provided
						if not restricted:
							userUtils.restrict(userID)
							userUtils.appendNotes(userID, "Restricted due to missing replay while submitting a score "
													  "(most likely he used a score submitter)")
							log.warning("**{}** ({}) has been restricted due to replay not found on map {}".format(
								username, userID, s.fileMd5
							), "cm")
							sendautobanmail()
				elif UsingAutopilot:
					# Save the replay if it was provided
					#log.debug("Saving replay ({})...".format(s.scoreID))
					log.chat("Saving replay ({})...".format(s.scoreID))
					replay = self.request.files["score"][0]["body"]
					with open("{}_ap/replay_ap_{}.osr".format(glob.conf.config["server"]["replayspath"], s.scoreID), "wb") as f:
						f.write(replay)
					
					# Send to cono ALL passed replays, even non high-scores
					if glob.conf.config["cono"]["enable"]:
						# We run this in a separate thread to avoid slowing down scores submission,
						# as cono needs a full replay
						threading.Thread(target=lambda: glob.redis.publish(
							"cono:analyze", json.dumps({
								"score_id": s.scoreID,
								"beatmap_id": beatmapInfo.beatmapID,
								"user_id": s.playerUserID,
								"game_mode": s.gameMode,
								"pp": s.pp,
								"replay_data": base64.b64encode(
									replayHelperAutopilot.buildFullReplay(
										s.scoreID,
										rawReplay=self.request.files["score"][0]["body"]
									)
								).decode(),
							})
						)).start()
					else:
						# Restrict if no replay was provided
						if not restricted:
							userUtils.restrict(userID)
							userUtils.appendNotes(userID, "Restricted due to missing replay while submitting a score "
													  "(most likely he used a score submitter)")
							log.warning("**{}** ({}) has been restricted due to replay not found on map {}".format(
								username, userID, s.fileMd5
							), "cm")
							sendautobanmail()
				else:
					# Save the replay if it was provided
					#log.debug("Saving replay ({})...".format(s.scoreID))
					log.chat("Saving replay ({})...".format(s.scoreID))
					replay = self.request.files["score"][0]["body"]
					with open("{}/replay_vn_{}.osr".format(glob.conf.config["server"]["replayspath"], s.scoreID), "wb") as f:
						f.write(replay)

					# Send to cono ALL passed replays, even non high-scores
					if glob.conf.config["cono"]["enable"]:
						# We run this in a separate thread to avoid slowing down scores submission,
						# as cono needs a full replay
						threading.Thread(target=lambda: glob.redis.publish(
							"cono:analyze", json.dumps({
								"score_id": s.scoreID,
								"beatmap_id": beatmapInfo.beatmapID,
								"user_id": s.playerUserID,
								"game_mode": s.gameMode,
								"pp": s.pp,
								"replay_data": base64.b64encode(
									replayHelper.buildFullReplay(
										s.scoreID,
										rawReplay=self.request.files["score"][0]["body"]
									)
								).decode(),
							})
						)).start()
					else:
						# Restrict if no replay was provided
						if not restricted:
							userUtils.restrict(userID)
							userUtils.appendNotes(userID, "Restricted due to missing replay while submitting a score "
													  "(most likely he used a score submitter)")
							log.warning("**{}** ({}) has been restricted due to replay not found on map {}".format(
								username, userID, s.fileMd5
							), "cm")
							sendautobanmail()

			# Update beatmap playcount (and passcount)
			beatmap.incrementPlaycount(s.fileMd5, s.passed)

			# Let the api know of this score
			if s.scoreID:
				glob.redis.publish("api:score_submission", s.scoreID)

			# Re-raise pp calc exception after saving score, cake, replay etc
			# so Sentry can track it without breaking score submission
			if midPPCalcException is not None:
				raise ppCalcException(midPPCalcException)

			# If there was no exception, update stats and build score submitted panel
			# Get "before" stats for ranking panel (only if passed)
			if s.passed:
				if UsingRelax:
					# Get stats and rank
					oldUserData = glob.userStatsCacheRX.get(userID, s.gameMode)
					oldRank = userUtils.getGameRankRx(userID, s.gameMode)

					# Try to get oldPersonalBestRank from cache
					oldPersonalBestRank = glob.personalBestCacheRX.get(userID, s.fileMd5)
					if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db
						oldScoreboard = scoreboardRelax.scoreboardRelax(username, s.gameMode, beatmapInfo, False)
						#oldScoreboard.setPersonalBest()
						
						oldScoreboard.setPersonalBestRank()

						oldPersonalBestRank = oldScoreboard.personalBestRank if oldScoreboard.personalBestRank > 0 else 0
				elif UsingAutopilot:
					# Get stats and rank
					oldUserData = glob.userStatsCacheAP.get(userID, s.gameMode)
					oldRank = userUtils.getGameRankAp(userID, s.gameMode)

					# Try to get oldPersonalBestRank from cache
					oldPersonalBestRank = glob.personalBestCacheAP.get(userID, s.fileMd5)
					if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db
						oldScoreboard = scoreboardAutopilot.scoreboardAutopilot(username, s.gameMode, beatmapInfo, False)
						#oldScoreboard.setPersonalBest()
						
						oldScoreboard.setPersonalBestRank()

						oldPersonalBestRank = oldScoreboard.personalBestRank if oldScoreboard.personalBestRank > 0 else 0
				else:
					# Get stats and rank
					oldUserData = glob.userStatsCache.get(userID, s.gameMode)
					oldRank = userUtils.getGameRank(userID, s.gameMode)

					# Try to get oldPersonalBestRank from cache
					oldPersonalBestRank = glob.personalBestCache.get(userID, s.fileMd5)
					if oldPersonalBestRank == 0:
						# oldPersonalBestRank not found in cache, get it from db
						oldScoreboard = scoreboard.scoreboard(username, s.gameMode, beatmapInfo, False)
						#oldScoreboard.setPersonalBest()
						
						oldScoreboard.setPersonalBestRank()

						oldPersonalBestRank = oldScoreboard.personalBestRank if oldScoreboard.personalBestRank > 0 else 0

			# Always update users stats (total/ranked score, playcount, level, acc and pp)
			# even if not passed
			log.debug("Updating {}'s stats...".format(username))
			if UsingRelax:	
				userUtils.updateStatsRx(userID, s)
			elif UsingAutopilot:	
				userUtils.updateStatsAp(userID, s)
			else:
				userUtils.updateStats(userID, s)

			# Get "after" stats for ranking panel
			# and to determine if we should update the leaderboard
			# (only if we passed that song)
			if s.passed:
				# Get new stats
				if UsingRelax:
					newUserData = userUtils.getUserStatsRx(userID, s.gameMode)
					glob.userStatsCacheRX.update(userID, s.gameMode, newUserData)
					leaderboardHelperRelax.update(userID, newUserData["pp"], s.gameMode)
					maxCombo = 0
				elif UsingAutopilot:
					newUserData = userUtils.getUserStatsAp(userID, s.gameMode)
					glob.userStatsCacheAP.update(userID, s.gameMode, newUserData)
					leaderboardHelperAutopilot.update(userID, newUserData["pp"], s.gameMode)
					maxCombo = 0
				else:
					newUserData = userUtils.getUserStats(userID, s.gameMode)
					glob.userStatsCache.update(userID, s.gameMode, newUserData)
					leaderboardHelper.update(userID, newUserData["pp"], s.gameMode)
					maxCombo = userUtils.getMaxCombo(userID, s.gameMode)

				# Update leaderboard (global and country) if score/pp has changed
				if s.completed == 3 and newUserData["pp"] != oldUserData["pp"]:
					if UsingRelax:
						leaderboardHelperRelax.update(userID, newUserData["pp"], s.gameMode)
						leaderboardHelperRelax.updateCountry(userID, newUserData["pp"], s.gameMode)
					elif UsingAutopilot:
						leaderboardHelperAutopilot.update(userID, newUserData["pp"], s.gameMode)
						leaderboardHelperAutopilot.updateCountry(userID, newUserData["pp"], s.gameMode)
					else:
						leaderboardHelper.update(userID, newUserData["pp"], s.gameMode)
						leaderboardHelper.updateCountry(userID, newUserData["pp"], s.gameMode)

			# TODO: Update total hits and max combo
			# Update latest activity
			userUtils.updateLatestActivity(userID)

			# IP log
			userUtils.IPLog(userID, ip)

			# Score submission and stats update done
			log.debug("Score submission and user stats update done!")

			# Score has been submitted, do not retry sending the score if
			# there are exceptions while building the ranking panel
			keepSending = True

			# At the end, check achievements
			if s.passed:
				new_achievements = secret.achievements.utils.unlock_achievements(s, beatmapInfo, newUserData)

			# Output ranking panel only if we passed the song
			# and we got valid beatmap info from db
			if beatmapInfo is not None and beatmapInfo != False and s.passed:
				log.debug("Started building ranking panel")

				# Trigger bancho stats cache update
				glob.redis.publish("peppy:update_cached_stats", userID)

				# Get personal best after submitting the score
				if UsingRelax:
					newScoreboard = scoreboardRelax.scoreboardRelax(username, s.gameMode, beatmapInfo, False)
					#newScoreboard.setPersonalBest()

					newScoreboard.setPersonalBestRank()

					personalBestID = newScoreboard.getPersonalBest()
					#assert personalBestID is not None
					assert personalBestID is not None, log.error("520 line personalBestID = {} 'assert personalBestID is not None' ERROR".format(personalBestID))
					currentPersonalBest = scoreRelax.score(personalBestID, newScoreboard.personalBestRank)
				elif UsingAutopilot:
					newScoreboard = scoreboardAutopilot.scoreboardAutopilot(username, s.gameMode, beatmapInfo, False)
					#newScoreboard.setPersonalBest()

					newScoreboard.setPersonalBestRank()

					personalBestID = newScoreboard.getPersonalBest()
					#assert personalBestID is not None
					assert personalBestID is not None, log.error("AP | 520 line personalBestID = {} 'assert personalBestID is not None' ERROR".format(personalBestID))
					currentPersonalBest = scoreAutopilot.score(personalBestID, newScoreboard.personalBestRank)
				else:
					newScoreboard = scoreboard.scoreboard(username, s.gameMode, beatmapInfo, False)
					#newScoreboard.setPersonalBest()

					newScoreboard.setPersonalBestRank()

					personalBestID = newScoreboard.getPersonalBest()
					assert personalBestID is not None
					currentPersonalBest = score.score(personalBestID, newScoreboard.personalBestRank)

				# Get rank info (current rank, pp/score to next rank, user who is 1 rank above us)
				if bool(s.mods & 128): #UsingRelax
					rankInfo = leaderboardHelperRelax.getRankInfo(userID, s.gameMode)
				elif bool(s.mods & 8192): #UsingAutopilot
					rankInfo = leaderboardHelperAutopilot.getRankInfo(userID, s.gameMode)
				else:
					rankInfo = leaderboardHelper.getRankInfo(userID, s.gameMode)

				log.warning("oldPersonalBest = {}".format(oldPersonalBest))

				# Output dictionary
				if newCharts:
					log.debug("Using new charts")
					dicts = [
						collections.OrderedDict([
							("beatmapId", beatmapInfo.beatmapID),
							("beatmapSetId", beatmapInfo.beatmapSetID),
							("beatmapPlaycount", beatmapInfo.playcount + 1),
							("beatmapPasscount", beatmapInfo.passcount + (s.completed == 3)),
							("approvedDate", beatmapInfo.rankingDate)
						]),
						BeatmapChart(
							oldPersonalBest if s.completed == 3 else currentPersonalBest,
							currentPersonalBest if s.completed == 3 else s,
							beatmapInfo.beatmapID,
						),
						OverallChart(
							userID, oldUserData, newUserData, s, new_achievements, oldRank, rankInfo["currentRank"]
						)
					]
				else:
					log.debug("Using old charts")
					dicts = [
						collections.OrderedDict([
							("beatmapId", beatmapInfo.beatmapID),
							("beatmapSetId", beatmapInfo.beatmapSetID),
							("beatmapPlaycount", beatmapInfo.playcount),
							("beatmapPasscount", beatmapInfo.passcount),
							("approvedDate", beatmapInfo.rankingDate)
						]),
						collections.OrderedDict([
							("chartId", "overall"),
							("chartName", "Overall Ranking"),
							("chartEndDate", ""),
							("beatmapRankingBefore", oldPersonalBestRank),
							("beatmapRankingAfter", newScoreboard.personalBestRank),
							("rankedScoreBefore", oldUserData["rankedScore"]),
							("rankedScoreAfter", newUserData["rankedScore"]),
							("totalScoreBefore", oldUserData["totalScore"]),
							("totalScoreAfter", newUserData["totalScore"]),
							("playCountBefore", newUserData["playcount"]),
							("accuracyBefore", float(oldUserData["accuracy"])/100),
							("accuracyAfter", float(newUserData["accuracy"])/100),
							("rankBefore", oldRank),
							("rankAfter", rankInfo["currentRank"]),
							("toNextRank", rankInfo["difference"]),
							("toNextRankUser", rankInfo["nextUsername"]),
							("achievements", ""),
							("achievements-new", secret.achievements.utils.achievements_response(new_achievements)),
							("onlineScoreId", s.scoreID)
						])
					]
				output = "\n".join(zingonify(x) for x in dicts)

				# Some debug messages
				log.debug("Generated output for online ranking screen!")
				log.debug(output)

				#cron.py | 중요! DiscordEmbed() 함수에서 color 항목 일부 동작 안함
				from discord_webhook import DiscordWebhook, DiscordEmbed
				def sendWebhooks(color):
					if color == 31406:
						vnrxmsg = "Relax"
					elif color == 13781460:
						vnrxmsg = "Vanilla"
					elif color == 7065737:
						vnrxmsg = "AutoPilot"

					if used_mods == 0:
						used_mods2 = ""
					elif used_mods != 0:
						used_mods2 = "+" + str(scoreUtils.readableMods(used_mods)) + f" ({used_mods})"

					try:
						beatmap_maxcombo = glob.db.fetch("SELECT max_combo FROM beatmaps WHERE beatmap_md5 = %s", [s.fileMd5])
						beatmap_maxcombo = beatmap_maxcombo["max_combo"]
					except:
						beatmap_maxcombo = "?"
						log.error(f"#1 디코 웹훅 | 비트맵 max_combo 조회 실패! | md5 = {s.fileMd5}")

					if s.gameMode == 2:
						ifFc = "{}x (FC)".format(s.maxCombo) if s.fullCombo else "{0}x/{1}x".format(s.maxCombo, beatmap_maxcombo)
						ctbIfFc = " {{ {0} / {1} / {2} / {3} }}".format(s.c300, s.c100, s.c50, s.cMiss)
					elif s.gameMode != 3:
						ifFc = "{}x (FC)".format(s.maxCombo) if s.fullCombo else "{0}x/{1}x".format(s.maxCombo, beatmap_maxcombo)
					else:
						ifFc = "{}x/{}x (FC)".format(s.maxCombo, beatmap_maxcombo) if s.fullCombo or s.maxCombo == beatmap_maxcombo else "{0}x/{1}x".format(s.maxCombo, beatmap_maxcombo)

					rank = generalUtils.getRank(s.gameMode, s.mods, (s.accuracy * 100),
									s.c300, s.c100, s.c50, s.cMiss)

					try:
						if isLoved["ranked"] == 2:
							ranked_img_url = "https://i.imgur.com/hfdujvi.png"
						elif isLoved["ranked"] == 5:
							ranked_img_url = "https://i.imgur.com/R7dFUL5.png"
						elif isLoved["ranked"] == 3:
							ranked_img_url = "https://i.imgur.com/lqsQe0T.png"
						elif isLoved["ranked"] == 4:
							ranked_img_url = "https://i.imgur.com/lqsQe0T.png"
						elif isLoved["ranked"] == 0:
							ranked_img_url = "https://i.imgur.com/1k2YqGp.png"
						else:
							ranked_img_url = "https://i.imgur.com/1k2YqGp.png"
					except:
						ranked_img_url = "https://i.imgur.com/1k2YqGp.png"

					try:
						if s.gameMode == 0:
							starmsg = str(round(beatmapInfo.starsStd, 2)) + " ⭐"
						elif s.gameMode == 1:
							starmsg = str(round(beatmapInfo.starsTaiko, 2)) + " ⭐"
						elif s.gameMode == 2:
							starmsg = str(round(beatmapInfo.starsCtb, 2)) + " ⭐"
						elif s.gameMode == 3:
							starmsg = str(round(beatmapInfo.starsMania, 2)) + " ⭐"
					except:
						starmsg = str(round(beatmapInfo.starsStd, 2)) + " ⭐"
						log.error(f"sendWebhooks() 함수 starmsg 에러 | STD로 기본 설정 {starmsg}")
					
					URL = glob.conf.config["discord"]["score"]
					webhook = DiscordWebhook(url=URL)
					embed = DiscordEmbed(title="Beatmap link", description=f"{username} ({userID}) #1 on https://{server_domain}/b/{beatmapInfo.beatmapID}", url=f"https://{server_domain}/b/{beatmapInfo.beatmapID}", color=color) #this is giving me discord.py vibes
					embed.set_author(name=f"{username}", url=f"https://{server_domain}/u/{userID}", icon_url=f"https://a.{server_domain}/{userID}") #will rank to random diff but yea
					
					embed.set_thumbnail(url=ranked_img_url)
					#log.warning(f"scoreData = {scoreData}")
					#log.info(f"dir(s) = {dir(s)}")
					#log.info(f"s.accuracy = {round(s.accuracy * 100, 2)}")
					#Webhook_fields.append({"name": "Relax", "value": relax_w, "inline": False})
					if s.gameMode == 2:
						embed.add_embed_field(name=f"[{vnrxmsg}] {gameModes.getGamemodeFull(s.gameMode)}", value=f"{beatmapInfo.songName} {used_mods2} | {s.score:,} | {ifFc} | ({round(s.accuracy * 100, 2)}%, {rank}) {ctbIfFc} | {round(s.pp, 2)}pp | {starmsg}", inline=False)	
					else:
						embed.add_embed_field(name=f"[{vnrxmsg}] {gameModes.getGamemodeFull(s.gameMode)}", value=f"{beatmapInfo.songName} {used_mods2} | ({round(s.accuracy * 100, 2)}%, {rank}) | {s.score:,} | {ifFc} | {round(s.pp, 2)}pp | {starmsg}", inline=False)

					embed.set_image(url=f"https://b.{server_domain}/bg/{beatmapInfo.beatmapID}")
					embed.set_footer(text='lets.py', icon_url=f"https://a.{server_domain}")
					embed.set_timestamp()
					webhook.add_embed(embed)
					print(" * Posting webhook!")
					webhook.execute()

				try:
					if s.gameMode == 0:
						starmsg = f"{str(round(beatmapInfo.starsStd, 2))} star"
					elif s.gameMode == 1:
						starmsg = f"{str(round(beatmapInfo.starsTaiko, 2))} star"
					elif s.gameMode == 2:
						starmsg = f"{str(round(beatmapInfo.starsCtb, 2))} star"
					elif s.gameMode == 3:
						starmsg = f"{str(round(beatmapInfo.starsMania, 2))}star"
				except:
					starmsg = str(round(beatmapInfo.starsStd, 2)) + "star"
					log.error(f"sendWebhooks() 함수 starmsg 에러 | STD로 기본 설정 {starmsg}")

				# send message to #announce if we're rank #1
				annmsg = "This is #1 alert python code (이거 보이면 에러났다는 뜻임)"
				log.error(f"#1 | newScoreboard.personalBestRank = {newScoreboard.personalBestRank} | 1 일때 실행")
				log.error(f"#1 | s.completed = {s.completed} | 3 일때 실행")

				annmsg = "[{}] [https://{}/u/{} {}] achieved rank #{} on [https://osu.{}/b/{} {}] ({}) {}pp {} completed = {} [osu://b/{} osu!direct]".format(
					"RELAX" if UsingRelax else ("AUTOPILOT" if UsingAutopilot else "VANILLA"),
					server_domain,
					userID,
					username.encode().decode("ASCII", "ignore"),
					newScoreboard.personalBestRank,
					server_domain,
					beatmapInfo.beatmapID,
					beatmapInfo.songName.encode().decode("ASCII", "ignore"),
					gameModes.getGamemodeFull(s.gameMode),
					int(s.pp),
					starmsg,
					s.completed,
					beatmapInfo.beatmapID
				)

				if UsingRelax:
					if newScoreboard.personalBestRank == 1 and s.completed == 3 and not restricted:
						params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": "#leaderboard", "msg": annmsg})
						requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
						log.chat("RX #1 메세지 전송됨")
						#디코 웹훅
						try:
							sendWebhooks(color=31406)
						except:
							log.error("RX | #1 디코 웹훅 전송 실패!")

					params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": "#score-submit", "msg": annmsg})
					requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
					log.chat(f"RX #{newScoreboard.personalBestRank} 메세지 전송됨")
				elif UsingAutopilot:
					if newScoreboard.personalBestRank == 1 and s.completed == 3 and not restricted:
						params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": "#leaderboard", "msg": annmsg})
						requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
						log.chat("AP #1 메세지 전송됨")
						#디코 웹훅
						try:
							sendWebhooks(color=7065737)
						except:
							log.error("AP | #1 디코 웹훅 전송 실패!")

					params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": "#score-submit", "msg": annmsg})
					requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
					log.chat(f"RX #{newScoreboard.personalBestRank} 메세지 전송됨")			
				else:
					if newScoreboard.personalBestRank == 1 and s.completed == 3 and not restricted:			
						params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": "#leaderboard", "msg": annmsg})
						requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
						log.chat("VN #1 메세지 전송됨")
						#디코 웹훅
						try:
							sendWebhooks(color=13781460)
						except:
							log.error("VN | #1 디코 웹훅 전송 실패!")

					params = urlencode({"k": glob.conf.config["server"]["apikey"], "to": "#score-submit", "msg": annmsg})
					requests.get("{}/api/v1/fokabotMessage?{}".format(glob.conf.config["server"]["banchourl"], params))
					log.chat(f"VN #{newScoreboard.personalBestRank} 메세지 전송됨")
							
				if UsingRelax:
					server = "Relax"
				elif UsingAutopilot:
					server = "Autopilot"
				else:
					server = "Vanilla"
					
				ppGained = newUserData["pp"] - oldUserData["pp"]
				gainedRanks = oldRank - rankInfo["currentRank"]
				# Write message to client
				self.write(output)
			else:
				if isX and False: return self.write("error: no") #TODO 2배 적용된 플카 재 계산 하고 이 코드 활성화 시키기, ((beatmap_playcount - scores) / 2) + scores
				else:
					# No ranking panel, send just "ok"
					self.write("ok")

			# Send username change request to bancho if needed
			# (key is deleted bancho-side)
			newUsername = glob.redis.get("ripple:change_username_pending:{}".format(userID))
			if newUsername is not None:
				log.debug("Sending username change request for user {} to Bancho".format(userID))
				glob.redis.publish("peppy:change_username", json.dumps({
					"userID": userID,
					"newUsername": newUsername.decode("utf-8")
				}))

			# Datadog stats
			glob.dog.increment(glob.DATADOG_PREFIX+".submitted_scores")

			log.error("submitModularHandler.py try: 마지막 줄")
		except exceptions.invalidArgumentsException:
			pass
		except exceptions.loginFailedException:
			self.write("error: pass")
		except exceptions.need2FAException:
			# Send error pass to notify the user
			# resend the score at regular intervals
			# for users with memy connection
			self.set_status(408)
			self.write("error: 2fa")
		except exceptions.userBannedException:
			self.write("error: ban")
		except exceptions.noBanchoSessionException:
			# We don't have an active bancho session.
			# Don't ban the user but tell the client to send the score again.
			# Once we are sure that this error doesn't get triggered when it
			# shouldn't (eg: bancho restart), we'll ban users that submit
			# scores without an active bancho session.
			# We only log through schiavo atm (see exceptions.py).
			self.set_status(408)
			self.write("error: pass")
		except:
			# Try except block to avoid more errors
			try:
				log.error("Unknown error in {}!\n```{}\n{}```".format(MODULE_NAME, sys.exc_info(), traceback.format_exc()))
				if glob.sentry:
					yield tornado.gen.Task(self.captureException, exc_info=True)
			except:
				pass

			# Every other exception returns a 408 error (timeout)
			# This avoids lost scores due to score server crash
			# because the client will send the score again after some time.
			if keepSending:
				self.set_status(408)
