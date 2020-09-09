from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import config


engine = create_engine('mssql+pyodbc://{}:{}@{}/{}'.format(config.user, config.password, config.host, config.name))
conn = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


def get_session():
    return session

def get_base():
    return Base