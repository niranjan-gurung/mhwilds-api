from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import RelatedList, Nested

from .models import ArmourModel, SlotModel, SkillModel, SkillRankModel

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
  slots = RelatedList(Nested('SlotSchema'))

class SlotSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SlotModel
    include_fk = True
    load_instance = True

class SkillSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SkillModel
    include_relationships = True
    load_instance = True

  id = auto_field()
  name = auto_field()
  type = auto_field()
  desc = auto_field()
  ranks = RelatedList(Nested('SkillRankSchema'))

class SkillRankSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SkillRankModel
    include_fk = True
    load_instance = True
  
  id = auto_field()
  level = auto_field()
  skill_id = auto_field()
  desc = auto_field()