from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user0 = User(name='Sadegh', age=30)
user1 = User(name='Reza', age=40)
user2 = User(name='Ali', age=15)
session.add(user0)

session.add_all([user1, user2])
session.commit()

# to print users
users = session.query(User).all()
print(users)

# accessing user's given data
user = users[0]
print(user.id,
      user.name,
      user.age)

# printing all given data
for user in users:
    print(f"user id: {user.id}, user name: {user.name}, user age: {user.age}")

# to filter and access
to_filter = session.query(User).filter_by(age=30).all()
print(to_filter)
to_get_first = session.query(User).filter_by(age=30).first()
print(to_get_first)

# to filter with one or none
one_none_filter = session.query(User).filter_by(id=1).one_or_none()
print(one_none_filter)

# to update a cell
user0.name = 'Not Sadegh Anymore'
print(user.name)
session.commit()

# to delete a user
session.delete(user0)
session.commit()