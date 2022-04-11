from flask import request
import pytest
from app import create_app

@pytest.fixture()
def app():
    test_app = create_app()
    test_app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield test_app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_home1(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home2(client):
    response = client.get("/home")
    assert response.status_code == 200

def test_form(client):
    file = 'test-tiny.tiff'
    data = {'email': 'amwarkow@gmail.com', 'file':(open(file, 'rb'), file), 'model':'Kevin'}
    response = client.get("/", data=data)
    assert response.status_code == 200

def test_server(client):
    response = client.get("/server")
    assert response.status_code == 200