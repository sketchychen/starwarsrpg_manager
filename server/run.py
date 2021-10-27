import os
import json
from flask import Flask
from flask_cors import CORS

from flask_restx import Api

from .config import load_config
from .documents import db
from .routes import api


env_config = load_config()

app = Flask(__name__)
app.config.from_object(env_config)


db.init_app(app)
api.init_app(app)
CORS(app)


# @app.after_request
# def after_request(response):
#     """
#        Sends back a custom error with {"success", "msg"} format
#     """

#     if int(response.status_code) >= 400:
#         response_data = json.loads(response.get_data())
#         if 'errors' in response_data:
#             response_data = {
#                 'success': False,
#                 'msg': list(response_data["errors"].items())[0][1]
#             }
#             response.set_data(json.dumps(response_data))
#         response.headers.add('Content-Type', 'application/json')
#     return response


@app.shell_context_processor
def make_shell_context():
    return {
        'app': app,
        'db': db,
    }


if __name__ == '__main__':
    app.run(debug=True)