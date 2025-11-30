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

def test_xss_sql_injection(booking_client):
        """
        Test XSS and SQL Injection vulnerabilities
        Test Covers: TC053-TC055
        """
        malicious_data = {
            "firstname": "<script>alert('XSS')</script>",
            "lastname": "'; DROP TABLE bookings; --",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                  "checkin": "2025-11-22", 
                  "checkout": "2025-11-25"
                  },
            "additionalneeds": "Breakfast"
        }
        response = booking_client.create_booking(malicious_data)
        assert response.status_code == 400  # Expecting rejection of malicious input