from fastapi import FastAPI
from database import create_db_and_tables, engine
from sqlmodel import Session, select
from models import User
from passlib.context import CryptContext

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    return pwd_context.hash(plain_password)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/register")
async def register( user: User):
    hashed_password = get_password_hash(user.password_hash)
    user.password_hash = hashed_password
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


@app.post("/signin")
async def signin( user: User):
    with Session(engine) as session:
        statement = select(User).where(User.username == user.username)
        db_user = session.exec(statement).first()
        if verify_password(user.password_hash, db_user.password_hash):
            return user

@app.delete("/user")
async def delete_user():
    print(" current_user needs to be retrevied and deleted") 
