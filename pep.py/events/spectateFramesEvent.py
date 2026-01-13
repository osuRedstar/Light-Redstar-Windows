from objects import glob
from constants import serverPackets
from common.log import logUtils as log

def handle(userToken, packetData):
	# get token data
	userID = userToken.userID

	# Send spectator frames to every spectator
	streamName = f"spect/{userID}"
	glob.streams.broadcast(streamName, serverPackets.spectatorFrames(packetData[7:]))
	log.debug(f"Broadcasting {userID}'s frames to {len(glob.streams.streams[streamName].clients)} clients")