import personalBestCache
import personalBestCacheRX
import personalBestCacheAP
import userStatsCache
import userStatsCacheRX
import userStatsCacheAP
from common.ddog import datadogClient
from common.files import fileBuffer, fileLocks
from common.web import schiavo

try:
	with open("version") as f:
		VERSION = f.read().strip()
except:
	VERSION = "Unknown"
ACHIEVEMENTS_VERSION = 1

DATADOG_PREFIX = "lets"
db = None
redis = None
conf = None
application = None
pool = None
pascoa = {}

debug = False
sentry = False

# Cache and objects
fLocks = fileLocks.fileLocks()
userStatsCache = userStatsCache.userStatsCache()
userStatsCacheRX = userStatsCacheRX.userStatsCacheRX()
userStatsCacheAP = userStatsCacheAP.userStatsCacheAP()
personalBestCache = personalBestCache.personalBestCache()
personalBestCacheRX = personalBestCacheRX.personalBestCacheRX()
personalBestCacheAP = personalBestCacheAP.personalBestCacheAP()
fileBuffers = fileBuffer.buffersList()
dog = datadogClient.datadogClient()
schiavo = schiavo.schiavo()
achievementClasses = {}

# Additional modifications
COMMON_VERSION_REQ = "1.2.1"
try:
	with open("common/version") as f:
		COMMON_VERSION = f.read().strip()
except:
	COMMON_VERSION = "Unknown"