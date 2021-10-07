from mongoengine import (
    Document,
    EmbeddedDocument,
    ListField,
    MultiLineStringField,
    LazyReferenceField,
    ReferenceField,
    StringField,
)

from . import character, user

class Campaign(Document):
    """
    1:M User:Campaign
    M:M Campaign:Character
    1:M Campaign:Event
    """
    name = StringField(required=True, min_length=4)
    owner = ReferenceField(user.User)
    characters = ListField(ReferenceField(character.Character))
    timeline = EmbeddedDocumentListField(Event)
    blurb = MultiLineStringField()


class Event(EmbeddedDocument):
    """
    Session summaries, character side stories, behind-the-scenes updates, etc.
    Basically a campaign's blog post.
    """
    owner = ReferenceField(user.User)
    name = StringField(required=True, min_length=4)
    characters = ListField(LazyReferenceField(character.Character))