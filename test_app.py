from fastapi.testclient import TestClient

from app import MESSAGE, app

client = TestClient(app)


def test_hello():
    response = client.get('/api/info')

    assert response.status_code == 200
    info = response.json()
    assert info['message'] == MESSAGE
    assert info['runtime'].startswith('Python ')
    assert info['pod']


def test_page():
    response = client.get('/')

    assert response.status_code == 200
    assert 'id="message"' in response.text
