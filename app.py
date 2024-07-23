from models import User
from sqlalchemy.orm import sessionmaker
from models import engine
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='Ali', age=25)
session.add(user1)
session.commit()
session.close()
