from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.logic import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")


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
