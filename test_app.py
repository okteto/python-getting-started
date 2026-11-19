from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_hello_world():
    response = client.get('/')

    assert response.status_code == 200
    assert response.text == 'Hello World!'
