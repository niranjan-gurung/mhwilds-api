from api import create_app, db
from api.models.armour import ArmourModel, SkillRankModel
from api.models.slot import SlotModel
from api.models.skill import SkillModel
from api.models.charm import CharmModel, CharmRankModel
from api.models.resistances import ResistancesModel

with create_app().app_context():
  # ar = ArmourModel(
  #   name='G.Arkveld Helm', 
  #   slug='g.arkveld-helm',         
  #   type='head', rank='low', rarity=4, defense=30)
  # ar1 = ArmourModel(
  #   name='G.Arkveld Mail', 
  #   slug='g.arkveld-mail',         
  #   type='chest', rank='low', rarity=4, defense=30)
  # ar2 = ArmourModel(
  #   name='G.Arkveld Vambraces', 
  #   slug='g.arkveld-vambraces',         
  #   type='gloves', rank='low', rarity=4, defense=30)
  # ar3 = ArmourModel(
  #   name='G.Arkveld Coil', 
  #   slug='g.arkveld-coil',         
  #   type='waist', rank='low', rarity=4, defense=30)
  # ar4 = ArmourModel(
  #   name='G.Arkveld Greaves', 
  #   slug='g.arkveld-greaves',         
  #   type='legs', rank='low', rarity=4, defense=30)
  
  # res = ResistancesModel(
  #   fire=2,
  #   water=0,
  #   ice=-0,
  #   thunder=-1,
  #   dragon=-4,
  #   armour=ar
  # )
  # res = ResistancesModel(
  #   fire=2,
  #   water=0,
  #   ice=-0,
  #   thunder=-1,
  #   dragon=-4,
  #   armour=ar1
  # )
  # res = ResistancesModel(
  #   fire=2,
  #   water=0,
  #   ice=-0,
  #   thunder=-1,
  #   dragon=-4,
  #   armour=ar2
  # )
  # res = ResistancesModel(
  #   fire=2,
  #   water=0,
  #   ice=-0,
  #   thunder=-1,
  #   dragon=-4,
  #   armour=ar3
  # )
  # res = ResistancesModel(
  #   fire=2,
  #   water=0,
  #   ice=-0,
  #   thunder=-1,
  #   dragon=-4,
  #   armour=ar4
  # )

  # slot1 = SlotModel(level=1, armour=ar)
  # #slot2 = SlotModel(level=1, armour=ar1)
  # slot3 = SlotModel(level=1, armour=ar2)
  # slot4 = SlotModel(level=1, armour=ar3)
  # slot4a = SlotModel(level=1, armour=ar3)
  # slot5 = SlotModel(level=1, armour=ar4)

  # sk = SkillModel(
  #   name='Flayer',
  #   type='Armour',
  #   desc='Makes it easier to inflict wounds. Upon inflicting enough damage, also deals additional non-elemental damage.'
  # )

  # skr1 = SkillRankModel(level=1, desc='Makes it ever so slightly easier to inflict wounds. Also deals additional non-elemental damage.', skill=sk)
  # skr2 = SkillRankModel(level=2, desc='Makes it moderately easier to inflict wounds. Also deals slightly more additional non-elemental damage.', skill=sk)
  # skr3 = SkillRankModel(level=3, desc='Makes it easier to inflict wounds. Also deals moderately more additional non-elemental damage.', skill=sk)
  # skr4 = SkillRankModel(level=4, desc='Makes it much easier to inflict wounds. Also deals more additional non-elemental damage.', skill=sk)
  # skr5 = SkillRankModel(level=5, desc='Makes it significantly easier to inflict wounds. Also deals much more additional non-elemental damage.', skill=sk)
  
  # sk1 = SkillModel(
  #   name='Blight Resistance',
  #   type='Armour',
  #   desc='Grants protection against all elemental blights.'
  # )

  # sk1r1 = SkillRankModel(level=1, desc='Reduces the duration of all elemental blights by 50%.', skill=sk1)
  # sk1r2 = SkillRankModel(level=2, desc='Reduces the duration of all elemental blights by 75%.', skill=sk1)
  # sk1r3 = SkillRankModel(level=3, desc='Nullifies all elemental blights.', skill=sk1)
  # #sk1r4 = SkillRankModel(level=4, desc='Reduces fixed stamina depletion by 40%.', skill=sk1)
  # #sk1r5 = SkillRankModel(level=5, desc='Reduces fixed stamina depletion by 50%.', skill=sk1)
 
  # sk2 = SkillModel(
  #   name='Aquatic/Oilsilt Mobility',
  #   type='Armour',
  #   desc='Grants resistance against impairments to mobility while in water, oilsilt, or streams.'
  # )

  # sk2r1 = SkillRankModel(level=1, desc='Negates the effects of muddy streams, and prevents you from being slowed down in water or oilsilt.', skill=sk2)
  # sk2r2 = SkillRankModel(level=2, desc='Also negates the effects of waves.', skill=sk2)
  # #sk2r3 = SkillRankModel(level=3, desc='Explosive power +30%', skill=sk2)
  
  # sk3 = SkillModel(
  #   name='Blast Resistance',
  #   type='Armour',
  #   desc='Grants protection against blastblight.'
  # )

  # sk3r1 = SkillRankModel(level=1, desc='Delays blastblight and reduces blast damage.', skill=sk3)
  # sk3r2 = SkillRankModel(level=2, desc='Greatly delays blastblight and greatly reduces blast damage.', skill=sk3)
  # sk3r3 = SkillRankModel(level=3, desc='Prevents blastblight.', skill=sk3)
  
  # marathon runner 1
  mathrn1 = db.session \
        .scalar(db.select(SkillRankModel) \
        .filter_by(id=103))
  mathrn2 = db.session \
        .scalar(db.select(SkillRankModel) \
        .filter_by(id=104))
  mathrn3 = db.session \
        .scalar(db.select(SkillRankModel) \
        .filter_by(id=105))

  charm = CharmModel(
    name='Marathon Charm'
  )

  chrmr1 = CharmRankModel(
    name='Marathon Charm 1', 
    level=1, 
    rarity=4,
    charm=charm,
    skills=[mathrn1])
  
  chrmr2 = CharmRankModel(
    name='Marathon Charm 2', 
    level=1, 
    rarity=5,
    charm=charm,
    skills=[mathrn2])
  chrmr3 = CharmRankModel(
    name='Marathon Charm 3', 
    level=1, 
    rarity=6,
    charm=charm,
    skills=[mathrn3])

  db.session.add(charm)
  db.session.commit()
 
  #db.session.add(ar3)
  # db.session.add_all([ar, ar1, ar2, ar3, ar4])
  # db.session.commit()
  # ar.skills.append(skr1)
  # ar1.skills.append(skr1)
  # ar1.skills.append(sk1r1)
  # ar2.skills.append(skr1)
  # ar3.skills.append(sk1r1)
  # ar4.skills.append(sk1r1)
  # db.session.commit()

# """create new table"""
# with create_app().app_context():
#   db.create_all()

# alpha = \u03b1 
# beta  = \u03b2