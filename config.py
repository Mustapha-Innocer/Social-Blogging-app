import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "JHJSDHJFSSNDYSAQBNB"

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProdConfig:
    pass

config = {
    "dev": DevConfig,
    "testing": TestingConfig,
    "prod": ProdConfig,
    "default": DevConfig
}