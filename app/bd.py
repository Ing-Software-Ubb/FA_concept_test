from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER ='root'
POSTGRES_PASSWORD = 'root'
POSTGRES_DB = 'test_db'
PORT = '5432'
SERVER = '172.20.0.3'

SQLALCHEMY_DATABASE_URL = 'postgres://'+POSTGRES_USER+':'+POSTGRES_PASSWORD+'@'+SERVER+':'+PORT+'/'+POSTGRES_DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()