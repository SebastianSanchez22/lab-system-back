from sqlalchemy import Column, Integer, String, inspect, DateTime
from sqlalchemy.orm import relationship, backref

from src.entities.models.laboratory import Base, TblLaboratories
from src.entities.models.user import TblUsers
from src.config.constants import SCHEMA

class TblReservations(Base):
    __tablename__ = 'tblReservations'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    bookingDate = Column(DateTime, nullable=False)
    user = relationship(TblUsers, backref= backref('user_details', cascade='all, delete-orphan'))
    laboratory = relationship(TblLaboratories, backref= backref('laboratory_details', cascade='all, delete-orphan'))

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}