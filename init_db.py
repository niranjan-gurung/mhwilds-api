from api import app, db, ArmourModel, SlotModel

with app.app_context():
  ar = ArmourModel(
    name='Arkvulcan Helm \u03b2', 
    slug='arkvulcan-helm-beta',         # slug name needs to be alpha/beta instead of unicode
    type='head', rank='high', rarity=8)

  slot1 = SlotModel(level=3, armour_model=ar)
  slot2 = SlotModel(level=2, armour_model=ar)
  slot3 = SlotModel(level=1, armour_model=ar)
  #slot4 = SlotModel(rank=1, armour_model=7)
  #slot5 = SlotModel(rank=2, armour_model=9)
  #slot6 = SlotModel(rank=1, armour_model=9)

  db.session.add(ar)
  db.session.add_all([slot1, slot2, slot3])
  
  db.session.commit()

# """create new table"""
# with app.app_context():
#   db.create_all()

# alpha = \u03b1 
# beta  = \u03b2