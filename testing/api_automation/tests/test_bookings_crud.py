import pytest

# Functional tests for Booking CRUD operations
def test_create_booking_valid(booking_client, sample_booking_data):
    """
    Test creating a booking with valid data 
    Test Case: TC001
    """
    response = booking_client.create_booking(sample_booking_data)
    assert response.status_code == 200
    
    booking_id = response.json().get("bookingid")
    assert booking_id is not None

    print(f"Booking created with ID: {booking_id}")

def test_read_all_bookings(booking_client):
    """
    Test retrieving all bookings
    Test Case: TC009
    """
    response = booking_client.get_all_bookings()
    assert response.status_code == 200

    print("All bookings retrieved successfully.")

def test_read_booking_by_id(booking_client, sample_booking_data):
    """
    Test retrieving a Booking by ID
    Test Case: TC010, TC018, TC042
    """
    booking = booking_client.create_booking(sample_booking_data)
    booking_id = booking.json().get("bookingid")
    
    response = booking_client.get_booking(booking_id)
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["firstname"] == sample_booking_data["firstname"]
    assert response_data["bookingdates"]["checkin"] == sample_booking_data["bookingdates"]["checkin"]

    print(f"Booking with ID: {booking_id} retrieved successfully.")

def test_update_booking_valid(booking_client, sample_booking_data, auth_token):
    """
    Test updating a Booking with valid data
    Test Case: TC011
    """
    booking = booking_client.create_booking(sample_booking_data)
    booking_id = booking.json().get("bookingid")
    
    update_data = sample_booking_data.copy()
    update_data["firstname"] = "Updated"
    
    updated = booking_client.update_booking(booking_id, update_data, auth_token)
    assert updated.status_code == 200
    
    updated_data = updated.json()
    assert updated_data["firstname"] == "Updated"

    print(f"Booking with ID: {booking_id} updated successfully")

def test_delete_booking_valid(booking_client, sample_booking_data, auth_token):
    """
    Test deleting a Booking with valid data
    Test Case: TC014
    """
    booking = booking_client.create_booking(sample_booking_data)
    booking_id = booking.json().get("bookingid")
    
    response = booking_client.delete_booking(booking_id, auth_token)
    assert response.status_code == 201

    print(f"Booking with ID: {booking_id} deleted successfully")

def test_delete_nonexistent_booking(booking_client, auth_token):
    """
    Test deleting a Nonexistent Booking
    Test Case: TC015
    """
    response = booking_client.delete_booking(999999, auth_token)
    assert response.status_code in [404, 201]

    print("Attempted to delete nonexistent booking, received status:", response.status_code)