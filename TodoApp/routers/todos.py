from fastapi import APIRouter,Depends,HTTPException,Path,Request
from sqlalchemy.orm import Session
from ..models import Todos 
from ..database import SessionLocal
from starlette import status
from typing import Annotated,Optional
from pydantic import BaseModel,Field
from .auth import get_current_user,get_current_user_cookie

router = APIRouter(
    prefix = '/todos',
    tags = ['todos']
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict , Depends(get_current_user)]

class TodoRequest(BaseModel):
    title : str = Field(min_length=3)
    description : str = Field(min_length=3,max_length=100)
    priority : int = Field(gt=0,lt=6)
    complete : bool
      



@router.get("/",status_code=status.HTTP_200_OK)
async def get_todos(db : db_dependency,user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail="user not authenticated")
    return db.query(Todos).filter(Todos.owner_id == user.get('user_id')).all() #passing in the model that we want format and getting all records

@router.get("/{todo_id}",status_code=status.HTTP_200_OK)
async def get_todo_id(user: user_dependency, db: db_dependency,todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail="user not authenticated")
    todo_model = db.query(Todos).filter(Todos.owner_id == user.get('user_id')).filter(Todos.id == todo_id).first() #so ids r unique so only one rec so return that instead of searching eveyrthing
    if todo_model is not None:
        return todo_model
    else:
        raise HTTPException(status_code=404,detail='todo item not found')
    
@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_todo(user : user_dependency , db:db_dependency,todo_req:TodoRequest):
    if user is None:
        raise HTTPException(status_code=401,detail="user not authenticated")
    todo_model= Todos(
        **todo_req.dict(),
        owner_id = user.get('user_id')
        )
    db.add(todo_model)
    db.commit()
    
@router.put("/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user : user_dependency , db: db_dependency ,todo_req:TodoRequest , todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail="user not authenticated")
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('user_id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail="Todo item not found")
   
    todo_model.title = todo_req.title
    todo_model.description = todo_req.description
    todo_model.priority = todo_req.priority
    todo_model.complete = todo_req.complete
    db.add(todo_model)
    db.commit()
     
@router.delete("/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user : user_dependency, db:db_dependency,todo_id:int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail="user not authenticated")
    todo_model = db.query(Todos).filter(Todos.id==todo_id).filter(Todos.owner_id == user.get('user_id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail="Todo item not found")
    db.query(Todos).filter(Todos.id==todo_id).filter(Todos.owner_id == user.get('user_id')).delete()
    db.commit()
 
###page renders todos_pages.py


