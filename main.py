from sqlalchemy import create_engine

db_url = "sqlite:///mydata.db"
engine = create_engine(db_url)
