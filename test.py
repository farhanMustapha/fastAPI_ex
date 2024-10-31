from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    id:int
    name:str
    grade:int


students=[
    Student(id=1,name="karim alami",grade=3),
    Student(id=2,name="mustapha farhan alami",grade=5),
    Student(id=3,name="khadija mourabi",grade=1),
    Student(id=4,name="mohamed abali",grade=0)
]

@app.get("/students/")
def read_students():
    return students


@app.post("/students/")
def creat_students(New_student:Student):
    students.append(New_student)
    return New_student