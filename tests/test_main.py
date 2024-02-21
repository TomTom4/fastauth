from app.main import app 
from fastapi.testclient import TestClient

test_client = TestClient(app)

def test_main():
    response = client.delete('/user')
    assert response.status_code == 401
