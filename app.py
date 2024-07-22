from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import or_, and_, not_
# import random

Session = sessionmaker(bind=engine)

session = Session()

# names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson",
#          "Taylor", "Anderson"]
#
# ages = [25, 30, 35, 22, 28, 40, 45, 50, 27, 33]
#
# for i in range(5):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)
#
# session.commit()

users = session.query(User.age).all()
for user in users:
    print(user.age)