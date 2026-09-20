from fastapi import status
from .utils import *
from ..routers.users import get_db,get_current_user

#big error in this and bit in admins url ka users/admin hi wrong likha tha and change num mai key hi wrong thi
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_get_profile(default_user):
    response = client.get('/user/profile')
    assert response.status_code == 200
    #assert response.json() is None #basically the profile doesnt exist in test db but since it passes exceptions of endpoint returns 200 but response is NOne as no profile
    #so if u want proper do it my WAY
    m = response.json()
    assert m['email'] == 'shrav@gmail.com'
    assert m['username'] == 'Shrav'
    assert m['first_name'] == 'hannah'
    assert m['last_name'] == 'montana'
    assert bcrypt_context.verify("hanannamontananna", m['hashed_password'])
    assert m['role'] == "A"
    assert m['phone_number'] == "287387402"
    
    
def test_change_password(default_user):
    request_data={
        'old_password' :'hanannamontananna',
        'new_password': 'shriyarocksaintnolie'
    }
    response = client.put('/user/password/',json = request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert bcrypt_context.verify('shriyarocksaintnolie',model.hashed_password)
    
def test_change_password_wrong_oldpass(default_user):
    request_data={
        'old_password':'bahahahahah',
        'new_password': 'shriyarocksaintnolie'
    }
    response = client.put('/user/password/',json = request_data)
    assert response.status_code == 401
    assert response.json() == {'detail':'error on password changes'}
    
    
def test_change_phone_number(default_user):
    request_data={
        'new_phone_num': '9869225748'
    }
    response = client.put('/user/phone_number/',json = request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert model.phone_number == '9869225748'
    

    
