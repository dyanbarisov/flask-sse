import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATION= True
    FLASK_ADMIN_SWATCH = "cerulean"

    # Flask-Security config
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = "password_hash"
    SECURITY_PASSWORD_SALT = "security_password_salt"

    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"

    # Flask-Security features
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_TOKEN_MAX_AGE = None
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"


class DevelopmentConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True
