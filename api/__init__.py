from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from .routes import api


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'swrpg_manager',
    'host': 'mongodb://127.0.0.1:27017/swrpg_manager',
    'port': 27017,
    'username':'admin',
    'password':'1234',
}

app.config.from_object('api.config.Config')

db = MongoEngine(app)
db.init_app(app)
rest_api.init_app(app)
CORS(app)

"""
   Custom responses
"""


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
