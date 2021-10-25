from flask_mongoengine import MongoEngine

from .campaign import Campaign
from .character import Character
from .user import User



db = MongoEngine()