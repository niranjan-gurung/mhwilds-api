from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested, fields
from api.models.skill import SkillModel, SkillRankModel

class SkillSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SkillModel
    include_relationships = True
    load_instance = True

  id = auto_field()
  name = auto_field()
  type = auto_field()
  desc = auto_field()
  ranks = Nested('SkillRankSchema', many=True)

class SkillRankSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SkillRankModel
    include_fk = True
    load_instance = True
  
  id = auto_field()
  level = auto_field()
  skill_id = auto_field()
  desc = auto_field()
  skill_name = fields.String(attribute='skill.name')