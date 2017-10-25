from flask import Flask, request, render_template, abort, jsonify, after_this_request
from models import Tenperatura

PORT = 5000
ADDR = "0.0.0.0"

app = Flask(__name__)

@app.route("/"):
def get_index():
    return render_template("index.html")


if __name__ == '__main__':
   app.run(host=ADDR, port=PORT)
