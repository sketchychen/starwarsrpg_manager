import jwt
import json

from flask_restx import Api, Resource, fields

from .documents import User


api = Api(version='1.0', title='Star Wars FFG Manager API')
ns = api.namespace('api')

@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

signup_model = api.model(
    'SignUpModel',
    {
        'username': fields.String(required=True, min_length=2, max_length=32),
        'email': fields.String(required=True, min_length=4, max_length=64),
        'passcode': fields.String(required=True, min_length=4, max_length=64),
    }
)
class RouteUser(Resource):
    def get(self, username):
        user = User.objects.get(pk=username).to_mongo()
        return user

    @api.expect(signup_model, validate=True)
    def post(self):
        # WIP
        req_data = request.get_json()

        _username = req_data.get('username')
        _email = req_data.get('email')

        ## CONSIDER HASHING HERE?
        _passcode = req_data.get('passcode')


ns.add_resource(RouteUser, '/user/<string:username>', endpoint='get')
ns.add_resource(RouteUser, '/user/register', endpoint='post')