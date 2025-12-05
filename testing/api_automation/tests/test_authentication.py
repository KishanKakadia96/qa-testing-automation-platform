import pytest
from ..configs.config import config

# Tests for authentication functionality of the Booking API
@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.positive
def test_valid_login(auth_client):
    """
    Test the login functionality with valid credentials.
    Test Case: TC016
    """
    token = auth_client.login(username=config.USERNAME, password=config.PASSWORD)
    assert token is not None
    assert isinstance(token, str)
    
    print(f"Login successful, received token")

@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize("username, password, test_scenario", [
    ("wronguser", config.PASSWORD, "Invalid Username"),
    (config.USERNAME, "wrongpass", "Invalid Password"),
])
def test_invalid_credentials(auth_client, username, password, test_scenario):
    '''
    Test login with invalid credentials (username or password)
    Test Case: TC017
    '''
    with pytest.raises(AssertionError):
        auth_client.login(username=username, password=password)
    
    print(f"Login failed as expected with invalid credentials")

@pytest.mark.auth
@pytest.mark.negative
def test_empty_credentials(auth_client):
    '''
    Test login with empty username and password
    Test Case: TC056
    '''
    with pytest.raises(AssertionError):
        auth_client.login(username="", password="")

    print("Login failed as expected with empty credentials")
