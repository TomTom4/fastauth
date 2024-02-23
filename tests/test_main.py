import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.dependencies import get_session
from sqlmodel import Session, create_engine
from sqlmodel.pool import StaticPool


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):

    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_register(client: TestClient):
    username = "mail@example.com"
    response = client.post(
        "/register", json={"username": username, "password_hash": "test1"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == username


def test_signin(client: TestClient):
    pass


def test_delete_user(client: TestClient):
    response = client.delete("/user")
    assert response.status_code == 401
