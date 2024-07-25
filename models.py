from sqlalchemy import (Column, ForeignKey, String, Integer, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


