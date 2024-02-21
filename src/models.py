from typing import Optional
from sqlmodel import Field, SQLModel, AutoString
from pydantic import EmailStr


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: EmailStr  = Field(unique=True, index=True, sa_type=AutoString)
    password_hash: str
