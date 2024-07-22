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

specific_users = session.query(User).where(
                                            and_(
                                                not_(User.age >= 35),
                                                not_(User.name == 'Smith'))).all()

for user in specific_users:
    print(f"{user.age} and {user.name}")
