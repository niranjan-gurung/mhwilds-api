from sqlalchemy.orm import Mapped, mapped_column, relationship
from api import db

class DecorationModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=True, nullable=False)
  desc: Mapped[str] = mapped_column(nullable=False)
  type: Mapped[str] = mapped_column(unique=False, nullable=False)
  rarity: Mapped[int] = mapped_column(nullable=False)
  slot: Mapped[int] = mapped_column(nullable=False)

  skills: Mapped[list['SkillRankModel']] = relationship(
    secondary='deco_skill_ranks',
    back_populates='decorations'
  )

  def __repr__(self):
    return f'<Decoration name {self.name}>'