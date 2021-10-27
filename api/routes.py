from flask_restx import Api, Resource, fields

from .dao import UserDAO


api = Api(version='1.0', title='Star Wars FFG Manager API')
ns = api.namespace('api')


@ns.route('/register')
class Register(Resource):
    dao = UserDAO()

    api_model = api.model(
        'RegisterModel',
        {
            'name': fields.String(required=True, min_length=2, max_length=32),
            'email': fields.String(required=True, min_length=4, max_length=64),
            'passcode': fields.String(required=True, min_length=4, max_length=64),
        }
    )

    @api.expect(api_model, validate=True)
    def post(self):
        kwargs = api.payload

        self.dao.create_one(**kwargs)


@ns.route('/user/<string:name>')
class RouteUser(Resource):
    dao = UserDAO()

    def get(self, name):
        result = self.dao.get_one(pk=name)

        return result

    def put(self, **kwargs):
        result = self.dao.update_one(**kwargs)

        return result


@ns.route('/character/create')
class CreateCharacter(Resource):
    """
    TODO: Use Permissions and CharacterDAO
    """
    character_creation_model = api.model(
        'CharacterCreationModel',
        {
            'name': fields.String(required=True, min_length=2),
            'species': fields.String(required=True, choices=()),
            'specialization': fields.String(required=True, min_length=3),
        }
    )

    @api.expect(character_creation_model, validate=True)
    def post(self):
        req_json = request.get_json()

        _name = req_json.get('name')
        _species = req_json.get('species')
        _specialization = req_json.get('specialization')

        pass  # WIP
