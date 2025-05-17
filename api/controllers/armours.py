from flask import request
from flask_restful import Resource
from api.models.armour import ArmourModel
from api.models.slot import SlotModel
from api.models.skill import SkillRankModel
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
      def process_armour_item(armour_item) -> dict:
        # extract nested data that needs special handling
        slots = armour_item.pop('slots', [])
        skill_rank_ids = armour_item.pop('skills', [])
        
        # load the armour model without slots and skills
        schema = ArmourSchema(session=db.session)
        armour = schema.load(armour_item)
        
        db.session.add(armour)
        db.session.flush()  # get ID for relationships without commiting
        
        # add slots
        for slot in slots:
          slot['armour_id'] = armour.id 
          slot_model = SlotModel(**slot)
          db.session.add(slot_model)
        
        # add skill associations
        # if skill_rank_ids contains IDs directly
        for skill_rank_id in skill_rank_ids:
          if isinstance(skill_rank_id, int):
            skill_rank = SkillRankModel.query.get(skill_rank_id)
            if skill_rank:
              armour.skills.append(skill_rank)
          # if skill_rank_ids contains objects with ID field
          elif isinstance(skill_rank_id, dict) and 'id' in skill_rank_id:
            skill_rank = SkillRankModel.query.get(skill_rank_id['id'])
            if skill_rank:
              armour.skills.append(skill_rank)
        db.session.commit()
        return {'id': armour.id, 'name': armour.name}

      if isinstance(json, list):
        for armour_item in json:
          try:
            result.append(process_armour_item(armour_item))
          except ValidationError as err:
            errors.append(process_armour_item(armour_item))
      else:
        result.append(process_armour_item(json))

      if errors:
        return {'success': result, 'errors': errors}, 207
      return {'success': result}, 201
    
    except ValidationError as err:
      db.session.rollback()
      return {'errors': err.messages}, 400
    except Exception as e:
      db.session.rollback()
      return {'error': str(e)}, 500
    
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