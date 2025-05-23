from sqlalchemy.orm import Mapped, mapped_column, relationship
from api import db

from api.models.charm import CharmRankModel 
from api.models.decoration import DecorationModel 
from api.models.charm_skill_ranks import charm_skill_ranks 
from api.models.deco_skill_ranks import deco_skill_ranks 

class SkillModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=True, nullable=False)
  type: Mapped[str] = mapped_column(nullable=False)   # armour / weapon
  desc: Mapped[str] = mapped_column(nullable=False)
  ranks: Mapped[list['SkillRankModel']] = relationship(
    'SkillRankModel',
    back_populates='skill', 
    order_by="SkillRankModel.id"
  )

  def __repr__(self):
    return '<Skill {}>, <Skill ranks {}>'.format(self.name, self.ranks)


class SkillRankModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  level: Mapped[int] = mapped_column(nullable=False)  # skill level
  desc: Mapped[str] = mapped_column(nullable=False)

  skill_id: Mapped[int] = mapped_column(
    db.ForeignKey('skill_model.id'), 
    nullable=False
  )
  
  skill: Mapped['SkillModel'] = relationship(
    back_populates='ranks', 
    foreign_keys=skill_id
  )

  armour: Mapped[list['ArmourModel']] = relationship(
    secondary='armour_skills', 
    back_populates='skills'
  )

  charms: Mapped[list['CharmRankModel']] = relationship(
    secondary='charm_skill_ranks',
    back_populates='skills'
  )

  decorations: Mapped[list['DecorationModel']] = relationship(
    secondary='deco_skill_ranks',
    back_populates='skills'
  )

  def __repr__(self):
    return '<Skill level {}>'.format(self.level)