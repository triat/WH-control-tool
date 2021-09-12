from bottle import request, abort
from utils import get_config


def requires_auth(f):
    """Provides token based authentication for any decorated function
    assuming the token is located in the json body"""

    def decorated(*args, **kwargs):
        try:
            token = request.json["token"]
        except KeyError:
            abort(400, "Missing token in body")

        if token != get_config("access_token"):
            abort(403, "Token refused")
        return f(*args, **kwargs)

    return decorated
