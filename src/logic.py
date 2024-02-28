from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
from fastapi import HTTPException, status
from src.configurations import Settings
from src.schemas import TokenData

settings: Settings = Settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_pem(pem_filepath: str):
    with open(pem_filepath, "r") as filestream:
        return filestream.read()


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    private_key = get_pem(settings.private_key)
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, private_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(plain_password):
    return pwd_context.hash(plain_password)


def decode_token(token):
    public_key = get_pem(settings.public_key)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = jwt.decode(token, public_key, algorithms=[settings.algorithm])
    username: str = payload.get("sub") or ""
    if username == "":
        raise credentials_exception
    return TokenData(username=username)
