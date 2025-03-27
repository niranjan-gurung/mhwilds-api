from sqlalchemy.orm import Mapped, mapped_column, relationship
from api import db

class SlotModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  level: Mapped[int] = mapped_column(nullable=True)
  armour_id: Mapped[int] = mapped_column(db.ForeignKey('armour_model.id'))
  armour = relationship('ArmourModel', back_populates='slots', foreign_keys=armour_id)

  def __repr__(self):
    return '<Slot level {}>'.format(self.level)