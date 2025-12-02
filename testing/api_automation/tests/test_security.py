import pytest

# Functional tests for security aspects of the Booking API
@pytest.mark.parametrize("operation", ["update", "delete"])
def test_unauthorized_operations(booking_client, sample_booking_data, operation):
        """
        Test unauthorized update and delete operations without auth token
        Test Covers: TC025, TC026, TC057, TC058
        """
        booking_id = booking_client.create_booking(sample_booking_data)
        
        if operation == "update":
            response = booking_client.update_booking(booking_id, sample_booking_data, "")
        else:  # delete
            response = booking_client.delete_booking(booking_id, "")
            
        # Restful Booker allows without token - document limitation
        assert response.status_code == 403

@pytest.mark.parametrize("data", [
    {"firstname": "<script>alert('XSS')</script>", "lastname": "Doe"},
    {"firstname": "'; DROP TABLE bookings; --", "lastname": "Doe"}
])
def test_xss_sql_injection(booking_client, data):
    """
    Test XSS and SQL Injection in input fields
    Test Covers: TC053, TC054
    """
    malicious_data = {**{"totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-11-22", "checkout": "2025-11-23"}}, **data}
    response = booking_client.create_booking(malicious_data)
    assert response.status_code == 400  # Expecting rejection of malicious input

@pytest.mark.parametrize("data", [
    {"firstname": "%", "lastname": "Doe"},
    {"firstname": "%ohn", "lastname": "Doe"},
    {"firstname": "John", "lastname": "%"},
    {"firstname": "John", "lastname": "D%e"}])
def test_sql_wildcard_injection(booking_client, data):
    """
    Test SQL wildcard injection in input fields
    Test Covers: TC055
    """
    base_data = {
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-11-22",
            "checkout": "2025-11-23"
        }
    }
    malicious_data = {**base_data, **data}
    response = booking_client.create_booking(malicious_data)

    assert response.status_code == 400  # Expecting rejection of wildcard injection