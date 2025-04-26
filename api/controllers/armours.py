from flask import request
from flask_restful import Resource
from api.models.armour import ArmourModel
from api.models.slot import SlotModel
from api.schemas.armour import ArmourSchema
from api import db
from marshmallow import ValidationError

class Armours(Resource):
  """get all armours OR single armour piece by id OR slug name"""
  def get(self, id=None, slug=None):
    schema = ArmourSchema()
    if id:
      armour = db.get_or_404(ArmourModel, id)
    elif slug:
      armour = db.session \
        .scalar(
          db.select(ArmourModel)
          .filter_by(slug=slug)
        )
    else:
      all_armours = db.session \
        .scalars(
          db.select(ArmourModel)
          .order_by(ArmourModel.id)
        ).all()
      schema = ArmourSchema(many=True)
      return schema.dump(all_armours)

    return schema.dump(armour)
  
  def post(self):
    json = request.get_json()
    result, errors = [], []
    try:
      if isinstance(json, list):
        for armour_item in json:
          try:
            slots = armour_item.pop('slots', [])
            schema = ArmourSchema(session=db.session)
            armour = schema.load(armour_item)
            
            db.session.add(armour)
            db.session.flush()

            for slot in slots:
              slot['armour_id'] = armour.id 
              slot_model = SlotModel(**slot)
              db.session.add(slot_model)

            result.append({'id': armour.id, 'name': armour.name})
          except ValidationError as err:
            errors.append({'item': armour, 'error': str(err)})

        db.session.commit()
      else:
        slots = json.pop('slots', [])
        schema = ArmourSchema(session=db.session)
        armour = schema.load(json)

        db.session.add(armour)
        db.session.flush()  

        for slot in slots:
          slot['armour_id'] = armour.id  
          slot_model = SlotModel(**slot)
          db.session.add(slot_model)

        db.session.commit()  
        result.append({'id': armour.id, 'name': armour.name})

        if errors:
          return {'success': result, 'errors': errors}, 207 
        return schema.dump(armour), 201
      
    except ValidationError as err:
      db.session.rollback()
      return {'errors': err.messages}, 400
  
  def patch(self, id):
    json = request.get_json()
    armour = db.get_or_404(ArmourModel, id)
    try:
      schema = ArmourSchema(session=db.session, partial=True)
      update = schema.load(json, instance=armour)

      db.session.commit()
      return schema.dump(update)
    except ValidationError as err:
      return {'errors': err.messages}, 422
  
  def delete(self, id):
    armour = db.get_or_404(ArmourModel, id)
    try:
      schema = ArmourSchema(session=db.session)
      db.session.delete(armour)
      db.session.commit()

      return schema.dump(armour), 204
    except ValidationError as err:
      db.session.rollback()
      return {'error': err.messages}, 400