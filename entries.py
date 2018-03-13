from flask import redirect, jsonify
import glob

@glob.app.route("/api")
def index():
    return redirect("http://github.com/osufx/osuapi-extended")