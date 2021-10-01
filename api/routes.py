from flask_restx import Api, Resource, fields
import jwt
from .documents import User


api = Api(version='1.0', title='Star Wars FFG Manager API')


signup_model = api.model(
    'SignUpModel',
    {
        'username': fields.String(required=True, min_length=2, max_length=32),
        'email': fields.String(required=True, min_length=4, max_length=64),
        'passphrase': fields.String(required=True, min_length=4, max_length=64),
    }
)

@api.route('/api/users/register')
class Register(Resource):
    """
        Creates a new user by taking 'signup_model' input
    """

    @api.expect(signup_model, validate=True)
    def post(self):
        req_data = request.get_json()

        _username = req_data.get('username')
        _email = req_data.get('email')

        ## CONSIDER HASHING HERE?
        _passphrase = req_data.get('passphrase')