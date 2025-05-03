from api import db

"""
Association Table for charm and skill
"""
charm_skill_ranks = \
  db.Table(
    'charm_skill_ranks',
    db.Column('charm_rank_id', db.Integer, db.ForeignKey('charm_rank_model.id'), unique=False),
    db.Column('skill_rank_id', db.Integer, db.ForeignKey('skill_rank_model.id'), unique=False)
  )