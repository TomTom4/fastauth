from datetime import timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import create_db_and_tables, engine
from sqlmodel import Session, select
from dependencies import get_current_user
from models import User
from schemas import Token, TokenData
from logic import create_access_token, verify_password, get_password_hash
from jose import JWTError
from configurations import Settings

settings = Settings()
app = FastAPI()

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
async def signin( form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    with Session(engine) as session:
        statement = select(User).where(User.username == form_data.username)
        user = session.exec(statement).first()
        if verify_password(form_data.password,user.password_hash):
            access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
            access_token = create_access_token(data={"sub": user.username},
                                                 expires_delta=access_token_expires)
            return Token(access_token=access_token, token_type="bearer")


@app.delete("/user")
async def delete_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
