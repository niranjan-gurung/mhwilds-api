from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from api import db

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

"""
  Models
"""
class ArmourModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=False, nullable=False)
  slug: Mapped[str] = mapped_column(unique=False, nullable=False)
  type: Mapped[str] = mapped_column(unique=False, nullable=False)
  rank: Mapped[str] = mapped_column(unique=False, nullable=False)
  rarity: Mapped[int] = mapped_column(unique=False, nullable=False)
  slots: Mapped[Optional[list['SlotModel']]] = relationship(cascade='all, delete-orphan', 
                                                            back_populates='armour')
  
  """TODO:"""
  #skills: Mapped[list['SkillModel']] = relationship(back_populates='armour')

  def __repr__(self):
    return '<Armour piece {}>'.format(self.name)
  

class SlotModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  level: Mapped[int] = mapped_column(nullable=True)
  armour_id: Mapped[int] = mapped_column(db.ForeignKey('armour_model.id'))
  armour: Mapped['ArmourModel'] = relationship(back_populates='slots', 
                                               foreign_keys=armour_id)

  def __repr__(self):
    return '<Slot level {}>'.format(self.level)
  
class SkillModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=True, nullable=False)
  type: Mapped[str] = mapped_column(nullable=False)   # armour / weapon
  desc: Mapped[str] = mapped_column(nullable=False)
  ranks: Mapped[list['SkillRankModel']] = relationship('SkillRankModel', 
                                                        back_populates='skill')
  
  # armour_id: Mapped[int] = mapped_column(db.ForeignKey('armour_model.id'))
  # armour: Mapped['ArmourModel'] = relationship(back_populates='skills', 
  #                                              foreign_keys=armour_id)

  def __repr__(self):
    return '{}-{}-{}-{}-{}' \
      .format(self.id, self.name, self.type, self.desc, self.ranks)
  
class SkillRankModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  level: Mapped[int] = mapped_column(nullable=False)  # skill level
  desc: Mapped[str] = mapped_column(nullable=False)

  skill_id: Mapped[int] = mapped_column(db.ForeignKey('skill_model.id'))
  skill: Mapped['SkillModel'] = relationship(back_populates='ranks', 
                                             foreign_keys=skill_id)
  
  def __repr__(self):
    return '{}-{}-{}'.format(self.id, self.level, self.desc)