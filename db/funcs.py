from sqlalchemy import create_engine
from db.session import engine
from db.session import SessionLocal
from db.base import Base
from db.models.person import Person
from db.models.password import Password

engine.connect()

session = SessionLocal()


def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(engine)

async def get_users():
    return session.query(Person).all()

async def get_user(email):
    p = session.query(Person).filter(Person.email == email).first()
    if p == None: return None
    return p.pw

async def new_user(data):
    r = await get_user(data["email"])
    if r == None:
        session.add(Person(name = data["username"], email = data["email"], is_active=True))
        session.add(Password(code=data["password"], person_email=data["email"]))
        session.commit()
        return True
    return False