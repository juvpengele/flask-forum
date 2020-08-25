import os
from dotenv import load_dotenv
from os import environ

APP_FOLDER = os.path.dirname(__file__)
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


class Config:
    APP_HOST = environ.get("APP_HOST")
    APP_NAME = environ.get("APP_NAME")

    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = environ.get("MAIL_SERVER")
    MAIL_PORT = environ.get("MAIL_PORT")
    MAIL_USERNAME = environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER")
    MAIL_USE_SSL = environ.get('MAIL_ENCRYPTION') == "ssl"
    MAIL_USE_TLS = environ.get('MAIL_ENCRYPTION') == "tls"

    APP_FOLDER = os.path.dirname(__file__)
    AVATAR_FOLDER = os.path.join(APP_FOLDER, 'public/images/avatars')

    DEBUG_TB_INTERCEPT_REDIRECTS = False