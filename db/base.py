#from db.base_class import Base
from db.models.person import Person
from db.models.record import Record

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()