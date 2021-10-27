from mongoengine import (
    BooleanField,
    Document,
    StringField,
)


def invalid_username(name):
    """
    TODO: update with regex, offensive terms
    """
    invalid_usernames = ('register', 'login')
    if name.lower() in invalid_usernames:
        raise ValidationError(f'{name} is not a valid username.')


class User(Document):
    name = StringField(
        primary_key=True, required=True,
        min_length=2, max_length=32,
        validation=invalid_username,
    )
    email = StringField(
        required=True, unique=True,
        min_length=4, max_length=64
    )
    passcode = StringField(required=True, min_length=8, max_length=32)
    is_admin = BooleanField(required=True, default=False)

"""

    pymongo>=3.4
    dateutil>=2.1.0
    Pillow>=2.0.0
    blinker>=1.3
    aniso8601==8.0.0; python_version < '3.5'
    aniso8601>=0.82; python_version >= '3.5'
    jsonschema
    Flask>=0.8, !=2.0.0
    werkzeug !=2.0.0
    pytz
    six>=1.3.0
    enum34; python_version < '3.4'

    Werkzeug
    Jinja
    MarkupSafe
    ItsDangerous
    Click
"""