from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.models.resistances import ResistancesModel

class ResistancesSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = ResistancesModel
    include_fk = True
    load_instance = True