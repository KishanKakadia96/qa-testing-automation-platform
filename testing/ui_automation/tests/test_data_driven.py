import pytest
import json
import os
from pages.booking_page import BookingPage


def load_test_data():
    """Load test data from JSON file"""
    data_file = os.path.join(os.path.dirname(__file__), '../data/booking_test_data.json')
    with open(data_file, 'r') as f:
        return json.load(f)


@pytest.mark.parallel
class TestDataDriven:
    """Data-driven tests using external test data"""
    
    @pytest.mark.parametrize("test_data", load_test_data())
    def test_booking_with_multiple_datasets(self, driver, test_data):
        """Test booking form with multiple test data sets"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        # Fill form with test data
        page.fill_firstname(test_data['firstname'])
        page.fill_lastname(test_data['lastname'])
        page.fill_email(test_data['email'])
        page.fill_phone(test_data['phone'])
        
        # Verify data is entered
        if test_data['firstname']:
            assert page.get_firstname_value() == test_data['firstname']
        if test_data['lastname']:
            assert page.get_lastname_value() == test_data['lastname']
    
    @pytest.mark.parametrize("firstname,lastname,email,expected", [
        ("John", "Doe", "john@test.com", True),
        ("Jane", "Smith", "jane@test.com", True),
        ("", "Brown", "brown@test.com", False),
        ("Mike", "", "mike@test.com", False),
    ])
    def test_name_fields_validation(self, driver, firstname, lastname, email, expected):
        """Test name field validation with inline data"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        page.fill_firstname(firstname)
        page.fill_lastname(lastname)
        page.fill_email(email)
        
        # Verify fields based on expected result
        if expected:
            assert page.get_firstname_value() == firstname
            assert page.get_lastname_value() == lastname
        else:
            # Check for empty fields
            if not firstname:
                assert page.get_firstname_value() == ""
            if not lastname:
                assert page.get_lastname_value() == ""
    
    @pytest.mark.parametrize("email", [
        "valid@email.com",
        "test.user@example.org",
        "user123@test.co.uk",
    ])
    def test_valid_email_formats(self, driver, email):
        """Test various valid email formats"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        page.fill_email(email)
        assert page.get_email_value() == email
    
    @pytest.mark.parametrize("phone", [
        "1234567890",
        "9876543210",
        "5551234567",
    ])
    def test_valid_phone_formats(self, driver, phone):
        """Test various valid phone formats"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        page.fill_phone(phone)
        assert page.get_phone_value() == phone
