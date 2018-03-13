from flask import request, redirect, jsonify
import glob
from api import difficulty

@glob.app.route("/")
@glob.app.route("/api")
def index():
    return redirect("http://github.com/osufx/osuapi-extended")

@glob.app.route("/api/getDifficulty", methods=["GET", "POST"])
def getDiff():
    return difficulty.handle(request)