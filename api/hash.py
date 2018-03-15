import urllib.request
from common import ppyFormat
from common.jsonFlaskFormat import jsonify
import status

def handle(request):
    ppy_data = urllib.request.urlopen('http://osu.ppy.sh/web/osu-gethashes.php?s={}'.format(request.args.get("s")))
    ppy_str = ppy_data.read()
    if len(ppy_str) > 3:
        data = ppyFormat.verticalSplit(ppy_str, ["_", "body_hash", "header_hash"])
        if len(data["body_hash"]) + len(data["header_hash"]) == 0:
            data = None
        else:
            data["body_hash"] = data["body_hash"].lower()
            data["header_hash"] = data["header_hash"].lower()
    else:
        data = None

    # Update status for api calls
    status.update(ext = 1)
    
    return jsonify(data)