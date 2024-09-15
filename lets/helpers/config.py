import os
import configparser

class config:
	"""
	config.ini object

	config -- list with ini data
	default -- if true, we have generated a default config.ini
	"""

	config = configparser.ConfigParser()
	extra = {}
	fileName = ""		# config filename
	default = True

	# Check if config.ini exists and load/generate it
	def __init__(self, __file):
		"""
		Initialize a config object

		__file -- filename
		"""

		self.fileName = __file
		if os.path.isfile(self.fileName):
			# config.ini found, load it
			self.config.read(self.fileName)
			self.default = False
		else:
			# config.ini not found, generate a default one
			self.generateDefaultConfig()
			self.default = True

	# Check if config.ini has all needed the keys
	def checkConfig(self):
		"""
		Check if this config has the required keys

		return -- True if valid, False if not
		"""

		try:
			# Try to get all the required keys
			self.config.get("db","host")
			self.config.get("db","username")
			self.config.get("db","password")
			self.config.get("db","database")
			self.config.get("db","workers")

			self.config.get("redis","host")
			self.config.get("redis","port")
			self.config.get("redis","database")
			self.config.get("redis","password")

			self.config.get("server", "host")
			self.config.get("server", "port")
			self.config.get("server", "debug")
			self.config.get("server", "beatmapcacheexpire")
			self.config.get("server", "serverurl")
			self.config.get("server", "banchourl")
			self.config.get("server", "threads")
			self.config.get("server", "apikey")
			self.config.get("server", "replayspath")
			self.config.get("server", "beatmapspath")
			self.config.get("server", "screenshotspath")
			self.config.get("server", "server-domain")

			self.config.get("sentry", "enable")
			self.config.get("sentry", "dsn")

			self.config.get("datadog", "enable")
			self.config.get("datadog", "apikey")
			self.config.get("datadog", "appkey")

			self.config.get("osuapi", "enable")
			self.config.get("osuapi", "apiurl")
			self.config.get("osuapi", "apikey")
			self.config.get("osuapi", "bancho_username")
			self.config.get("osuapi", "bancho_password")

			self.config.get("beatconnect", "enable")
			self.config.get("beatconnect", "apikey")

			self.config.get("cheesegull", "apiurl")

			self.config.get("discord", "enable")
			self.config.get("discord", "ahook")
			self.config.get("discord", "score")
			self.config.get("discord", "rxscore")

			self.config.get("cono", "enable")

			self.config.get("custom", "config")
			return True
		except:
			return False


	# Generate a default config.ini
	def generateDefaultConfig(self):
		"""Open and set default keys for that config file"""

		# Open config.ini in write mode
		f = open(self.fileName, "w")

		# Set keys to config object
		self.config.add_section("db")
		self.config.set("db", "host", "localhost")
		self.config.set("db", "username", "Your_DB_username")
		self.config.set("db", "password", "Your_DB_password")
		self.config.set("db", "database", "Your_DB_database")
		self.config.set("db", "workers", "16")

		self.config.add_section("redis")
		self.config.set("redis", "host", "localhost")
		self.config.set("redis", "port", "6379")
		self.config.set("redis", "database", "0")
		self.config.set("redis", "password", "Your_redis_password")

		self.config.add_section("server")
		self.config.set("server", "host", "0.0.0.0")
		self.config.set("server", "port", "5002")
		self.config.set("server", "debug", "False")
		self.config.set("server", "beatmapcacheexpire", "86400")
		self.config.set("server", "serverurl", "http://127.0.0.1:5002")
		self.config.set("server", "banchourl", "http://127.0.0.1:5001")
		self.config.set("server", "threads", "16")
		self.config.set("server", "apikey", "changeme")
		self.config.set("server", "replayspath", ".data/replays")
		self.config.set("server", "beatmapspath", ".data/beatmaps")
		self.config.set("server", "screenshotspath", ".data/screenshots")
		self.config.set("server", "server-domain", "redstar.moe")

		self.config.add_section("sentry")
		self.config.set("sentry", "enable", "False")
		self.config.set("sentry", "dsn", "")

		self.config.add_section("datadog")
		self.config.set("datadog", "enable", "False")
		self.config.set("datadog", "apikey", "")
		self.config.set("datadog", "appkey", "")

		self.config.add_section("osuapi")
		self.config.set("osuapi", "enable", "True")
		self.config.set("osuapi", "apiurl", "https://osu.ppy.sh")
		self.config.set("osuapi", "apikey", "Your_Bancho_APIKKEY")
		self.config.set("osuapi", "bancho_username", "")
		self.config.set("osuapi", "bancho_password", "")

		self.config.add_section("beatconnect")
		self.config.set("beatconnect", "enable", "False")
		self.config.set("beatconnect", "apikey", "")

		self.config.add_section("cheesegull")
		self.config.set("cheesegull", "apiurl", "http://localhost:6201/api")

		self.config.add_section("discord")
		self.config.set("discord", "enable", "False")
		self.config.set("discord", "ahook", "")
		self.config.set("discord", "score", "")
		self.config.set("discord", "rxscore", "")

		self.config.add_section("cono")
		self.config.set("cono", "enable", "False")

		self.config.add_section("custom")
		self.config.set("custom", "config", "common/config.json")

		# Write ini to file and close
		self.config.write(f)
		f.close()
