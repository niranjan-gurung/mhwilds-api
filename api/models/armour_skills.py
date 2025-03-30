from api import db

"""
Association Table for armour and skill
"""
armour_skills = \
  db.Table(
    'armour_skills',
    db.Column('armour_id', db.Integer, db.ForeignKey('armour_model.id'), unique=False),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill_rank_model.id'), unique=False)
  )