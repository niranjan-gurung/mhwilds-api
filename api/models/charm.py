from sqlalchemy.orm import Mapped, mapped_column, relationship
from api import db

from api.models.charm_ranks import charm_skill_ranks

class CharmModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=True, nullable=False)
  ranks: Mapped[list['CharmRankModel']] = relationship(
    back_populates='charm', 
    order_by="CharmRankModel.id"
  )

  def __repr__(self):
    return f'<Charm name {self.name}>'

class CharmRankModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(nullable=False)
  desc: Mapped[str] = mapped_column(nullable=False)
  level: Mapped[int] = mapped_column(nullable=False)
  rarity: Mapped[int] = mapped_column(nullable=False)

  charm_id: Mapped[int] = mapped_column(
    db.ForeignKey('charm_model.id'), 
    nullable=False
  )

  charm: Mapped['CharmModel'] = relationship(
    back_populates='ranks',
    foreign_keys=charm_id
  )

  skills: Mapped[list['SkillRankModel']] = relationship(
    secondary='charm_skill_ranks',
    back_populates='charms'
  )

  def __repr__(self):
    return '<Charm name {}>, <Charm level {}>'.format(self.name, self.level)