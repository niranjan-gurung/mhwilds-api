from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from api.models.armour import ArmourModel
from api.schemas.slot import SlotSchema
# from api.schemas.skill import SkillRankSchema

class ArmourSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = ArmourModel
    include_relationships = True
    load_instance = True

  id = auto_field()
  name = auto_field()
  slug = auto_field()
  type = auto_field()
  rank = auto_field()
  rarity = auto_field()
  slots = Nested('SlotSchema', many=True)
  skills = Nested('SkillRankSchema', many=True)