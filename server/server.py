from flask import Flask, request, render_template, abort, jsonify, after_this_request
from models import Tenperatura
from validator import validate_json, validate_schema
import db_helper as db

PORT = 5000
ADDR = "0.0.0.0"

app = Flask(__name__)

# Importak
@app.route("/client.js")
def get_client_js():
	return app.send_static_file("client.js")

@app.route("/assets/<path:path>")
def get_asset(path):
	return app.send_static_file("assets/"+path)

@app.route("/images/<path:path>")
def get_images(path):
	return app.send_static_file("images/"+path)

@app.route("/")
def get_index():
    return render_template("index.html")

# AJAX routes

@app.route("/ajax/add_temp", methods=["POST"])
@validate_json
@validate_schema("add_temp")
def add_temp():
	data = request.get_json(silent = True)
	tenp = Tenperatura(data["tenp"], data["garagardoa"])
	if not db.add(tenp):
		return jsonify({"error": "Datu basean arazo bat gertatu da"}), 500
	else:
		return jsonify({"success": "true"}), 200

@app.route("/ajax/get_temps", methods=["GET"])
def get_temps():
	temps = db.get_current_temps()

	if not temps:
		return jsonify({"error" : "Datu basean arazo bat gertatu da"}), 500
	else:
		return jsonify(success="true", temps=[e.serialize() for e in temps]), 200


if __name__ == '__main__':
   app.run(host=ADDR, port=PORT)
