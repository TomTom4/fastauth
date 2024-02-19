from fastapi import FastAPI
from database import create_db_and_tables, engine
from sqlmodel import Session, select
from models import User

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/register")
async def register( user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user 


@app.post("/signin")
async def signin( user: User):
    with Session(engine) as session:
        statement = select(User).where(User.username == user.username,
                                       User.password_hash == user.password_hash)
        user = session.exec(statement).first()
    return user 

@app.delete("/user")
async def delete_user():
    print(" current_user needs to be retrevied and deleted") 
