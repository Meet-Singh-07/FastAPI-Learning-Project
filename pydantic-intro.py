from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import List, Dict, Optional
#1. Define Data Model
class Student(BaseModel):
    name: str = Field(max_length = 15, description = "Name of the Student", default = None)
    age: int = Field (gt=0, lt =30, description= "Age of the student must be less than 30 ", strict= True)
    cgpa: float
    email : EmailStr
    hostel: bool
    interest : List[str] 
    contact_details : Optional[Dict[str, str]] 

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        return value

    @field_validator("name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()

    @field_validator("age", mode= "before")
    @classmethod
    def age_validation(cls, value):
        if value >= 100:
            raise ValueError("The age cannot be greater than 100!")
        return value
# student_info = Student("Meet", 21) 
# student_info.model_dump()
    @model_validator(mode= "after")
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 18 and "emergency" not in model.contact_details:
            raise ValueError("Please add emergency contact")
        return model

        
student_info = {
    "name" : "Meet Singh",
    "age": 22,
    "cgpa": 9.01,
    "hostel": False,
    "interest" : ["Movies", "Building"],
    "contact_details" : {
        "email" : "meet.singh@example.com"
    },
    "email" : "meet.singh@example.com"
}

#2. Initaialize Pydantic Object 

std = Student(**student_info) # ** used to unpack the dict and we can use the field of the dict now 

def insert_student(student: Student):
    print(student)
   

#3. Passing to the function 

insert_student(std)