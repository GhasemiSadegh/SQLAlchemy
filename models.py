from sqlalchemy import (Column, ForeignKey, String, Integer, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    id = Column(Integer, ForeignKey=True)


class Addresses(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)


class User(BaseModel):
