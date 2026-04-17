
from flask import Flask, request, jsonify
from flask_cors import CORS
import random, datetime

app = Flask(__name__)
CORS(app)

logs = []

@app.route("/collect", methods=["POST"])
def collect():
    data = request.json

    click = data.get("click_interval",0)
    scroll = data.get("scroll_amount",0)
    redirect = data.get("redirect_count",0)

    if scroll > 2000 or redirect > 1:
        prediction = "Hijacked"
        confidence = round(random.uniform(0.7,0.9),2)
    else:
        prediction = "Normal"
        confidence = round(random.uniform(0.6,0.8),2)

    log = {
        "timestamp": str(datetime.datetime.now()),
        "click": click,
        "scroll": scroll,
        "redirect": redirect,
        "prediction": prediction,
        "confidence": confidence
    }

    logs.append(log)

    return jsonify({"status":"ok"})


@app.route("/logs")
def get_logs():
    return jsonify(logs[-30:])


app.run(port=5000)
