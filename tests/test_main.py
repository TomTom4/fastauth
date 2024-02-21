from fastapi.testclient import TestClient
from src.main import app 

test_client = TestClient(app)

def test_main():
    response = test_client.delete('/user')
    assert response.status_code == 401
