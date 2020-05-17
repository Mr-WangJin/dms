
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()

def db_connect():
	engine = sa.create_engine(BASE_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()
