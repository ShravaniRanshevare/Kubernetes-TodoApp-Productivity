from fastapi import APIRouter,Depends,HTTPException,Path,Request
from sqlalchemy.orm import Session
from ..models import Users 
from ..database import SessionLocal
from starlette import status
from typing import Annotated,Optional
from pydantic import BaseModel,Field
from .auth import get_current_user,get_current_user_cookie
from passlib.context import CryptContext


router = APIRouter(
    prefix="/user",
    tags = ['user']
    )

class PasswordRequest(BaseModel):
    old_password: str 
    new_password: str = Field(min_length=5)
    
class PhoneUpdate(BaseModel):
    new_phone_num: str 
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict , Depends(get_current_user)]

@router.get("/profile",status_code=status.HTTP_200_OK)
async def get_profile(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail="not authenticated")
    user_model = db.query(Users).filter(Users.id == user.get('user_id')).first()
    return user_model 

@router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency,db:db_dependency,passwords:PasswordRequest):
    if user is None:
        raise HTTPException(status_code=401,detail="not authenticated")
    user_model = db.query(Users).filter(Users.id == user.get('user_id')).first()
    
    if not bcrypt_context.verify(passwords.old_password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail="error on password changes")
    user_model.hashed_password = bcrypt_context.hash(passwords.new_password)
    db.add(user_model)
    db.commit()
    
@router.put("/phone_number",status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(user:user_dependency,db:db_dependency,phone_num : PhoneUpdate):
    if user is None:
        raise HTTPException(status_code=401,detail="not authenticated")
    user_model = db.query(Users).filter(Users.id == user.get('user_id')).first()
    user_model.phone_number = phone_num.new_phone_num
    db.add(user_model)
    db.commit()

