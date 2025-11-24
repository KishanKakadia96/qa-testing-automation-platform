import pytest
from api_client.auth_client import AuthClient
from api_client.booking_client import BookingClient
from config.config import BASE_URL

@pytest.fixture(scope="module") #use fixture to create fresh client instance
def auth_client():
    return AuthClient(BASE_URL)

@pytest.fixture(scope="module")
def booking_client():
    return BookingClient(BASE_URL)

def test_login(auth_client):
    """Test the login functionality of the AuthClient."""
    token = auth_client.login(username="admin", password="password123")
    assert token is not None
    assert isinstance(token, str)
    print(f"Received Auth Token: {token}")

def test_create_and_get_booking(booking_client):
    """Test creating and retrieving a booking."""
    # Sample booking data
    booking_data = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-11-23",
            "checkout": "2025-11-25"
        },
        "additionalneeds": "Breakfast"
    }

    # Create booking
    response = booking_client.create_booking(booking_data)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    # Retrieve booking
    get_response = booking_client.get_booking(booking_id)
    assert get_response.status_code == 200
    retrieved_data = get_response.json()
    assert retrieved_data["firstname"] == booking_data["firstname"]
    assert retrieved_data["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]

    print(f"Booking created and verified successfully with ID: {booking_id}")

def test_update_booking(booking_client, auth_client):
    """Test updating a Booking"""
    #First create a booking to update
    booking_data = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-11-23",
            "checkout": "2025-11-25"
        },
        "additionalneeds": "Lunch"
    }

    # Create booking
    response =booking_client.create_booking(booking_data)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    # Login to get token
    token = auth_client.login(username="admin", password="password123")
    assert token is not None
    # Update booking data
    updated_data = {
        "firstname": "Updated",
        "lastname": "User",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-01",
            "checkout": "2025-12-05"
        },
        "additionalneeds": "Dinner"
    }
    update_response = booking_client.update_booking(booking_id, updated_data, token)
    assert update_response.status_code == 200
    updated_booking = update_response.json()
    assert updated_booking["firstname"] == updated_data["firstname"]
    assert updated_booking["totalprice"] == updated_data["totalprice"]

    print(f"Booking with ID: {booking_id} updated successfully.")

def test_delete_booking(booking_client, auth_client):
    """Test deleting a Booking"""
    #First create a booking to delete
    booking_data = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-11-23",
            "checkout": "2025-11-25"
        },
        "additionalneeds": "Snacks"
    }

    # Create booking
    response =booking_client.create_booking(booking_data)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    # Login to get token
    token = auth_client.login(username="admin", password="password123")
    assert token is not None

    # Delete booking
    delete_response = booking_client.delete_booking(booking_id, token)
    assert delete_response.status_code == 201  # As per API docs, deletion returns 201

    # Verify deletion by attempting to get the deleted booking
    get_response = booking_client.get_booking(booking_id)
    assert get_response.status_code == 404  # Should return 404 Not Found

    print(f"Booking with ID: {booking_id} deleted successfully.")