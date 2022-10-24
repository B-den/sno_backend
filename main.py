import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from db.session import engine
from db.session import SessionLocal
from db.base import Base
from db.models.person import Person

engine.connect()

session = SessionLocal()

def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(engine)


#app = FastAPI()

d = Person(id = None, name = 'Mn', nickname = 'mx', email = 'mx@ya.ru', is_active = False)

session.add_all([d])
session.commit()

#if __name__ == "__main__":
#    uvicorn.run(app)        # or cmd: uvicorn main:app --reload