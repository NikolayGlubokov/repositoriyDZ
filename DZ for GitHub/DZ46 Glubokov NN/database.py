from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_name = 'blacklist.db'

engine = create_engine(f'sqlite:///{database_name}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)