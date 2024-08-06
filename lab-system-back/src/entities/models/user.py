from sqlalchemy import Column, Integer, String, inspect

from src.entities.models.laboratory import Base
from src.config.constants import SCHEMA

class TblUsers(Base):
    __tablename__ = 'tblUsers'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}