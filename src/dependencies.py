from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from jose import JWTError
from src.database import engine
from src.models import User
from src.logic import decode_token


async def get_session():
    with Session(engine) as session:
        yield session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(get_session)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data = decode_token(token)
    except JWTError:
        raise credentials_exception
    statement = select(User).where(User.username == token_data.username)
    user = session.exec(statement).first()
    if not user:
        raise credentials_exception
    return user
