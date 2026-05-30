from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def CheckHeath():
  return{
    "message":"FastApi  app is working"
  }