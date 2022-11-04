from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Person(Base):
	__tablename__ = "people"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False)
	nickname = Column(String, nullable=True)
	email = Column(String,nullable=False,unique=True,index=True)
	is_active = Column(Boolean(),default=True)
	pw = relationship('Password', backref='Person', uselist=False)