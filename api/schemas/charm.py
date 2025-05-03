from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested, fields
from api.models.charm import CharmModel, CharmRankModel
from api.schemas.skill import SkillRankSchema
from marshmallow import post_dump

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
    exclude = ('id',)

  charm_id = auto_field()
  name = auto_field()
  desc = fields.String(data_key='description')
  level = auto_field()
  rarity = auto_field()
  skills = Nested('SkillRankSchema', many=True)

  @post_dump
  def format_charm_id(self, data, **kwargs):
    if 'charm_id' in data:
      data['charm_id'] = {"id": data['charm_id']}
    return data