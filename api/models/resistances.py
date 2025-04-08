from sqlalchemy.orm import Mapped, mapped_column, relationship
from api import db

class ResistancesModel(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  fire: Mapped[int] = mapped_column(unique=False, nullable=False)
  water: Mapped[int] = mapped_column(unique=False, nullable=False)
  ice: Mapped[int] = mapped_column(unique=False, nullable=False)
  thunder: Mapped[int] = mapped_column(unique=False, nullable=False)
  dragon: Mapped[int] = mapped_column(unique=False, nullable=False)
  
  armour_id: Mapped[int] = mapped_column(db.ForeignKey('armour_model.id'), 
                                         nullable=False)
  armour = relationship(
    'ArmourModel', 
    back_populates='resistances', 
    foreign_keys=armour_id
  )

  def __repr__(self):
    return '<Resistances: {}, {}, {}, {}, {}>' \
      .format(self.fire, self.water, self.ice, self.thunder, self.dragon)