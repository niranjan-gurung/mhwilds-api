from flask import request
from flask_restful import Resource
from api.schemas.decoration import DecorationSchema, DecorationModel
from api import db
from marshmallow import ValidationError

class Decorations(Resource):
  def get(self, id=None):
    schema = DecorationSchema()
    if id:
      deco = db.get_or_404(DecorationModel, id)
    else:
      all_decos = db.session \
        .scalars(
          db.select(DecorationModel)
          .order_by(DecorationModel.id)
        ).all()
      schema = DecorationSchema(many=True)
      return schema.dump(all_decos)
    return schema.dump(deco)
  
  def post(self):
    json = request.get_json()
    try:
      schema = DecorationSchema(session=db.session)
      deco = schema.load(json)

      db.session.add(deco)
      db.session.commit()
      return schema.dump(deco), 201

    except ValidationError as err:
      db.session.rollback()
      return {'errors': err.messages}, 400