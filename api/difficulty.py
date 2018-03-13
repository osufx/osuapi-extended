import urllib.request
#from flask import jsonify
from common import ppyFormat
from common.jsonFlaskFormat import jsonify

def handle(request):
    ppy_data = urllib.request.urlopen('http://osu.ppy.sh/web/osu-getdifficulty.php?c[]={}'.format(request.args.get("c")))
    ppy_str = ppy_data.read()
    if len(ppy_str) <= 0:
        return jsonify(None)
    data = ppyFormat.verticalSplit(ppy_str, ["checksum", "mode", "mods", "diff_unified"])
    return jsonify(data)