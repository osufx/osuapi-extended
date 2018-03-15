import time,datetime
import glob
from common.jsonFlaskFormat import jsonify

last_update = 0

def handle():
    # Update the times before we serve
    update()

    data = {
        "time": {
            "start": glob.start_time,
            "current": current_time()
        },
        "ext": {
            "total": glob.total_ext_api_calls,
            "current_minute": glob.minute_ext_api_calls,
            "last_minute": glob.last_ext_api_calls
        },
        "osu": {
            "total": glob.total_osu_api_calls,
            "current_minute": glob.minute_osu_api_calls,
            "last_minute": glob.last_osu_api_calls
        }
    }

    return jsonify(data)

def start():
    # Set current timestamp
    glob.start_time = current_time()
    last_update = glob.start_time

def update(*args, ext = 0, api = 0):
    global last_update
    time_diff = int(current_time() / 60) - int(last_update / 60)
    print(time_diff)
    if time_diff == 1:
        glob.last_ext_api_calls = glob.minute_ext_api_calls
        glob.last_osu_api_calls = glob.minute_osu_api_calls
    elif time_diff > 1:
        glob.last_ext_api_calls = 0
        glob.last_osu_api_calls = 0
    
    if time_diff > 0:
        last_update = current_time()
    
    glob.total_ext_api_calls += ext
    glob.total_osu_api_calls += api
    glob.minute_ext_api_calls += ext
    glob.minute_osu_api_calls += api

def current_time():
    return int(time.mktime(datetime.datetime.today().timetuple()))
