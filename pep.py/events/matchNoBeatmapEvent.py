from events import matchBeatmapEvent

def handle(tornadoRequest, userToken, packetData): matchBeatmapEvent.handle(tornadoRequest, userToken, packetData, False)