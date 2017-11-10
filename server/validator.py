from functools import wraps
from flask import jsonify, request, abort


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            js = request.json
            if js == None:
                raise Exception
        except:
            return jsonify({"error": "Eskaera ez da egokia"}), 400
        return f(*args, **kw)
    return wrapper

def validate_schema(name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, name)
            except Exception, e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator

def validate(input, name):
    if name == "add_temp":
        validate_add_temp(input)
    else:
        pass

def validate_add_temp(input):
    try:
        tenp = float(input["tenp"])
        garagardoa = int(input["garagardoa"])
    except:
        raise Exception("Eskaera ez da egokia")

    if not (tenp and garagardoa):
        raise Exception("Eskaera ez da egokia")
