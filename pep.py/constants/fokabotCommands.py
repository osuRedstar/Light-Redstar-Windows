import json
import random
import re
import threading

import requests
import time

from common import generalUtils
from common.constants import mods
from common.log import logUtils as log
from common.ripple import userUtils, scoreUtils
from constants import exceptions, slotStatuses, matchModModes, matchTeams, matchTeamTypes, matchScoringTypes
from common.constants import gameModes
from common.constants import privileges
from constants import serverPackets
from helpers import aobaHelper
from helpers import systemHelper
from objects import fokabot
from objects import glob
from helpers import chatHelper as chat
from common.web import cheesegull
from datetime import datetime
from helpers import configHelper

conf = configHelper.config("config.ini")
bancho_api_key = conf.config["osu"]["apikey"]
server_domain = conf.config["server"]["server-domain"]
letsapiurl = conf.config["server"]["letsapiurl"].rstrip("/")

def userDomainCheck():
	try:
		userDomain = re.sub(r"^c\d*\.|^ce\.", "", glob.self.request.host)
		return server_domain if userDomain == server_domain else userDomain
	except Exception as e: print(e); return server_domain

# Redstar, catboy, 네리냥, catboy, 치무, 블켓, 사요봇, 비트,
def redstarMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://redstar.moe/d/{bsid} {sn}] from Redstar, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)

def catboyMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://catboy.best/d/{bsid} {sn}] from Redstar, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)

def nerinyanMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://nerinyan.moe/d/{bsid} {sn}] from Nerinyan, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)

def catboyMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://catboy.best/d/{bsid} {sn}] from catboy, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)

def chimuMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://chimu.moe/d/{bsid} {sn}] from chimu, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)	

# 실 사용은 chimu
def bloodcatMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://chimu.moe/d/{bsid} {sn}] from Bloodcat, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)

def sayobotMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://txy1.sayobot.cn/beatmaps/download/full/{bsid} {sn}] from sayobot, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)	

def beatconnectMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://beatconnect.io/b/{bsid} {sn}] from Beatconnect, or [osu://dl/{bsid} osu!direct]".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)
	
def mirrorMessage(beatmapID):
	beatmap = glob.db.fetch("SELECT song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
	if beatmap is None:
		log.error(f"{beatmapID} cheesegull에서 곡 이름 조회함")
		sql = '''
			SELECT CONCAT(s.artist, ' - ', s.title, ' [', b.diff_name, ']') AS song_name, s.id AS beatmapset_id
			FROM cheesegull.sets AS s
			JOIN cheesegull.beatmaps AS b ON s.id = b.parent_set_id
			WHERE b.id = %s
		'''
		beatmap = glob.db.fetch(sql, [beatmapID])
		if beatmap is None:
			return "Sorry, I'm not able to provide a download link for this map :("
	return "Download [https://osu.ppy.sh/d/{bsid} {sn}] from [https://redstar.moe/d/{bsid} Redstar], [https://nerinyan.moe/d/{bsid} NeriNyan], [https://catboy.best/d/{bsid} catboy] [https://chimu.moe/d/{bsid} chimu], [https://chimu.moe/d/{bsid} Bloodcat], [https://txy1.sayobot.cn/beatmaps/download/full/{bsid} sayobot], [https://beatconnect.io/b/{bsid} Beatconnect] or [osu://dl/{bsid} osu!direct].".format(
		bsid = beatmap["beatmapset_id"],
		sn = beatmap["song_name"]
	)
	
"""
Commands callbacks

Must have fro, chan and messages as arguments
:param fro: username of who triggered the command
:param chan: channel"(or username, if PM) where the message was sent
:param message: list containing arguments passed from the message
				[0] = first argument
				[1] = second argument
				. . .

return the message or **False** if there's no response by the bot
TODO: Change False to None, because False doesn't make any sense
"""
def instantRestart(fro, chan, message):
	glob.streams.broadcast("main", serverPackets.notification("We are restarting Bancho. Be right back!"))
	systemHelper.scheduleShutdown(0, True, delay=5)
	return False

def faq(fro, chan, message):
	# TODO: Unhardcode this
	""" messages = {
		"rules": "Please make sure to check (Debian's rules)[https://debian.moe/doc/rules].",
		"swearing": "Please don't abuse swearing",
		"spam": "Please don't spam",
		"offend": "Please don't offend other players",
		"github": "(Debian's Github page!)[https://github.com/DebianOSU]",
		"discord": "(Join Debian Discord!)[https://discord.gg/nQBfTTe]",
		"changelog": "Check the (changelog)[https://debian.moe/changelog] !",
		"english": "Please keep this channel in english.",
		"topic": "Can you please drop the topic and talk about something else?",
		"lines": "Please try to keep your sentences on a single line to avoid getting silenced."
	} """
	messages = {
		"rules": f"Please make sure to check (Redstar's rules)[https://{server_domain}/doc/rules].",
		"swearing": "Please don't abuse swearing",
		"spam": "Please don't spam",
		"offend": "Please don't offend other players",
		"github": "(Debian's Github page!)[https://github.com/osuRedstar]",
		"discord": f"(Join Debian Discord!)[https://discord.{server_domain}]",
		"changelog": f"Check the (changelog)[https://{server_domain}/changelog] !",
		"english": "Please keep this channel in english.",
		"topic": "Can you please drop the topic and talk about something else?",
		"lines": "Please try to keep your sentences on a single line to avoid getting silenced."
	}
	key = message[0].lower()
	if key not in messages:
		return False
	return messages[key]

def roll(fro, chan, message):
	maxPoints = 100
	if len(message) >= 1:
		if message[0].isdigit() and int(message[0]) > 0:
			maxPoints = int(message[0])

	points = random.randrange(0,maxPoints)
	return "{} rolls {} points!".format(fro, str(points))

#def ask(fro, chan, message):
#	return random.choice(["yes", "no", "maybe"])

def alert(fro, chan, message):
	msg = ' '.join(message[:]).strip()
	if not msg:
		return False
	glob.streams.broadcast("main", serverPackets.notification(msg))
	chat.sendMessage(glob.BOT_NAME, "#announce", msg)
	return False

def announce(fro, chan, message):
	msg = ' '.join(message[:]).strip()
	if not msg:
		return False
	chat.sendMessage(glob.BOT_NAME, "#announce", msg)
	return False

def alertUser(fro, chan, message):
	target = message[0].lower()
	targetToken = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True)
	if targetToken is not None:
		msg = ' '.join(message[1:]).strip()
		if not msg:
			return False
		targetToken.enqueue(serverPackets.notification(msg))
		return False
	else:
		return "User offline."

def moderated(fro, chan, message):
	try:
		# Make sure we are in a channel and not PM
		if not chan.startswith("#"):
			raise exceptions.moderatedPMException

		# Get on/off
		enable = True
		if len(message) >= 1:
			if message[0] == "off":
				enable = False

		# Turn on/off moderated mode
		glob.channels.channels[chan].moderated = enable
		return "This channel is {} in moderated mode!".format("now" if enable else "no longer")
	except exceptions.moderatedPMException:
		return "You are trying to put a private chat in moderated mode. Are you serious?!? You're fired."

def kickAll(fro, chan, message):
	# Kick everyone but mods/admins
	toKick = []
	with glob.tokens:
		for key, value in glob.tokens.tokens.items():
			if not value.admin:
				toKick.append(key)

	# Loop though users to kick (we can't change dictionary size while iterating)
	for i in toKick:
		if i in glob.tokens.tokens:
			glob.tokens.tokens[i].kick()

	return "Whoops! Rip everyone."

def kick(fro, chan, message):
	# Get parameters
	target = message[0].lower()
	if target == glob.BOT_NAME.lower():
		return "Nope."

	# Get target token and make sure is connected
	tokens = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True, _all=True)
	if len(tokens) == 0:
		return "{} is not online".format(target)

	# Kick users
	for i in tokens:
		i.kick()

	# Bot response
	return "{} has been kicked from the server.".format(target)

def fokabotReconnect(fro, chan, message):
	# Check if the bot is already connected
	if glob.tokens.getTokenFromUserID(999) is not None:
		return "{} is already connected to Bancho".format(glob.BOT_NAME)

	# Bot is not connected, connect it
	fokabot.connect()
	return False

def silence(fro, chan, message):
	message = [x.lower() for x in message]
	target = message[0]
	amount = message[1]
	unit = message[2]
	reason = ' '.join(message[3:]).strip()
	if not reason:
		return "Please provide a valid reason."
	if not amount.isdigit():
		return "The amount must be a number."

	# Get target user ID
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)

	# Make sure the user exists
	if not targetUserID:
		return "{}: user not found".format(target)

	# Calculate silence seconds
	if unit == 's':
		silenceTime = int(amount)
	elif unit == 'm':
		silenceTime = int(amount) * 60
	elif unit == 'h':
		silenceTime = int(amount) * 3600
	elif unit == 'd':
		silenceTime = int(amount) * 86400
	else:
		return "Invalid time unit (s/m/h/d)."

	# Max silence time is 7 days
	if silenceTime > 604800:
		return "Invalid silence time. Max silence time is 7 days."

	# Send silence packet to target if he's connected
	targetToken = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True)
	if targetToken is not None:
		# user online, silence both in db and with packet
		targetToken.silence(silenceTime, reason, userID)
	else:
		# User offline, silence user only in db
		userUtils.silence(targetUserID, silenceTime, reason, userID)

	# Log message
	msg = "{} has been silenced for the following reason: {}".format(target, reason)
	return msg

def removeSilence(fro, chan, message):
	# Get parameters
	for i in message:
		i = i.lower()
	target = message[0]

	# Make sure the user exists
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)
	if not targetUserID:
		return "{}: user not found".format(target)

	# Send new silence end packet to user if he's online
	targetToken = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True)
	if targetToken is not None:
		# User online, remove silence both in db and with packet
		targetToken.silence(0, "", userID)
	else:
		# user offline, remove islene ofnlt from db
		userUtils.silence(targetUserID, 0, "", userID)

	return "{}'s silence reset".format(target)

def ban(fro, chan, message):
	# Get parameters
	for i in message:
		i = i.lower()
	target = message[0]

	# Make sure the user exists
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)
	if not targetUserID:
		return "{}: user not found".format(target)
	if targetUserID in (999, 1000):
		return "NO!"
	# Set allowed to 0
	userUtils.ban(targetUserID)

	# Send ban packet to the user if he's online
	targetToken = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True)
	if targetToken is not None:
		targetToken.enqueue(serverPackets.loginBanned())

	log.rap(userID, "has banned {}".format(target), True)
	return "RIP {}. You will not be missed.".format(target)

def unban(fro, chan, message):
	# Get parameters
	for i in message:
		i = i.lower()
	target = message[0]

	# Make sure the user exists
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)
	if not targetUserID:
		return "{}: user not found".format(target)

	# Set allowed to 1
	userUtils.unban(targetUserID)

	log.rap(userID, "has unbanned {}".format(target), True)
	return "Welcome back {}!".format(target)

def restrict(fro, chan, message):
	# Get parameters
	for i in message:
		i = i.lower()
	target = message[0]

	# Make sure the user exists
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)
	if not targetUserID:
		return "{}: user not found".format(target)
	if targetUserID in (999, 1000):
		return "NO!"
		
	# Put this user in restricted mode
	userUtils.restrict(targetUserID)

	# Send restricted mode packet to this user if he's online
	targetToken = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True)
	if targetToken is not None:
		targetToken.setRestricted()

	log.rap(userID, "has put {} in restricted mode".format(target), True)
	return "Bye bye {}. See you later, maybe.".format(target)

def unrestrict(fro, chan, message):
	# Get parameters
	for i in message:
		i = i.lower()
	target = message[0]

	# Make sure the user exists
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)
	if not targetUserID:
		return "{}: user not found".format(target)

	# Set allowed to 1
	userUtils.unrestrict(targetUserID)

	log.rap(userID, "has removed restricted mode from {}".format(target), True)
	return "Welcome back {}!".format(target)

def restartShutdown(restart):
	"""Restart (if restart = True) or shutdown (if restart = False) pep.py safely"""
	msg = "We are performing some maintenance. Bancho will {} in 5 seconds. Thank you for your patience.".format("restart" if restart else "shutdown")
	systemHelper.scheduleShutdown(5, restart, msg)
	return msg

def systemRestart(fro, chan, message):
	return restartShutdown(True)

def systemShutdown(fro, chan, message):
	return restartShutdown(False)

def systemReload(fro, chan, message):
	glob.banchoConf.reload()
	return "Bancho settings reloaded!"

def systemMaintenance(fro, chan, message):
	# Turn on/off bancho maintenance
	maintenance = True

	# Get on/off
	if len(message) >= 2:
		if message[1] == "off":
			maintenance = False

	# Set new maintenance value in bancho_settings table
	glob.banchoConf.setMaintenance(maintenance)

	if maintenance:
		# We have turned on maintenance mode
		# Users that will be disconnected
		who = []

		# Disconnect everyone but mod/admins
		with glob.tokens:
			for _, value in glob.tokens.tokens.items():
				if not value.admin:
					who.append(value.userID)

		glob.streams.broadcast("main", serverPackets.notification("Our bancho server is in maintenance mode. Please try to login again later."))
		glob.tokens.multipleEnqueue(serverPackets.loginError(), who)
		msg = "The server is now in maintenance mode!"
	else:
		# We have turned off maintenance mode
		# Send message if we have turned off maintenance mode
		msg = "The server is no longer in maintenance mode!"

	# Chat output
	return msg

def systemStatus(fro, chan, message):
	# Print some server info
	data = systemHelper.getSystemInfo()

	# Final message
	letsVersion = glob.redis.get("lets:version")
	if letsVersion is None:
		letsVersion = "\_(-w-)_/"
	else:
		letsVersion = letsVersion.decode("utf-8")
	msg = "pep.py bancho server v{}\n".format(glob.VERSION)
	msg += "LETS scores server v{}\n".format(letsVersion)
	msg += "made by the osu!Redstar\n"
	msg += "\n"
	msg += "=== BANCHO STATS ===\n"
	msg += "Connected users: {}\n".format(data["connectedUsers"])
	msg += "Multiplayer matches: {}\n".format(data["matches"])
	msg += "Uptime: {}\n".format(data["uptime"])
	msg += "\n"
	msg += "=== SYSTEM STATS ===\n"
	msg += "CPU: {} {}%\n".format(data["cpuName"], data["cpuUsage"])
	msg += "RAM: {}GB/{}GB {}%\n".format(data["usedMemory"], data["totalMemory"], data["memoryUsage"])
	if data["unix"]:
		msg += "Load average: {}/{}/{}\n".format(data["loadAverage"][0], data["loadAverage"][1], data["loadAverage"][2])

	return msg


def getPPMessage(userID, just_data = False):
	try:
		# Get user token
		token = glob.tokens.getTokenFromUserID(userID)
		if token is None:
			return False

		currentMap = token.tillerino[0]
		currentMods = token.tillerino[1]
		currentAcc = token.tillerino[2]
		
		if just_data:
			data = glob.db.fetch(f"""SELECT song_name, pp_100, pp_99, pp_98, pp_95, hit_length as length,
						difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania,
						ar, bpm FROM beatmaps WHERE beatmap_id = {currentMap}""")
			if data is None:
				log.error("ERROR | getPPMessage | data is None")
				return "Error in LETS API call (DB ERROR!)."
			else:
				data = {
					"song_name": data["song_name"],
					"pp": [data["pp_100"], data["pp_99"], data["pp_98"], data["pp_95"]],
					"length": data["length"],
					"stars": data["difficulty_std"],
					"ar": data["ar"],
					"bpm": data["bpm"],
					"message": "ok",
					"status": 200
				}
		else:
			# Send request to LETS api
			resp = requests.get(f"{letsapiurl}/v1/pp?b={currentMap}&m={currentMods}", timeout=10)
			try:
				assert resp is not None
				data = json.loads(resp.text)
			except (json.JSONDecodeError, AssertionError):
				raise exceptions.apiException()

			# Make sure status is in response data
			if "status" not in data:
				raise exceptions.apiException()

			# Make sure status is 200
			if data["status"] != 200:
				if "message" in data:
					return "Error in LETS API call ({}).".format(data["message"])
				else:
					raise exceptions.apiException()

		if just_data:
			return data

		# Return response in chat
		# Song name and mods
		#msg = "{song}{plus}{mods}  ".format(song=data["song_name"], plus="+" if currentMods > 0 else "", mods=scoreUtils.readableMods(currentMods))
		msg = "[https://osu.ppy.sh/b/{bid} Bancho] | [https://osu.{domain}/b/{bid} {song}] {plus}{mods}  ".format(domain=userDomainCheck(), bid=currentMap, song=data["song_name"], plus="+" if currentMods > 0 else "", mods=scoreUtils.readableMods(currentMods))

		# PP values
		""" if currentAcc == -1:
			msg += "100%: {pp100}pp | 99% {pp99}pp | 98%: {pp98}pp | 95%: {pp95}pp".format(pp100=round(data["pp"][0], 2), pp99=round(data["pp"][1], 2), pp98=round(data["pp"][2], 2), pp95=round(data["pp"][3], 2))
		else:
			msg += "{acc:.2f}%: {pp}pp".format(acc=token.tillerino[2], pp=round(data["pp"][0], 2)) """
		
		newurl = f"https://old.{server_domain}/letsapi/v1/pp?b={currentMap}&m={currentMods}"
		#pp조회시 조회는 되나, pp가 0로 표시될 때 생기는 에러 예외처리
		try:
			msg += "[{url} 100%: {pp100}pp | 99% {pp99}pp | 98%: {pp98}pp | 95%: {pp95}pp]".format(url=newurl, pp100=round(data["pp"][0], 2), pp99=round(data["pp"][1], 2), pp98=round(data["pp"][2], 2), pp95=round(data["pp"][3], 2))
		except:
			try:
				msg += f"| ERROR : [{newurl} {data['pp']}pp]"
			except:
				msg += "| ERROR : pp ERROR"

		originalAR = data["ar"]
		# calc new AR if HR/EZ is on
		if (currentMods & mods.EASY) > 0:
			data["ar"] =round(max(0, data["ar"] / 2), 2)
		if (currentMods & mods.HARDROCK) > 0:
			data["ar"] =round(min(10, data["ar"] * 1.4), 2)
		
		arstr = " ({})".format(originalAR) if originalAR != data["ar"] else ""
		
		# Beatmap info
		msg += " | {bpm} BPM | AR {ar}{arstr} | {stars:.2f} stars | [osu://b/{bid} osu!direct]".format(bpm=data["bpm"], stars=data["stars"], ar=data["ar"], arstr=arstr, bid=currentMap)

		# Return final message
		return msg
	except requests.exceptions.RequestException:
		# RequestException
		return "API Timeout. Please try again in a few seconds."
	except exceptions.apiException:
		# API error
		return "Unknown error in LETS API call."
	#except:
		# Unknown exception
		# TODO: print exception
	#	return False

