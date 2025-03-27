from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.slot import SlotModel

class SlotSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SlotModel
    include_fk = True
    load_instance = True