from enum import Enum
from typing import Literal

from pydantic import BaseModel, field_validator, model_validator

class Gender(str,Enum):
    male = "male"
    female = "female"


class Adderess(BaseModel): 
    city : str 
    pin : int 


class Student(BaseModel):
    name : str
    age : int 
    gender : Gender #Literal["male", "female"]
    address : Adderess

student_address = {
    "city": "Uttar Pradesh",
    "pin": 2021220
}

student_info = { "name": "Meet", "age": 21, "gender" : "male","address": student_address}

address = Adderess(**student_address)

student = Student(**student_info)

print(student)
print(type(student.gender))

# temp = student.model_dump()
# print(temp)
# print(type(temp))
# print(student)

