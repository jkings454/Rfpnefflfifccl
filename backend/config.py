import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite:///db/test.db"

class Production(Config):
    DATABASE_URI = os.getenv("DATABASE_URI", "")

class Development(Config):
    DEBUG = True

class Testing(Config):
    TESTING = True