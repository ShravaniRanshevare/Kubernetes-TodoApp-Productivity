from fastapi import FastAPI,Request
from .models import Base
from .database import engine
from .routers import auth,todos,admin,users
from starlette import status
from fastapi.middleware.cors import CORSMiddleware


# we want to create todos table in DB 
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

@app.get("/health",status_code=status.HTTP_200_OK)
def get_health():
    return {"message":"healthy app"}






     

    
    
    
    

    
    
    
    

    
    
