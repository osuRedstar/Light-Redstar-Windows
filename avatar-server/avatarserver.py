import requests, random, os
from flask import Flask, send_file, jsonify, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv

load_dotenv()
OSU_API_KEYs = eval(os.environ["OSU_API_KEYs"])

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=2, x_proto=1, x_host=1, x_port=1, x_prefix=1) #ProxyFix 미들웨어 추가
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

avatar_dir = "avatars" # no slash
avatar2_dir = "bancho" # no slash

# create avatars directory if it does not exist
for ad in [avatar_dir, avatar2_dir]:
	if not os.path.exists(ad): os.makedirs(ad)

@app.route("/status")
def serverStatus(): return jsonify({"response" : 200, "status" : 1})

@app.route("/<int:uid>")
def serveAvatar(uid):
	# Check if avatar exists
	avatarid = uid if os.path.isfile(f"{avatar_dir}/{uid}.png") else -1
	return send_file(f"{avatar_dir}/{avatarid}.png") # Serve actual avatar or default one

@app.route("/bancho/id/<int:uid>")
def serveAvatar2(uid):
	# Check if avatar exists
	""" if os.path.isfile("{}/{}.png".format(avatar2_dir, uid)):
		avatarid = uid
	else:
		with open(f"bancho/{uid}.png", 'wb') as f: f.write(requests.get(f"https://a.ppy.sh/{uid}").content)
		avatarid = uid """

	with open(f"bancho/{uid}.png", 'wb') as f: f.write(requests.get(f"https://a.ppy.sh/{uid}").content)
	return send_file(f"{avatar2_dir}/{uid}.png") # Serve actual avatar or default one

@app.route("/bancho/u/<string:username>")
def serveAvatar3(username):
	key = random.choice(OSU_API_KEYs)
	uid = requests.get(f"https://osu.ppy.sh/api/get_user?k={key}&u={username}").json()[0]['user_id']
	return serveAvatar2(uid)

##############################################################################

@app.route("/")
def index(): return send_file(f"{avatar_dir}/-1.png")

@app.route("/<string:f>")
def serveAvatar4(f): return send_file(f"{avatar_dir}/{f}") if os.path.isfile(f"{avatar_dir}/{f}") else send_file(f"{avatar_dir}/-404.png"), 404

@app.route('/favicon.ico')
def favicon(): return send_file(f"{avatar_dir}/-1.png")

@app.route("/docs")
def	docs(): return render_template('docs.html')

###############################################################################

@app.errorhandler(404)
def page_not_found(error): return send_file(f"{avatar_dir}/-404.png"), 404

# Run the server
app.run(host="0.0.0.0", port=5000)