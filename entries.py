from flask import request, redirect, jsonify
import glob
from api import difficulty
from api import hash as apiHash

@glob.app.route("/")
@glob.app.route("/api")
def index():
    return redirect("http://github.com/osufx/osuapi-extended/wiki")

@glob.app.route("/api/getDifficulty", methods=["GET", "POST"])
def getDiff():
    return difficulty.handle(request)

@glob.app.route("/api/getHash", methods=["GET", "POST"])
def getHash():
    return apiHash.handle(request)