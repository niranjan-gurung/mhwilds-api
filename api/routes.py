from .controllers.armours import Armours
from .controllers.skills import Skills
from flask_restful import Api

def init_routes(api: Api):
  api.add_resource(Armours, 
                   '/api/armours/', 
                   '/api/armours/<int:id>', 
                   '/api/armours/<string:slug>')
    
  api.add_resource(Skills, '/api/skills/')