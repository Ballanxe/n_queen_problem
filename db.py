import psycopg2
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database is in a Docker container
engine = create_engine('postgresql+psycopg2://postgres:123456@172.17.0.3/n_queens_db?port=5432')

Session = sessionmaker(bind=engine)

Base = declarative_base()
