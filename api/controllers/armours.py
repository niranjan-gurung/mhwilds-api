from flask_restful import Resource, reqparse, marshal_with, abort

from api.models.armour import ArmourModel
from api.schemas.armour import ArmourSchema
from ..resource_fields import armour_fields
from api import db

armour_args = reqparse.RequestParser()
armour_args.add_argument('name', type=str, required=True, help="Armour name can't be blank")
armour_args.add_argument('slug', type=str, required=True, help="Armour slug can't be blank")
armour_args.add_argument('type', type=str, required=True, help="Armour type can't be blank")
armour_args.add_argument('rank', type=str, required=True, help="Armour rank can't be blank")
armour_args.add_argument('rarity', type=int, required=True, help="Armour rarity can't be blank")

class Armours(Resource):
  """get all armours OR single armour piece by id OR slug name"""
  @marshal_with(armour_fields)
  def get(self, id=None, slug=None):
    schema = ArmourSchema()
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
      schema = ArmourSchema(many=True)
      return schema.dump(all_armours)
    
    if not armour:
      abort(404, "Armour id not found")
    return schema.dump(armour)
  
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
      armour.slots = args['slots']

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