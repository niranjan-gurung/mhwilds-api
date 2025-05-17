from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from api.models.slot import SlotModel

class SlotSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SlotModel
    include_fk = True
    load_instance = True
    exclude = ('id', 'armour_id')

  level = auto_field()