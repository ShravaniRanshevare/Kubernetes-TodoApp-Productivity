from fastapi import status
from ..routers.todos import get_db,get_current_user
from ..models import Todos
from .utils import *

        

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user
    


#uk db is empty so no todos r expected 
def test_read_all_authenticated(default_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK #so after this we made a test for create one which already ran did not delete now this test goes bonkers cz there r 

    todo = response.json()[0]
    assert todo['title'] == 'drop package off'
    assert todo['description'] == 'amazon got it wrong'
    assert todo['priority'] == 5
    assert todo['complete'] is False
    assert todo['owner_id'] == 1
    

def test_get_todo_id(default_todo):
    response = client.get("/todos/1")
    assert response.status_code == status.HTTP_200_OK
    todo = response.json()
    assert todo['title'] == 'drop package off'
    assert todo['description'] == 'amazon got it wrong'
    assert todo['priority'] == 5
    assert todo['complete'] is False
    assert todo['owner_id'] == 1
    
def test_get_todo_id_wrong_ver():
    response = client.get("/todos/2")
    assert response.status_code == 404
    assert response.json() == {'detail':'todo item not found'}
    
    
def test_create_todo(default_todo): #added it nontheless just to see if new gets created or not?
    request_data = {
        'title':'New Todo!',
        'description':'testing',
        'priority':3,
        'complete':False} #the model tht we use just have these fields
    response = client.post("/todos/create/",json=request_data)
        
    assert response.status_code == 201
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data['title']
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')
    
def test_update_todo(default_todo): #id is 1 for this
    request_data = {'title' : 'drop package off',
        'description': 'amazon got it wrong',
        'priority':5,
        'complete':True}
    response = client.put("/todos/1/",json = request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.complete == True
    
def test_update_todo_not_found(default_todo): #id is 1 for this
    request_data = {'title' : 'drop package off',
        'description': 'amazon got it wrong',
        'priority':5,
        'complete':True}
    response = client.put("/todos/3/",json = request_data)
    assert response.status_code == 404
    assert response.json() == {'detail':'Todo item not found'}
    
def test_delete_todo(default_todo):
    response = client.delete("/todos/1")
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None
    
def test_delete_todo_not_found(default_todo):
    response = client.delete("/todos/999")
    assert response.status_code == 404
    assert response.json() == {'detail':'Todo item not found'}
    
     

    