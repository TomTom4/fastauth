from fastapi.testclient import TestClient
from jose import jwt


def test_token_verification(client: TestClient):
    print("hello")
    user_as_dict = {"email": "mail@example.com", "password": "test1"}
    client.post("/register", json=user_as_dict)
    response = client.post(
        "/signin",
        data={
            "username": user_as_dict["email"],
            "password": user_as_dict["password"],
        },
    )
    token = response.json()["access_token"]
    assert response.status_code == 200
    response = client.get("/.well-known/jwks.json")
    assert response.status_code == 200
    key = response.json()
    algorithm = jwt.get_unverified_header(token).get("alg")
    user_info = jwt.decode(token=token, key=key, algorithms=algorithm)
    assert user_info["sub"] == user_as_dict["email"]
