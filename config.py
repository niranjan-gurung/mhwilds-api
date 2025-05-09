import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
  SECRET_KEY = 'dev'
  SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False