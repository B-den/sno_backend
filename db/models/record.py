from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Record(Base):
	__tablename__ = "records"
	id = Column(Integer, primary_key=True, index=True)
