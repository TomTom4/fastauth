from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from src.database import create_db_and_tables
from src.dependencies import get_session, get_current_user
from src.models import User, InUser, OutUser
from src.schemas import Token
from src.logic import create_access_token, verify_password, get_password_hash
from src.configurations import Settings
from src.jwks import JWKS, build_jwks

settings: Settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

origins = ['http://localhost']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/.well-known/jwks.json")
async def get_jwks():
    jwks: JWKS = build_jwks()
    return jwks.model_dump(exclude_none=True)


@app.post("/register", response_model=OutUser)
async def register(user: InUser, session: Annotated[Session, Depends(get_session)]):
    hashed_password = get_password_hash(user.password)
    user.password_hash = hashed_password
    try:
        db_user = User.model_validate(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return user
    except IntegrityError:
        raise HTTPException(status_code=409, detail="User already exists")


@app.post("/signin")
async def signin(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_session)],
):
    statement = select(User).where(User.username == form_data.username)
    user: User = session.exec(statement).first()
    if verify_password(form_data.password, user.password_hash):
        access_token_expires = timedelta(minutes=settings.access_token_expires_minutes)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")


@app.delete("/user")
async def delete_user(
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    session.delete(current_user)
    session.commit()
    return current_user


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(app)
