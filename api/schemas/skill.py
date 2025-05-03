from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested, fields
from api.models.skill import SkillModel, SkillRankModel
from marshmallow import post_dump

class SkillSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SkillModel
    include_relationships = True
    load_instance = True

  name = auto_field()
  type = auto_field()
  desc = fields.String(data_key='description')
  ranks = Nested('SkillRankSchema', many=True)

class SkillRankSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SkillRankModel
    include_fk = True
    load_instance = True
  
  skill = fields.String(attribute='skill.name')
  id = auto_field()
  level = auto_field()
  desc = fields.String(data_key='description')

  @post_dump
  def format_charm_id(self, data, **kwargs):
    if 'skill_id' in data:
      data['skill'] = {
        "id": data['skill_id'],
        "name": data['skill']
      }
      del data['skill_id']
    return data