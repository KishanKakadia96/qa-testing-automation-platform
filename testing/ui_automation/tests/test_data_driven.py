import pytest
import json
import os

def load_test_data():
    """Load test data from JSON file"""
    data_file = os.path.join(os.path.dirname(__file__), '../data/booking_test_data.json')
    with open(data_file, 'r') as f:
        return json.load(f)

@pytest.mark.parallel
class TestDataDriven:
    """Data-driven tests using external test data"""
    
    @pytest.mark.parametrize("test_data", load_test_data())
    def test_booking_with_multiple_datasets(self, test_data, booking_page):
        """Test booking form with multiple test data sets"""
        # Fill form with test data
        booking_page.click_single_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_firstname(test_data['firstname'])
        booking_page.fill_lastname(test_data['lastname'])
        booking_page.fill_email(test_data['email'])
        booking_page.fill_phone(test_data['phone'])
        
        # Verify data is entered
        if test_data['firstname']:
            assert booking_page.get_firstname_value() == test_data['firstname']
        if test_data['lastname']:
            assert booking_page.get_lastname_value() == test_data['lastname']
    
    @pytest.mark.parametrize("firstname,lastname,email,expected", [
        ("John", "Doe", "john@test.com", True),
        ("Jane", "Smith", "jane@test.com", True),
        ("", "Brown", "brown@test.com", False),
        ("Mike", "", "mike@test.com", False),
    ])
    def test_name_fields_validation(self, firstname, lastname, email, expected, booking_page):
        """Test name field validation with inline data"""
        booking_page.click_single_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_firstname(firstname)
        booking_page.fill_lastname(lastname)
        booking_page.fill_email(email)
        
        # Verify fields based on expected result
        if expected:
            assert booking_page.get_firstname_value() == firstname
            assert booking_page.get_lastname_value() == lastname
        else:
            # Check for empty fields
            if not firstname:
                assert booking_page.get_firstname_value() == ""
            if not lastname:
                assert booking_page.get_lastname_value() == ""
    
    @pytest.mark.parametrize("email", [
        "valid@email.com",
        "test.user@example.org",
        "user123@test.co.uk",
    ])
    def test_valid_email_formats(self, email, booking_page):
        """Test various valid email formats"""
        booking_page.click_single_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_email(email)
        assert booking_page.get_email_value() == email
    
    @pytest.mark.parametrize("phone", [
        "1234567890",
        "9876543210",
        "5551234567",
    ])
    def test_valid_phone_formats(self, driver, phone, booking_page):
        """Test various valid phone formats"""
        booking_page.click_single_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_phone(phone)
        assert booking_page.get_phone_value() == phone
