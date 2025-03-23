from flask_restful import Resource, reqparse, marshal_with

from ..schema import SkillModel, SkillSchema
from api import db
from ..resource_fields import skills_fields

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