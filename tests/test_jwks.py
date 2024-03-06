from src.jwks import JWK, JWKS


def test_public_jwk_symetric_algorithm():
    example_key = {
        "kty": "EC",
        "crv": "P-256",
        "x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
        "y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
        "use": "enc",
        "kid": "1",
    }
    # TODO: implement test
    symetric_jwk = None
    assert symetric_jwk == example_key


def test_public_jwk_asymetric_algorithm():
    example_key = {}
    asymetric_jwk = None
    # TODO: implement test
    assert asymetric_jwk == example_key


def test_public_jwks():
    # TODO: implement test
    assert "jwks" == []
