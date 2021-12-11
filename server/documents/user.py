from mongoengine import (
    BooleanField,
    Document,
    EmailField,
    StringField,
)


__all__ = ('User', )


class User(Document):
    name = StringField(
        primary_key=True, required=True,
        min_length=2, max_length=32,
    )
    email = EmailField(required=True, unique=True, perm_level=3)
    passcode = StringField(required=True, min_length=8, perm_level=5)
    is_admin = BooleanField(required=True, default=False)