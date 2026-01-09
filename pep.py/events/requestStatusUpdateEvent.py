from constants import serverPackets


def handle(tornadoRequest, userToken, packetData):
	# Update cache and send new stats
	userToken.updateCachedStats()
	userToken.enqueue(serverPackets.userStats(userToken.userID))
