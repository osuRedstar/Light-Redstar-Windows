"""FokaBot related functions"""
import re

from common import generalUtils
from common.constants import actions
from common.ripple import userUtils
from constants import fokabotCommands
from constants import serverPackets
from objects import glob
from helpers import configHelper

conf = configHelper.config("config.ini")

npRegex = re.compile("^https?:\\/\\/osu\\.ppy\\.sh\\/beatmapsets\\/(-?\\d+)#\\/(-?\\d+)")
def RGX(url): return re.findall(r"\d+", url)
def npRegex_BanchoWebLink(url):
	try:
		mode = re.search(r"#(\w+)/", url).group(1)
	except:
		mode = ""
	bid = re.findall(r"\d+", url)
	bid = bid[len(bid) - 1]
	return [mode, bid]

def connect(timeOffset = 9):
	"""
	Connect FokaBot to Bancho

	:return:
	"""
	glob.BOT_NAME = userUtils.getUsername(999)
	token = glob.tokens.addToken(999)
	token.actionID = actions.SUBMITTING
	token.actionText = "\nIm Not Devi*ntA*t"
	token.pp = 727
	token.accuracy = 0.9885
	token.playcount = 26956
	token.totalScore = 237228316533
	token.timeOffset = timeOffset
	token.timezone = 24+token.timeOffset
	#token.country = 111 jp
	#token.country = 180 pw
	#token.country = 118 kp
	token.country = 118
	glob.streams.broadcast("main", serverPackets.userPanel(999))
	glob.streams.broadcast("main", serverPackets.userStats(999))

def disconnect():
	"""
	Disconnect FokaBot from Bancho

	:return:
	"""
	glob.tokens.deleteToken(glob.tokens.getTokenFromUserID(999))

def fokabotResponse(fro, chan, message):
	"""
	Check if a message has triggered FokaBot

	:param fro: sender username
	:param chan: channel name (or receiver username)
	:param message: chat mesage
	:return: FokaBot's response or False if no response
	"""
	for i in fokabotCommands.commands:
		# Loop though all commands
		if re.compile("^{}( (.+)?)?$".format(i["trigger"])).match(message.strip()):
			# message has triggered a command

			# Make sure the user has right permissions
			_userId = userUtils.getID(fro)
			if i["privileges"] is not None:
				if userUtils.getPrivileges(_userId) & i["privileges"] == 0:
					if i["trigger"] == "!mp":
						try:
							refers = glob.matches.matches[fokabotCommands.getMatchIDFromChannel(chan)].refers
							if not _userId in refers:
								return False
						except:
							return False
					else:
						return False

			# Check argument number
			message = message.split(" ")
			if i["syntax"] != "" and len(message) <= len(i["syntax"].split(" ")):
				return "Wrong syntax: {} {}".format(i["trigger"], i["syntax"])

			# Return response or execute callback
			if i["callback"] is None:
				return i["response"]
			else:
				return i["callback"](fro, chan, message[1:])

		elif (i["startswith"] or i["endswith"]) and (message.startswith(i['trigger']) or message.endswith(i['trigger'])):
			# message has triggered a command

			# Make sure the user has right permissions
			_userId = userUtils.getID(fro)
			if i["privileges"] is not None:
				if userUtils.getPrivileges(_userId) & i["privileges"] == 0:
					if i["trigger"] == "!mp":
						try:
							refers = glob.matches.matches[fokabotCommands.getMatchIDFromChannel(chan)].refers
							if not _userId in refers:
								return False
						except:
							return False
					else:
						return False

			# Check argument number
			message = message.split(" ")
			if i["syntax"] != "" and len(message) <= len(i["syntax"].split(" ")):
				return "Wrong syntax: {} {}".format(i["trigger"], i["syntax"])

			# Return response or execute callback
			if i["callback"] is None:
				return i["response"]
			else:
				return i["callback"](fro, chan, message[0])

	# No commands triggered
	return False
