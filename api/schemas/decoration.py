from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested, fields
from api.models.decoration import DecorationModel 

class DecorationSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = DecorationModel
    include_relationships = True
    load_instance = True

  id = auto_field()
  name = auto_field()
  desc = fields.String(data_key='description')
  type = auto_field()
  rarity = auto_field()
  slot = auto_field()
  skills = Nested('SkillRankSchema', many=True)