from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5050/pp"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)