from sqlalchemy.orm import sessionmaker
from models import engine, User

Session = sessionmaker(bind=engine)
session = Session()

session.commit()

user = User(name='Ali', age=100)
session.add(user)
print(f'name is {user.name} and age is {user.age}')



