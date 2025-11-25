import pytest
from api_client.booking_client import BookingClient
from config.config import BASE_URL

@pytest.fixture(scope="module")
def booking_client():
    return BookingClient(BASE_URL)

def test_update_without_token(booking_client):
    # First create a booking
    data = {
        "firstname": "User1",
        "lastname": "Test",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-12-01", "checkout": "2025-12-05"},
        "additionalneeds": ""
    }
    create_res = booking_client.create_booking(data)
    booking_id = create_res.json().get("bookingid")
    
    # Try to update without token
    update_data = data.copy()
    update_data["firstname"] = "Updated"
    response = booking_client.update_booking(booking_id, update_data, token="")
    
    assert response.status_code == 403  # Forbidden
    print(f"Status: {response.status_code}")

def test_delete_without_token(booking_client):
    # Create booking first
    data = {
        "firstname": "User2",
        "lastname": "Test",
        "totalprice": 100,
        "depositpaid": False,
        "bookingdates": {"checkin": "2025-12-01", "checkout": "2025-12-05"},
        "additionalneeds": ""
    }
    create_res = booking_client.create_booking(data)
    booking_id = create_res.json().get("bookingid")
    
    # Try delete without token
    response = booking_client.delete_booking(booking_id, token="")
    assert response.status_code == 403
    print(f"Status: {response.status_code}")
