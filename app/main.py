from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from database import create_db_and_tables, engine
from sqlmodel import Session, select
from models import User
from schemas.token import Token, TokenData
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from configurations import Settings

settings = Settings()
app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key,
                             algorithm=settings.algorithm)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(plain_password):
    return pwd_context.hash(plain_password)

def decode_token(token):
    payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    return TokenData(username=username)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data = decode_token(token)
    except JWTError:
        raise credentials_exception
    with Session(engine) as session:
        statement = select(User).where(User.username == token_data.username)
        user = session.exec(statement).first()
        if not user:
            raise credentials_exception
        return user

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
    print(" current_user needs to be retrevied and deleted") 
    return current_user
