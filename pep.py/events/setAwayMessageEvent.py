from common.log import logUtils as log
from constants import clientPackets
from constants import serverPackets
from objects import glob

def handle(userToken, packetData):
	# get token data
	username = userToken.username

	# Read packet data
	packetData = clientPackets.setAwayMessage(packetData)

	# Set token away message
	userToken.awayMessage = packetData["awayMessage"]

	# Send private message from the bot
	fokaMessage = "Your away message has been reset" if userToken.awayMessage == "" else f"Your away message is now: {userToken.awayMessage}"
	userToken.enqueue(serverPackets.sendMessage(glob.BOT_NAME, username, fokaMessage))
	log.info(f"{username} has changed their away message to: {userToken.awayMessage}")