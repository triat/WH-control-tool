from bottle import route, run, request, Response
import requests

from auth import requires_auth
from utils import get_config


@route("/configuration", method="POST")
@requires_auth
def update_config():
    params = request.json
    config = get_config(params.get("config_name"))
    if config is None:
        return Response("Configuration not found", status=404)

    try:
        resp = requests.put(
            f"http://localhost:5001/symbols/algousdt/liqsize/{config['liqsize']}"
        )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

    return Response("Updated", status=200)


run(host="localhost", port=8080, debug=True, reloader=True)
