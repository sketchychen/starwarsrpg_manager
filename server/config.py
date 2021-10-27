import os

from datetime import timedelta


ENV = os.environ.get('FLASK_ENV')


class Config(object):
    """
    Base config, uses staging database server.
    """
    DEBUG = False
    TESTING = False
    DB_SERVER = '127.0.0.1'
    MONDODB_DB = 'swrpg_manager'
    MONGODB_PORT = 27017


class ProductionConfig(Config):
    """
    Uses production database server.
    """
    # SECRET_KEY = "flask-app-secret-key-change-it"
    # JWT_SECRET_KEY = "jwt-app-secret-key-change-it"
    # JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)


class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = '127.0.0.1'


class TestingConfig(Config):
    DB_SERVER = '127.0.0.1'
    DATABASE_URI = 'mongodb:///:memory:'
    TESTING = True


def load_config():
    if ENV == 'production':
        return ProductionConfig
    elif ENV == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig