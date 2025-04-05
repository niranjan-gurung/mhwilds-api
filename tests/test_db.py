from api import create_app, db
from api.models.armour import ArmourModel, SkillRankModel
from api.models.slot import SlotModel
from api.models.skill import SkillModel

with create_app().app_context():
  # print('test from test_db.py')
  ar = ArmourModel(
    name='Arkvulcan Mail \u03b2', 
    slug='arkvulcan-mail-beta',         # slug name needs to be alpha/beta instead of unicode
    type='chest', rank='high', rarity=8)
  
  slot1 = SlotModel(level=3, armour=ar)
  slot2 = SlotModel(level=2, armour=ar)

  db.session.add(ar)
  db.session.add_all([slot1, slot2])

  sk = SkillModel(
    name='Convert Element',
    type='Armour',
    desc='After taking elemental damage, temporarily grants you dragon element effects. (Cooldown after effect ends.)'
  )

  skr1 = SkillRankModel(level=1, desc='While active, deals extra dragon damage after dealing enough elemental damage. Slightly increases dragon attack.', skill=sk)
  skr2 = SkillRankModel(level=2, desc='Increases additional dragon damage and increases dragon attack.', skill=sk)
  db.session.add(sk)
  db.session.add_all([skr1, skr2])

  db.session.commit()

  # head
  # hb = db.session \
  #       .scalar(db.select(ArmourModel) \
  #       .filter_by(id=4))
  # hbs = db.session \
  #       .scalar(db.select(SkillRankModel) \
  #       .filter_by(id=6))
  
  # print(hbs.skill.name)
  # ma = db.session \
  #       .scalar(db.select(ArmourModel) \
  #       .filter_by(id=4))
  # mas1 = db.session \
  #       .scalar(db.select(SkillRankModel) \
  #       .filter_by(id=6))   # wex lvl 1
  # hb.skills.append(hbs)
  # db.session.add(hb)
  # db.session.commit()

  # slot1 = SlotModel(level=3, armour=ar)
  # slot2 = SlotModel(level=2, armour=ar)
  # slot3 = SlotModel(level=1, armour_model=ar)
  # slot4 = SlotModel(rank=1, armour_model=7)
  # slot5 = SlotModel(rank=2, armour_model=9)
  # slot6 = SlotModel(rank=1, armour_model=9)

  # sk = SkillModel(
  #   name='Convert Element',
  #   type='Armour',
  #   desc='After taking elemental damage, temporarily grants you dragon element effects. (Cooldown after effect ends.)'
  # )

  # skr1 = SkillRankModel(level=1, desc='While active, deals extra dragon damage after dealing enough elemental damage. Slightly increases dragon attack.', skill=sk)
  # skr2 = SkillRankModel(level=2, desc='Increases additional dragon damage and increases dragon attack.', skill=sk)
  # skr3 = SkillRankModel(level=3, desc='Further increases additional dragon damage and greatly increases dragon attack.', skill=sk)
  # skr4 = SkillRankModel(level=4, desc='Attacks that hit weak points have 20% increased affinity, with an extra 15% on wounds', skill=sk)
  # skr5 = SkillRankModel(level=5, desc='Attacks that hit weak points have 30% increased affinity, with an extra 20% on wounds', skill=sk)

  # db.session.add(sk)
  # db.session.add_all([skr1, skr2, skr3])
  # db.session.commit()

# """create new table"""
# with create_app().app_context():
#   db.create_all()

# alpha = \u03b1 
# beta  = \u03b2