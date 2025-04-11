from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from api import db

from api.models.skill import SkillRankModel
from api.models.slot import SlotModel
from api.models.resistances import ResistancesModel
from api.models.armour_skills import armour_skills 

class ArmourModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=False, nullable=False)
  slug: Mapped[str] = mapped_column(unique=False, nullable=False)
  type: Mapped[str] = mapped_column(unique=False, nullable=False)
  rank: Mapped[str] = mapped_column(unique=False, nullable=False)
  rarity: Mapped[int] = mapped_column(unique=False, nullable=False)
  defense: Mapped[int] = mapped_column(unique=False, nullable=False)

  resistances: Mapped['ResistancesModel'] = relationship(
    cascade='all, delete-orphan',
    back_populates='armour'
  )

  slots: Mapped[Optional[list['SlotModel']]] = relationship(
    cascade='all, delete-orphan', 
    back_populates='armour'
  )

  skills: Mapped[Optional[list['SkillRankModel']]] = relationship(
    secondary=armour_skills, 
    back_populates='armour'
  )

  def __repr__(self):
    return '<Armour piece {}>'.format(self.name)