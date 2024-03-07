from typing import Optional, List, Literal
from pydantic import BaseModel, HttpUrl, Field


class JWK(BaseModel):
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
    kid: Optional[str] = None
    x5u: Optional[HttpUrl] = None
    x5c: Optional[str] = None
    x5t: Optional[str] = None
    x5tS256: Optional[str] = Field(default=None, alias="x5t#256")


class ElipticCurveJWK(JWK):
    kty: Literal["EC"] = "EC"
    crv: Literal["P-256", "P-384", "P-521"]
    x: str
    y: Optional[str] = None


class PrivateElipticCurveJWK(ElipticCurveJWK):
    d: str


class RSAJWK(JWK):
    kty: Literal["RSA"] = "RSA"
    n: str
    e: str


class PrivateRSAJWK(RSAJWK):
    d: str
    p: str
    q: str
    dp: str
    dq: str
    qi: str
    oth: str


class JWKS(BaseModel):
    keys: List[JWK]
