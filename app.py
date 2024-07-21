from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user = User(name='Sadegh', age=30)
user1 = User(name='Reza', age=40)
user2 = User(name='Ali', age=15)
session.add(user)


session.add_all([user1, user2])
session.commit()

# to print users
users = session.query(User).all()
print(users)

# accessing user's parameters

user = users[0]
print(user.id,
      user.name,
      user.age)
