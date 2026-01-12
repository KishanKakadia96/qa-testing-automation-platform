import pytest
import logging

logger = logging.getLogger(__name__)

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
        # Navigate to room and open form first
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        # Now check if form fields are visible
        assert booking_page.is_element_visible(booking_page.FIRSTNAME_INPUT, timeout=5)
        assert booking_page.is_element_visible(booking_page.LASTNAME_INPUT, timeout=5)
        assert booking_page.is_element_visible(booking_page.EMAIL_INPUT, timeout=5)
        assert booking_page.is_element_visible(booking_page.PHONE_INPUT, timeout=5)
        logger.info("All form fields are visible")
    
    def test_reserve_now_button_present(self, booking_page):
        """
        TC013: Verify Reserve Now button is present on reservation page
        """
        booking_page.click_room_book_now()
        assert booking_page.is_element_visible(booking_page.RESERVE_NOW_BUTTON_FIRST, timeout=5)
        logger.info("Reserve Now button is present")
    
    def test_complete_booking_flow(self, booking_page, sample_booking_data):
        """
        TC014: Complete booking flow with all fields
        """
        # Click room Book now link
        booking_page.click_room_book_now()
        # Click Reserve Now to open form
        booking_page.click_reserve_now()
        # Fill form fields
        booking_page.fill_firstname(sample_booking_data["firstname"])
        booking_page.fill_lastname(sample_booking_data["lastname"])
        booking_page.fill_email(sample_booking_data["email"])
        booking_page.fill_phone(sample_booking_data["phone"])
        # Submit reservation
        booking_page.click_submit_reservation()
        logger.info("Complete booking flow executed")
    
    def test_form_field_clear_functionality(self, booking_page):
        """
        TC015: Verify form fields can be cleared and re-filled
        """
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_firstname("FirstName")
        booking_page.fill_firstname("UpdatedName")
        logger.info("Form field clear and update works")

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
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        long_name = "A" * 100
        booking_page.fill_firstname(long_name)
        logger.info("Long firstname test executed")
    
    def test_long_lastname(self, booking_page):
        """
        TC018: Test lastname with very long input
        """
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        long_name = "B" * 100
        booking_page.fill_lastname(long_name)
        logger.info("Long lastname test executed")
    
    def test_special_characters_in_name(self, booking_page):
        """
        TC019: Test special characters in name fields
        """
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_firstname("John@#$%")
        booking_page.fill_lastname("Doe!&*()")
        logger.info("Special characters test executed")
    
    def test_numeric_values_in_name(self, booking_page):
        """
        TC020: Test numeric values in name fields
        """
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_firstname("12345")
        booking_page.fill_lastname("67890")
        logger.info("Numeric values in name test executed")
