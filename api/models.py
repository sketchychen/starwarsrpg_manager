from flask_mongoengine import MongoEngine
from mongoengine import (
    IntField,
    ListField,
    MultiLineStringField,
    ReferenceField,
    StringField,
)

from constants import characteristics, skills, talents


db = MongoEngine(app)


class User(db.Document):
    email = db.StringField(required=True, min_length=4, max_length=64)
    username = db.StringField(required=True, min_length=2, max_length=32)


class Campaign(db.Document):
    name = StringField(required=True, min_length=4)
    owner = ReferenceField('User')
    roster = ListField()  # agg Character
    events = ListField()  # agg Event, Sessions?


class Character(db.Document):
    name = StringField(require=True, min_length=4)
    species = StringField(choices=())
    career = StringField(choices=())
    total_xp = IntField(default=100)
    available_xp = IntField(default=100)
    stats = DictField(
        default={
            'soak_value': 0
            'force_rating': 0
            'wounds': {
            'threshold': 0
                    'current': 0
                }
                'strain': {
            'threshold': 0
                    'current': 0
                }
                'defense': {
            'ranged': 0
                    'melee': 0
                }
            }
    )
    characteristics = DictField(
        default={
            characteristic.BRAWN[0]: 0,
            characteristic.AGILITY[0]: 0,
            characteristic.INTELLECT[0]: 0,
            characteristic.CUNNING[0]: 0,
            characteristic.WILLPOWER[0]: 0,
            characteristic.PRESENCE[0]: 0,
        }
    )
    skills = DictField(default=skills.SKILLS_DICT)
    talents = ListField(ReferenceField('Talent'))
    # equipment = {
    #     'weapons': [],  # agg constants & custom ITEM
    #     'armor': [],  # agg constants & custom ITEM
    #     'personal': [],  # agg constants & custom ITEM
    #         # {
    #         #     'name': ''
    #                 #     'description': ''
    #                 #     'rarity': 1
    #                 #     'encumbrance': 0
    #                 #     'price': 0
    #                 #     'quantity': 1
    #                 # }
    # }
    notes = MultiLineStringField()
