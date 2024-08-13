from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # يسمح بالوصول من إي مصدر
    allow_credentials= True,
    allow_nethods=["*"],
    allow_headers=["*"]
)

class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="Moahmmed", grade=5),
    Student(id=2, name="Khaled", grade=4),
]

@app.get("/studentsAPI/")
def view():
    return students

@app.post("/studentsAPI/")
def create_student(New_student: Student):
    students.append(New_student)
    return New_student

@app.put("/studentsAPI/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "لايوجد طالب بهذا الرقم"}

@app.delete("/studentsAPI/{student_id}")
def remove_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"mwssage": "تم حذف الطالب بنجاح!"}
    return {"error": "لايوجد طالب بهذا الرقم"}
