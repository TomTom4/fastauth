from fastapi import FastAPI
from database import create_db_and_tables 

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/register")
async def register( username, password):
    return {"username": username, "password": password}

@app.post("/signin")
async def signin( username, password):
    return {"username": username, "password": password}

@app.delete("/user")
async def delete_user():
    print(" current_user needs to be retrevied and deleted") 
