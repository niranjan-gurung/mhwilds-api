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

  from .controllers import armours, skills
  api.add_resource(armours.Armours, 
                   '/api/armours/', 
                   '/api/armours/<int:id>', 
                   '/api/armours/<string:slug>')
  
  api.add_resource(skills.Skills, '/api/skills/')
  api.init_app(app)

  @app.route('/')
  def hello():
    return {"hello": "world"}
  
  return app