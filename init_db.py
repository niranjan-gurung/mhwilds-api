from api import app, db, ArmourModel, SlotModel, SkillModel, SkillRankModel

with app.app_context():
  # ar = ArmourModel(
  #   name='Arkvulcan Mail \u03b2', 
  #   slug='arkvulcan-mail-beta',         # slug name needs to be alpha/beta instead of unicode
  #   type='chest', rank='high', rarity=8)

  # slot1 = SlotModel(level=3, armour=ar)
  # slot2 = SlotModel(level=2, armour=ar)
  #slot3 = SlotModel(level=1, armour_model=ar)
  #slot4 = SlotModel(rank=1, armour_model=7)
  #slot5 = SlotModel(rank=2, armour_model=9)
  #slot6 = SlotModel(rank=1, armour_model=9)

  sk = SkillModel(
    name='Weakness Exploit',
    type='Armour',
    desc='Increases affinity of attacks that expoit a monster\'s weak points and wounds'
  )

  skr1 = SkillRankModel(level=1, desc='Attacks that hit weak points gain affinity +5%, with an extra 3% on wounds', skill=sk)
  skr2 = SkillRankModel(level=2, desc='Attacks that hit weak points gain affinity +10%, with an extra 5% on wounds', skill=sk)
  skr3 = SkillRankModel(level=3, desc='Attacks that hit weak points gain affinity +15%, with an extra 10% on wounds', skill=sk)
  skr4 = SkillRankModel(level=4, desc='Attacks that hit weak points have 20% increased affinity, with an extra 15% on wounds', skill=sk)
  skr5 = SkillRankModel(level=5, desc='Attacks that hit weak points have 30% increased affinity, with an extra 20% on wounds', skill=sk)

  #print(skr1)
  db.session.add(sk)
  #db.session.add(slot1)
  db.session.add_all([skr1, skr2, skr3, skr4, skr5])
  db.session.commit()

# """create new table"""
# with app.app_context():
#   db.create_all()

# alpha = \u03b1 
# beta  = \u03b2