def tillerinoNp(fro, chan, message):
	try:
		# Mirror list trigger for #spect_
		if chan.startswith("#spect_"):
			spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
			spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
			if spectatorHostToken is None:
				return False
			return mirrorMessage(spectatorHostToken.beatmapID)

		# Run the command in PM only
		""" if chan.startswith("#"):
			return False """

		playWatch = message[1] == "playing" or message[1] == "watching" or message[1] == "editing"
		# Get URL from message
		if message[1] == "listening":
			beatmapURL = str(message[3][1:])
		elif playWatch:
			beatmapURL = str(message[2][1:])
		else:
			return False

		modsEnum = 0
		mapping = {
			"-Easy": mods.EASY,
			"-NoFail": mods.NOFAIL,
			"+Hidden": mods.HIDDEN,
			"+HardRock": mods.HARDROCK,
			#"+Nightcore": mods.NIGHTCORE,
			"+Nightcore": 576,
			"+DoubleTime": mods.DOUBLETIME,
			"-HalfTime": mods.HALFTIME,
			"+Flashlight": mods.FLASHLIGHT,
			"-SpunOut": mods.SPUNOUT
		}

		if playWatch:
			for part in message:
				part = part.replace("\x01", "")
				if part in mapping.keys():
					modsEnum += mapping[part]

		# Get beatmap id from URL
		#beatmapID = fokabot.npRegex.search(beatmapURL).groups(0)[1]
		try:
			beatmapID = fokabot.RGX(beatmapURL)[1]
			log.info(f"tillerinoNp() beatmapID = {beatmapID}")
			by_message = "by /np"
		except:
			log.debug("RGX 실패!")
			beatmapID = fokabot.RGX(beatmapURL)[0]
			log.info(f"tillerinoNp() beatmapID = {beatmapID}")
			by_message = "by /np"

		# Update latest tillerino song for current token
		token = glob.tokens.getTokenFromUsername(fro)
		if token is not None:
			token.tillerino = [int(beatmapID), modsEnum, -1.0, by_message]
		userID = token.userID

		# Return tillerino message
		return getPPMessage(userID)
	except:
		log.error(f"tillerinoNp() 함수 에러남 | message = {message}")
		log.error(f"beatmapURL = {beatmapURL}")
		return False


def tillerinoMods(fro, chan, message, modsNumType=None):
	try:
		""" # Run the command in PM only
		if chan.startswith("#"):
			return False """

		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False
		userID = token.userID

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0 and modsNumType is None:
			return "Please give me a beatmap first with /np command."

		# Check passed mods and convert to enum
		modsEnum = scoreUtils.readableModsReverse(message[0])
		if type(modsEnum) != int : return modsEnum

		# Set mods
		token.tillerino[1] = modsEnum
		try:
			token.tillerino[3] = f"by !with)"
		except:
			token.tillerino.append(f"by !with")

		if modsNumType is not None:
			token.tillerino[3] = f"by {modsNumType})"
			return modsEnum
		else:
			# Return tillerino message for that beatmap with mods
			return getPPMessage(userID)
	except:
		return False

def tillerinoAcc(fro, chan, message):
	try:
		return "blocked !acc <accuracy> command"
		# Run the command in PM only
		""" if chan.startswith("#"):
			return False """

		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False
		userID = token.userID

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0:
			return "Please give me a beatmap first with /np command."

		# Convert acc to float
		acc = float(message[0])

		# Set new tillerino list acc value
		token.tillerino[2] = acc

		# Return tillerino message for that beatmap with mods
		return getPPMessage(userID)
	except ValueError:
		return "Invalid acc value"
	except:
		return False

def tillerinoLast(fro, chan, message, bpp_command = False):
	try:
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			log.error("ERROR: No token")
			return "ERROR: No token"
		userID = token.userID

		try:
			if message[0].lower() == "vn":
				status_rx = False
				status_ap = False
			elif message[0].lower() == "rx":
				status_rx = True
				status_ap = False
			elif message[0].lower() == "ap":
				status_rx = False
				status_ap = True
			else:
				status = glob.db.fetch("SELECT current_status FROM users_stats WHERE id = %s", [userID])
				status_rx = status["current_status"].endswith("on Relax")
				status_ap = status["current_status"].endswith("on AP")
		except:
			status = glob.db.fetch("SELECT current_status FROM users_stats WHERE id = %s", [userID])
			status_rx = status["current_status"].endswith("on Relax")
			status_ap = status["current_status"].endswith("on AP")

		#특정 비트맵 last 조회
		add_md5_scoredata = ""
		last_user_last = False
		try:
			#!last 1919312
			bid = int(message[0])
			log.info(f"특정 비트맵 last 조회 | bid = message[0] = {bid}")
			bmd5 = glob.db.fetch(f"SELECT beatmap_md5 FROM beatmaps WHERE beatmap_id = {bid}")["beatmap_md5"]
			add_md5_scoredata = f"AND beatmap_md5 = '{bmd5}'"
			last_user_last = True
		except:
			pass
		try:
			#!last vn 1919312
			bid = int(message[1])
			log.info(f"특정 비트맵 last 조회 | bid = message[1] = {bid}")
			bmd5 = glob.db.fetch(f"SELECT beatmap_md5 FROM beatmaps WHERE beatmap_id = {bid}")["beatmap_md5"]
			add_md5_scoredata = f"AND beatmap_md5 = '{bmd5}'"
			last_user_last = True
		except:
			pass

		#특정 유저 last 조회
		try:
			if not last_user_last:
				rqUserID = userUtils.getID(message[1])
				if message[1] == "":
					raise
				elif rqUserID != 0:
					userID = rqUserID
					fro = message[1]
					log.info(f"{message[1]} ({userID}) 의 last 조회 | message[1]")
				else:
					return f"{message[1]} is not user. (message[1])"
			last_user_last = True
		except:
			pass
		try:
			if not last_user_last:
				rqUserID = userUtils.getID(message[0])
				if message[0] == "" or message[0].lower() in ["vn", "rx", "ap"]:
					raise
				elif rqUserID != 0:
					userID = rqUserID
					fro = message[0]
					log.info(f"{message[0]} ({userID}) 의 last 조회 | message[0]")
				else:
					return f"{message[0]} is not user. (message[0])"
		except:
			pass

		if status_rx:
			log.chat("tillerinoLast()함수 릴렉스 확인")

			#data = glob.db.fetch("""SELECT beatmaps.song_name as sn, scores_relax.*,
			#	beatmaps.ranked as beatmap_ranked_status, beatmaps.beatmap_id as bid, beatmaps.beatmapset_id as bsid, beatmaps.difficulty_std, beatmaps.difficulty_taiko, beatmaps.difficulty_ctb, beatmaps.difficulty_mania, beatmaps.max_combo as fc
			#FROM scores_relax
			#LEFT JOIN beatmaps ON beatmaps.beatmap_md5=scores_relax.beatmap_md5
			#LEFT JOIN users ON users.id = scores_relax.userid
			#WHERE users.username = %s
			#ORDER BY scores_relax.time DESC
			#LIMIT 1""", [fro])

			#!bpp 명령어 실행시 !last 의 정렬을 pp로 하여 리턴함
			if bpp_command == False:
				scoredata = glob.db.fetch(f"SELECT * FROM scores_relax WHERE userid = {userID} {add_md5_scoredata} ORDER BY time DESC LIMIT 1")
			else:
				scoredata = glob.db.fetch(f"SELECT * FROM scores_relax WHERE userid = {userID} {add_md5_scoredata} ORDER BY pp DESC LIMIT 1")
			
			if scoredata is None:
				return "[Relax] There is no recent play data."
			data = glob.db.fetch("SELECT song_name as sn from beatmaps WHERE beatmap_md5 = %s", [scoredata["beatmap_md5"]])
			beatmapdata = glob.db.fetch("""SELECT ranked as beatmap_ranked_status, beatmap_id as bid, beatmapset_id as bsid, difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania, max_combo as fc
			from beatmaps WHERE beatmap_md5 = %s""", [scoredata["beatmap_md5"]])
			if not data and not beatmapdata: return "[ERROR!] | I Think map was updated. Not Found DB"
			data.update(scoredata)
			data.update(beatmapdata)
			
			msg = "[Relax] "
		elif status_ap:
			log.chat("tillerinoLast()함수 AP 확인")

			#data = glob.db.fetch("""SELECT beatmaps.song_name as sn, scores_ap.*,
			#	beatmaps.ranked as beatmap_ranked_status, beatmaps.beatmap_id as bid, beatmaps.beatmapset_id as bsid, beatmaps.difficulty_std, beatmaps.difficulty_taiko, beatmaps.difficulty_ctb, beatmaps.difficulty_mania, beatmaps.max_combo as fc
			#FROM scores_ap
			#LEFT JOIN beatmaps ON beatmaps.beatmap_md5=scores_ap.beatmap_md5
			#LEFT JOIN users ON users.id = scores_ap.userid
			#WHERE users.username = %s
			#ORDER BY scores_ap.time DESC
			#LIMIT 1""", [fro])

			#!bpp 명령어 실행시 !last 의 정렬을 pp로 하여 리턴함
			if bpp_command == False:
				scoredata = glob.db.fetch(f"SELECT * FROM scores_ap WHERE userid = {userID} {add_md5_scoredata} ORDER BY time DESC LIMIT 1")
			else:
				scoredata = glob.db.fetch(f"SELECT * FROM scores_ap WHERE userid = {userID} {add_md5_scoredata} ORDER BY pp DESC LIMIT 1")
			
			if scoredata is None:
				return "[AP] There is no recent play data."
			data = glob.db.fetch("SELECT song_name as sn from beatmaps WHERE beatmap_md5 = %s", [scoredata["beatmap_md5"]])
			beatmapdata = glob.db.fetch("""SELECT ranked as beatmap_ranked_status, beatmap_id as bid, beatmapset_id as bsid, difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania, max_combo as fc
			from beatmaps WHERE beatmap_md5 = %s""", [scoredata["beatmap_md5"]])
			if not data and not beatmapdata: return "[ERROR!] | I Think map was updated. Not Found DB"
			data.update(scoredata)
			data.update(beatmapdata)
			
			msg = "[AP] "
		else:
			log.chat("tillerinoLast()함수 바닐라 확인")

			#data = glob.db.fetch("""SELECT beatmaps.song_name as sn, scores.*,
			#	beatmaps.ranked as beatmap_ranked_status, beatmaps.beatmap_id as bid, beatmaps.beatmapset_id as bsid, beatmaps.difficulty_std, beatmaps.difficulty_taiko, beatmaps.difficulty_ctb, beatmaps.difficulty_mania, beatmaps.max_combo as fc
			#FROM scores
			#LEFT JOIN beatmaps ON beatmaps.beatmap_md5=scores.beatmap_md5
			#LEFT JOIN users ON users.id = scores.userid
			#WHERE users.username = %s
			#ORDER BY scores.time DESC
			#LIMIT 1""", [fro])

			#!bpp 명령어 실행시 !last 의 정렬을 pp로 하여 리턴함
			if bpp_command == False:
				scoredata = glob.db.fetch(f"SELECT * FROM scores WHERE userid = {userID} {add_md5_scoredata} ORDER BY time DESC LIMIT 1")
			else:
				scoredata = glob.db.fetch(f"SELECT * FROM scores WHERE userid = {userID} {add_md5_scoredata} ORDER BY pp DESC LIMIT 1")

			if scoredata is None:
				#return False
				return "[Vanilla] There is no recent play data."
			data = glob.db.fetch("SELECT song_name as sn from beatmaps WHERE beatmap_md5 = %s", [scoredata["beatmap_md5"]])
			beatmapdata = glob.db.fetch("""SELECT ranked as beatmap_ranked_status, beatmap_id as bid, beatmapset_id as bsid, difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania, max_combo as fc
			from beatmaps WHERE beatmap_md5 = %s""", [scoredata["beatmap_md5"]])
			if not data and not beatmapdata: return "[ERROR!] | I Think map was updated. Not Found DB"
			data.update(scoredata)
			data.update(beatmapdata)

			msg = "[Vanilla] "

		diffString = "difficulty_{}".format(gameModes.getGameModeForDB(data["play_mode"]))
		rank = generalUtils.getRank(data["play_mode"], data["mods"], data["accuracy"],
									data["300_count"], data["100_count"], data["50_count"], data["misses_count"])

		#ifPlayer = "{0} | ".format(fro)# if chan != glob.BOT_NAME else ""
		if status_rx:
			ifPlayer = f"[https://{server_domain}/u/rx/{userID} {fro}] | "
		elif status_ap:
			ifPlayer = f"[https://{server_domain}/u/ap/{userID} {fro}] | "
		else:
			ifPlayer = f"[https://{server_domain}/u/{userID} {fro}] | "

		#userID, fro 재설정
		userID = token.userID
		fro = token.username

		ifFc = " | {}x (FC)".format(data["fc"]) if data["max_combo"] == data["fc"] else " | {0}x/{1}x".format(data["max_combo"], data["fc"])
		#beatmapLink = "[http://redstar.moe/b/{1} {0}]".format(data["sn"], data["bid"])
		beatmapLink = "[https://osu.{}/b/{} {}]".format(userDomainCheck(), data["bid"], data["sn"])
		hasPP = data["play_mode"] != gameModes.CTB

		#위에서 할당됨
		#msg = "[Relax] "
		msg += ifPlayer
		msg += beatmapLink
		if data["play_mode"] != gameModes.STD:
			msg += " <{0}>".format(gameModes.getGameModeForPrinting(data["play_mode"]))

		if data["mods"]:
			""" if status_rx:
				msg += ' +' + scoreUtils.readableMods(data["mods"]) + "RX"
				log.info(scoreUtils.readableMods(data["mods"]) + "RX")
			elif status_ap:
				msg += ' +' + scoreUtils.readableMods(data["mods"]) + "AP"
				log.info(scoreUtils.readableMods(data["mods"]) + "AP")
			else:
				msg += ' +' + scoreUtils.readableMods(data["mods"])
				log.info(scoreUtils.readableMods(data["mods"])) """
			msg += ' +' + scoreUtils.readableMods(data["mods"])
			log.info(scoreUtils.readableMods(data["mods"]))

		
		log.info("data['mods'] = {}".format(data["mods"]))

		if not hasPP:
			msg += " | {0:,}".format(data["score"])
			msg += ifFc
			msg += " | {0:.2f}%, {1}".format(data["accuracy"], rank.upper())
			msg += " {{ {0} / {1} / {2} / {3} }}".format(data["300_count"], data["100_count"], data["50_count"], data["misses_count"])
			#pp 추가
			msg += f" | {round(data['pp'], 2)}pp"
			msg += " | {0:.2f} stars".format(data[diffString])

			#ctb token.tillerino 추가
			token.tillerino[0] = data["bid"]
			token.tillerino[1] = data["mods"]
			token.tillerino[2] = round(data["accuracy"], 2)
			try:
				token.tillerino[3] = f"by !last ({msg[0:msg.index(']') + 1]})"
			except:
				token.tillerino.append(f"by !last ({msg[0:msg.index(']') + 1]})")

			return msg

		msg += " ({0:.2f}%, {1})".format(data["accuracy"], rank.upper())

		#ranked_status추가
		#커스텀 비트맵 추가
		if data["bid"] <= 0:
			msg += " | Qualified (Custom Map, Deleted Map)"
		else:
			if data["beatmap_ranked_status"] == 2:
				msg += " | Ranked"
			elif data["beatmap_ranked_status"] == 5:
				msg += " | Loved"
			elif data["beatmap_ranked_status"] == 3:
				msg += " | Approved (Ranked)"
			elif data["beatmap_ranked_status"] == 4:
				msg += " | Qualified (Not Ranked Yet)"
			elif data["beatmap_ranked_status"] == 0:
				msg += " | Unranked"
			else:
				msg += " | Ranked status Unknown"
		#스코어 추가
		msg += " | {:,}".format(data["score"], ",d")

		msg += ifFc
		msg += " | {0:.2f}pp".format(data["pp"])

		stars = data[diffString]
		if data["mods"]:
			token = glob.tokens.getTokenFromUsername(fro)
			if token is None:
				return False
			userID = token.userID
			token.tillerino[0] = data["bid"]
			token.tillerino[1] = data["mods"]
			token.tillerino[2] = round(data["accuracy"], 2)
			try:
				token.tillerino[3] = f"by !last ({msg[0:msg.index(']') + 1]})"
			except:
				token.tillerino.append(f"by !last ({msg[0:msg.index(']') + 1]})")
		#노모드의 경우 token.tillerino 할당이 되지 않으므로 else 추가함
		else:
			token.tillerino[0] = data["bid"]
			token.tillerino[1] = data["mods"]
			token.tillerino[2] = round(data["accuracy"], 2)
			try:
				token.tillerino[3] = f"by !last ({msg[0:msg.index(']') + 1]})"
			except:
				token.tillerino.append(f"by !last ({msg[0:msg.index(']') + 1]})")

		#if data["mods"]: 안에 속해있었는데 else: 를 추가함으로 인하여 if data["mods"]: 밖으로 뺌
		oppaiData = getPPMessage(userID, just_data=True)
		if "stars" in oppaiData:
			stars = oppaiData["stars"]

		msg += " | {0:.2f} stars".format(stars)

		#시간 추가
		msg += f" | {unix_to_date(data['time'])}"

		#completed 추가
		msg += f" | completed = {data['completed']}"
		#id (replay) 추가
		if status_rx:
			msg += f" | id (replay) = [https://{server_domain}/web/replays_relax/{data['id']} {data['id']}]"
		elif status_ap:
			msg += f" | id (replay) = [https://{server_domain}/web/replays_ap/{data['id']} {data['id']}]"
		else:
			msg += f" | id (replay) = [https://{server_domain}/web/replays/{data['id']} {data['id']}]"
		#dl추가
		msg += " | [osu://b/{} osu!direct]".format(data["bid"])

		# Send request to LETS api
		#에러 무한반복 (아니 꺼도 또 무한반복? osuapiHelper.py 에서 커스텀 비트맵 pp조회 키면 또 에러남 ㅅㅂ)
		url = f"https://old.{server_domain}/letsapi/v1/pp?b={data['bid']}&m={data['mods']}"
		resp = requests.get(url, timeout=8)
		try:
			assert resp is not None
			odata = json.loads(resp.text)
		except (json.JSONDecodeError, AssertionError):
			raise exceptions.apiException()

		try:
			msg2 = "[{url} 100%: {pp100}pp | 99% {pp99}pp | 98%: {pp98}pp | 95%: {pp95}pp]".format(url=url, pp100=round(odata["pp"][0], 2), pp99=round(odata["pp"][1], 2), pp98=round(odata["pp"][2], 2), pp95=round(odata["pp"][3], 2))
			fokamessage(chan, msg2)
		except:
			fokamessage(chan, "ERROR | culc pp error | DEAD")
			
		return msg

	except Exception as a:
		log.error(a)
		#return False
		return a


