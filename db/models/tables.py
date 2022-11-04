from sqlalchemy import MetaData, Table, Integer, String, Column, Text, DateTime, Boolean
from sqlalchemy.orm import mapper
from datetime import datetime

metadata = MetaData()

people = Table('people', metadata,
	Column('id',Integer(), primary_key=True, index=True),
	Column('name',String(), nullable=False),
	Column('nickname',String(), nullable=True),
	Column('email',String(),nullable=False,unique=True,index=True),
	Column('is_active',Boolean(),default=True)
	)

class People(object):
	pass
mapper(People, people)