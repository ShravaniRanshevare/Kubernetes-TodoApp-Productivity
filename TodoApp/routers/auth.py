from fastapi import APIRouter,Depends,HTTPException,Request
from pydantic import BaseModel,Field
from ..models import Users
from passlib.context import CryptContext
from ..database import SessionLocal
from typing import Annotated,Optional
from sqlalchemy.orm import Session
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError #needs secret and algo
from datetime import timedelta,datetime,timezone
import os

#authentication of details ,creating,verification of token done by functions 

router = APIRouter(
    prefix = '/auth',
    tags=['auth']
    
    )

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = 'HS256'



bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer= OAuth2PasswordBearer(tokenUrl='auth/token') #contains url  that the client wll send to our fast api

class UserRequest(BaseModel): 
    email : str = Field(min_length=3)
    username: str = Field(min_length=3,max_length = 10)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    password: str = Field(min_length=5)
    role: str
    phone_number: str
    

    
class Token(BaseModel): #role will also be part maybe ? - for admin and not admin
    access_token: str
    token_type : str





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]


def authenticate_user(username: str ,password: str , db):
    user_exists_model = db.query(Users).filter(Users.username==username).first()
    if user_exists_model is None:
        return False
    if not bcrypt_context.verify(password,user_exists_model.hashed_password):
        return False
    return user_exists_model

def create_access_token(username:str,user_id:int, role : str, expires_delta:timedelta):
    encode = {'sub':username,'id':user_id, 'role': role}
    expire = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expire})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]): #takes token which depends on auth2bearer which gets token
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
        username:str = payload.get('sub')
        userid:int=payload.get('id')
        role : str = payload.get('role')
        if username is None or userid is None or role is None:
            raise HTTPException(status_code =401 , detail='could not validate credentials')
        return {'username':username,'user_id':userid, 'user_role': role}
    except JWTError:
        raise HTTPException(status_code =401 , detail='could not validate user')
        
async def get_current_user_cookie(token:str):
    if not token:
        return None
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
        username:str = payload.get('sub')
        userid:int=payload.get('id')
        role : str = payload.get('role')
        if username is None or userid is None or role is None:
            return None
        return {'username':username,'user_id':userid, 'user_role': role}
    except JWTError:
        return None

    
@router.post("/register",status_code = status.HTTP_201_CREATED) #registrtion ? 
async def create_user(db: db_dependency, user_req: UserRequest):
    #since diff column names hashed and password trick wont work so have to type out 
    user_model = Users(
        email = user_req.email,
        username = user_req.username,
        first_name = user_req.first_name,
        last_name = user_req.last_name,
        hashed_password = bcrypt_context.hash(user_req.password[:72]),
        role = user_req.role,
        is_active = True,
        phone_number = user_req.phone_number
        )
    db.add(user_model)
    db.commit()
    
@router.post("/token",response_model=Token) #request form tons of variables sp form_data.password etc 
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm,Depends()], db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code =401 , detail='could not validate credentials')
    token = create_access_token(user.username,user.id, user.role, timedelta(minutes=20))
    return {'access_token':token,'token_type':'bearer'}


    
    
    
    
    