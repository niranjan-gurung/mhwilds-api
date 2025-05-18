from flask import request, jsonify
from flask_restful import Resource
from api.schemas.charm import CharmModel, CharmSchema, CharmRankModel
from api.schemas.skill import SkillRankModel
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
    result, errors = [], []
    try:
      def process_charm_item(charm_item) -> dict:
        ranks: list = charm_item.pop('ranks', [])
        schema = CharmSchema(session=db.session)
        charm = schema.load(charm_item)

        db.session.add(charm)
        db.session.flush()

        # process CharmRankModel:
        for rank in ranks:
          skill_rank_ids = []   # stores skill ranks from SkillRankModel
          skills = rank.pop('skills', [])

          # handle 'skills' field within each rank:
          for skill in skills:
            skill_rank = SkillRankModel.query.get(skill['id'])
            if skill_rank:
              skill_rank_ids.append(skill_rank)

          charm_rank = CharmRankModel(**rank, charm_id=charm.id)
          charm_rank.skills.extend(skill_rank_ids)
          db.session.add(charm_rank)

        db.session.commit()
        return {'id': charm.id, 'name': charm.name}

      if isinstance(json, list):
        for charm_item in json:
          try:
            result.append(process_charm_item(charm_item))
          except ValidationError as err:
            errors.append({'error': str(err), 'charm_item': charm_item})
      else:
        result.append(process_charm_item(json))
      
      if errors:
        return {'success': result, 'errors': errors}, 207
      return {'success': result}, 201
   
    except ValidationError as err:
      db.session.rollback()
      return {'errors': err.messages}, 400
    except Exception as e:
      db.session.rollback()
      return {'error': str(e)}, 500