import pytest
from api_client.booking_client import BookingClient
from config.config import BASE_URL

@pytest.fixture(scope="module")
def booking_client():
    return BookingClient(BASE_URL)

@pytest.mark.parametrize("firstname, lastname, totalprice, expected_status", [
    # TODO: API currently does NOT validate these, expects 200, file bugs
    ("", "Doe", 100, 400),  # Missing first name
    ("John", "", 100, 400), # Missing last name
    ("John", "Doe", -50, 400), # Negative price
    ("A"*300, "B"*300, 100, 200), # Very long firstname and lastname
])
def test_create_booking_variations(booking_client, firstname, lastname, totalprice, expected_status):
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-11",
            "checkout": "2025-12-15"
        },
        "additionalneeds": ""
    }
    response = booking_client.create_booking(data)
    assert response.status_code == expected_status

@pytest.mark.parametrize("checkin, checkout, expected_status", [
    ("2025-12-20", "2025-12-15", 400),  # Checkout before checkin
    ("invalid-date", "2025-12-15", 400), # Invalid date format
    ("2025-13-01", "2025-12-15", 400),   # Invalid month
])
def test_invalid_dates(booking_client, checkin, checkout, expected_status):
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": ""
    }
    response = booking_client.create_booking(data)
    print(f"Checkin: {checkin}, Checkout: {checkout}")
    print(f"Status: {response.status_code}, Body: {response.text}")
    assert response.status_code == expected_status

