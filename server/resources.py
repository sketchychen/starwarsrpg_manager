from flask_restx import Namespace, Resource, fields

from dao import UserDAO


ns = Namespace('api')

new_user = ns.model(
    'NewUser',
    {
        'name': fields.String(required=True, min_length=2, max_length=32),
        'email': fields.String(required=True, min_length=4, max_length=64),
        'passcode': fields.String(required=True, min_length=8, max_length=64),
    }
)

new_character = ns.model(
    'NewCharacter',
    {
        'name': fields.String(required=True, min_length=2),
        'species': fields.String(required=True, choices=()),
        'specialization': fields.String(required=True, min_length=3),
    }
)

class Register(Resource):
    dao = UserDAO()

    @ns.expect(new_user, validate=True)
    def post(self):
        kwargs = ns.payload

        return self.dao.create_one(**kwargs)


class RouteUser(Resource):
    dao = UserDAO()

    def get(self, name):
        result = self.dao.get_one(pk=name)

        return result

    def put(self, **kwargs):
        result = self.dao.update_one(**kwargs)

        return result


class CreateCharacter(Resource):
    """
    TODO: Use Permissions and CharacterDAO
    """
    @ns.expect(new_character, validate=True)
    def post(self):
        req_json = request.get_json()

        _name = req_json.get('name')
        _species = req_json.get('species')
        _specialization = req_json.get('specialization')

        pass  # WIP
