from ..database import Base
from ..main import app
from ..models import Todos,Users
from fastapi.testclient import TestClient
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest
from ..routers.auth import bcrypt_context


SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread': False},poolclass= StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base.metadata.create_all(bind=engine)


#testing if fake db works and overriding it so we dont test production one db dependency 
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def override_get_current_user():
    return {'username': 'Shrav','user_id':1, 'user_role': 'A'} #user dependency

client = TestClient(app)

@pytest.fixture
def default_todo():
    todo_model = Todos (
        title = 'drop package off',
        description= 'amazon got it wrong',
        priority=5,
        complete=False,
        owner_id = 1)
    db = TestingSessionLocal()
    db.add(todo_model)
    db.commit()
    yield todo_model
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()
        
@pytest.fixture
def default_user():   
    user_model = Users(
        email = 'shrav@gmail.com',
        username = 'Shrav',
        first_name = 'hannah',
        last_name = 'montana',
        hashed_password = bcrypt_context.hash("hanannamontananna"),
        role = "A",
        phone_number = "287387402"
        )
    db = TestingSessionLocal()
    db.add(user_model)
    db.commit()
    yield user_model
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()
    
    
        