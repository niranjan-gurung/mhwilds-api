from api import db

"""
Association Table for decoration and skill
"""
deco_skill_ranks = \
  db.Table(
    'deco_skill_ranks',
    db.Column('decoration_id', db.Integer, db.ForeignKey('decoration_model.id'), unique=False),
    db.Column('skill_rank_id', db.Integer, db.ForeignKey('skill_rank_model.id'), unique=False)
  )