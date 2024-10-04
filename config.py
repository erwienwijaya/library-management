import os
from dotenv import load_dotenv

# Load file .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_DEV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TESTING = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True