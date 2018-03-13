from flask import request, Response, json
import glob

def jsonify(*args, **kwargs):
    indent = None
    separators = (',', ':')
    comp = "comp" not in request.args

    if glob.app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not request.is_xhr and comp:
        indent = 2
        separators = (', ', ': ')

    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs

    return Response(
        (json.dumps(data, indent=indent, separators=separators), comp and '\n' or ''),
        mimetype=glob.app.config['JSONIFY_MIMETYPE']
    )