from .controllers.armours import Armours
from .controllers.skills import Skills
from .controllers.charms import Charms
from .controllers.decorations import Decorations
from flask_restful import Api

def init_routes(api: Api):
  api.add_resource(Armours, 
                   '/api/armours/', 
                   '/api/armours/<int:id>', 
                   '/api/armours/<string:slug>')
    
  api.add_resource(Skills, 
                   '/api/skills/',
                   '/api/skills/<int:id>')
  
  api.add_resource(Charms, 
                   '/api/charms/',
                   '/api/charms/<int:id>')
  
  api.add_resource(Decorations, 
                   '/api/decorations/',
                   '/api/decorations/<int:id>')