import traceback
import json
from flask import Flask, jsonify
import glob

app = Flask(__name__)

with open("config.json", "r") as f:
    glob.config = json.load(f)

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handle(error):
    error_message = None
    if error.code == 500:
        error_message = "We had an error on our end, we are very sorry."
    elif error.code == 404:
        error_message = "We are unable to find the requested page."
    elif error.code == 403:
        error_message = "You do not seem to have permission to see this page."
    
    res = {
        "code": error.code,
        "message": error_message
    }

    if glob.config["web"]["debug"]:
        res["traceback_stack"] = traceback.format_stack()

    return jsonify(res)

if __name__ == "__main__":
    app.run(**glob.config["web"])