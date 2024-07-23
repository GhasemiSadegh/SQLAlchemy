from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db_url = 'sqlite:///mydata.sqlite'
engine = create_engine(db_url)


class User(Base):
    __tablename__ = 'mytable'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)
