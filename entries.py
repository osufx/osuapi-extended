from flask import request, redirect, jsonify, url_for
import glob
from api import difficulty
from api import hash as apiHash
import status

@glob.app.route("/")
def index():
    return jsonify(AvailableRoutes=[url_for(url.endpoint) for url in glob.app.url_map.iter_rules() if url.endpoint is not "static"])

@glob.app.route("/api")
def wiki():
    return redirect("http://github.com/osufx/osuapi-extended/wiki")

@glob.app.route("/api/getDifficulty", methods=["GET", "POST"])
def getDiff():
    return difficulty.handle(request)

@glob.app.route("/api/getHash", methods=["GET", "POST"])
def getHash():
    return apiHash.handle(request)

@glob.app.route("/stat")
def getStatus():
    return status.handle()