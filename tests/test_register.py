from fastapi.testclient import TestClient
from sqlmodel import Session, select
from src.models import User


def test_register_new_user(client: TestClient, session: Session):
    user_as_dict = {"email": "mail@example.com", "password": "test1"}
    response = client.post("/register", json=user_as_dict)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_as_dict["email"]
    statement = select(User).where(User.username == user_as_dict["email"])
    user = session.exec(statement).first()
    assert user


def test_register_existing_user(client: TestClient, session: Session):
    user_as_dict = {"username": "mail@example.com", "password_hash": "test1"}
    user = User(
        username=user_as_dict["username"], password_hash=user_as_dict["password_hash"]
    )
    session.add(user)
    session.commit()
    response = client.post("/register", json=user_as_dict)
    assert response.status_code == 409
