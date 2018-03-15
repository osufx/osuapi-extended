import urllib.request
import json
import glob
import status

def call_api(endpoint, **kwargs):
    query = "?k={}".format(glob.config["api-key"])
    if kwargs is not None and len(kwargs) is not 0:
        args = []
        for key, value in kwargs.items():
            args.append("{}={}".format(key, value))
        query += "&" + "&".join(args)
    endcall = endpoint + query
    ppy_data = urllib.request.urlopen('http://osu.ppy.sh/api/{}'.format(endcall))

    # Update status for api calls
    status.update(api = 1)

    return json.loads(ppy_data.read().decode("utf-8"))