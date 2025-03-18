from flask import Flask
from flask_restful import Resource, Api, reqparse, marshal_with, fields, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Related, Nested
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

"""
schema (armour):
  - armour fields 
    ** Prioritised fields **
    - id (int)
    - name (str)
    - slug (str): a unique identifier used inside the url request
    - type (str): head, chest, arms etc.
    - rank: (str) low or high
    - rarity (int): 1-8
    - deco slots (list[slots]): ex. list[{'rank': 3, 'rank': 1, 'rank': 1}]
    - skills (list[skills])

    ** TODO later on: **
    - set bonus
    - defense
    - resistances
"""
class ArmourModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=False, nullable=False)
  slug: Mapped[str] = mapped_column(unique=False, nullable=False)
  type: Mapped[str] = mapped_column(unique=False, nullable=False)
  rank: Mapped[str] = mapped_column(unique=False, nullable=False)
  rarity: Mapped[int] = mapped_column(unique=False, nullable=False)
  slots: Mapped['SlotModel'] = relationship('SlotModel', 
                                            cascade='all, delete-orphan', 
                                            back_populates='armour')

  def __repr__(self):
    return '{}-{}-{}-{}-{}'\
      .format(self.name, self.slug, self.type, self.rank, self.rarity)

class SlotModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  level: Mapped[int] = mapped_column(nullable=True)
  armour_id: Mapped[int] = mapped_column(db.ForeignKey('armour_model.id', ondelete='CASCADE'))
  armour: Mapped['ArmourModel'] = relationship('ArmourModel', 
                                               back_populates='slots', 
                                               foreign_keys=[armour_id])

  def __repr__(self):
    return '{}-{}'.format(self.id, self.level)

class SlotSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = SlotModel
    include_fk = True
  
class ArmourSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = ArmourModel
    include_relationships = True

  id = auto_field()
  name = auto_field()
  slug = auto_field()
  type = auto_field()
  rank = auto_field()
  slots = Nested(SlotSchema)
  #slots = Related(['id', 'level'])

armour_args = reqparse.RequestParser()
armour_args.add_argument('name', type=str, required=True, help="Armour name can't be blank")
armour_args.add_argument('slug', type=str, required=True, help="Armour slug can't be blank")
armour_args.add_argument('type', type=str, required=True, help="Armour type can't be blank")
armour_args.add_argument('rank', type=str, required=True, help="Armour rank can't be blank")
armour_args.add_argument('rarity', type=int, required=True, help="Armour rarity can't be blank")

slot_fields = {
  'id': fields.Integer,
  'level': fields.Integer,
  'armour_id': fields.Integer
}

armour_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'slug': fields.String,
  'type': fields.String,
  'rank': fields.String,
  'rarity': fields.Integer,
  'slots': fields.List(fields.Nested(slot_fields))
}

class Armours(Resource):
  """get all armours OR single armour piece by id OR slug name"""
  @marshal_with(armour_fields)
  def get(self, id=None, slug=None):
    armour_schema = ArmourSchema()
    if id:
      armour = db.session \
        .scalar(db.select(ArmourModel) \
        .filter_by(id=id))
    elif slug:
      armour = db.session \
        .scalar(db.select(ArmourModel) \
        .filter_by(slug=slug))
    else:
      all_armours = db.session \
        .scalars(db.select(ArmourModel)) \
        .all()
      armour_schema = ArmourSchema(many=True)
      return armour_schema.dump(all_armours)
    
    if not armour:
      abort(404, "Armour id not found")
    return armour_schema.dump(armour)
    
  @marshal_with(armour_fields)
  def post(self):
    args = armour_args.parse_args()
    armour = ArmourModel(
      name=args['name'], 
      slug=args['slug'], 
      type=args['type'], 
      rank=args['rank'], 
      rarity=args['rarity']
    )
    
    db.session.add(armour)
    db.session.commit()
    
    result = db.session \
      .scalars(db.select(ArmourModel)) \
      .all()
    return result, 201
  
  @marshal_with(armour_fields)
  def patch(self, id):
    args = armour_args.parse_args()
    if id:
      armour = db.session \
        .scalar(db.select(ArmourModel) \
        .filter_by(id=id))

      if not armour:
        abort(404, "Armour id not found")

      armour.name = args['name']
      armour.slug = args['slug']
      armour.type = args['type']
      armour.rank = args['rank']
      armour.rarity = args['rarity']

      db.session.commit()
      return armour
  
  @marshal_with(armour_fields)
  def delete(self, id):
    if id:
      armour = db.session \
        .scalar(db.select(ArmourModel) \
        .filter_by(id=id))

      if not armour:
        abort(404, "Armour id not found")

      db.session.delete(armour)
      db.session.commit()

      result = db.session \
        .scalars(db.select(ArmourModel)) \
        .all()
      return result, 204

api.add_resource(Armours, 
                 '/api/armours/', 
                 '/api/armours/<int:id>', 
                 '/api/armours/<string:slug>')

@app.route('/')
def hello():
  return {"hello": "world"}

if __name__ == '__main__':
  app.run(debug=True)