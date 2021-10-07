import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from .config import load_config
from .routes import rest_api


env_config = load_config()

app = Flask(__name__)
app.config.from_object(env_config)

db = MongoEngine(app)

rest_api.init_app(app)
CORS(app)


@app.after_request
def after_request(response):
    """
       Sends back a custom error with {"success", "msg"} format
    """

    if int(response.status_code) >= 400:
        response_data = json.loads(response.get_data())
        if "errors" in response_data:
            response_data = {"success": False,
                             "msg": list(response_data["errors"].items())[0][1]}
            response.set_data(json.dumps(response_data))
        response.headers.add('Content-Type', 'application/json')
    return response
