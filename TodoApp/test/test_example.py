import pytest

class Student:
    def __init__(self,first_name:str,last_name:str,major:str,years:int):
        self.first_name=first_name
        self.last_name= last_name
        self.major = major
        self.years = years
        
@pytest.fixture #import cz of this 
def default_student():
    return Student('Joe','Doe','Computer Science',3)

def test_instantiation(default_student): #looks for a pytest fixture named this
    assert default_student.first_name == 'Joe','first name shud be Joe'
    assert default_student.last_name == 'Doe','last name shud be Joe'
    assert default_student.major == 'Computer Science'
    assert default_student.years == 3
        
    