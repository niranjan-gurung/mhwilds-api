from sqlalchemy.orm import Mapped, mapped_column, relationship
from api import db

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
    return '<Skill {}>, <Skill ranks {}>'.format(self.name, self.ranks)
  
class SkillRankModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  level: Mapped[int] = mapped_column(nullable=False)  # skill level
  desc: Mapped[str] = mapped_column(nullable=False)

  skill_id: Mapped[int] = mapped_column(db.ForeignKey('skill_model.id'))
  skill: Mapped['SkillModel'] = relationship(back_populates='ranks', 
                                             foreign_keys=skill_id)
  
  def __repr__(self):
    return '<Skill level {}>'.format(self.level)