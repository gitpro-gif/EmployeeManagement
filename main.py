from fastapi import FastAPI

app = FastAPI()

Employees = []

@app.get("/")
def CheckHeath():
  return{
    "message":"FastApi  app is working"
  }

@app.get("/about")
def AbhayFunction():
  return {
    "message": "I am abhay"
  }

@app.post("/")
def AddEmployee(id: int, name: str, salary: int):
  employee = {
    "id": id,
    "name":  name,
    "salary":  salary
  }

  Employees.append(employee)
  return {
    "message": "Student Added",
    "data": employee
  }
