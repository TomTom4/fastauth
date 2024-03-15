from fastapi.testclient import TestClient


def test_signin(client: TestClient):
    user_as_dict = {"username": "mail@example.com", "password_hash": "test1"}
    client.post("/register", json=user_as_dict)
    response = client.post(
        "/signin",
        data={
            "username": user_as_dict["username"],
            "password": user_as_dict["password_hash"],
        },
    )
    assert response.status_code == 200
    print(response.json())
