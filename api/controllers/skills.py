from flask_restful import Resource, reqparse
from api.schemas.skill import SkillModel, SkillSchema
from api import db

skill_args = reqparse.RequestParser()

class Skills(Resource):
  def get(self, id=None):
    schema = SkillSchema()
    if id:
      skill = db.get_or_404(SkillModel, id)
    else:
      all_skills = db.session \
        .scalars(db.select(SkillModel)) \
        .all()
      schema = SkillSchema(many=True)
      return schema.dump(all_skills)
    
    return schema.dump(skill)
  
  def post(self):
    args = skill_args.parse_args()
    """
    args = skill_args.parse_args()
    skill = SkillModel(
      name=args['name'], 
      type=args['type'], 
      desc=args['desc']
    )
    """
    result = db.session \
      .scalars(db.select(SkillModel)) \
      .all()
    return result, 201

  def patch(self, id):
    args = skill_args.parse_args()
    skill = db.get_or_404(SkillModel, id)
    
    """
    update goes here..

    skill.name = args['name']
    skill.type = args['type']
    """

    db.session.commit()
    return skill

  def delete(self, id):
    skill = db.get_or_404(SkillModel, id)

    db.session.delete(skill)
    db.session.commit()

    result = db.session \
      .scalars(db.select(SkillModel)) \
      .all()
    return result, 204