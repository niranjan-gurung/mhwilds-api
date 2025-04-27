from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from api.models.charm import CharmModel, CharmRankModel
from api.schemas.skill import SkillRankSchema

class CharmSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = CharmModel
    include_relationships = True
    load_instance = True

  id = auto_field()
  name = auto_field()
  ranks = Nested('CharmRankSchema', many=True)

class CharmRankSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = CharmRankModel
    include_fk = True
    load_instance = True
  
  id = auto_field()
  name = auto_field()
  level = auto_field()
  rarity = auto_field()
  skills = Nested('SkillRankSchema', many=True)