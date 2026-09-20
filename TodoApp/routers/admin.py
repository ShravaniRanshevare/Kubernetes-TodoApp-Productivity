from fastapi import APIRouter,Depends,HTTPException,Path
from sqlalchemy.orm import Session
from ..models import Todos,Users 
from ..database import SessionLocal
from starlette import status
from typing import Annotated,Optional
from pydantic import BaseModel,Field
from .auth import get_current_user

router = APIRouter(
    prefix = '/admin',
    tags = ['admin']
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]

@router.get("/users",status_code=status.HTTP_200_OK)
async def get_users(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != "A" :
        raise HTTPException(status_code=401,detail="user not authenticated")
    
    return db.query(Users).all()
        
@router.get("/todos",status_code=status.HTTP_200_OK)
async def get_todos(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != "A":
        raise HTTPException(status_code=401,detail="authentication failed")
    return db.query(Todos).all()

@router.delete("/todos/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency,todo_id:int = Path(gt=0)):
    if user is None or user.get('user_role') != "A":
        raise HTTPException(status_code=401,detail="authentication failed")
    todo = db.query(Todos).filter(Todos.id==todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404,detail="todo not found")
    db.query(Todos).filter(Todos.id==todo_id).delete()
    db.commit()


