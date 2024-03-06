from typing import Optional, List, Literal
from pydantic import BaseModel, HttpUrl, Field


class JWK(BaseModel):
    kty: Literal["RSA", "EC"] = "RSA"
    use: Literal["sig", "enc"] = "sig"
    key_ops: Optional[
        Literal[
            "sign",
            "verify",
            "encrypt",
            "decrypt",
            "wrapKey",
            "unwrapKey",
            "deriveKey",
            "deriveBits",
        ]
    ] = None
    alg: Optional[str] = None
    kid: Optional[str] = 
    x5u: Optional[HttpUrl]
    x5c: Optional[str]
    x5t: Optional[str]
    x5tS256: Optional[str] = Field(alias="x5t#256")


class JWKS(BaseModel):
    keys: List[JWK]
