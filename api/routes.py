import jwt
import json

from flask_restx import Api, Resource, fields

from .documents import User


api = Api(version='1.0', title='Star Wars FFG Manager API')
ns = api.namespace('api')


@ns.route('/user')
class Register(Resource):
    signup_model = api.model(
        'SignUpModel',
        {
            'username': fields.String(required=True, min_length=2, max_length=32),
            'email': fields.String(required=True, min_length=4, max_length=64),
            'passcode': fields.String(required=True, min_length=4, max_length=64),
        }
    )

    @api.expect(signup_model, validate=True)
    def post(self):
        # WIP
        req_data = request.get_json()

        _username = req_data.get('username')
        _email = req_data.get('email')

        ## CONSIDER HASHING HERE?
        _passcode = req_data.get('passcode')


@ns.route('/user/<string:username>')
class RouteUser(Resource):
    """
    TODO: Permissions for query and update
    """
    doc = User

    def query(self, pk):
        return doc.objects.get(pk=pk).to_mongo()

    def get(self, username):
        user = User.objects.get(pk=username).to_mongo()
        return user

    def put(self, username):
        user = User.objects.get(pk=username).to_mongo()