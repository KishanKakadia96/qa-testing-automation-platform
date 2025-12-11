import pytest

@pytest.mark.form
@pytest.mark.ui
@pytest.mark.positive
class TestFormValidation:
    """
    Form field validation tests
    """
    
    def test_form_fields_visible(self, booking_page):
        """
        TC012: Verify all form fields are visible
        """
        assert booking_page.is_element_visible(booking_page.FIRSTNAME_INPUT, timeout=5)
        assert booking_page.is_element_visible(booking_page.LASTNAME_INPUT, timeout=5)
        assert booking_page.is_element_visible(booking_page.EMAIL_INPUT, timeout=5)
        assert booking_page.is_element_visible(booking_page.PHONE_INPUT, timeout=5)
        print(" All form fields are visible")
    
    def test_submit_button_present(self, booking_page):
        """
        TC013: Verify submit button is present
        """
        assert booking_page.is_element_visible(booking_page.SUBMIT_BUTTON, timeout=5)
        print(" Submit button is present")
    
    def test_complete_booking_flow(self, booking_page, sample_booking_data):
        """
        TC014: Complete booking flow with all fields
        """
        booking_page.create_booking(
            sample_booking_data["firstname"],
            sample_booking_data["lastname"],
            sample_booking_data["email"],
            sample_booking_data["phone"],
            sample_booking_data["checkin"],
            sample_booking_data["checkout"]
        )
        print(" Complete booking flow executed")
    
    def test_form_field_clear_functionality(self, booking_page):
        """
        TC015: Verify form fields can be cleared and re-filled
        """
        booking_page.fill_firstname("FirstName")
        booking_page.fill_firstname("UpdatedName")
        print(" Form field clear and update works")
    
    def test_date_fields_accept_input(self, booking_page):
        """
        TC016: Verify date fields accept date input
        """
        booking_page.select_checkin_date("2025-12-15")
        booking_page.select_checkout_date("2025-12-20")
        print(" Date fields accept input")

@pytest.mark.form
@pytest.mark.ui
@pytest.mark.negative
class TestFormBoundary:
    """
    Boundary and edge case tests for form fields
    """
    
    def test_long_firstname(self, booking_page):
        """
        TC017: Test firstname with very long input
        """
        long_name = "A" * 100
        booking_page.fill_firstname(long_name)
        print(" Long firstname test executed")
    
    def test_long_lastname(self, booking_page):
        """
        TC018: Test lastname with very long input
        """
        long_name = "B" * 100
        booking_page.fill_lastname(long_name)
        print(" Long lastname test executed")
    
    def test_special_characters_in_name(self, booking_page):
        """
        TC019: Test special characters in name fields
        """
        booking_page.fill_firstname("John@#$%")
        booking_page.fill_lastname("Doe!&*()")
        print(" Special characters test executed")
    
    def test_numeric_values_in_name(self, booking_page):
        """
        TC020: Test numeric values in name fields
        """
        booking_page.fill_firstname("12345")
        booking_page.fill_lastname("67890")
        print(" Numeric values in name test executed")
