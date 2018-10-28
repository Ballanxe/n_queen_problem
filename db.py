import psycopg2
from sqlalchemy.engine import create_engine



ENGINE = create_engine('postgresql+psycopg2://postgres:123456@172.17.0.3/n_queens_db?port=5432') ### 
CONNECTION = engine.connect()