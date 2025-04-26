from flask import request
from flask_restful import Resource
from api.schemas.skill import SkillModel, SkillRankModel, SkillSchema
from api import db
from marshmallow import ValidationError

class Skills(Resource):
  def get(self, id=None):
    schema = SkillSchema()
    if id:
      skill = db.get_or_404(SkillModel, id)
    else:
      all_skills = db.session \
        .scalars(
          db.select(SkillModel)
          .order_by(SkillModel.id)
        ).all()
      schema = SkillSchema(many=True)
      return schema.dump(all_skills)
    
    return schema.dump(skill)
  
  def post(self):
    json = request.get_json()
    result = [], errors = []
    try:
      if isinstance(json, list):
        for skill_item in json:
          try:
            ranks = skill_item.pop('ranks', [])
            schema = SkillSchema(session=db.session)
            skill = schema.load(skill_item)

            db.session.add(skill)
            db.session.flush()

            for rank in ranks:
              rank['skill_id'] = skill.id
              skill_rank = SkillRankModel(**rank)
              db.session.add(skill_rank)
            
            result.append({'id': skill.id, 'name': skill.name})
          except ValidationError as err:
            errors.append({'item': skill, 'error': str(err)})

        db.session.commit()
      else:
        # single skill object:
        ranks = json.pop('ranks', [])
        schema = SkillSchema(session=db.session)
        skill = schema.load(json)

        db.session.add(skill)
        db.session.flush()

        for rank in ranks:
          rank['skill_id'] = skill.id
          skill_rank = SkillRankModel(**rank)
          db.session.add(skill_rank)
        
        db.session.commit()
        result.append({'id': skill.id, 'name': skill.name})

        if errors:
          return {'success': result, 'errors': errors}, 207
        return schema.dump(skill), 201
      
    except ValidationError as err:
      db.session.rollback()
      return {'errors': err.messages}, 400

  def patch(self, id):
    json = request.get_json()
    skill = db.get_or_404(SkillModel, id)
    try:
      schema = SkillSchema(session=db.session, partial=True)
      update = schema.load(json, instance=skill, partial=True)

      db.session.commit()
      return schema.dump(update)
    except ValidationError as err:
      return {'errors': err.messages}, 422

  def delete(self, id):
    skill = db.get_or_404(SkillModel, id)
    try:
      schema = SkillSchema(session=db.session)
      db.session.delete(skill)
      db.session.commit()

      return schema.dump(skill), 204
    except ValidationError as err:
      db.session.rollback()
      return {'error': err.messages}, 400