from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user = User(name='Sadegh', age=30)

session.add(user)

session.commit()
