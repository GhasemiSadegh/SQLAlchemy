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
    id = Column(Integer, primary_key=True)


class Addresses(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id = Column(ForeignKey("users.id"))

    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')>"


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    age = Column(Integer)
    addresses = relationship(Addresses) # "Addresses" if not in the same file

    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')>"


Base.metadata.create_all(engine)