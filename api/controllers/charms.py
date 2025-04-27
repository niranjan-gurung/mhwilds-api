from flask_restful import Resource
from api.schemas.charm import CharmModel, CharmSchema
from api import db

class Charms(Resource):
  def get(self, id=None):
    schema = CharmSchema()
    if id:
      charm = db.get_or_404(CharmModel, id)
    else:
      all_charms = db.session \
        .scalars(
          db.select(CharmModel)
          .order_by(CharmModel.id)
        ).all()
      schema = CharmSchema(many=True)
      return schema.dump(all_charms)
    return schema.dump(charm)
  
  def post(self):
    pass