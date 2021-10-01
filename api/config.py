import os
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config(object):
    """
    Base config, uses staging database server.
    """
    TESTING = False
    DB_SERVER = '192.168.1.56'

    @property
    def DATABASE_URI(self):  # Note: all caps
        return f"mongodb://user@{self.DB_SERVER}/foo"


class ProductionConfig(Config):
    """
    Uses production database server.
    """
    # SECRET_KEY = "flask-app-secret-key-change-it"
    # JWT_SECRET_KEY = "jwt-app-secret-key-change-it"
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'


class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DATABASE_URI = 'mongodb:///:memory:'
    TESTING = True
