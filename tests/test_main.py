from fastapi.testclient import TestClient


def test_register(client: TestClient):
    user_as_dict = {"username": "mail@example.com", "password_hash": "test1"}
    response = client.post("/register", json=user_as_dict)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user_as_dict["username"]


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


def test_delete_user(client: TestClient):
    response = client.delete("/user")
    assert response.status_code == 401
