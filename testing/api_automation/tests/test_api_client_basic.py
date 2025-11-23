import pytest
from api_client.auth_client import AuthClient
from api_client.booking_client import BookingClient
from config.config import BASE_URL

@pytest.fixture(scope="module")
def auth_client():
    return AuthClient(BASE_URL)

@pytest.fixture(scope="module")
def booking_client():
    return BookingClient(BASE_URL)

def test_login(auth_client):
    token = auth_client.login(username="admin", password="password123")
    assert token is not None
    assert isinstance(token, str)
    print(f"Received Auth Token: {token}")

def test_create_and_get_booking(booking_client):
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
