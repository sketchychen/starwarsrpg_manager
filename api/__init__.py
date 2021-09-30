import json

from flask import Flask
from flask_cors import CORS

from models import db
from routes import api


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': '192.168.1.35',
    'port': 12345,
    'username':'webapp',
    'password':'pwd123'
}
app.config.from_pyfile('the-config.cfg')
app.config.from_object('api.config.BaseConfig')

db.init_app(app)
api.init_app(app)
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