def getBeatmapRequest(fro, chan, message): # Grab a random beatmap request. TODO: Add gamemode handling to this and !request
	request = glob.db.fetch("SELECT * FROM rank_requests LIMIT 1;")
	if request is not None:
		username = userUtils.getUsername(request['userid'])
		mapData = glob.db.fetch("SELECT song_name, ranked FROM beatmaps WHERE beatmap_id = {} ORDER BY difficulty_std DESC LIMIT 1;".format(request['bid']))
		glob.db.execute("DELETE FROM rank_requests WHERE id = {};".format(request['id']))
		#return "[https://debian.moe/u/{userID} {username}] nominated beatmap: [https://osu.ppy.sh/b/{beatmapID} {songName}] for status change. {AinuBeatmapLink}The request has been deleted, so please decide it's status.".format(userID=request['userid'], username=username, beatmapID=request['bid'], songName=mapData['song_name'], AinuBeatmapLink='[https://debian.moe/b/{} Ainu beatmap Link]. '.format(request['bid']))
		return "[https://{domain}/u/{userID} {username}] nominated beatmap: [https://osu.{domain}/b/{beatmapID} {songName}] for status change. {AinuBeatmapLink}The request has been deleted, so please decide it's status.".format(domain=server_domain, userID=request['userid'], username=username, beatmapID=request['bid'], songName=mapData['song_name'], AinuBeatmapLink='[https://{}/b/{} Ainu beatmap Link]. '.format(userDomainCheck(), request['bid']))
	else:
		return "All nominations have been checked. Thank you for your hard work! :)"
	
	return "The beatmap ranking system has been reworked."



def mm00(fro, chan, message):
	random.seed()
	return random.choice(["meme", "MA MAURO ESISTE?"])

def pp(fro, chan, message):
	""" if chan.startswith("#"):
		return False """

	gameMode = None
	if len(message) >= 1:
		gm = {
			"standard": 0,
			"std": 0,
			"taiko": 1,
			"ctb": 2,
			"mania": 3
		}
		if message[0].lower() not in gm:
			return "What's that game mode? I've never heard of it :/"
		else:
			gameMode = gm[message[0].lower()]

	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	
	#rx, ap 추가
	status = glob.db.fetch("SELECT current_status FROM users_stats WHERE id = %s", [token.userID])
		
	status_rx = status["current_status"].endswith("on Relax")
	status_ap = status["current_status"].endswith("on AP")

	if gameMode is None:
		gameMode = token.gameMode
	""" if gameMode == gameModes.TAIKO or gameMode == gameModes.CTB:
		return "PP for your current game mode is not supported yet." """
	
	#rx, ap 추가
	gm = gameModes.getGamemodeFull(gameMode)
	if status_rx:
		pp = userUtils.getPPRX(token.userID, gameMode)
		return "[Relax] {} | You have {:,} pp".format(gm, pp)
	elif status_ap:
		pp = userUtils.getPPAP(token.userID, gameMode)
		return "[AP] {} | You have {:,} pp".format(gm, pp)
	else:
		pp = userUtils.getPP(token.userID, gameMode)
		return "[Vanilla] {} | You have {:,} pp".format(gm, pp)
	

def updateBeatmap(fro, chan, message):
	try:
		# Run the command in PM only
		if chan.startswith("#"):
			return False

		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0:
			return "Please give me a beatmap first with /np command."

		# Send the request to cheesegull
		ok, message = cheesegull.updateBeatmap(token.tillerino[0])
		if ok:
			return "An update request for that beatmap has been queued. Check back in a few minutes and the beatmap should be updated!"
		else:
			return "Error in beatmap mirror API request: {}".format(message)
	except:
		return False

def report(fro, chan, message):
	msg = ""
	try:
		# TODO: Rate limit
		# Regex on message
		reportRegex = re.compile("^(.+) \((.+)\)\:(?: )?(.+)?$")
		result = reportRegex.search(" ".join(message))

		# Make sure the message matches the regex
		if result is None:
			raise exceptions.invalidArgumentsException()

		# Get username, report reason and report info
		target, reason, additionalInfo = result.groups()
		target = chat.fixUsernameForBancho(target)

		# Make sure the target is not foka
		if target.lower() == glob.BOT_NAME.lower():
			raise exceptions.invalidUserException()

		# Make sure the user exists
		targetID = userUtils.getID(target)
		if targetID == 0:
			raise exceptions.userNotFoundException()

		# Make sure that the user has specified additional info if report reason is 'Other'
		if reason.lower() == "other" and additionalInfo is None:
			raise exceptions.missingReportInfoException()

		# Get the token if possible
		chatlog = ""
		token = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True)
		if token is not None:
			chatlog = token.getMessagesBufferString()

		# Everything is fine, submit report
		glob.db.execute("INSERT INTO reports (id, from_uid, to_uid, reason, chatlog, time) VALUES (NULL, %s, %s, %s, %s, %s)", [userUtils.getID(fro), targetID, "{reason} - ingame {info}".format(reason=reason, info="({})".format(additionalInfo) if additionalInfo is not None else ""), chatlog, int(time.time())])
		msg = "You've reported {target} for {reason}{info}. A Community Manager will check your report as soon as possible. Every !report message you may see in chat wasn't sent to anyone, so nobody in chat, but admins, know about your report. Thank you for reporting!".format(target=target, reason=reason, info="" if additionalInfo is None else " (" + additionalInfo + ")")
		adminMsg = "{user} has reported {target} for {reason} ({info})".format(user=fro, target=target, reason=reason, info=additionalInfo)

		# Log report in #admin and on discord
		chat.sendMessage(glob.BOT_NAME, "#admin", adminMsg)
		log.warning(adminMsg, discord="cm")
	except exceptions.invalidUserException:
		msg = "Hello, {} here! You can't report me. I won't forget what you've tried to do. Watch out.".format(glob.BOT_NAME)
	except exceptions.invalidArgumentsException:
		msg = "Invalid report command syntax. To report an user, click on it and select 'Report user'."
	except exceptions.userNotFoundException:
		msg = "The user you've tried to report doesn't exist."
	except exceptions.missingReportInfoException:
		msg = "Please specify the reason of your report."
	except:
		raise
	finally:
		if msg != "":
			token = glob.tokens.getTokenFromUsername(fro)
			if token is not None:
				if token.irc:
					chat.sendMessage(glob.BOT_NAME, fro, msg)
				else:
					token.enqueue(serverPackets.notification(msg))
	return False

def getMatchIDFromChannel(chan):
	if not chan.lower().startswith("#multi_"):
		raise exceptions.wrongChannelException()
	parts = chan.lower().split("_")
	if len(parts) < 2 or not parts[1].isdigit():
		raise exceptions.wrongChannelException()
	matchID = int(parts[1])
	if matchID not in glob.matches.matches:
		raise exceptions.matchNotFoundException()
	return matchID

def getSpectatorHostUserIDFromChannel(chan):
	if not chan.lower().startswith("#spect_"):
		raise exceptions.wrongChannelException()
	parts = chan.lower().split("_")
	if len(parts) < 2 or not parts[1].isdigit():
		raise exceptions.wrongChannelException()
	userID = int(parts[1])
	return userID

