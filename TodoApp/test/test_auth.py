from .utils import *
from fastapi import status,HTTPException
from ..routers.auth import get_db,bcrypt_context,authenticate_user,create_access_token,SECRET_KEY,ALGORITHM,get_current_user
from ..models import Users
from datetime import timedelta,datetime,timezone
from jose import jwt



app.dependency_overrides[get_db] = override_get_db
   



def test_authenticate_user(default_user): #checks if user is in db ie identified
    db = TestingSessionLocal()
    response = authenticate_user('Shrav','hanannamontananna',db)
    assert response is not None
    m =  response
    assert m.username == 'Shrav' #also try non existent and do assert response is False
    response = authenticate_user('Shrav','nananananana',db)
    assert response is  False
    response = authenticate_user('Shriya','nananananana',db)
    assert response is False
    
def test_create_access_token(default_user): #making sure token process doesnt change things
    token = create_access_token('Shrav',1,'A',timedelta(days=1))
    decoded = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM],options={'verify_signature':False})
    assert decoded.get('sub') == 'Shrav'
    assert decoded.get('id') == 1
    assert decoded.get('role') == 'A'

@pytest.mark.asyncio
async def test_get_current_user(default_user): #pytest cant do async testing for unit tests need to install pytest asyncio 
    encode = {'sub':'Shrav','id':1,'role':'A'}
    token = jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)
    response = await get_current_user(token=token) #async function hai hence
    
    assert response['username']=='Shrav'
    assert response['user_id']== 1
    assert response['user_role']=='A'

@pytest.mark.asyncio
async def test_missing_payload():
    #does it mean the token when decoded is missing one or more values
    encode = {'role':'user'}
    token = jwt.encode(encode,SECRET_KEY,algorithm = ALGORITHM)
    with pytest.raises(HTTPException) as excinfo: #if while were testing an exception is raised during this applicataion bcz of async maybe 
        await get_current_user(token=token)
    assert excinfo.value.status_code == 401 #go ahead and assert this 
    assert excinfo.value.detail == "could not validate credentials"
    
    
    