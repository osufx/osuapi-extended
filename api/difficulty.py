import urllib.request
#from flask import jsonify
from common import ppyFormat
from common.jsonFlaskFormat import jsonify
from common.utils import AddListsUnique
import ppyapi as api

def handle(request):
    checksum = request.args.getlist("c")

    api_data = []

    param_s = request.args.getlist("s")
    param_b = request.args.getlist("b")

    for param in param_s:
        data = api.call_api("get_beatmaps", s=param)
        AddListsUnique(api_data, data)
    
    for param in param_b:
        data = api.call_api("get_beatmaps", b=param)
        AddListsUnique(api_data, data)

    AddListsUnique(checksum, [x["file_md5"] for x in api_data])
    checksum = "&c[]=".join(checksum)
    ppy_data = urllib.request.urlopen('http://osu.ppy.sh/web/osu-getdifficulty.php?c[]={}'.format(checksum))
    ppy_str = ppy_data.read()
    if len(ppy_str) <= 0:
        return jsonify(None)
    data = ppyFormat.verticalSplit(ppy_str, ["checksum", "mode", "mods", "diff_unified"])
    return jsonify(data)