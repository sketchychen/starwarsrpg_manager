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
    passcode = StringField(required=True, min_length=8)
    is_admin = BooleanField(required=True, default=False)
