from common.log import logUtils as log
from common.ripple import userUtils
from constants import clientPackets


def handle(tornadoRequest, userToken, packetData):
	# Friend remove packet
	friendID = clientPackets.addRemoveFriend(packetData)["friendID"]
	userUtils.removeFriend(userToken.userID, friendID)

	# Console output
	log.info(f"{userToken.username} have removed {str(friendID)} from their friends")
