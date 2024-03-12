from src.jwks import ElipticCurveJWK, RSAJWK, JWKS, build_jwk


def test_public_jwk_asymetric_algorithm():
    example_key = {
        "kty": "EC",
        "crv": "P-256",
        "x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
        "y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
        "use": "enc",
        "kid": "1",
    }
    asymetric_jwk = ElipticCurveJWK(
        crv="P-256",
        x="MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
        y="4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
        use="enc",
        kid="1",
    )
    assert asymetric_jwk.model_dump(exclude_none=True) == example_key


def test_public_jwk_symetric_algorithm():
    example_key = {
        "kty": "RSA",
        "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx\
     4cbbfAAtVT86zwu1RK7aPFFxuhDR1L6tSoc_BJECPebWKRXjBZCiFV4n3oknjhMs\
     tn64tZ_2W-5JsGY4Hc5n9yBXArwl93lqt7_RN5w6Cf0h4QyQ5v-65YGjQR0_FDW2\
     QvzqY368QQMicAtaSqzs8KJZgnYb9c7d0zgdAZHzu6qMQvRL5hajrn1n91CbOpbI\
     SD08qNLyrdkt-bFTWhAI4vMQFh6WeZu0fM4lFd2NcRwr3XPksINHaQ-G_xBniIqb\
     w0Ls1jF44-csFCur-kEgU8awapJzKnqDKgw",
        "e": "AQAB",
        "alg": "RS256",
        "kid": "2011-04-29",
    }
    symetric_jwk = RSAJWK(
        n="0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx\
     4cbbfAAtVT86zwu1RK7aPFFxuhDR1L6tSoc_BJECPebWKRXjBZCiFV4n3oknjhMs\
     tn64tZ_2W-5JsGY4Hc5n9yBXArwl93lqt7_RN5w6Cf0h4QyQ5v-65YGjQR0_FDW2\
     QvzqY368QQMicAtaSqzs8KJZgnYb9c7d0zgdAZHzu6qMQvRL5hajrn1n91CbOpbI\
     SD08qNLyrdkt-bFTWhAI4vMQFh6WeZu0fM4lFd2NcRwr3XPksINHaQ-G_xBniIqb\
     w0Ls1jF44-csFCur-kEgU8awapJzKnqDKgw",
        e="AQAB",
        alg="RS256",
        kid="2011-04-29",
    )
    assert symetric_jwk.model_dump(exclude_none=True) == example_key


def test_public_jwks():
    example_set = {
        "keys": [
            {
                "kty": "EC",
                "crv": "P-256",
                "x": "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
                "y": "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
                "use": "enc",
                "kid": "1",
            },
            {
                "kty": "RSA",
                "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx\
     4cbbfAAtVT86zwu1RK7aPFFxuhDR1L6tSoc_BJECPebWKRXjBZCiFV4n3oknjhMs\
     tn64tZ_2W-5JsGY4Hc5n9yBXArwl93lqt7_RN5w6Cf0h4QyQ5v-65YGjQR0_FDW2\
     QvzqY368QQMicAtaSqzs8KJZgnYb9c7d0zgdAZHzu6qMQvRL5hajrn1n91CbOpbI\
     SD08qNLyrdkt-bFTWhAI4vMQFh6WeZu0fM4lFd2NcRwr3XPksINHaQ-G_xBniIqb\
     w0Ls1jF44-csFCur-kEgU8awapJzKnqDKgw",
                "e": "AQAB",
                "alg": "RS256",
                "kid": "2011-04-29",
            },
        ]
    }
    asymetric_jwk = ElipticCurveJWK(
        crv="P-256",
        x="MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
        y="4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
        use="enc",
        kid="1",
    )
    symetric_jwk = RSAJWK(
        n="0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2aiAFbWhM78LhWx\
     4cbbfAAtVT86zwu1RK7aPFFxuhDR1L6tSoc_BJECPebWKRXjBZCiFV4n3oknjhMs\
     tn64tZ_2W-5JsGY4Hc5n9yBXArwl93lqt7_RN5w6Cf0h4QyQ5v-65YGjQR0_FDW2\
     QvzqY368QQMicAtaSqzs8KJZgnYb9c7d0zgdAZHzu6qMQvRL5hajrn1n91CbOpbI\
     SD08qNLyrdkt-bFTWhAI4vMQFh6WeZu0fM4lFd2NcRwr3XPksINHaQ-G_xBniIqb\
     w0Ls1jF44-csFCur-kEgU8awapJzKnqDKgw",
        e="AQAB",
        alg="RS256",
        kid="2011-04-29",
    )

    jwk_set = JWKS(keys=[asymetric_jwk, symetric_jwk])

    assert jwk_set.model_dump(exclude_none=True) == example_set


def test_build_eliptic_curve_jwk():
    jwk = build_jwk()
    assert jwk
