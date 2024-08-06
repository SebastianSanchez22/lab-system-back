from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import declarative_base

from src.config.constants import SCHEMA

Base = declarative_base()
metadata = Base.metadata

class TblLaboratories(Base):
    __tablename__ = 'tblLaboratories'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    schedule = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}