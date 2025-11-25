import pytest
from api_client.auth_client import AuthClient
from config.config import BASE_URL

@pytest.fixture(scope="module")
def auth_client():
    return AuthClient(BASE_URL)

def test_valid_login(auth_client):
    token = auth_client.login(username="admin", password="password123")
    assert token is not None
    assert isinstance(token, str)
    print(f"Token: {token}")

def test_invalid_username(auth_client):
    with pytest.raises(AssertionError):
        auth_client.login(username="wronguser", password="password123")

def test_invalid_password(auth_client):
    with pytest.raises(AssertionError):
        auth_client.login(username="admin", password="wrongpass")

def test_empty_credentials(auth_client):
    with pytest.raises(AssertionError):
        auth_client.login(username="", password="")
