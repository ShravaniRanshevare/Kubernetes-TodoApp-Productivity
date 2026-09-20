from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

driver = os.getenv("POSTGRES_driver")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
name = os.getenv("POSTGRES_NAME")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")


sqlalchemy_url = f"{driver}://{user}:{password}@{host}:{port}/{name}"
#'postgresql://neondb_owner:npg_rfENWgjuG5x9@ep-ancient-breeze-za7mlkx8-pooler.c-2.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
#"mysql+pymysql://root:Shravani123!@127.0.0.1:3306/TodoApplicationDatabase"
#sqlite to create our db in this directory named todos.db
#"sqlite:///./todo.db"
#"postgresql+psycopg2://postgres:test1234!@postgres:5432/TodoApplicationDatabase"
                                                    #'postgresql://postgres:test1234!@localhost/TodoApplicationDatabase' - postgres

#engine = open the connection to use db
engine = create_engine(sqlalchemy_url,pool_pre_ping=True,
    pool_recycle=300) #to prevent race conditions for the connectargs check same htread false - for sqlite only

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)#create a database session to operate 

Base = declarative_base() #a db object to interact 
