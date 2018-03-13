import urllib.request
#from flask import jsonify
from common import ppyFormat
from common.jsonFlaskFormat import jsonify

def handle(request):
    ppy_data = urllib.request.urlopen('http://osu.ppy.sh/web/osu-getdifficulty.php?c[]={}'.format(request.args.get("c")))
    data = ppyFormat.verticalSplit(ppy_data.read(), ["checksum", "mode", "mods", "diff_unified"])
    return jsonify(data)