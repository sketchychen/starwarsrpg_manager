from mongoengine import (
    EmbeddedDocument,
    IntField,
    DynamicField,
    LazyReferenceField,
)

from .user import User


class FieldChangeLog(EmbeddedDocument):
    """
    Record changes to field values and who made them.

    Example:
    {
        _id: "4c6b9456f61f000000007ba6"
        title: [
            { version: 1, value: "Hello world", user_pk: 2 },
            { version: 6, value: "Foo", user_pk: 5 }
        ],
        body: [
            { version: 1, value: "Is this thing on?", user_pk: 2 },
            { version: 2, value: "What should I write?", user_pk: 2 },
            { version: 6, value: "This is the new body", user_pk: 5 }
        ],
    }
    """
    version = IntField(default=0)
    value = DynamicField(required=True)
    user_pk = LazyReferenceField(User)
