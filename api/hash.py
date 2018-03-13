import urllib.request
from common import ppyFormat
from common.jsonFlaskFormat import jsonify

def handle(request):
    ppy_data = urllib.request.urlopen('http://osu.ppy.sh/web/osu-gethashes.php?s={}'.format(request.args.get("s")))
    ppy_str = ppy_data.read()
    if len(ppy_str) > 3:
        data = ppyFormat.verticalSplit(ppy_str, ["res", "body_hash", "header_hash"])
        if len(data["body_hash"]) + len(data["header_hash"]) == 0:
            data = None
    else:
        data = None
    return jsonify(data)