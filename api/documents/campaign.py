from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    ListField,
    MapField,
    MultiLineStringField,
    LazyReferenceField,
    ReferenceField,
    StringField,
)

from . import audit, character, user


class Event(EmbeddedDocument):
    """
    Session summaries, character side stories, behind-the-scenes updates, etc.
    Basically a campaign's blog post.
    """
    owner = ReferenceField(user.User)
    name = StringField(required=True, min_length=4)
    tags = ListField(StringField(max_length=32))
    changelogs = MapField(EmbeddedDocumentField(document_type=audit.FieldChangeLog))


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
    synopsis = MultiLineStringField()