def multiplayer(fro, chan, message):
	def mpListRefer():
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		return str(_match.refers)

	def mpAddRefer():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp addref <user>")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		username = message[1].strip()
		if not username:
			raise exceptions.invalidArgumentsException("Please provide a username")
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		_match.addRefer(userID)
		return "Added {} to refers".format(username)

	def mpRemoveRefer():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp rmref <user>")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		username = message[1].strip()
		if not username:
			raise exceptions.invalidArgumentsException("Please provide a username")
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		_match.removeRefer(userID)
		return "Removed {} from refers".format(username)

	def mpMake():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp make <name>")
		matchName = " ".join(message[1:]).strip()
		if not matchName:
			raise exceptions.invalidArgumentsException("Match name must not be empty!")
		matchID = glob.matches.createMatch(matchName, generalUtils.stringMd5(generalUtils.randomString(32)), 0, "Tournament", "", 0, -1, isTourney=True)
		glob.matches.matches[matchID].sendUpdates()
		return "Tourney match #{} created!".format(matchID)

	def mpJoin():
		if len(message) < 2 or not message[1].isdigit():
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp join <id>")
		matchID = int(message[1])
		userToken = glob.tokens.getTokenFromUsername(fro, ignoreIRC=True)
		if userToken is None:
			raise exceptions.invalidArgumentsException(
				"No game clients found for {}, can't join the match. "
			    "If you're a referee and you want to join the chat "
				"channel from IRC, use /join #multi_{} instead.".format(fro, matchID)
			)
		userToken.joinMatch(matchID)
		return "Attempting to join match #{}!".format(matchID)

	def mpClose():
		matchID = getMatchIDFromChannel(chan)
		glob.matches.disposeMatch(matchID)
		return "Multiplayer match #{} disposed successfully".format(matchID)

	def mpLock():
		matchID = getMatchIDFromChannel(chan)
		glob.matches.matches[matchID].isLocked = True
		return "This match has been locked"

	def mpUnlock():
		matchID = getMatchIDFromChannel(chan)
		glob.matches.matches[matchID].isLocked = False
		return "This match has been unlocked"

	def mpSize():
		if len(message) < 2 or not message[1].isdigit() or int(message[1]) < 2 or int(message[1]) > 16:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp size <slots(2-16)>")
		matchSize = int(message[1])
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.forceSize(matchSize)
		return "Match size changed to {}".format(matchSize)

	def mpMove():
		if len(message) < 3 or not message[2].isdigit() or int(message[2]) < 0 or int(message[2]) > 16:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp move <username> <slot>")
		username = message[1]
		newSlotID = int(message[2])
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		success = _match.userChangeSlot(userID, newSlotID)
		if success:
			result = "Player {} moved to slot {}".format(username, newSlotID)
		else:
			result = "You can't use that slot: it's either already occupied by someone else or locked"
		return result

	def mpHost():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp host <username>")
		username = message[1].strip()
		if not username:
			raise exceptions.invalidArgumentsException("Please provide a username")
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		success = _match.setHost(userID)
		return "{} is now the host".format(username) if success else "Couldn't give host to {}".format(username)

	def mpClearHost():
		matchID = getMatchIDFromChannel(chan)
		glob.matches.matches[matchID].removeHost()
		return "Host has been removed from this match"

	def mpStart():
		def _start():
			matchID = getMatchIDFromChannel(chan)
			success = glob.matches.matches[matchID].start()
			if not success:
				chat.sendMessage(glob.BOT_NAME, chan, "Couldn't start match. Make sure there are enough players and "
												  "teams are valid. The match has been unlocked.")
			else:
				chat.sendMessage(glob.BOT_NAME, chan, "Have fun!")


		def _decreaseTimer(t):
			if t <= 0:
				_start()
			else:
				if t % 10 == 0 or t <= 5:
					chat.sendMessage(glob.BOT_NAME, chan, "Match starts in {} seconds.".format(t))
				threading.Timer(1.00, _decreaseTimer, [t - 1]).start()

		if len(message) < 2 or not message[1].isdigit():
			startTime = 0
		else:
			startTime = int(message[1])

		force = False if len(message) < 3 else message[2].lower() == "force"
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]

		# Force everyone to ready
		someoneNotReady = False
		for i, slot in enumerate(_match.slots):
			if slot.status != slotStatuses.READY and slot.user is not None:
				someoneNotReady = True
				if force:
					_match.toggleSlotReady(i)

		if someoneNotReady and not force:
			return "Some users aren't ready yet. Use '!mp start force' if you want to start the match, " \
				   "even with non-ready players."

		if startTime == 0:
			_start()
			return "Starting match"
		else:
			_match.isStarting = True
			threading.Timer(1.00, _decreaseTimer, [startTime - 1]).start()
			return "Match starts in {} seconds. The match has been locked. " \
				   "Please don't leave the match during the countdown " \
				   "or you might receive a penalty.".format(startTime)

	def mpInvite():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp invite <username>")
		username = message[1].strip()
		if not username:
			raise exceptions.invalidArgumentsException("Please provide a username")
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		token = glob.tokens.getTokenFromUserID(userID, ignoreIRC=True)
		if token is None:
			raise exceptions.invalidUserException("That user is not connected to bancho right now.")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.invite(999, userID)
		token.enqueue(serverPackets.notification("Please accept the invite you've just received from {} to "
												 "enter your tourney match.".format(glob.BOT_NAME)))
		return "An invite to this match has been sent to {}".format(username)

	def mpMap():
		if len(message) < 2 or not message[1].isdigit() or (len(message) == 3 and not message[2].isdigit()):
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp map <beatmapid> [<gamemode>]")
		beatmapID = int(message[1])
		gameMode = int(message[2]) if len(message) == 3 else 0
		if gameMode < 0 or gameMode > 3:
			raise exceptions.invalidArgumentsException("Gamemode must be 0, 1, 2 or 3")
		beatmapData = glob.db.fetch("SELECT * FROM beatmaps WHERE beatmap_id = %s LIMIT 1", [beatmapID])
		if beatmapData is None:
			raise exceptions.invalidArgumentsException("The beatmap you've selected couldn't be found in the database."
													   "If the beatmap id is valid, please load the scoreboard first in "
													   "order to cache it, then try again.")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.beatmapID = beatmapID
		_match.beatmapName = beatmapData["song_name"]
		_match.beatmapMD5 = beatmapData["beatmap_md5"]
		_match.gameMode = gameMode
		_match.resetReady()
		_match.sendUpdates()
		return "Match map has been updated"

	def mpSet():
		if len(message) < 2 or not message[1].isdigit() or \
				(len(message) >= 3 and not message[2].isdigit()) or \
				(len(message) >= 4 and not message[3].isdigit()):
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp set <teammode> [<scoremode>] [<size>]")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		matchTeamType = int(message[1])
		matchScoringType = int(message[2]) if len(message) >= 3 else _match.matchScoringType
		if not 0 <= matchTeamType <= 3:
			raise exceptions.invalidArgumentsException("Match team type must be between 0 and 3")
		if not 0 <= matchScoringType <= 3:
			raise exceptions.invalidArgumentsException("Match scoring type must be between 0 and 3")
		oldMatchTeamType = _match.matchTeamType
		_match.matchTeamType = matchTeamType
		_match.matchScoringType = matchScoringType
		if len(message) >= 4:
			_match.forceSize(int(message[3]))
		if _match.matchTeamType != oldMatchTeamType:
			_match.initializeTeams()
		if _match.matchTeamType == matchTeamTypes.TAG_COOP or _match.matchTeamType == matchTeamTypes.TAG_TEAM_VS:
			_match.matchModMode = matchModModes.NORMAL

		_match.sendUpdates()
		return "Match settings have been updated!"

	def mpAbort():
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.abort()
		return "Match aborted!"

	def mpKick():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp kick <username>")
		username = message[1].strip()
		if not username:
			raise exceptions.invalidArgumentsException("Please provide a username")
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		slotID = _match.getUserSlotID(userID)
		if slotID is None:
			raise exceptions.userNotFoundException("The specified user is not in this match")
		for i in range(0, 2):
			_match.toggleSlotLocked(slotID)
		return "{} has been kicked from the match.".format(username)

	def mpPassword():
		password = "" if len(message) < 2 or not message[1].strip() else message[1]
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.changePassword(password)
		return "Match password has been changed!"

	def mpRandomPassword():
		password = generalUtils.stringMd5(generalUtils.randomString(32))
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.changePassword(password)
		return "Match password has been changed to a random one"

	def mpMods():
		if len(message) < 2:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp <mod1> [<mod2>] ...")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		newMods = 0
		freeMod = False
		for _mod in message[1:]:
			log.info("_mod = {}".format(_mod))
			if _mod.isdigit():
				log.info("_mod {} 값이 숫자임을 감지".format(_mod))

			if _mod.lower().strip() == "none" or _mod == "0":
				newMods = 0
				break
			elif _mod.lower().strip() == "nf" or _mod == "1":
				newMods |= mods.NOFAIL
			elif _mod.lower().strip() == "ez" or _mod == "2":
				newMods |= mods.EASY
			elif _mod.lower().strip() == "td" or _mod == "4":
				newMods |= mods.TOUCHSCREEN
			elif _mod.lower().strip() == "hd" or _mod == "8":
				newMods |= mods.HIDDEN
			elif _mod.lower().strip() == "hr" or _mod == "16":
				newMods |= mods.HARDROCK
			elif _mod.lower().strip() == "sd" or _mod == "32":
				newMods |= mods.SUDDENDEATH
			elif _mod.lower().strip() == "dt" or _mod == "64":
				newMods |= mods.DOUBLETIME
			elif _mod.lower().strip() == "rx" or _mod == "128":
				newMods |= mods.RELAX
			elif _mod.lower().strip() == "ht" or _mod == "256":
				newMods |= mods.HALFTIME
			elif _mod.lower().strip() == "nc" or _mod == "512" or _mod == "576":
				#modsEnum += mods.NIGHTCORE
				#modsEnum += 576
				newMods |= mods.NIGHTCORE
			elif _mod.lower().strip() == "fl" or _mod == "1024":
				newMods |= mods.FLASHLIGHT
			elif _mod.lower().strip() == "at" or _mod == "2048":
				newMods |= mods.AUTOPLAY
			elif _mod.lower().strip() == "so" or _mod == "4096":
				newMods |= mods.SPUNOUT
			elif _mod.lower().strip() == "ap" or _mod == "8192":
				newMods |= mods.RELAX2
			elif _mod.lower().strip() == "pf" or _mod == "16384":
				newMods |= mods.PERFECT
			elif _mod.lower().strip() == "k4" or _mod == "32768":
				newMods |= mods.KEY4
			elif _mod.lower().strip() == "k5" or _mod == "65536":
				newMods |= mods.KEY5
			elif _mod.lower().strip() == "k6" or _mod == "131072":
				newMods |= mods.KEY6
			elif _mod.lower().strip() == "k7" or _mod == "262144":
				newMods |= mods.KEY7
			elif _mod.lower().strip() == "k8" or _mod == "524288":
				newMods |= mods.KEY8
			elif _mod.lower().strip() == "KEYMOD" or _mod == "1015808":
				newMods |= mods.KEYMOD
			elif _mod.lower().strip() == "fi" or _mod == "1048576":
				newMods |= mods.FADEIN
			elif _mod.lower().strip() == "rd" or _mod == "2097152":
				newMods |= mods.RANDOM
			elif _mod.lower().strip() == "LASTMOD" or _mod == "4194304":
				newMods |= mods.LASTMOD
			elif _mod.lower().strip() == "k9" or _mod == "16777216":
				newMods |= mods.KEY9
			elif _mod.lower().strip() == "k10" or _mod == "33554432":
				newMods |= mods.KEY10
			elif _mod.lower().strip() == "k1" or _mod == "67108864":
				newMods |= mods.KEY1
			elif _mod.lower().strip() == "k3" or _mod == "134217728":
				newMods |= mods.KEY3
			elif _mod.lower().strip() == "k2" or _mod == "268435456":
				newMods |= mods.KEY2
			elif _mod.lower().strip() == "v2" or _mod == "536870912":
				newMods |= mods.SCOREV2
			elif _mod.lower().strip() == "mr" or _mod == "1073741824":
				newMods |= mods.MIRROR
			""" if _mod.lower().strip() == "hd":
				newMods |= mods.HIDDEN
			elif _mod.lower().strip() == "hr":
				newMods |= mods.HARDROCK
			elif _mod.lower().strip() == "dt":
				newMods |= mods.DOUBLETIME
			elif _mod.lower().strip() == "fl":
				newMods |= mods.FLASHLIGHT
			elif _mod.lower().strip() == "fi":
				newMods |= mods.FADEIN
			elif _mod.lower().strip() == "ez":
				newMods |= mods.EASY
			if _mod.lower().strip() == "none":
				newMods = 0 """

			if _mod.lower().strip() == "freemod" or _mod.lower().strip() == "free":
				freeMod = True
			if _mod.lower().strip() == "-" or _mod.lower().strip() == "-0":
				freeMod = True

		_match.matchModMode = matchModModes.FREE_MOD if freeMod else matchModModes.NORMAL
		_match.resetReady()
		if _match.matchModMode == matchModModes.FREE_MOD:
			_match.resetMods()
		_match.changeMods(newMods)
		return "Match mods ({}) have been updated!".format(newMods)

	def mpTeam():
		if len(message) < 3:
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp team <username> <colour>")
		username = message[1].strip()
		if not username:
			raise exceptions.invalidArgumentsException("Please provide a username")
		colour = message[2].lower().strip()
		if colour not in ["red", "blue"]:
			raise exceptions.invalidArgumentsException("Team colour must be red or blue")
		userID = userUtils.getIDSafe(username)
		if userID is None:
			raise exceptions.userNotFoundException("No such user")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.changeTeam(userID, matchTeams.BLUE if colour == "blue" else matchTeams.RED)
		return "{} is now in {} team".format(username, colour)

	def mpSettings():
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		single = False if len(message) < 2 else message[1].strip().lower() == "single"
		msg = "PLAYERS IN THIS MATCH "
		if not single:
			msg += "(use !mp settings single for a single-line version):"
			msg += "\n"
		else:
			msg += ": "
		empty = True
		for slot in _match.slots:
			if slot.user is None:
				continue
			readableStatuses = {
				slotStatuses.READY: "ready",
				slotStatuses.NOT_READY: "not ready",
				slotStatuses.NO_MAP: "no map",
				slotStatuses.PLAYING: "playing",
			}
			if slot.status not in readableStatuses:
				readableStatus = "???"
			else:
				readableStatus = readableStatuses[slot.status]
			empty = False
			msg += "* [{team}] <{status}> ~ {username}{mods}{nl}".format(
				team="red" if slot.team == matchTeams.RED else "blue" if slot.team == matchTeams.BLUE else "!! no team !!",
				status=readableStatus,
				username=glob.tokens.tokens[slot.user].username,
				mods=" (+ {})".format(scoreUtils.readableMods(slot.mods)) if slot.mods > 0 else "",
				nl=" | " if single else "\n"
			)
		if empty:
			msg += "Nobody.\n"
		msg = msg.rstrip(" | " if single else "\n")
		return msg

	def mpScoreV():
		if len(message) < 2 or message[1] not in ("1", "2"):
			raise exceptions.invalidArgumentsException("Wrong syntax: !mp scorev <1|2>")
		_match = glob.matches.matches[getMatchIDFromChannel(chan)]
		_match.matchScoringType = matchScoringTypes.SCORE_V2 if message[1] == "2" else matchScoringTypes.SCORE
		_match.sendUpdates()
		return "Match scoring type set to scorev{}".format(message[1])

	def mpHelp():
		return "Supported subcommands: !mp <{}>".format("|".join(k for k in subcommands.keys()))

	try:
		subcommands = {
			"listref": mpListRefer,
			"addref": mpAddRefer,
			"rmref": mpRemoveRefer,
			"make": mpMake,
			"close": mpClose,
			"join": mpJoin,
			"lock": mpLock,
			"unlock": mpUnlock,
			"size": mpSize,
			"move": mpMove,
			"host": mpHost,
			"clearhost": mpClearHost,
			"start": mpStart,
			"invite": mpInvite,
			"map": mpMap,
			"set": mpSet,
			"abort": mpAbort,
			"kick": mpKick,
			"password": mpPassword,
			"randompassword": mpRandomPassword,
			"mods": mpMods,
			"team": mpTeam,
			"settings": mpSettings,
            "scorev": mpScoreV,
			"help": mpHelp
		}
		requestedSubcommand = message[0].lower().strip()
		if requestedSubcommand not in subcommands:
			raise exceptions.invalidArgumentsException("Invalid subcommand")
		return subcommands[requestedSubcommand]()
	except (exceptions.invalidArgumentsException, exceptions.userNotFoundException, exceptions.invalidUserException) as e:
		return str(e)
	except exceptions.wrongChannelException:
		return "This command only works in multiplayer chat channels"
	except exceptions.matchNotFoundException:
		return "Match not found"
	except:
		raise

def switchServer(fro, chan, message):
	# Get target user ID
	target = message[0]
	newServer = message[1].strip()
	if not newServer:
		return "Invalid server IP"
	targetUserID = userUtils.getIDSafe(target)
	userID = userUtils.getID(fro)

	# Make sure the user exists
	if not targetUserID:
		return "{}: user not found".format(target)

	# Connect the user to the end server
	userToken = glob.tokens.getTokenFromUserID(userID, ignoreIRC=True, _all=False)
	userToken.enqueue(serverPackets.switchServer(newServer))

	# Disconnect the user from the origin server
	# userToken.kick()
	return "{} has been connected to {}".format(target, newServer)

def rtx(fro, chan, message):
	target = message[0]
	message = " ".join(message[1:]).strip()
	if not message:
		return "Invalid message"
	targetUserID = userUtils.getIDSafe(target)
	if not targetUserID:
		return "{}: user not found".format(target)
	userToken = glob.tokens.getTokenFromUserID(targetUserID, ignoreIRC=True, _all=False)
	userToken.enqueue(serverPackets.rtx(message))
	return ":ok_hand:"
	
