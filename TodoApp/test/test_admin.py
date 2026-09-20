from fastapi import status
from ..routers.admin import get_db,get_current_user
from ..models import Todos
from .utils import *


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user
    


def test_get_todos_admin(default_todo):
    response = client.get("/admin/todos")
    assert response.status_code == 200
    todo = response.json()[0]
    assert todo['title'] == 'drop package off'
    assert todo['description'] == 'amazon got it wrong'
    assert todo['priority'] == 5
    assert todo['complete'] is False
    assert todo['owner_id'] == 1
    




def test_delete_todo(default_todo):
    response = client.delete('/admin/todos/1') #remember prefix !!!!!
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None
    
def test_delete_todo_not_found(default_todo):
    response = client.delete("/admin/todos/999")
    assert response.status_code == 404
    assert response.json() == {'detail':'todo not found'}
    
    