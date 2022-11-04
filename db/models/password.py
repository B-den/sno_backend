from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Password(Base):
	__tablename__ = "passwords"

	id = Column(Integer(), primary_key=True, index=True)
	code = Column(String, nullable=False)
	person_email = Column(String(), ForeignKey('people.email'))