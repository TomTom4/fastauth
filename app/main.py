from fastapi import FastAPI
from database import create_db_and_tables
from models import User

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/register")
async def register( user: User):
    return {"username": user.username, "password": user.password_hash}

@app.post("/signin")
async def signin( user: User):
    return {"username": user.username, "password": user.password_hash}

@app.delete("/user")
async def delete_user():
    print(" current_user needs to be retrevied and deleted") 
