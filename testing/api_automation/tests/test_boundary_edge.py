#Testing boundary and edge cases for booking API
    
def test_boundary_extreme_values(booking_client):
    """
    Test extreme values for booking creation.
    Test Covers: TC034-TC036, TC045-TC046, TC066
    """
    extreme_data = {
        "firstname": "A" * 300,
        "lastname": "B" * 300,
        "totalprice": 999999,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-12-31"},
        "additionalneeds": "@#$%^&*()" + "a" * 500  # TC045-TC046
    }
    response = booking_client.create_booking(extreme_data)
    assert response.status_code == 200