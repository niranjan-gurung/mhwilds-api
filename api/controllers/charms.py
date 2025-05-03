from flask import request
from flask_restful import Resource
from api.schemas.charm import CharmModel, CharmSchema
from api import db
from marshmallow import ValidationError

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
    json = request.get_json()
    try:
      schema = CharmSchema(session=db.session)
      charm = schema.load(json)

      db.session.add(charm)
      db.session.commit()
      return schema.dump(charm), 201

    except ValidationError as err:
      db.session.rollback()
      return {'errors': err.messages}, 400