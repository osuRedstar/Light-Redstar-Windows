from common.log import logUtils as log
from constants import clientPackets
from constants import serverPackets
from objects import glob
from common.constants import mods

def handle(userToken, packetData):
	# Get usertoken data
	userID = userToken.userID
	username = userToken.username

	# Make sure we are not banned
	#if userUtils.isBanned(userID):
	#	userToken.enqueue(serverPackets.loginBanned())
	#	return

	# Send restricted message if needed
	#if userToken.restricted:
	#	userToken.checkRestricted(True)

	# Change action packet
	packetData = clientPackets.userActionChange(packetData)

	# If we are not in spectate status but we're spectating someone, stop spectating
	'''
if userToken.spectating != 0 and userToken.actionID != actions.WATCHING and userToken.actionID != actions.IDLE and userToken.actionID != actions.AFK:
	userToken.stopSpectating()

# If we are not in multiplayer but we are in a match, part match
if userToken.matchID != -1 and userToken.actionID != actions.MULTIPLAYING and userToken.actionID != actions.MULTIPLAYER and userToken.actionID != actions.AFK:
	userToken.partMatch()
		'''

	# Update cached stats if our pp changed if we've just submitted a score or we've changed gameMode
	#if (userToken.actionID == actions.PLAYING or userToken.actionID == actions.MULTIPLAYING) or (userToken.pp != userUtils.getPP(userID, userToken.gameMode)) or (userToken.gameMode != packetData["gameMode"]):

	# Update cached stats if we've changed gamemode
	if userToken.gameMode != packetData["gameMode"]:
		userToken.gameMode = packetData["gameMode"]
		userToken.updateCachedStats()

	# Always update action id, text, md5 and beatmapID
	userToken.actionID = packetData["actionID"]
	#userToken.actionID = packetData["actionText"]
	userToken.actionMd5 = packetData["actionMd5"]
	userToken.actionMods = packetData["actionMods"]
	userToken.beatmapID = packetData["beatmapID"]

	if bool(packetData["actionMods"] & 128) == True:
		userToken.relaxing = True
		userToken.autopiloting = False
		#if userToken.actionID in (0, 1, 14):
		if userToken.actionID in (0, 14):
			UserText = packetData["actionText"] + "on Relax"
		else:
			UserText = packetData["actionText"] + "on Relax"
		userToken.actionText = UserText
		userToken.updateCachedStats()
	
		if userToken.relaxAnnounce == False:
			userToken.relaxAnnounce = True
			userToken.autopilotAnnounce = False
			userToken.enqueue(serverPackets.notification("You're playing with Relax, we've changed the leaderboard to Relax."))
	#AP 모드 추가
	elif bool(packetData["actionMods"] & 8192) == True:
		userToken.relaxing = False
		userToken.autopiloting = True
		if userToken.actionID in (0, 14):
			UserText = packetData["actionText"] + "on AP"
		else:
			UserText = packetData["actionText"] + "on AP"
		userToken.actionText = UserText
		userToken.updateCachedStats()
	
		if userToken.autopilotAnnounce == False:
			userToken.relaxAnnounce = False
			userToken.autopilotAnnounce = True
			userToken.enqueue(serverPackets.notification("You're playing with AutoPilot, we've changed the leaderboard to Autopilot."))
	#AFK 추가
	elif userToken.actionID in (1, 1):
		status = glob.db.fetch("SELECT current_status FROM users_stats WHERE id = %s", [userID])
		status_rx = status["current_status"].endswith("on Relax")
		status_ap = status["current_status"].endswith("on AP")
		
		log.info("status_rx = {}".format(status_rx))
		log.info("status_ap = {}".format(status_ap))

		if status_rx:
			UserText = packetData["actionText"] + "AFK on Relax"
			log.info("AFK on Relax")
		elif status_ap:
			UserText = packetData["actionText"] + "AFK on AP"
			log.info("AFK on AP")
		else:
			UserText = packetData["actionText"] + "AFK"
			log.info("AFK")
	else:
		UserText = packetData["actionText"]
		userToken.actionText = UserText
		userToken.relaxing = False
		userToken.autopiloting = False
		userToken.updateCachedStats()

		if userToken.relaxAnnounce == True:
			userToken.relaxAnnounce = False
			userToken.enqueue(serverPackets.notification("You've disabled relax. We've changed back to the Regular leaderboard."))
		elif userToken.autopilotAnnounce == True:
			userToken.autopilotAnnounce = False
			userToken.enqueue(serverPackets.notification("You've disabled autopilot. We've changed back to the Regular leaderboard."))

	glob.db.execute("UPDATE users_stats SET current_status = %s WHERE id = %s", [UserText, userID])
	# Enqueue our new user panel and stats to us and our spectators
	recipients = [userToken]
	if len(userToken.spectators) > 0:
		for i in userToken.spectators:
			if i in glob.tokens.tokens:
				recipients.append(glob.tokens.tokens[i])

	for i in recipients:
		if i is not None:
			# Force our own packet
			force = True if i == userToken else False
			i.enqueue(serverPackets.userPanel(userID, force))
			i.enqueue(serverPackets.userStats(userID, force))

	# Console output
	from common.web import requestsManager
	ip = requestsManager.asyncRequestHandler.getRequestIP(glob.self)
	log.info("{} | {} changed action: {} [{}][{}][{}]".format(ip, username, str(userToken.actionID), userToken.actionText, userToken.actionMd5, userToken.beatmapID))
