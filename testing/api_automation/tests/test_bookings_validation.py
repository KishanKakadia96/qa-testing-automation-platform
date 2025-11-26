import pytest
from ..api_client.booking_client import BookingClient
from ..config.config import BASE_URL
from .conftest import load_test_data

test_data = load_test_data('bookings_test_data.json')

@pytest.fixture(scope="module")
def booking_client():
    return BookingClient(BASE_URL)

@pytest.mark.parametrize("data", test_data)
def test_create_booking_from_file(booking_client, data):
    expected_status = data["expected_status"]
    payload = {k: v for k, v in data.items() if k != "expected_status"}

    response = booking_client.create_booking(payload)

    print(f"Payload: {payload}")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.text}")

    assert response.status_code == expected_status

