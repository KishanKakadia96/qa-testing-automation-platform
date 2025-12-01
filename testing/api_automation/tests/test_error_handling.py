#Tests for error handling scenarios

def test_malformed_requests(booking_client):
    """
    Test handling of malformed requests.
    TC023-TC024, TC059-TC060: Malformed requests
    """
    response = booking_client.post("/booking", data="{invalid_json}")
    assert response.status_code == 400
    
def test_invalid_endpoints(booking_client):
    """
    Test handling of invalid endpoints and methods.
    TC076-TC078: Invalid endpoints/methods
    """
    response = booking_client.get("/invalid-endpoint")
    assert response.status_code == 404