def editMap(fro, chan, message): # Using Atoka's editMap with Aoba's edit
	# Put the gathered values into variables to be used later
	messages = [m.lower() for m in message]  #!map rank set [something]
	rankType = message[0]
	mapType = message[1]
	mapID = message[2]
	try:
		Force = message[3].lower() == "force"
	except:
		Force = False
	if Force:
		ForceMessage = "(Force) | "
	else:
		ForceMessage = ""

	# Get persons userID, privileges, and token
	userID = userUtils.getID(fro)
	privileges = userUtils.getPrivileges(userID)
	token = glob.tokens.getTokenFromUserID(userID)
	name = userUtils.getUsername(userID)

	# Only allow users to request maps in #admin channel or PMs with AC. Heavily reduced spam smh
	""" if chan.startswith('#') and chan != '#admin' and not privileges & 8388608:
		return "Map ranking is not permitted in regular channels, please do so in PMs with AC (or #admin if administrator)." """

	# Grab beatmapData from db
	try:
		beatmapData = glob.db.fetch("SELECT beatmapset_id, song_name, ranked FROM beatmaps WHERE beatmap_id = {} LIMIT 1".format(mapID))
		BmapName = beatmapData['song_name'].split("[")[0].rstrip()
	except:
		return "We could not find that beatmap. Perhaps check you are using the BeatmapID (not BeatmapSetID), and typed it correctly."

	if 's' in mapType.lower():
		mapType = 'set'
	#elif 'd' in mapType.lower() or 'm' in mapType.lower():
	elif 'b' in mapType.lower() or 'm' in mapType.lower():
		mapType = 'map'
	else:
		return "Please specify whether your request is a single difficulty, or a full set (map/set). Example: '!map unrank/rank/love set/map 256123 mania'."

	#비트맵의 개수가 RedstarDB랑 맞지 않으면 거절
	param = {'k': bancho_api_key, 's': beatmapData['beatmapset_id']}
	beatmap_count_check = requests.get('https://osu.ppy.sh/api/get_beatmaps', params=param)
	beatmap_count_check = beatmap_count_check.json()
	beatmap_count_check = len(beatmap_count_check)

	beatmap_count_check_redstar = glob.db.fetchAll("SELECT beatmap_id FROM beatmaps WHERE beatmapset_id = {}".format(beatmapData['beatmapset_id']))
	beatmap_count_check_redstar = len(beatmap_count_check_redstar)

	if beatmap_count_check != beatmap_count_check_redstar:
		if beatmap_count_check > beatmap_count_check_redstar and Force == False:
			return f"refused | [https://osu.ppy.sh/s/{beatmapData['beatmapset_id']} {beatmapData['beatmapset_id']}] mapset's beatmap count = {beatmap_count_check}, RedstarDB's beatmap count = {beatmap_count_check_redstar}"
		else:
			fokamessage(chan, f"[https://{server_domain}/u/{userID} {name}] | Not match | [https://osu.ppy.sh/s/{beatmapData['beatmapset_id']} {beatmapData['beatmapset_id']}] mapset's beatmap count = {beatmap_count_check}, RedstarDB's beatmap count = {beatmap_count_check_redstar}")

	# User has AdminManageBeatmaps perm
	if privileges & 256:

		# Figure out which ranked status we're requesting to
		""" if 'r' in rankType.lower():# and 'u' not in rankType.lower():
			rankType = 'ranked'
			rankTypeID = 2
			freezeStatus = 1
		#추가
		elif "a" in rankType.lower():
			rankType = "approved"
			rankTypeID = 3
			freezeStatus = 1
		elif 'l' in rankType.lower():
			rankType = 'loved'
			rankTypeID = 5
			#freezeStatus = 2
			freezeStatus = 1
		#추가
		elif "q" in rankType.lower():
			rankType = "qualified"
			rankTypeID = 4
			freezeStatus = 1
		elif 'u' in rankType.lower() or 'g' in rankType.lower():
			rankType = 'unranked'
			rankTypeID = 0
			#freezeStatus = 0
			freezeStatus = 1
		else:
			return "Please enter a valid ranked status (rank, approved, love, qualified, unrank)." """
		
		if rankType == "ranked":
			status = "ranked"
			rankTypeID = 2
			freezeStatus = 1
		elif rankType == "loved":
			status = "loved"
			rankTypeID = 5
			freezeStatus = 1
		#추가
		elif rankType == "approved":
			status = "approved"
			rankTypeID = 3
			freezeStatus = 1
		#추가
		elif rankType == "qualified":
			status = "qualified"
			rankTypeID = 4
			freezeStatus = 1
		elif rankType == "unranked":
			status = "unranked"
			rankTypeID = 0
			freezeStatus = 1
		else:
			return "Please enter a valid ranked status (ranked, approved, loved, qualified, unranked)."
		
		if beatmapData['ranked'] == rankTypeID:
			if Force:
				fokamessage(chan, f"[https://{server_domain}/u/{userID} {name}] | Skipped | This map is already {status}")
			else:
				return "This map is already {}".format(status)

		if mapType == 'set':
			numDiffs = glob.db.fetch("SELECT COUNT(id) FROM beatmaps WHERE beatmapset_id = {}".format(beatmapData["beatmapset_id"]))
			glob.db.execute("UPDATE beatmaps SET ranked = {}, ranked_status_freezed = {}, rankedby = {} WHERE beatmapset_id = {} LIMIT {}".format(rankTypeID, freezeStatus, userID, beatmapData["beatmapset_id"], numDiffs["COUNT(id)"]))
		else:
			glob.db.execute("UPDATE beatmaps SET ranked = {}, ranked_status_freezed = {}, rankedby = {} WHERE beatmap_id = {} LIMIT 1".format(rankTypeID, freezeStatus, userID, mapID ))

		# Announce / Log to admin panel logs when ranked status is changed
		log.rap(userID, "has {} beatmap ({}): {} ({})".format(status, mapType, beatmapData["song_name"], mapID), True)
		if mapType.lower() == 'set':
			msg = f"{ForceMessage}[https://{server_domain}/u/{userID} {fro}] has {status} beatmap set: [https://osu.{userDomainCheck()}/s/{beatmapData['beatmapset_id']} {BmapName}]"
		else:
			msg = f"{ForceMessage}[https://{server_domain}/u/{userID} {fro}] has {status} beatmap: [https://osu.{userDomainCheck()}/b/{mapID} {beatmapData['song_name']}]"

		chat.sendMessage(glob.BOT_NAME, "#ranked", msg)
		
		
		beatmaps = glob.db.fetchAll("SELECT beatmap_id FROM beatmaps WHERE beatmapset_id = %s", (beatmapData["beatmapset_id"],))
		
		isstd_istaiko_isctb_ismania = [0, 0, 0, 0]
		for bid in beatmaps:
			log.debug("BeatmapID = {}".format(bid["beatmap_id"]))
			mode = glob.db.fetch("SELECT difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania FROM beatmaps WHERE beatmap_id = %s", (bid["beatmap_id"],))

			isskip = 0
			#모든 모드난이도가 0일때 거르는 코드
			if isskip == 0 and mode["difficulty_std"] == 0 and mode["difficulty_taiko"] == 0 and mode["difficulty_ctb"] == 0 and mode["difficulty_mania"] == 0:
				log.warning("모든 모드의 난이도가 0임, BeatmapID = {}".format(bid["beatmap_id"]))
				log.warning("DB에서 {} 비트맵 데이터 삭제.".format(bid["beatmap_id"]))
				glob.db.execute("DELETE FROM beatmaps WHERE beatmap_id = %s", (bid["beatmap_id"],))
				isskip = 1
			#std
			if isstd_istaiko_isctb_ismania[0] == 0:
				if isskip == 0 and mode["difficulty_std"] != 0:
					log.info(" {} = STD".format(bid["beatmap_id"]))
					isstd_istaiko_isctb_ismania[0] = 1
					isskip = 1
			#Taiko
			if isstd_istaiko_isctb_ismania[1] == 0:
				if isskip == 0 and mode["difficulty_std"] == 0 and mode["difficulty_taiko"] != 0:
					log.info(" {} = Taiko".format(bid["beatmap_id"]))
					isstd_istaiko_isctb_ismania[1] = 1
					isskip = 1
			#ctb
			if isstd_istaiko_isctb_ismania[2] == 0:
				if isskip == 0 and mode["difficulty_std"] == 0 and mode["difficulty_ctb"] != 0:
					log.info(" {} = CTB".format(bid["beatmap_id"]))
					isstd_istaiko_isctb_ismania[2] = 1
					isskip = 1
			#Mania
			if isstd_istaiko_isctb_ismania[3] == 0:
				if isskip == 0 and mode["difficulty_std"] == 0 and mode["difficulty_mania"] != 0:
					log.info(" {} = Mania".format(bid["beatmap_id"]))
					isstd_istaiko_isctb_ismania[3] = 1
					isskip = 1
		
		log.info("BeatmapSet, isstd_istaiko_isctb_ismania = {}".format(isstd_istaiko_isctb_ismania))

		with_mode_text_1 = ""
		with_mode_text_2 = ""
		with_mode_text_3 = ""
		with_mode_text_4 = ""

		#with_mode_text 1 ~ 4 값 세팅
		xx_i = 0
		for xx in isstd_istaiko_isctb_ismania:
			if xx == 1:
				if xx_i == 0:
					with_mode_text_1 = "With Std!!  "
				if xx_i == 1:
					with_mode_text_2 = "With Taiko!!  "
				if xx_i == 2:
					with_mode_text_3 = "With Ctb!!  "
				if xx_i == 3:
					with_mode_text_4 = "With Mania!!  "
			xx_i += 1

		xx_i = 0

		URL = glob.conf.config["discord"]["ranked-std"]
		from discord_webhook import DiscordWebhook, DiscordEmbed
		if mapType == "set":
			for xx in isstd_istaiko_isctb_ismania:
				if xx == 1:
					if xx_i == 0:
						URL = glob.conf.config["discord"]["ranked-std"]
					if xx_i == 1:
						URL = glob.conf.config["discord"]["ranked-taiko"]
					if xx_i == 2:
						URL = glob.conf.config["discord"]["ranked-ctb"]
					if xx_i == 3:
						URL = glob.conf.config["discord"]["ranked-mania"]

					webhook = DiscordWebhook(url=URL)
					embed = DiscordEmbed(description=f"{ForceMessage}Status Changed by {name}", color=13781460)#13781460
					embed.set_author(name=f"{BmapName} was just {status} \n{with_mode_text_1}{with_mode_text_2}{with_mode_text_3}{with_mode_text_4} (Beatmap_Set)", url=f"https://{server_domain}/b/{mapID}", icon_url=f"https://a.{server_domain}/{userID}") #will rank to random diff but yea
					embed.set_footer(text="via pep.py!")
					#embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{BeatmapSet}/covers/cover.jpg")
					embed.set_image(url=f"https://b.{server_domain}/bg/+{beatmapData['beatmapset_id']}")
					webhook.add_embed(embed)
					webhook.execute()
					print(" * Posting webhook! (set)")

				xx_i += 1
		else:
			mode2 = glob.db.fetch("SELECT difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania FROM beatmaps WHERE beatmap_id = %s", (mapID,))
			if mode2["difficulty_std"] != 0:
				URL = glob.conf.config["discord"]["ranked-std"]
			elif mode2["difficulty_taiko"] != 0:
				URL = glob.conf.config["discord"]["ranked-taiko"]
			elif mode2["difficulty_ctb"] != 0:
				URL = glob.conf.config["discord"]["ranked-ctb"]
			elif mode2["difficulty_mania"] != 0:
				URL = glob.conf.config["discord"]["ranked-mania"]
			
			webhook = DiscordWebhook(url=URL)
			embed = DiscordEmbed(description=f"{ForceMessage}Status Changed by {name}", color=13781460) #this is giving me discord.py vibes
			embed.set_author(name=f"{beatmapData['song_name']} was just {status} (Beatmap)", url=f"https://{server_domain}/b/{mapID}", icon_url=f"https://a.{server_domain}/{userID}")
			embed.set_footer(text="via pep.py!")
			#embed.set_image(url=f"https://assets.ppy.sh/beatmaps/{mapa[1]}/covers/cover.jpg")
			embed.set_image(url=f"https://b.{server_domain}/bg/{mapID}")
			webhook.add_embed(embed)
			webhook.execute()
			print(" * Posting webhook! (map)")

		""" if glob.conf.config["discord"]["enable"]:
			if mapType == "set":
				webhookdesp = "{} (set) has been {} by {}".format(beatmapData["song_name"], status, name)
			else:
				webhookdesp = "{} has been {} by {}".format(beatmapData["song_name"], status, name)

			webhook = aobaHelper.Webhook(URL, color=0xadd8e6, footer="This beatmap was {} on osu!Redstar".format(status))
			#webhook.set_author(name=name, icon='https://a.debian.moe/{}'.format(str(userID)), url="https:/debian.moe/u/{}".format(str(userID)))
			webhook.set_author(name=name, icon='https://a.redstar.moe/{}'.format(str(userID)), url="https:/redstar.moe/u/{}".format(str(userID)))
			webhook.set_title(title="New {} map!".format(status), url='https://redstar.moe/b/{}'.format(str(mapID)))
			webhook.set_desc(webhookdesp)
			webhook.set_image(f"https://b.redstar.moe/bg/+{beatmapData['beatmapset_id']}")
			webhook.post()
			print(" * Posting webhook! (map)") """

		return msg

def postAnnouncement(fro, chan, message): # Post to #announce ingame
	announcement = ' '.join(message[0:])
	chat.sendMessage(glob.BOT_NAME, "#announce", announcement)
	userID = userUtils.getID(fro)
	name = userUtils.getUsername(userID)

	if glob.conf.config["discord"]["enable"] == True:
		webhook = aobaHelper.Webhook(glob.conf.config["discord"]["announcement"], color=0xadd8e6, footer="This announcement was posted in-game")
		#webhook.set_author(name=name, icon='https://a.debian.moe/{}'.format(str(userID)), url="https://debian.moe/u/{}".format(str(userID)))
		webhook.set_author(name=name, icon='https://a.{}/{}'.format(server_domain, str(userID)), url="https://{}/u/{}".format(server_domain, str(userID)))
		webhook.set_title(title="=-= ANNOUNCEMENT =-=")
		webhook.set_desc(announcement)
		webhook.post()

	return "Announcement successfully sent."

def usePPBoard(fro, chan, message):
	messages = [m.lower() for m in message]
	relax = message[0]

	userID = userUtils.getID(fro)

	if "rx" in relax.lower():
		modsType = "rx"
	elif "ap" in relax.lower():
		modsType = "ap"
	elif "vn" in relax.lower():
		modsType = "vn"

	try:
		force = message[1] == "force" if modsType == "rx" or modsType == "ap" else False
	except:
		force = False

	# Set PPBoard value in user_stats table
	userUtils.setPPBoard(userID, modsType, force=force)
	return "{forced}You're using PPBoard in {rx}.".format(forced="Force | " if force else "", rx='relax' if modsType == "rx" else ("autopilot" if modsType == "ap" else "vanilla"))

def useScoreBoard(fro, chan, message):
	messages = [m.lower() for m in message]
	relax = message[0]

	userID = userUtils.getID(fro)
	
	if "rx" in relax.lower():
		modsType = "rx"
	elif "ap" in relax.lower():
		modsType = "ap"
	elif "vn" in relax.lower():
		modsType = "vn"

	try:
		force = message[1] == "force" if modsType == "rx" or modsType == "ap" else False
	except:
		force = False

	# Set PPBoard value in user_stats table
	userUtils.setScoreBoard(userID, modsType, force=force)
	return "{forced}You're using Scoreboard in {rx}.".format(forced="Force | " if force else "", rx='relax' if modsType == "rx" else ("autopilot" if modsType == "ap" else "vanilla"))

def whitelistUserPPLimit(fro, chan, message):
	messages = [m.lower() for m in message]
	target = message[0]
	relax = message[1]

	userID = userUtils.getID(target)

	if userID == 0:
		return "That user does not exist."

	if 'x' in relax:
		rx = True
	else:
		rx = False

	userUtils.whitelistUserPPLimit(userID, rx)
	return "{user} has been whitelisted from autorestrictions on {rx}.".format(user=target, rx='relax' if rx else 'vanilla')

# Redstar, catboy, 네리냥, 치무, 블켓, 사요봇, 비트,
def redstar(fro, chan, message):
	#일반 채팅에서 !dl 사용
	try:
		try:
			matchID = getMatchIDFromChannel(chan)
		except exceptions.wrongChannelException:
			matchID = None
		try:
			spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
		except exceptions.wrongChannelException:
			spectatorHostUserID = None

		if matchID is not None:
			if matchID not in glob.matches.matches:
				return "This match doesn't seem to exist... Or does it...?"
			beatmapID = glob.matches.matches[matchID].beatmapID
		else:
			spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
			if spectatorHostToken is None:
				return "The spectator host is offline."
			beatmapID = spectatorHostToken.beatmapID
		return redstarMessage(beatmapID)
	except:
		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False
		userID = token.userID

		log.warning(f"[https://{server_domain}/u/{userID} {fro}] use !dl on {chan} channel!")

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0:
			return "Please give me a beatmap first with /np command."

		return redstarMessage(token.tillerino[0])

def catboy(fro, chan, message):
	#일반 채팅에서 !dl 사용
	try:
		try:
			matchID = getMatchIDFromChannel(chan)
		except exceptions.wrongChannelException:
			matchID = None
		try:
			spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
		except exceptions.wrongChannelException:
			spectatorHostUserID = None

		if matchID is not None:
			if matchID not in glob.matches.matches:
				return "This match doesn't seem to exist... Or does it...?"
			beatmapID = glob.matches.matches[matchID].beatmapID
		else:
			spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
			if spectatorHostToken is None:
				return "The spectator host is offline."
			beatmapID = spectatorHostToken.beatmapID
		return catboyMessage(beatmapID)
	except:
		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False
		userID = token.userID

		log.warning(f"[https://{server_domain}/u/{userID} {fro}] use !catboy on {chan} channel!")

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0:
			return "Please give me a beatmap first with /np command."

		return redstarMessage(token.tillerino[0])

def nerinyan(fro, chan, message):
	#일반 채팅에서 !dl 사용
	try:
		try:
			matchID = getMatchIDFromChannel(chan)
		except exceptions.wrongChannelException:
			matchID = None
		try:
			spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
		except exceptions.wrongChannelException:
			spectatorHostUserID = None

		if matchID is not None:
			if matchID not in glob.matches.matches:
				return "This match doesn't seem to exist... Or does it...?"
			beatmapID = glob.matches.matches[matchID].beatmapID
		else:
			spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
			if spectatorHostToken is None:
				return "The spectator host is offline."
			beatmapID = spectatorHostToken.beatmapID
		return nerinyanMessage(beatmapID)
	except:
		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False
		userID = token.userID

		log.warning(f"[https://{server_domain}/u/{userID} {fro}] use !nerinyan on {chan} channel!")

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0:
			return "Please give me a beatmap first with /np command."

		return nerinyanMessage(token.tillerino[0])

def chimu(fro, chan, message):
	try:
		matchID = getMatchIDFromChannel(chan)
	except exceptions.wrongChannelException:
		matchID = None
	try:
		spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
	except exceptions.wrongChannelException:
		spectatorHostUserID = None

	if matchID is not None:
		if matchID not in glob.matches.matches:
			return "This match doesn't seem to exist... Or does it...?"
		beatmapID = glob.matches.matches[matchID].beatmapID
	else:
		spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
		if spectatorHostToken is None:
			return "The spectator host is offline."
		beatmapID = spectatorHostToken.beatmapID
	return chimuMessage(beatmapID)	

def bloodcat(fro, chan, message):
	try:
		matchID = getMatchIDFromChannel(chan)
	except exceptions.wrongChannelException:
		matchID = None
	try:
		spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
	except exceptions.wrongChannelException:
		spectatorHostUserID = None

	if matchID is not None:
		if matchID not in glob.matches.matches:
			return "This match doesn't seem to exist... Or does it...?"
		beatmapID = glob.matches.matches[matchID].beatmapID
	else:
		spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
		if spectatorHostToken is None:
			return "The spectator host is offline."
		beatmapID = spectatorHostToken.beatmapID
	return bloodcatMessage(beatmapID)

def sayobot(fro, chan, message):
	try:
		matchID = getMatchIDFromChannel(chan)
	except exceptions.wrongChannelException:
		matchID = None
	try:
		spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
	except exceptions.wrongChannelException:
		spectatorHostUserID = None

	if matchID is not None:
		if matchID not in glob.matches.matches:
			return "This match doesn't seem to exist... Or does it...?"
		beatmapID = glob.matches.matches[matchID].beatmapID
	else:
		spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
		if spectatorHostToken is None:
			return "The spectator host is offline."
		beatmapID = spectatorHostToken.beatmapID
	return sayobotMessage(beatmapID)	

def beatconnect(fro, chan, message):
	try:
		matchID = getMatchIDFromChannel(chan)
	except exceptions.wrongChannelException:
		matchID = None
	try:
		spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
	except exceptions.wrongChannelException:
		spectatorHostUserID = None

	if matchID is not None:
		if matchID not in glob.matches.matches:
			return "This match doesn't seem to exist... Or does it...?"
		beatmapID = glob.matches.matches[matchID].beatmapID
	else:
		spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
		if spectatorHostToken is None:
			return "The spectator host is offline."
		beatmapID = spectatorHostToken.beatmapID
	return beatconnectMessage(beatmapID)

def mirror(fro, chan, message):
	#일반 채팅에서 !dl 사용
	try:
		try:
			matchID = getMatchIDFromChannel(chan)
		except exceptions.wrongChannelException:
			matchID = None
		try:
			spectatorHostUserID = getSpectatorHostUserIDFromChannel(chan)
		except exceptions.wrongChannelException:
			spectatorHostUserID = None

		if matchID is not None:
			if matchID not in glob.matches.matches:
				return "This match doesn't seem to exist... Or does it...?"
			beatmapID = glob.matches.matches[matchID].beatmapID
		else:
			spectatorHostToken = glob.tokens.getTokenFromUserID(spectatorHostUserID, ignoreIRC=True)
			if spectatorHostToken is None:
				return "The spectator host is offline."
			beatmapID = spectatorHostToken.beatmapID
		return mirrorMessage(beatmapID)
	except:
		# Get token and user ID
		token = glob.tokens.getTokenFromUsername(fro)
		if token is None:
			return False
		userID = token.userID

		log.warning(f"[https://{server_domain}/u/{userID} {fro}] use !mirror on {chan} channel!")

		# Make sure the user has triggered the bot with /np command
		if token.tillerino[0] == 0:
			return "Please give me a beatmap first with /np command."

		return mirrorMessage(token.tillerino[0])
	

