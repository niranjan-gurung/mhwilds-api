from flask_restful import Resource, reqparse, marshal_with

from api.schemas.skill import SkillModel, SkillSchema
from ..resource_fields import skills_fields
from api import db

skill_args = reqparse.RequestParser()

class Skills(Resource):
  @marshal_with(skills_fields)
  def get(self):
    all_skills = db.session \
      .scalars(db.select(SkillModel)) \
      .all()
    schema = SkillSchema(many=True)
    return schema.dump(all_skills)
  
  @marshal_with(skills_fields)
  def post(self):
    # args = skill_args.parse_args()
    # skill = SkillModel(
    #   name=args['name'], 
    #   type=args['type'], 
    #   desc=args['desc']
    # )
    pass