import os
import json
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_restx import Api


from .config import load_config
from . import resources


env_config = load_config()

app = Flask(__name__)
app.config.from_object(env_config)

db = MongoEngine()
db.init_app(app)

api = Api(version='1.0', title='Star Wars FFG Manager API')
api.add_namespace(resources.ns)
resources.ns.add_resource(resources.Register, '/register')
resources.ns.add_resource(resources.RouteUser, '/user/<string:name>')
resources.ns.add_resource(resources.CreateCharacter, '/character/create')
api.init_app(app)

CORS(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'app': app,
        'db': db,
    }


if __name__ == '__main__':
    app.run(debug=True)