from sqlalchemy.orm import sessionmaker
from models import User, engine
import random

Session = sessionmaker(bind=engine)

session = Session()
#
# user0 = User(name='Sadegh', age=30)
# user1 = User(name='Reza', age=40)
# user2 = User(name='Ali', age=15)
# session.add(user0)
#
# session.add_all([user1, user2])
# session.commit()
#
# # to print users
# users = session.query(User).all()
# print(users)
#
# # accessing user's given data
# user = users[0]
# print(user.id,
#       user.name,
#       user.age)
#
# # printing all given data
# for user in users:
#     print(f"user id: {user.id}, user name: {user.name}, user age: {user.age}")
#
# # to filter and access
# to_filter = session.query(User).filter_by(age=30).all()
# print(to_filter)
# to_get_first = session.query(User).filter_by(age=30).first()
# print(to_get_first)
#
# # to filter with one or none
# one_none_filter = session.query(User).filter_by(id=1).one_or_none()
# print(one_none_filter)
#
# # to update a cell
# user0.name = 'Not Sadegh Anymore'
# print(user.name)
# session.commit()
#
# # to delete a user
# session.delete(user0)
# session.commit()

names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson",
         "Taylor", "Anderson"]

ages = [25, 30, 35, 22, 28, 40, 45, 50, 27, 33]

for i in range(5):
    user = User(name=random.choice(names), age=random.choice(ages))
    session.add(user)

session.commit()
# # query all users ordered by age (ascending)
# users = session.query(User).order_by(User.age).all()
# for user in users:
#     print(f"user id: {user.id}, user name: {user.name}, user age: {user.age}")
# print('next command')
#
# # the same (descending)
# users = session.query(User).order_by(User.age.desc()).all()
# for user in users:
#     print(f"user id: {user.id}, user name: {user.name}, user age: {user.age}")
# print('next command')
#
# # the same but ordering with name and age at the same time
# users = session.query(User).order_by(User.age, User.name).all()
# for user in users:
#     print(f"user id: {user.id}, user name: {user.name}, user age: {user.age}")
#
# session.commit()

users = session.query(User).filter_by(age=33).all()
other_users = session.query(User).where(User.age >= 35).all()
for user in users:
    print(f'user {user.name} age is 33 >> {user.age}')

for user in other_users:
    print(f'user {user.name} is over 35 >> {user.age}')

