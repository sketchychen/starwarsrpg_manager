from mongoengine import (
    BooleanField,
    Document,
    StringField,
)


class User(Document):
    is_admin = BooleanField(required=True, default=False)
    email = StringField(required=True, min_length=4, max_length=64)
    username = StringField(required=True, min_length=2, max_length=32)
    passphrase = StringField(required=True, min_length=8, max_length=32)
