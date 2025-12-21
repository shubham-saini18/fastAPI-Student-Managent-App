from fastapi import FastAPI
import json

app = FastAPI()

def load_students():
    with open('students.json',"r") as f:
        students_data = json.load(f)
    return students_data

@app.get("/")
def home():
    return {'message': 'This is my Student Management System'}

@app.get("/about")
def home():
    return {'Author': 'Shubham Saini'}

@app.get("/students")
def view():
    students_data = load_students()
    return students_data

@app.get('/student/{student_id}')
def view_student(student_id: str):
    students_data = load_students()
    if student_id in students_data:
        return students_data[student_id]
    return {'error': 'Student not found'}