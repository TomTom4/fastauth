from fastapi.testclient import TestClient


def test_signin(client: TestClient):
    user_as_dict = {"email": "mail@example.com", "password": "test1"}
    client.post("/register", json=user_as_dict)
    response = client.post(
        "/signin",
        data={
            "username": user_as_dict["email"],
            "password": user_as_dict["password"],
        },
    )
    assert response.status_code == 200
    print(response.json())
