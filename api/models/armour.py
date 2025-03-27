from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from api import db

from api.models.slot import SlotModel

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