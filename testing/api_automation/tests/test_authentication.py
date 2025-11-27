import pytest
from ..configs.config import config

# Tests for authentication functionality of the Booking API
''' 
Note: 
username and password are already available on website documentation,
but for Actual production-level testing, these should be stored securely in environment variables.
'''
def test_valid_login(auth_client):
    """Test the login functionality with valid credentials."""
    token = auth_client.login(username=config.USERNAME, password=config.PASSWORD)
    assert token is not None
    assert isinstance(token, str)
    print(f"Token: {token}")

def test_invalid_username(auth_client):
    '''Test login with invalid username'''
    with pytest.raises(AssertionError):
        auth_client.login(username="wronguser", password=config.PASSWORD)

def test_invalid_password(auth_client):
    '''Test login with invalid password'''
    with pytest.raises(AssertionError):
        auth_client.login(username=config.USERNAME, password="wrongpass")

def test_empty_credentials(auth_client):
    '''Test login with empty username and password'''
    with pytest.raises(AssertionError):
        auth_client.login(username="", password="")
