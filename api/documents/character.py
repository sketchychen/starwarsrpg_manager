from mongoengine import (
    BooleanField,
    Document,
    DictField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    IntField,
    ListField,
    MapField,
    MultiLineStringField,
    ReferenceField,
    StringField,
)

from . import audit, campaign, user
from ..lib import stats, skills


class Ability(EmbeddedDocument):
    """
    Record character's rank of acquired talent and special abilities.
    """
    name = StringField(primary_key=True, unique=True, required=True, min_length=2)
    rank = IntField(required=True, default=1)
    description = StringField(required=True, min_length=2)
    changelogs = MapField(EmbeddedDocumentField(document_type=audit.FieldChangeLog))
    source = StringField(default='Custom', choices=())


class Career(EmbeddedDocument):
    """
    Record character's acquired talents from respective talent trees.
    """
    name = StringField(unique=True, required=True, min_length=2)
    specialization = StringField(choices=())
    unlocked_talent_nodes = ListField(child=BooleanField(),
        min_length=20, max_length=20, default=[False for i in range(0, 20)])
    source = StringField(default='Custom', choices=())


class Item(EmbeddedDocument):
    """
    Record character's equipment quantity.

    While the official books provide the standard Items,
    these fields are provided in case users are allowed to personalize their own.
    """
    meta = {'allow_inheritance': True}

    name = StringField(primary_key=True, unique=True, required=True, min_length=2)
    category = StringField(required=True, default='Gear')
    description = StringField(required=True, min_length=2)
    rarity = IntField(required=True, default=1)
    encumbrance = IntField(required=True, default=0)
    price = IntField(required=True, default=0)
    quantity = IntField(required=True, default=1)
    source = StringField(required=True, choices=())


class Weapon(Item):
    category = StringField(required=True, default='Weapon')
    hp = IntField(null=True, default=0)
    skill = StringField(null=True, choices=skills.SKILLS_TUPLE)
    damage = IntField(null=True, default=0)
    range_type = StringField(null=True, choices=('Engaged', 'Short', 'Medium', 'Long'))
    special = MapField(field=IntField())


class Armor(Item):
    category = StringField(required=True, default='Armor')
    hp = IntField(null=True, default=0)
    defense = IntField(null=True, default=0)
    soak = IntField(null=True, default=0)


class Mod(Item):
    category = StringField(required=True, default='Mod')
    hp = IntField(null=True, default=0)
    base_modifier = MapField(IntField())
    mod_options = StringField(null=True)  # tentative


class Character(Document):
    """
    Can be either PC or NPC, denoted by field 'is_npc'.

    1:M User:Character
    M:M Character:Campaign
    1:M Character:Item
    """
    owner = ReferenceField(user.User)
    is_npc = BooleanField(default=False)
    name = StringField(required=True, min_length=2)
    species = StringField(required=True, choices=())
    career = EmbeddedDocumentField(Career)
    total_xp = IntField(default=100)
    available_xp = IntField(default=100)
    stats = DictField(default=stats.STATS_DICT)
    skills = DictField(default=skills.SKILLS_DICT)
    abilities = EmbeddedDocumentListField(document_type=Ability)
    credits = IntField(default=0)
    equipment = EmbeddedDocumentListField(document_type=Item)
    notes = MultiLineStringField()
    changelogs = MapField(EmbeddedDocumentField(document_type=audit.FieldChangeLog))
