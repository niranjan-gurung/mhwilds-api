from flask_restful import Resource, reqparse
from api.models.armour import ArmourModel
from api.schemas.armour import ArmourSchema
from api import db

armour_args = reqparse.RequestParser()
armour_args.add_argument('name', type=str, required=True, help="Armour name can't be blank")
armour_args.add_argument('slug', type=str, required=True, help="Armour slug can't be blank")
armour_args.add_argument('type', type=str, required=True, help="Armour type can't be blank")
armour_args.add_argument('rank', type=str, required=True, help="Armour rank can't be blank")
armour_args.add_argument('rarity', type=int, required=True, help="Armour rarity can't be blank")
armour_args.add_argument('defense', type=int, required=True, help="Armour defense can't be blank")

class Armours(Resource):
  """get all armours OR single armour piece by id OR slug name"""
  def get(self, id=None, slug=None):
    schema = ArmourSchema()
    if id:
      armour = db.get_or_404(ArmourModel, id)
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

    return schema.dump(armour)
  
  def post(self):
    args = armour_args.parse_args()
    armour = ArmourModel(
      name=args['name'], 
      slug=args['slug'], 
      type=args['type'], 
      rank=args['rank'], 
      rarity=args['rarity'],
      defense=args['defense']
    )
    
    db.session.add(armour)
    db.session.commit()
    
    result = db.session \
      .scalars(db.select(ArmourModel)) \
      .all()
    return result, 201
  
  def patch(self, id):
    args = armour_args.parse_args()
    armour = db.get_or_404(ArmourModel, id)

    armour.name = args['name']
    armour.slug = args['slug']
    armour.type = args['type']
    armour.rank = args['rank']
    armour.rarity = args['rarity']
    armour.defense = args['defense']

    db.session.commit()
    return armour
  
  def delete(self, id):
    armour = db.get_or_404(ArmourModel, id)

    db.session.delete(armour)
    db.session.commit()

    result = db.session \
      .scalars(db.select(ArmourModel)) \
      .all()
    return result, 204