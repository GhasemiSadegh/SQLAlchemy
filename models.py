from sqlalchemy import Column, String, Integer, create_engine, not_, and_, or_
from sqlalchemy.orm import declarative_base, sessionmaker

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
session.commit()

# user1 = User(name='Ali', age=25)
# user2 = User(name='Kazem', age=34)
# user3 = User(name='Jalil', age=34)
# user4 = User(name='Shakib', age=40)
#
# session.add_all([user1, user2, user3, user4])
# session.commit()

users = session.query(User).where(and_(User.age >= 34, User.name == "Jalil", User.id > 4)).all()

for user in users:
    print(user.name, user.age)
