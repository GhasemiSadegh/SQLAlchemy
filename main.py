from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db_url = "sqlite:///mydata.db"
engine = create_engine(db_url)
Base.metadata.create_all(engine)
