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

from .character import Character
from .audit import FieldChangeLog
from .user import User


__all__ = ('Campaign', )


class Event(EmbeddedDocument):
    """
    Session summaries, character side stories, behind-the-scenes updates, etc.
    Basically a campaign's blog post.
    """
    owner = LazyReferenceField(User)
    name = StringField(required=True, min_length=4)
    tags = ListField(StringField(max_length=32))
    body = StringField(required=True, min_length=4)
    changelogs = MapField(EmbeddedDocumentField(document_type=audit.FieldChangeLog))


class Campaign(Document):
    """
    1:M User:Campaign
    M:M Campaign:Character
    1:M Campaign:Event
    """
    name = StringField(required=True, min_length=4)
    owner = LazyReferenceField(User)
    editors = ListField(LazyReferenceField(User))
    characters = ListField(ReferenceField(Character))
    timeline = EmbeddedDocumentListField(Event)
    synopsis = MultiLineStringField()