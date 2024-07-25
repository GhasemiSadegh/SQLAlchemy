from models import User, Addresses, session

# creating users

user1 = User(name="John Doe", age=52)
user2 = User(name="Jane Smith", age=34)

# creating addresses
address1 = Addresses(city="New York", state="NY", zip_code=10001)
address2 = Addresses(city="Los Angles", state="CA", zip_code=90001)
address3 = Addresses(city="Chicago", state="IL", zip_code=60601)

# associating addresses with the users
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)

session.commit()

print(f"{user1.addresses = }")