def mods_list(message):
	newMods = 0
	freeMod = False
	log.info("message[1:] = {}".format(message[1:]))
	for _mod in message[1:]:
		log.info("_mod = {}".format(_mod))
		
		if _mod.isdigit():
			log.info("_mod {} 값이 숫자임을 감지".format(_mod))

		if _mod.lower().strip() == "none" or _mod == "0" or _mod == "" or _mod == " ":
			newMods = 0
			break
		elif _mod.lower().strip() == "nf" or _mod == "1":
			newMods |= mods.NOFAIL
		elif _mod.lower().strip() == "ez" or _mod == "2":
			newMods |= mods.EASY
		elif _mod.lower().strip() == "td" or _mod == "4":
			newMods |= mods.TOUCHSCREEN
		elif _mod.lower().strip() == "hd" or _mod == "8":
			newMods |= mods.HIDDEN
		elif _mod.lower().strip() == "hr" or _mod == "16":
			newMods |= mods.HARDROCK
		elif _mod.lower().strip() == "sd" or _mod == "32":
			newMods |= mods.SUDDENDEATH
		elif _mod.lower().strip() == "dt" or _mod == "64":
			newMods |= mods.DOUBLETIME
		elif _mod.lower().strip() == "rx" or _mod == "128":
			newMods |= mods.RELAX
		elif _mod.lower().strip() == "ht" or _mod == "256":
			newMods |= mods.HALFTIME
		elif _mod.lower().strip() == "nc" or _mod == "512" or _mod == "576":
			#modsEnum += mods.NIGHTCORE
			#modsEnum += 576
			#newMods |= mods.NIGHTCORE
			newMods |= 576
		elif _mod.lower().strip() == "fl" or _mod == "1024":
			newMods |= mods.FLASHLIGHT
		elif _mod.lower().strip() == "at" or _mod == "2048":
			newMods |= mods.AUTOPLAY
		elif _mod.lower().strip() == "so" or _mod == "4096":
			newMods |= mods.SPUNOUT
		elif _mod.lower().strip() == "ap" or _mod == "8192":
			newMods |= mods.RELAX2
		elif _mod.lower().strip() == "pf" or _mod == "16384":
			newMods |= mods.PERFECT
		elif _mod.lower().strip() == "k4" or _mod == "32768":
			newMods |= mods.KEY4
		elif _mod.lower().strip() == "k5" or _mod == "65536":
			newMods |= mods.KEY5
		elif _mod.lower().strip() == "k6" or _mod == "131072":
			newMods |= mods.KEY6
		elif _mod.lower().strip() == "k7" or _mod == "262144":
			newMods |= mods.KEY7
		elif _mod.lower().strip() == "k8" or _mod == "524288":
			newMods |= mods.KEY8
		elif _mod.lower().strip() == "KEYMOD" or _mod == "1015808":
			newMods |= mods.KEYMOD
		elif _mod.lower().strip() == "fi" or _mod == "1048576":
			newMods |= mods.FADEIN
		elif _mod.lower().strip() == "rd" or _mod == "2097152":
			newMods |= mods.RANDOM
		elif _mod.lower().strip() == "LASTMOD" or _mod == "4194304":
			newMods |= mods.LASTMOD
		elif _mod.lower().strip() == "k9" or _mod == "16777216":
			newMods |= mods.KEY9
		elif _mod.lower().strip() == "k10" or _mod == "33554432":
			newMods |= mods.KEY10
		elif _mod.lower().strip() == "k1" or _mod == "67108864":
			newMods |= mods.KEY1
		elif _mod.lower().strip() == "k3" or _mod == "134217728":
			newMods |= mods.KEY3
		elif _mod.lower().strip() == "k2" or _mod == "268435456":
			newMods |= mods.KEY2
		elif _mod.lower().strip() == "v2" or _mod == "536870912":
			newMods |= mods.SCOREV2
		elif _mod.lower().strip() == "mr" or _mod == "1073741824":
			newMods |= mods.MIRROR

		if _mod.lower().strip() == "freemod" or _mod.lower().strip() == "free":
			freeMod = True
		if _mod.lower().strip() == "-" or _mod.lower().strip() == "-0":
			freeMod = True

	log.info("newMods = {}".format(newMods))
	return newMods

