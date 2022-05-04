from flask import send_from_directory
import pytest
from app import create_app


@pytest.fixture()
def app():
    ''' creates app for testing '''
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    # other setup can go here

    yield app


@pytest.fixture()
def test_client(app):
    ''' creates client for testing '''
    return app.test_client()


def test_home(client):
    ''' tests homepage '''
    response = client.get("/")
    assert response.status_code == 200
    response = client.get("/home")
    assert response.status_code == 200


def test_post_home(client):
    ''' tests homepage'''
    response = client.post("/")
    assert response.status_code == 405


def test_valid_file(client):
    ''' tests valid file input to form '''
    file = 'test-tiny.tiff'
    data = {'email': 'amwarkow@gmail.com',
            'file': (open(file, 'rb'), file), 'model': 'kevin_initial'}
    response = client.get("/", data=data)
    assert response.status_code == 200


def test_submit_form(client):
    ''' tests submitting of filled out form'''
    file = 'test-tiny.tiff'
    data = {'email': 'amwarkow@gmail.com',
            'file': (open(file, 'rb'), file), 'model': 'kevin_initial'}
    response = client.post("/server", data=data)
    assert response.status_code == 200


def test_submit_incomplete(client):
    ''' tests for submission of incomplete form'''


def test_invalid_file(client):
    ''' tests invalid file error '''
    file = 'test-tiny.png'
    data = {'email': 'amwarkow@gmail.com',
            'file': (open(file, 'rb'), file), 'model': 'kevin_initial'}
    response = client.post("/server", data=data)
    assert response.status_code == 200
    assert file.encode() not in response.data


def test_model_status(client):
    ''' tests model status route returns successfully'''
    response = client.get("/modelStatus")
    assert response.status_code == 200
    assert b"status" in response.data
