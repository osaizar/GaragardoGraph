from flask import Flask, request, render_template, abort, jsonify, after_this_request
from models import Tenperatura

PORT = 5000
ADDR = "0.0.0.0"

app = Flask(__name__)

# Importak
@app.route("/assets/<path:path>")
def get_asset(path):
	return app.send_static_file("assets/"+path)

@app.route("/images/<path:path>")
def get_images(path):
	return app.send_static_file("images"+path)

@app.route("/")
def get_index():
    return render_template("index.html")


if __name__ == '__main__':
   app.run(host=ADDR, port=PORT)
