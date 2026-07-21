from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name":"john",
        "age":17,
        "year":"year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdatedStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name":"Hello World"}

@app.get("/get-student/{id_student}")
def get_student(id_student: int = Path(description="The ID of the student you want to verify", gt=0, lt=10)):
    return students[id_student]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exist"}
    
    students[student_id] = student.model_dump()
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdatedStudent):
    if student_id not in students:
        return {"Error":"Student doesn't exist"}

    students[student_id].update(student.model_dump(exclude_unset=True))
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student doesn't exist"}
    
    del students[student_id]
    return {"message":"Student deleted succesfully"}