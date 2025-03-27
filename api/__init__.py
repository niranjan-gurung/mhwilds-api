from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
api = Api()
migrate = Migrate()

def create_app(config_class=Config):

  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  migrate.init_app(app, db)

  from api.routes import init_routes 
  init_routes(api)
  api.init_app(app)
  
  return app