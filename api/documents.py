from mongoengine import (
    BooleanField,
    Document,
    DictField,
    IntField,
    LazyReferenceField,
    ListField,
    MapField,
    MultiLineStringField,
    ReferenceField,
    StringField,
)

from . import stats, skills, talents


class User(Document):
    is_admin = BooleanField(required=True, default=False)
    email = StringField(required=True, min_length=4, max_length=64)
    username = StringField(required=True, min_length=2, max_length=32)
    passphrase = StringField(required=True, min_length=8, max_length=32)


class Campaign(Document):
    name = StringField(required=True, min_length=4)
    owner = ReferenceField(User)
    roster = ListField()  # agg Character
    timeline = ListField(EmbeddedDocumentField(Event))  # agg Event, Sessions?


class Character(Document):
    owner = ReferenceField(User)
    name = StringField(required=True, min_length=2)
    species = StringField(required=True, choices=())
    notes = MultiLineStringField()
    campaigns = ListField(ReferenceField(Campaign))
    is_npc = BooleanField(default=False)
    career = StringField(choices=())
    specialization = StringField(choices=())
    total_xp = IntField(default=100)
    available_xp = IntField(default=100)
    stats = DictField(default=stats.STATS_DICT)
    skills = DictField(default=skills.SKILLS_DICT)
    unlocked_talent_nodes = ListField(child=BooleanField(),
        min_length=20, max_length=20, default=[False for i in range(0, 20)])
    abilities = ListField(ListField(min_length=2, max_length=2))  # [ability name, rank]
    credits = IntField(default=0)
    equipment = ListField(ReferenceField(Item))


# ## MOSTLY DEFAULT DATA (with customizing exceptions)

# class Ability(Document):
#     name = StringField(primary_key=True, unique=True, required=True, min_length=2)


# class Item(Document):
#     name = StringField(primary_key=True, unique=True, required=True, min_length=2)
#     category = StringField(required=True, choices=('weapon', 'armor', 'personal'))
#     description = StringField(required=True, min_length=2)
#     rarity = IntField(required=True, default=1)
#     encumbrance = IntField(required=True, default=0)
#     price = IntField(required=True, default=0)
#     skill = StringField(null=True, choices=skills.SKILLS_ALL)
#     damage = IntField(null=True, default=0)
#     range_type = StringField(null=True, choices=('Engaged', 'Short', 'Medium', 'Long'))
#     special = StringField(null=True, min_length=2)


# class Specialization(Document):
#     name = StringField(unique=True, required=True, min_length=2)
#     career = StringField(choices=(''))
