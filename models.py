from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
db_url = 'sqlite:///db.sqlite'
engine = create_engine(db_url)


class User(Base):
    __tablename__ = 'mytable'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='Ali', age=25)
user2 = User(name='Kazem', age=34)
user3 = User(name='Jalil', age=34)
user4 = User(name='Shakib', age=40)

session.add(user1)
session.commit()
session.close()
