import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from src.dependencies import get_current_user, get_session
from src.models import User
from src.main import app


@pytest.fixture(name="authentified_client")
def authentified_client_fixture(session: Session):
    def get_session_override():
        return session

    user = User(username="test", password_hash="test")
    session.add(user)
    session.commit()

    def get_current_user_override():
        return user

    app.dependency_overrides[get_session] = get_session_override
    app.dependency_overrides[get_current_user] = get_current_user_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_delete_user_not_signedin(client: TestClient):
    response = client.delete("/user")
    assert response.status_code == 401


def test_delete_user_authentified(authentified_client: TestClient):
    response = authentified_client.delete("/user")
    assert response.status_code == 200
