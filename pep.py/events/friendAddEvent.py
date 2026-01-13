from common.log import logUtils as log
from common.ripple import userUtils
from constants import clientPackets

def handle(userToken, packetData):
	# Friend add packet
	friendID = clientPackets.addRemoveFriend(packetData)["friendID"]
	userUtils.addFriend(userToken.userID, friendID)

	# Console output
	log.info(f"{userToken.username} have added {str(friendID)} to their friends")