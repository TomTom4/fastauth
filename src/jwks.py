from typing import Optional, List
from pydantic import BaseModel, HttpUrl, Field


class JWK(BaseModel):
    kty: str
    use: Optional[str]
    key_ops: Optional[str]
    alg: Optional[str]
    kid: Optional[str]
    x5u: Optional[HttpUrl]
    x5c: Optional[str]
    x5t: Optional[str]
    x5tS256: Optional[str] = Field(alias="x5t#256")


class JWKS(BaseModel):
    keys: List[JWK]
