from flask import send_from_directory
import pytest
from app import create_app


@pytest.fixture()
def test_app():
    ''' creates app for testing '''
    t_app = create_app()
    t_app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield t_app

    # clean up / reset resources here

@pytest.fixture()
def test_client(app):
    ''' creates client for testing '''
    return app.test_client()


@pytest.fixture()
def runner(app):
    ''' cli runner '''
    return app.test_cli_runner()

def test_home1(client):
    ''' tests homepage '''
    response = client.get("/")
    assert response.status_code == 200

def test_home2(client):
    ''' tests homepage'''
    response = client.get("/home")
    assert response.status_code == 200

def test_form(client):
    ''' tests form file upload '''
    file = 'test-tiny.tiff'
    data = {'email': 'amwarkow@gmail.com', 'file':(open(file, 'rb'), file), 'model':'Kevin'}
    response = client.get("/", data=data)
    assert response.status_code == 200

def test_server(client):
    ''' tests server homepage '''
    response = client.get("/server")
    assert response.status_code == 200

def test_invalid_file(client):
    ''' tests invalid file error '''
    file = 'test-0.png'
    data = {'email': 'amwarkow@gmail.com', 'file':(open(file, 'rb'), file), 'model':'Kevin'}
    response = client.get("/", data=data)
    assert response.status_code == 400