def ingame_rank_request(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	# Make sure the user has triggered the bot with /np command
	if token.tillerino[0] == 0:
		return "Please give me a beatmap first with /np command."

	bid = token.tillerino[0]

	isranked = glob.db.fetch(f"SELECT ranked, song_name, beatmapset_id, ranked_status_freezed, rankedby FROM beatmaps WHERE beatmap_id = {bid}")
	if isranked is None:
		fokamessage(chan, f"{bid} 비트맵은 Redstar DB에 존재하지 않습니다. 또는 Bancho에서 삭제된 맵일 가능성이 높습니다.")
		fokamessage(chan, f"{bid} beatmap does not exist in Redstar DB. or Most likely a map that has been removed from Bancho.")
		return

	#userID = userUtils.getID(fro)
	rqcheck = glob.db.fetch(f"SELECT * FROM rank_requests WHERE bid = {bid}")
	if isranked["ranked"] == 0 and isranked["ranked_status_freezed"] == 0:
		if rqcheck is None:
			log.info("pep | 리퀘 요청 중")
			glob.db.execute(f"INSERT INTO rank_requests (id, userid, bid, type, time, blacklisted) VALUES ('NULL', {userID}, {bid}, 'b', {time.time()}, 0)")
		else:
			log.warning("pep | 리퀘가 존재함")
			return "request exists"
		
		time.sleep(1)

		log.info("pep | 어드민 패널 퀄파셋 요청")
		r = requests.get(f'https://admin.{server_domain}/frontend/rank_request/set_qualified/b/{bid}')
		r = r.text
		
		#데이터 처리량 많을때 리턴 인게임에서 rebuse 뜸
		fokamessage(chan, r)

		return f"[https://{server_domain}/u/{userID} {fro}] | [https://osu.{userDomainCheck()}/s/{isranked['beatmapset_id']} {isranked['song_name']}] Changed Qualified!"
	else:
		if isranked["ranked"] is 0:
			ranked_status_txt = "unranked"
		elif isranked["ranked"] is 2:
			ranked_status_txt = "ranked"
		elif isranked["ranked"] is 5:
			ranked_status_txt = "loved"
		elif isranked["ranked"] is 3:
			ranked_status_txt = "approved"
		elif isranked["ranked"] is 4:
			ranked_status_txt = "qualified"
		else:
			ranked_status_txt = "Ranked status not found"

		if rqcheck is None and isranked["ranked"] is 4:
			log.info("pep | 리퀘 재요청 중 ({}된 맵)".format(ranked_status_txt))
			glob.db.execute(f"INSERT INTO rank_requests (id, userid, bid, type, time, blacklisted) VALUES ('NULL', {userID}, {bid}, 'b', {time.time()}, 0)")
			fokamessage(chan, f"[https://osu.{userDomainCheck()}/b/{bid} {bid}] 비트맵은 {ranked_status_txt}상태이고 리퀘만 누락되어 리퀘 재요청함")
		
		log.warning("{} 해당 비트맵 상태 = {}".format(bid, ranked_status_txt))
		
		rankedby_msg = f"[https://{server_domain}/u/{isranked['rankedby']} {userUtils.getUsername(isranked['rankedby'])}]"  if isranked["rankedby"] != "Bancho" else "Bancho"
		

		return f"refuse [https://{server_domain}/u/{userID} {fro}] | [https://osu.{userDomainCheck()}/b/{bid} {isranked['song_name']}] is {ranked_status_txt} by {rankedby_msg}"

def song_info(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	# Make sure the user has triggered the bot with /np command
	if token.tillerino[0] == 0:
		return "Please give me a beatmap first with /np command."

	bid = token.tillerino[0]

	try:
		#songinfo = glob.db.fetch(f"SELECT ranked, song_name, beatmapset_id FROM beatmaps WHERE beatmap_id = {message[0]}")
		songinfo = glob.db.fetch(f"SELECT * FROM beatmaps WHERE beatmap_id = {bid}")
		
		if songinfo is None:
			fokamessage(chan, f"{bid} 비트맵은 Redstar DB에 존재하지 않습니다. Bancho에서 삭제된 맵일 가능성이 높습니다.")
			fokamessage(chan, f"{bid} beatmap does not exist in Redstar DB. Most likely a map that has been removed from Bancho.")
			return
		
		if songinfo['rankedby'] != "Bancho":
			rankedby_username = glob.db.fetch(f"SELECT username FROM users WHERE id = {songinfo['rankedby']}")
			rankedby_username = rankedby_username['username']
			
			rankedby_msg = f"(Ranked by [https://{server_domain}/u/{songinfo['rankedby']} {rankedby_username}])"

		else:
			#rankedby_msg = f"(Ranked by [https://osu.ppy.sh/b/{songinfo['beatmap_id']}] Bancho)"
			rankedby_msg = f"(Ranked by Bancho)"
		
		#newMods = mods_list(message)
		newMods = tillerinoMods(fro, chan, message if message != [] else ["no"], modsNumType="!songinfo")

		log.info("pp_songinfo 조회중...")
		r = requests.get(f"{letsapiurl}/v1/pp?b={bid}&m={newMods}").json()

		try:
			pp_msg = f"100%={round(r['pp'][0])}pp,  99%={round(r['pp'][1])}pp,  98%={round(r['pp'][2])}pp,  95%={round(r['pp'][3])}pp"
		except:
			pp_msg = f"Query = {r}"

		request_link = f"https://old.{server_domain}/letsapi/v1/pp?b={bid}&m={newMods}"
		
		newMods_name = f"{'+' + message[0].upper() + ' pp' if message != [] else 'pp'}"

		if songinfo["ranked"] is 0:
			ranked_status_txt = "Unranked"
		elif songinfo["ranked"] is 2:
			ranked_status_txt = "Ranked"
		elif songinfo["ranked"] is 5:
			ranked_status_txt = "Loved"
		elif songinfo["ranked"] is 3:
			ranked_status_txt = "Approved"
		elif songinfo["ranked"] is 4:
			ranked_status_txt = "Qualified"
		else:
			ranked_status_txt = "Ranked status not found"

		#Bancho api 조회
		try:
			log.info("Bancho date 조회중...")
			bancho_info = requests.get(f'https://osu.ppy.sh/api/get_beatmaps?k={bancho_api_key}&b={bid}').json()[0]
		except:
			log.error("!songinfo | Bancho date 오류 (Bancho 불러오기 실패)")
			bancho_info = {'submit_date':0, 'last_update':0, 'approved_date':0}#, 'total_length':0}
			log.info(f"bancho_info = {bancho_info}")

		#Redstar api 조회
		try:
			log.info("Redstar date 조회중...")
			redstar_info = requests.get(f'https://{server_domain}/api/v1/get_beatmaps?b={bid}').json()[0]
			if songinfo['rankedby'] != "Bancho":
				redstar_last_update_date = f", (last_update = {redstar_info['last_update']})"
			else:
				redstar_last_update_date = ""
		except:
			redstar_last_update_date = ""

		def culc_length(l):
			h = "{0:02d}".format(l // 60 // 60)
			m = "{0:02d}".format(l // 60)
			s = "{0:02d}".format(l % 60)
			return f"{h}:{m}:{s}"

		try:
			l = int(bancho_info["total_length"])

			length = culc_length(l)

			if (newMods & mods.DOUBLETIME > 0) or (newMods & mods.NIGHTCORE > 0):
				log.info("!songinfo | length 'DT' 감지")
				l = round(l / 1.5)
				length += f" (DT {culc_length(l)})"
			elif newMods & mods.HALFTIME > 0:
				log.info("!songinfo | length 'HT' 감지")
				l = round(l / 0.75)
				length += f" (HT {culc_length(l)})"
			else:
				pass
		except:
			log.error("!songinfo | length 오류 (Bancho 불러오기 실패)")
			log.info("!songinfo | redstar 요청")
			try:
				l = int(redstar_info["total_length"])

				length = culc_length(l)

				if (newMods & mods.DOUBLETIME > 0) or (newMods & mods.NIGHTCORE > 0):
					log.info("!songinfo | length 'DT' 감지")
					l = round(l / 1.5)
					length += f" (DT {culc_length(l)})"
				elif newMods & mods.HALFTIME > 0:
					log.info("!songinfo | length 'HT' 감지")
					l = round(l * 1.5)
					length += f" (HT {culc_length(l)})"
				else:
					pass
			except:
				log.error("!songinfo | length 오류 (Bancho, redstar 불러오기 실패)")
				length = "| ERROR | 00:00:00"

		try:
			bancho_info["approved"] = int(bancho_info["approved"])
			if bancho_info["approved"] == -2:
				bancho_ranked_status = "Graveyard (Unranked)"
			elif bancho_info["approved"] == -1:
				bancho_ranked_status = "WIP (Unranked)"
			elif bancho_info["approved"] == 0:
				bancho_ranked_status = "Pending (Unranked)"
			elif bancho_info["approved"] == 1:
				bancho_ranked_status = "Ranked"
			elif bancho_info["approved"] == 2:
				bancho_ranked_status = "Approved"
			elif bancho_info["approved"] == 3:
				bancho_ranked_status = "Qualified"
			elif bancho_info["approved"] == 4:
				bancho_ranked_status = "Loved"
			else:
				bancho_ranked_status = "Ranked status not found"
		except:
			bancho_ranked_status = "Ranked status not found"

		try:
			creator = f"[https://osu.ppy.sh/users/{bancho_info['creator_id']} {bancho_info['creator']}]"
		except:
			creator = f"Not Found"
		
		msg = f"[https://{server_domain}/u/{userID} {fro}] | "
		msg += f"[https://osu.{userDomainCheck()}/b/{bid} {songinfo['song_name']}] is {ranked_status_txt} {rankedby_msg}{redstar_last_update_date} | "
		msg += f"{newMods_name} is [{request_link} {pp_msg}] | "
		msg += f"Beatmap_md5 = [https://old.{server_domain}/letsapi/v1/find-beatmap-md5?md5={songinfo['beatmap_md5']} {songinfo['beatmap_md5']}], BeatmapID = [https://{userDomainCheck()}/b/{songinfo['beatmap_id']} {songinfo['beatmap_id']}], BeatmapSetID = [https://osu.ppy.sh/s/{songinfo['beatmapset_id']} {songinfo['beatmapset_id']}] | "
		msg += f"length = {length}, maxCombo = {songinfo['max_combo']}, bpm = {songinfo['bpm']}, AR = {songinfo['ar']}, OD = {songinfo['od']} | "
		msg += f"difficulty_std = {songinfo['difficulty_std']}, difficulty_taiko = {songinfo['difficulty_taiko']}, difficulty_ctb = {songinfo['difficulty_ctb']}, difficulty_mania = {songinfo['difficulty_mania']} | "
		msg += f"Creator = {creator}, submit_date = {bancho_info['submit_date']}, last_update = {bancho_info['last_update']}, approved_date = {bancho_info['approved_date']}, ({bancho_ranked_status} In Bancho) | "
		msg += f"[osu://b/{songinfo['beatmap_id']} osu!direct]"

		return msg
	except:
		log.error("ERROR | song_info() 함수 예외처리됨")
		msg = f"ERROR | [https://{server_domain}/u/{userID} {fro}] | "
		msg += f"[https://osu.{userDomainCheck()}/b/{bid} {bid}] beatmap does not exist in Redstar DB. Most likely a map that has been removed from Bancho."
		return msg
	
def md5tobid(fro, chan, message):
	userID = userUtils.getID(fro)
	try:
		r = requests.get(f"{letsapiurl}/v1/find-beatmap-md5?md5={message[0]}").json()
		msg = f"[https://{server_domain}/u/{userID} {fro}] | [https://old.{server_domain}/letsapi/v1/find-beatmap-md5?md5={message[0]} Link]  [https://osu.{userDomainCheck()}/b/{r['beatmap_id']} {r['beatmap_id']}]"
		return msg
	except:
		log.error("ERROR | md5tobid() 함수 예외처리됨")
		msg = f"ERROR | [https://{server_domain}/u/{userID} {fro}] | [https://old.{server_domain}/letsapi/v1/find-beatmap-md5?md5={message[0]} https://old.{server_domain}/letsapi/v1/find-beatmap-md5?md5={message[0]}]"
		return msg
def tokenTillerino(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	# Make sure the user has triggered the bot with /np command
	if token.tillerino[0] == 0:
		try:
			if token.tillerino[3] is not None:
				fokamessage(chan, f"NODATA 2 | {token.tillerino}")
				return "Please give me a beatmap first with /np command. XD"
		except:
			fokamessage(chan, f"NODATA | {token.tillerino}")
			return "Please give me a beatmap first with /np command."
	
	log.info(f"[Beatmap_ID, mod (number), acc]  |  {token.tillerino}")
	return f"[Beatmap_ID, mod (number), acc]  |  {token.tillerino}"

def delTokenTillerino(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	token.tillerino[0] = 0
	token.tillerino[1] = 0
	token.tillerino[2] = -1.0
	try:
		if token.tillerino[3] is not None:
			token.tillerino[3] = "by !del token.tillerino"
	except:
		token.tillerino.append("by !del token.tillerino")
		
	return f"Done | {token.tillerino}"

def inputTokenTillerino(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	del message[0]
	
	for i in range(4):
		try:
			token.tillerino[i] = message[i]
		except:
			try:
				token.tillerino[i] = 0
			except:
				token.tillerino.append(0)
	
	if token.tillerino[3] == 0:
		token.tillerino[3] = "by !input token.tillerino"
	else:
		token.tillerino.append("by !input token.tillerino")
		
	return f"Done | {token.tillerino}"

def kickself(fro, chan, message):
	# Get parameters
	target = fro.lower()
	if target == glob.BOT_NAME.lower():
		return "Nope."

	# Get target token and make sure is connected
	tokens = glob.tokens.getTokenFromUsername(userUtils.safeUsername(target), safe=True, _all=True)
	if len(tokens) == 0:
		return "{} is not online".format(target)

	# Kick users
	for i in tokens:
		i.kick()

	# Bot response
	return "{} has been self kicked from the server.".format(target)

def bpp_with_tillerinoLast(fro, chan, message):
	return tillerinoLast(fro=fro, chan=chan, message=message, bpp_command=True)

def view_banneduser_record_ingame(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	dbcheck = glob.db.fetch("SELECT value_int FROM system_settings WHERE name = 'view_banneduser_record_ingame'")
	if dbcheck is None:
		log.error("ERROR | view_banneduser_record_ingame | dbcheck is None")
		return "DB ERROR"

	if message[0].lower() == "true" or message[0] == "1":
		lock = 1
	elif message[0].lower() == "check":
		return str(dbcheck["value_int"])
	else:
		lock = 0
		
	if dbcheck["value_int"] == lock:
		log.warning(f"view_banneduser_record_ingame | 바꾸려는 상태와 현재 상태 동일함.")
		return "refused | The state to be replaced is the same as the current state."
	
	log.rap(userID, f"{fro} ({userID}) has changed view_banneduser_record_ingame. {dbcheck['value_int']} --> {lock}", through="pep.py")
	log.info(f"{fro} ({userID}) has changed view_banneduser_record_ingame. {dbcheck['value_int']} --> {lock}")

	glob.db.execute(f"UPDATE system_settings SET value_int = {lock} WHERE name = 'view_banneduser_record_ingame'")
	return f"[https://{server_domain}/u/{userID} {fro}] ({userID}) has changed view_banneduser_record_ingame. {dbcheck['value_int']} --> {lock}"

def replayID_convert(fro, chan, message):

	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	replayMType = message[0].upper()
	replayID = message[1]

	if replayMType == "VN":
		type = ["Vanilla", "", ""]
	elif replayMType == "RX":
		type = ["Relax", "_relax", "rx/"]
	elif replayMType == "AP":
		type = ["AP", "_ap", "ap/"]
	else:
		type = ["Vanilla", "", ""]
		
	score_info = glob.db.fetch(f"SELECT userid, beatmap_md5, mods, completed, accuracy, pp, play_mode, 300_count, 100_count, 50_count, misses_count, time FROM scores{type[1]} WHERE id = {replayID}")
	if score_info is None:
		log.error("ERROR | replayID_convert | score_info is None")
		return "DB ERROR | score_info is None"
	else:
		uname = glob.db.fetch(f"SELECT username FROM users WHERE id = {score_info['userid']}")
	
	beatmap_info = glob.db.fetch(f"SELECT beatmap_id, beatmapset_id, song_name, ranked FROM beatmaps WHERE beatmap_md5 = '{score_info['beatmap_md5']}'")
	if beatmap_info is None:
		log.error("ERROR | replayID_convert | beatmap_info is None")
		return "DB ERROR | beatmap_info is None"

	mods = scoreUtils.readableMods(score_info['mods'])
	rank = generalUtils.getRank(score_info["play_mode"], score_info["mods"], score_info["accuracy"],
									score_info["300_count"], score_info["100_count"], score_info["50_count"], score_info["misses_count"])
	
	msg = f"[{type[0]}] [https://{server_domain}/u/{type[2]}{userID} {uname['username']}] | [https://osu.{userDomainCheck()}/b/{beatmap_info['beatmap_id']} {beatmap_info['song_name']}]"
	msg += f" + {mods}" if mods != "" else ""
	msg += f" ({round(score_info['accuracy'], 2)}%, {rank})"
	#ranked_status추가
		#커스텀 비트맵 추가
	if beatmap_info["beatmap_id"] <= 0:
		msg += " | Qualified (Custom Map, Deleted Map)"
	else:
		if beatmap_info["ranked"] == 2:
			msg += " | Ranked"
		elif beatmap_info["ranked"] == 5:
			msg += " | Loved"
		elif beatmap_info["ranked"] == 3:
			msg += " | Approved (Ranked)"
		elif beatmap_info["ranked"] == 4:
			msg += " | Qualified (Not Ranked Yet)"
		elif beatmap_info["ranked"] == 0:
			msg += " | Unranked"
		else:
			msg += " | Ranked status Unknown"
	if score_info["play_mode"] == 0:
		msg += " | STD"
	elif score_info["play_mode"] == 1:
		msg += " | Taiko"
	elif score_info["play_mode"] == 2:
		msg += " | CTB"
	elif score_info["play_mode"] == 3:
		msg += " | Mania"
	else:
		msg += " | UNKNOWN gamemode"
	msg += f" | {round(score_info['pp'], 2)}pp | completed = {score_info['completed']} | {unix_to_date(score_info['time'])}"
	msg += f" | BeatmapID = [https://{userDomainCheck()}/b/{beatmap_info['beatmap_id']} {beatmap_info['beatmap_id']}], BeatmapSetID = [https://osu.ppy.sh/s/{beatmap_info['beatmapset_id']} {beatmap_info['beatmapset_id']}]"
	msg += f" | [https://{server_domain}/web/replays{type[1]}/{replayID} Replay download] | [osu://b/{beatmap_info['beatmap_id']} osu!direct]"

	return msg

def history_beatmap(fro, chan, message):
	log.chat(f"history 조회중")

	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	replayMType = message[0].upper()
	bid = int(message[1])

	if replayMType == "VN":
		type = ["Vanilla", "", ""]
	elif replayMType == "RX":
		type = ["Relax", "_relax", "rx/"]
	elif replayMType == "AP":
		type = ["AP", "_ap", "ap/"]
	else:
		type = ["Vanilla", "", ""]

	md5 = glob.db.fetch(f"SELECT beatmap_md5 FROM beatmaps WHERE beatmap_id = {bid}")["beatmap_md5"]
	
	history_info = glob.db.fetchAll(f"SELECT * FROM scores{type[1]} WHERE userid = {userID} AND beatmap_md5 = '{md5}' ORDER BY id DESC")
	# id, beatmap_md5, userid, score, max_combo, full_combo, mods, 300_count, 100_count, 50_count,
	# katus_count, gekis_count, misses_count, time, play_mode, completed, accuracy, pp, playtime

	log.info(f"len(history_info) = {len(history_info)}")

	if len(history_info) == 0:
		log.error("ERROR | history_beatmap | history_info is None")
		return "DB ERROR | history_info is None"

	beatmap_info = glob.db.fetch(f"SELECT beatmap_id, beatmapset_id, song_name, ranked, max_combo as fc, difficulty_std, difficulty_taiko, difficulty_ctb, difficulty_mania FROM beatmaps WHERE beatmap_md5 = '{md5}'")
	if beatmap_info is None:
		log.error("ERROR | replayID_convert | beatmap_info is None")
		return "DB ERROR | beatmap_info is None"
	
	for data in history_info:
		msg = f"[{type[0]}] "

		#ifPlayer
		msg += f"[https://{server_domain}/u/{type[2]}{userID} {fro}] | "

		#beatmapLink
		msg  += "[https://osu.{}/b/{} {}]".format(userDomainCheck(), bid, beatmap_info["song_name"])

		if data["play_mode"] != gameModes.STD:
			msg += " <{0}>".format(gameModes.getGameModeForPrinting(data["play_mode"]))

		if data["mods"]:
			msg += ' +' + scoreUtils.readableMods(data["mods"])

		hasPP = data["play_mode"] != gameModes.CTB
		ifFc = " | {}x (FC)".format(beatmap_info["fc"]) if data["max_combo"] == beatmap_info["fc"] else " | {0}x/{1}x".format(data["max_combo"], beatmap_info["fc"])

		diffString = "difficulty_{}".format(gameModes.getGameModeForDB(data["play_mode"]))
		rank = generalUtils.getRank(data["play_mode"], data["mods"], data["accuracy"],
									data["300_count"], data["100_count"], data["50_count"], data["misses_count"])
		if not hasPP:
			msg += " | {0:,}".format(data["score"])
			msg += ifFc
			msg += " | {0:.2f}%, {1}".format(data["accuracy"], rank.upper())
			msg += " {{ {0} / {1} / {2} / {3} }}".format(data["300_count"], data["100_count"], data["50_count"], data["misses_count"])
			#pp 추가
			msg += f" | {round(data['pp'], 2)}pp"
			msg += " | {0:.2f} stars".format(data[diffString])

			#ctb token.tillerino 추가
			token.tillerino[0] = bid
			token.tillerino[1] = data["mods"]
			token.tillerino[2] = round(data["accuracy"], 2)
			try:
				token.tillerino[3] = f"by !history ({msg[0:msg.index(']') + 1]})"
			except:
				token.tillerino.append(f"by !history ({msg[0:msg.index(']') + 1]})")

			return msg
		
		msg += " ({0:.2f}%, {1})".format(data["accuracy"], rank.upper())

		#ranked_status추가
		#커스텀 비트맵 추가
		if bid <= 0:
			msg += " | Qualified (Custom Map, Deleted Map)"
		else:
			if beatmap_info["ranked"] == 2:
				msg += " | Ranked"
			elif beatmap_info["ranked"] == 5:
				msg += " | Loved"
			elif beatmap_info["ranked"] == 3:
				msg += " | Approved (Ranked)"
			elif beatmap_info["ranked"] == 4:
				msg += " | Qualified (Not Ranked Yet)"
			elif beatmap_info["ranked"] == 0:
				msg += " | Unranked"
			else:
				msg += " | Ranked status Unknown"
		#스코어 추가
		msg += " | {:,}".format(data["score"], ",d")

		msg += ifFc
		msg += " | {0:.2f}pp".format(data["pp"])

		stars = beatmap_info[diffString]
		if data["mods"]:
			token.tillerino[0] = bid
			token.tillerino[1] = data["mods"]
			token.tillerino[2] = round(data["accuracy"], 2)
			try:
				token.tillerino[3] = f"by !history ({msg[0:msg.index(']') + 1]})"
			except:
				token.tillerino.append(f"by !history ({msg[0:msg.index(']') + 1]})")
		#노모드의 경우 token.tillerino 할당이 되지 않으므로 else 추가함
		else:
			token.tillerino[0] = bid
			token.tillerino[1] = data["mods"]
			token.tillerino[2] = round(data["accuracy"], 2)
			try:
				token.tillerino[3] = f"by !history ({msg[0:msg.index(']') + 1]})"
			except:
				token.tillerino.append(f"by !history ({msg[0:msg.index(']') + 1]})")

		#if data["mods"]: 안에 속해있었는데 else: 를 추가함으로 인하여 if data["mods"]: 밖으로 뺌
		oppaiData = getPPMessage(userID, just_data=True)
		if "stars" in oppaiData:
			stars = oppaiData["stars"]

		msg += " | {0:.2f} stars".format(stars)

		#시간 추가
		msg += f" | {unix_to_date(data['time'])}"

		#completed 추가
		msg += f" | completed = {data['completed']}"
		#id (replay) 추가
		msg += f" | id (replay) = [https://{server_domain}/web/replays{type[1]}/{data['id']} {data['id']}]"
		#dl추가
		msg += " | [osu://b/{} osu!direct]".format(bid)

		fokamessage(chan, msg)

	# Send request to LETS api
	#에러 무한반복 (아니 꺼도 또 무한반복? osuapiHelper.py 에서 커스텀 비트맵 pp조회 키면 또 에러남 ㅅㅂ)
	try:
		url = f"https://old.{server_domain}/letsapi/v1/pp?b={bid}&m={data['mods']}"
		msg2 = "[{url} 100%: {pp100}pp | 99% {pp99}pp | 98%: {pp98}pp | 95%: {pp95}pp]".format(url=url, pp100=round(oppaiData["pp"][0], 2), pp99=round(oppaiData["pp"][1], 2), pp98=round(oppaiData["pp"][2], 2), pp95=round(oppaiData["pp"][3], 2))
		fokamessage(chan, msg2)
		return fokamessage(chan, f"count = {len(history_info)}")
	except:
		return fokamessage(chan, "ERROR | culc pp error | DEAD")

def map_suggest(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID

	mapType = message[0].lower()

	try:
		isset = message[1]
		try:
			setbid = message[2]
		except:
			return "NO BeatmapID!"
	except:
		isset = False

	mapList = glob.db.fetchAll(f"SELECT id, type, beatmap_id, song_name, ppMsg, datetime FROM mapsuggest WHERE type = '{mapType}'")

	if mapList == () and isset == False:
		return f"NO DATA!!!!! | mapType = {mapType}"

	if isset:
		if userID == 1000 or userID == 999:
			data = glob.db.fetch(f"SELECT song_name, pp_100, pp_99, pp_98, pp_95 FROM beatmaps WHERE beatmap_id = {setbid}")
			ppMsg = f"100%: {data['pp_100']}pp | 99%: {data['pp_99']}pp | 98%: {data['pp_98']}pp | 95%: {data['pp_95']}pp"

			query = 'INSERT INTO mapsuggest (id, type, beatmap_id, song_name, ppMsg, datetime) VALUES (%s, %s, %s, %s, %s, %s)'
			values = ("NULL", mapType, setbid, data["song_name"], ppMsg, int(time.time()))
			try:
				glob.db.execute(query, values)
				return f"Success INSERT | {mapType} | [https://osu.{userDomainCheck()}/b/{setbid} {data['song_name']}] | pp = {ppMsg} | [osu://b/{setbid} osu!direct]"
			except:
				log.error(f"setbid = {setbid} | DB INSERT 실패!")
				return f"setbid = {setbid} | DB INSERT Fail!"
		else:
			return "You have not set Permission!"
	else:
		for i in mapList:
			fokamessage(fro, f"{mapType} | [https://osu.{userDomainCheck()}/b/{i['beatmap_id']} {i['song_name']}] | pp = {i['ppMsg']} | [osu://b/{i['beatmap_id']} osu!direct]")
		return f"[https://{server_domain}/u/{userID} {fro}] Check [https://{server_domain}/u/999 Devlant]'s message!"

def servers_status(fro, chan, message):
	bancho_url = f"https://c.{server_domain}/api/v1/serverStatus"
	lets_url = f"{letsapiurl}/v1/status"
	api_url = f"https://{server_domain}/api/v1/ping"
	mediaserver_url = f"https://b.{server_domain}/status"

	try:
		bancho_status = requests.get(bancho_url).json()
		fokamessage(chan, f"Bancho : [{bancho_url} {bancho_status}]")
	except:
		fokamessage(chan, f"ERROR | [{bancho_url} Bancho]")
	try:
		lets_status = requests.get(lets_url).json()
		fokamessage(chan, f"lets : [{lets_url} {lets_status}]")
	except:
		fokamessage(chan, f"ERROR | [{lets_url} lets]")
	try:
		api_status = requests.get(api_url).json()
		fokamessage(chan, f"api : [{api_url} {api_status}]")
	except:
		fokamessage(chan, f"ERROR | [{api_url} api]")
	try:
		mediaserver_status = requests.get(mediaserver_url, headers={"User-Agent": f"https://c.{server_domain}"}).json()
		fokamessage(chan, f"mediaserver : [{mediaserver_url} {mediaserver_status}]")
	except:
		fokamessage(chan, f"ERROR | [{mediaserver_url} mediaserver]")

	return
	""" #api mirrors
		@app.route("/js/status/api")
		def ApiStatus():
			try:
				return jsonify(requests.get(UserConfig["ServerURL"] + "api/v1/ping", verify=False, timeout=1).json())
			except Exception as err:
				print("[ERROR] /js/status/api: ", err)
				return jsonify({
					"code" : 503
				})
		@app.route("/js/status/lets")
		def LetsStatus():
			try:
				return jsonify(requests.get(UserConfig["LetsAPI"] + "v1/status", verify=False, timeout=1).json()) #this url to provide a predictable result
			except Exception as err:
				print("[ERROR] /js/status/lets: ", err)
				return jsonify({
					"server_status" : 0
				})
		@app.route("/js/status/bancho")
		def BanchoStatus():
			try:
				return jsonify(requests.get(UserConfig["BanchoURL"] + "api/v1/serverStatus", verify=False, timeout=1).json()) #this url to provide a predictable result
			except Exception as err:
				print("[ERROR] /js/status/bancho: ", err)
				return jsonify({
					"result" : 0
				}) """

def tillerinoRecommand(fro, chan, message):
	# Get token and user ID
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		return False
	userID = token.userID
	
	try:
		if "RX" in message[0].upper():
			status_rx = True
			status_ap = False
		elif "AP" in message[0].upper():
			status_rx = False
			status_ap = True
		else:
			status_rx = False
			status_ap = False
	except:
		status_rx = False
		status_ap = False

	try:
		mods = message[0]
	except:
		mods = "NO"
	modsNum = tillerinoMods(fro, chan, [mods], modsNumType="!r")

	if status_rx:
		totalPP = userUtils.calculatePPRelax(userID, 0)
		try:
			avgPP = int(userUtils.calculatePPRelax(userID, 0, limit=10)) / 10
		except:
			return "[RX] NO DATA"
	elif status_ap:
		totalPP = userUtils.calculatePPAutopilot(userID, 0)
		try:
			avgPP = int(userUtils.calculatePPAutopilot(userID, 0, limit=10)) / 10
		except:
			return "[AP] NO DATA"
	else:
		totalPP = userUtils.calculatePP(userID, 0)
		try:
			avgPP = int(userUtils.calculatePP(userID, 0, limit=10)) / 10
		except:
			return "[VN] NO DATA"
	
	rcl = glob.db.fetchAll("SELECT * FROM beatmaps WHERE pp_100 BETWEEN (%s - 50) AND (%s + 50) AND ranked IN (2, 3) ORDER BY pp_100 DESC", [avgPP, avgPP])
	if rcl is None:
		return "Sorry, I'm not able to provide a recommandsList :("

	num = random.randint(1, len(rcl))
	rc = {}
	for i, j in zip(rcl, range(len(rcl))):
		if j == num:
			log.error(f"j = {j} | i = {i}")
			rc["bid"] = i["beatmap_id"]
			rc["bsid"] = i["beatmapset_id"]
			rc["songname"] = i["song_name"]
			rc["pp100"] = i["pp_100"]
			rc["pp99"] = i["pp_99"]
			rc["pp98"] = i["pp_98"]
			rc["pp95"] = i["pp_95"]

	log.info(f"tillerino r | mods = {mods} | modsNum = {modsNum}")
	log.info(f"totalPP = {totalPP} | avgPP = {avgPP}")
	log.warning(rc)

	#msg2 = "[{url} 100%: {pp100}pp | 99% {pp99}pp | 98%: {pp98}pp | 95%: {pp95}pp]".format(url=url, pp100=round(odata["pp"][0], 2), pp99=round(odata["pp"][1], 2), pp98=round(odata["pp"][2], 2), pp95=round(odata["pp"][3], 2))
	return f"[https://osu.{userDomainCheck()}/b/{rc['bid']} {rc['songname']}] {f'+{mods.upper()}' if modsNum != 0 else ''} 100%: {rc['pp100']}pp | 99% {rc['pp99']}pp | 98%: {rc['pp98']}pp | 95%: {rc['pp95']}pp [osu://b/{rc['bid']} osu!direct]"

def B_dl(fro, chan, message):
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None: log.error("ERROR: No token")
	try:
		bid = token.tillerino[0] = int(message[0])
		try: token.tillerino[3] = f"by !b {bid}"
		except: token.tillerino.append(f"by !b {bid}")
		return f"[osu://b/{bid} {bid}]"
	except: return f"{message[0]} is not Number!"

def D_dl(fro, chan, message):
	try: bsid = int(message[0]); return f"[osu://s/{bsid} {bsid}]"
	except: return f"{message[0]} is not Number!"

def BanchoLink_to_mirror(fro, chan, message):
	mode = fokabot.npRegex_BanchoWebLink(message)[0]
	beatmapID = fokabot.npRegex_BanchoWebLink(message)[1]

	if mode == "osu":
		mode = "STD"
	elif mode == "taiko":
		mode = "Taiko"
	elif mode == "fruits":
		mode = "CTB"
	elif mode == "mania":
		mode = "Mania"
	else:
		mode = "?"

	return f"{mode} | {mirrorMessage(beatmapID)}"

def multiLeaderboard(fro, chan, message):
	token = glob.tokens.getTokenFromUsername(fro)
	if token is None:
		log.error("ERROR: No token")
		return "ERROR: No token"
	bid = int(token.tillerino[0])

	# Make sure the user has triggered the bot with /np command
	if bid == 0:
		return "Please give me a beatmap first with /np command."

	beatmap_md5 = glob.db.fetch(f"SELECT beatmap_md5, song_name, mode, ranked FROM beatmaps WHERE beatmap_id = {bid}")
	beatmap_md5, songname, gamemode, ranked = (beatmap_md5["beatmap_md5"], beatmap_md5["song_name"], beatmap_md5["mode"], beatmap_md5["ranked"])

	if not gamemode: #std
		if message[0].lower() == "std" or message[0].lower() == "s": mod = 0; modType = "[STD]"
		elif message[0].lower() == "taiko" or message[0].lower() == "t": mod = 1; modType = "[Taiko]"
		elif message[0].lower() == "ctb" or message[0].lower() == "c": mod = 2; modType = "[CTB]"
		elif message[0].lower() == "mania" or message[0].lower() == "m": mod = 3; modType = "[Mania]"
		else: mod = 0; modType = "[STD]"
	else: #NOT std
		if gamemode == 0: mod = 0; modType = "[STD]"
		elif gamemode == 1: mod = 1; modType = "[Taiko]"
		elif gamemode == 2: mod = 2; modType = "[CTB]"
		elif gamemode == 3: mod = 3; modType = "[Mania]"
		else: mod = 0; modType = "[STD]"

	if message[1].lower() == "vn":
		relax = ""; sort = "score"; modeType = "[Vanilla]"
	elif message[1].lower() == "rx":
		if mod == 3: return "Doesn't Exist RX Mania"
		relax = "_relax"; sort = "pp"; modeType = "[Relax]"
	elif message[1].lower() == "ap":
		if mod != 0: return "Doesn't Exist AP Taiko, AP CTB, AP Mania"
		relax = "_ap"; sort = "pp"; modeType = "[AP]"
	else:
		relax = ""; sort = "score"; modeType = "[Vanilla]"
	if relax and (ranked == 5 or ranked == 4): sort = "score"

	if ranked == 2: rankedRead = "Ranked"
	elif ranked == 5: rankedRead = "Loved"
	elif ranked == 3: rankedRead = "Approved (Ranked)"
	elif ranked == 4: rankedRead = "Qualified (Not Ranked Yet)"
	elif ranked == 0: rankedRead = "Unranked"
	else: rankedRead = "Ranked status Unknown"

	leaderboard = glob.db.fetchAll(f"SELECT u.username, s.* FROM scores{relax} as s JOIN users AS u ON s.userid = u.id WHERE s.beatmap_md5 = %s AND s.play_mode = %s AND s.completed = 3 AND u.privileges & 1 > 0 ORDER BY {sort} DESC LIMIT 10000", [beatmap_md5, mod])
	if not leaderboard: return f"{modType} {modeType} [osu://b/{bid} {songname}] has NO DATA"

	for i, d in enumerate(leaderboard):
		clan = glob.db.fetch("SELECT tag FROM clans AS c JOIN user_clans AS uc ON c.id = uc.clan WHERE uc.user = %s", [d["userid"]])
		username = f"[{clan['tag']}] {d['username']}" if False and clan else d["username"]
		mods = scoreUtils.readableMods(d['mods'])
		if mods: mods = ' +' + mods
		rank = generalUtils.getRank(d["play_mode"], d["mods"], d["accuracy"], d["300_count"], d["100_count"], d["50_count"], d["misses_count"])
		msg = f"{modType} {modeType} #{i+1} [https://{server_domain}/u/{d['userid']} {username}] | [osu://b/{bid} {songname}]{mods} ({round(d['accuracy'], 2)}%, {rank}) | {rankedRead} | {d['score']:,} | {round(d['pp'], 2)}pp | {unix_to_date(d['time'])}"
		fokamessage(chan, msg)

####################################################################################################

def fokamessage(chan, message):
	return chat.sendMessage(glob.BOT_NAME, chan.encode().decode("latin-1"), message.encode().decode("latin-1"))

def unix_to_date(time): return datetime.fromtimestamp(int(time))

"""
Commands list

trigger: message that triggers the command
callback: function to call when the command is triggered. Optional.
response: text to return when the command is triggered. Optional.
syntax: command syntax. Arguments must be separated by spaces (eg: <arg1> <arg2>)
privileges: privileges needed to execute the command. Optional.
"""
commands = [
	{
		"trigger": "!roll",
		"callback": roll
	}, {
		"trigger": "!faq",
		"syntax": "<name>",
		"callback": faq
	}, {
		"trigger": "!report",
		"callback": report
	}, {
		"trigger": "!help",
		"response": f"Click (here)[https://{server_domain}/index.php?p=16&id=4] for full command list"
	}, {
		"trigger": "!ppboard",
		"syntax": "<relax(rx)/vanilla(vn)/autopilot(ap)>",
		"callback": usePPBoard
	}, {
		"trigger": "!scoreboard",
		"syntax": "<relax(rx)/vanilla(vn)/autopilot(ap)>",
		"callback": useScoreBoard
	}, {
		"trigger": "!whitelist",
		"privileges": privileges.ADMIN_BAN_USERS,
		"syntax": "<target> <relax/vanilla>",
		"callback": whitelistUserPPLimit
	}, {
		"trigger": "!announce",
		"syntax": "<announcement>",
		"privileges": privileges.ADMIN_SEND_ALERTS,
		"callback": postAnnouncement
	},	#{
		#"trigger": "!ask",
		#"syntax": "<question>",
		#"callback": ask
	#}, {
	{
		"trigger": "!maprq",
		"privileges": privileges.ADMIN_MANAGE_BEATMAPS,
		"callback": getBeatmapRequest
	}, {
		"trigger": "!alert",
		"syntax": "<message>",
		"privileges": privileges.ADMIN_SEND_ALERTS,
		"callback": alert
	}, {
		"trigger": "!alertuser",
		"syntax": "<username> <message>",
		"privileges": privileges.ADMIN_SEND_ALERTS,
		"callback": alertUser,
	}, {
		"trigger": "!moderated",
		"privileges": privileges.ADMIN_CHAT_MOD,
		"callback": moderated
	}, {
		"trigger": "!kickall",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": kickAll
	}, {
		"trigger": "!kick",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_KICK_USERS,
		"callback": kick
	}, {
		"trigger": "!bot reconnect",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": fokabotReconnect
	}, {
		"trigger": "!silence",
		"syntax": "<target> <amount> <unit(s/m/h/d)> <reason>",
		"privileges": privileges.ADMIN_SILENCE_USERS,
		"callback": silence
	}, {
		"trigger": "!removesilence",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_SILENCE_USERS,
		"callback": removeSilence
	}, {
		"trigger": "!채금",
		"syntax": "<target> <amount> <unit(s/m/h/d)> <reason>",
		"privileges": privileges.ADMIN_SILENCE_USERS,
		"callback": silence
	}, {
		"trigger": "!채금해제",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_SILENCE_USERS,
		"callback": removeSilence
	}, {
		"trigger": "!system restart",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemRestart
	}, {
		"trigger": "!시스템 재시작",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemRestart
	}, {
		"trigger": "!system shutdown",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemShutdown
	}, {
		"trigger": "!시스템 종료",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemShutdown
	}, {
		"trigger": "!system reload",
		"privileges": privileges.ADMIN_MANAGE_SETTINGS,
		"callback": systemReload
	}, {
		"trigger": "!시스템 리로드",
		"privileges": privileges.ADMIN_MANAGE_SETTINGS,
		"callback": systemReload
	}, {
		"trigger": "!system maintenance",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemMaintenance
	}, {
		"trigger": "!시스템 점검",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemMaintenance
	}, {
		"trigger": "!system status",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemStatus
	}, {
		"trigger": "!시스템 상태",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": systemStatus
	}, {
		"trigger": "!ban",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_BAN_USERS,
		"callback": ban
	}, {
		"trigger": "!unban",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_BAN_USERS,
		"callback": unban
	}, {
		"trigger": "!restrict",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_BAN_USERS,
		"callback": restrict
	}, {
		"trigger": "!unrestrict",
		"syntax": "<target>",
		"privileges": privileges.ADMIN_BAN_USERS,
		"callback": unrestrict
	}, {
		"trigger": "\x01ACTION is listening to",
		"callback": tillerinoNp
	}, {
		"trigger": "\x01ACTION is playing",
		"callback": tillerinoNp
	}, {
		"trigger": "\x01ACTION is watching",
		"callback": tillerinoNp
	}, {
		"trigger": "\x01ACTION is editing",
		"callback": tillerinoNp
	}, {
		"trigger": "!with",
		"callback": tillerinoMods,
		"syntax": "<mods>"
	}, {
		"trigger": "!last",
		"callback": tillerinoLast
	}, {
		"trigger": "!ir",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"callback": instantRestart
	}, {
		"trigger": "!pp",
		"callback": pp
	}, {
		"trigger": "!update",
		"callback": updateBeatmap
	}, {
		"trigger": "!mp",
		"privileges": privileges.USER_TOURNAMENT_STAFF,
		"syntax": "<subcommand>",
		"callback": multiplayer
	}, {
		"trigger": "!switchserver",
		"privileges": privileges.ADMIN_MANAGE_SERVERS,
		"syntax": "<username> <server_address>",
		"callback": switchServer
	}, {
		"trigger": "!rtx",
		"privileges": privileges.ADMIN_MANAGE_USERS,
		"syntax": "<username> <message>",
		"callback": rtx
	}, { # 네리냥, Redstar, catboy 치무, 블켓, 사요봇, 비트,
		"trigger": "!nerinyan",
		"callback": nerinyan
	}, {
		"trigger": "!dl",
		"callback": redstar
	}, {
		"trigger": "!dl2",
		"callback": nerinyan
	}, {
		"trigger": "!catboy",
		"callback": catboy
	}, {
		"trigger": "!chimu",
		"callback": chimu
	}, {
		"trigger": "!bloodcat",
		"callback": bloodcat
	}, {
		"trigger": "!bc",
		"callback": bloodcat
	}, {
		"trigger": "!sayobot",
		"callback": sayobot
	}, {
		"trigger": "!beatconnect",
		"callback": beatconnect
	}, {
		"trigger": "!mirror",
		"callback": mirror
	}, {
		"trigger": "!acc",
		"callback": tillerinoAcc,
		"syntax": "<accuarcy>"
	}, {
		"trigger": "!rankrq",
		#"syntax": "<Beatmap_id>",
		"callback": ingame_rank_request
	}, {
		"trigger": "!songinfo",
		#"syntax": "<Beatmap_id>",
		"callback": song_info
	}, {
		"trigger": "!md5tobid",
		"syntax": "<BeatmapMD5>",
		"callback": md5tobid
	}, {	#!map unrank/rank/love set/map 256123
		"trigger": "!map",
		"syntax": "<ranked/approved/loved/qualified/unranked> <set/map> <BeatmapID>",
		"privileges": privileges.ADMIN_MANAGE_BEATMAPS,
		"callback": editMap
	}, {
		"trigger": "!token.tillerino",
		"callback": tokenTillerino
	}, {
		"trigger": "!del token.tillerino",
		"callback": delTokenTillerino
	}, {
		"trigger": "!input token.tillerino",
		#"syntax": "<Beatmap_id, mods(option), acc(option), by(option)>",
		#"syntax": "<Beatmap_id> <mods(option), acc(option), by(option)>",
		"callback": inputTokenTillerino
	}, {
		"trigger": "!kickself",
		"callback": kickself
	}, {
		"trigger": "!bpp",
		"callback": bpp_with_tillerinoLast
	}, {
		"trigger": "!view_banneduser_record_ingame",
		"syntax": "<True(1)/False(0)/check>",
		"privileges": privileges.ADMIN_MANAGE_SETTINGS,
		"callback": view_banneduser_record_ingame
	}, {
		"trigger": "!vbri",
		"syntax": "<True(1)/False(0)/check>",
		"privileges": privileges.ADMIN_MANAGE_SETTINGS,
		"callback": view_banneduser_record_ingame
	}, {
		"trigger": "!view_banneduser",
		"syntax": "<True(1)/False(0)/check>",
		"privileges": privileges.ADMIN_MANAGE_SETTINGS,
		"callback": view_banneduser_record_ingame
	}, {
		"trigger": "!replay",
		"syntax": "<vn/rx/ap> <ReplayID>",
		"callback": replayID_convert
	}, {
		"trigger": "!history",
		"syntax": "<vn/rx/ap> <BeatmapID>",
		"callback": history_beatmap
	}, {
		"trigger": "!mapsuggest",
		"syntax": "<jump/stream/+set(1000,999)>",
		"callback": map_suggest
	}, {
		"trigger": "!status",
		"callback": servers_status
	}, {
		"trigger": "!r",
		"callback": tillerinoRecommand
	}, {
		"trigger": "!b",
		"syntax": "<BeatmapID>",
		"callback": B_dl
	}, {
		"trigger": "!d",
		"syntax": "<BeatmapSetID>",
		"callback": D_dl
	}, {
		"trigger": "!lb",
		"syntax": "<std(s)/taiko(t)/ctb(c)/mania(m)> <vn/rx/ap>",
		"callback": multiLeaderboard
	}, {
		"trigger": "https://osu.ppy.sh/beatmapsets/",
		"callback": BanchoLink_to_mirror,
		"startswith": True
	}, {
		"trigger": "https://osu.ppy.sh/b/",
		"callback": BanchoLink_to_mirror,
		"startswith": True
	}, {
		"trigger": "https://osu.ppy.sh/s/",
		"callback": BanchoLink_to_mirror,
		"startswith": True
	}
]

# Commands list default values
for cmd in commands:
	cmd.setdefault("syntax", "")
	cmd.setdefault("privileges", None)
	cmd.setdefault("callback", None)
	cmd.setdefault("response", "u w0t m8?")
	cmd.setdefault("startswith", False)
	cmd.setdefault("endswith", False)