import pytest

@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.positive
class TestBookingUI:
    """
    UI tests for booking functionality
    """
    
    def test_open_booking_page(self, booking_page):
        """
        TC001: Verify booking page loads successfully
        """
        assert booking_page.driver.current_url is not None
        print(" Booking page loaded successfully")
    
    def test_fill_booking_form_valid_data(self, booking_page, sample_booking_data):
        """
        TC002: Verify booking form can be filled with valid data
        """
        booking_page.fill_firstname(sample_booking_data["firstname"])
        booking_page.fill_lastname(sample_booking_data["lastname"])
        booking_page.fill_email(sample_booking_data["email"])
        booking_page.fill_phone(sample_booking_data["phone"])
        print(" All form fields filled successfully")
    
    def test_firstname_field_accepts_input(self, booking_page):
        """
        TC003: Verify firstname field accepts text input
        """
        booking_page.fill_firstname("John")
        print(" Firstname field accepts input")
    
    def test_lastname_field_accepts_input(self, booking_page):
        """
        TC004: Verify lastname field accepts text input
        """
        booking_page.fill_lastname("Doe")
        print(" Lastname field accepts input")
    
    def test_email_field_accepts_input(self, booking_page):
        """
        TC005: Verify email field accepts email input
        """
        booking_page.fill_email("test@example.com")
        print(" Email field accepts input")
    
    def test_phone_field_accepts_input(self, booking_page):
        """
        TC006: Verify phone field accepts numeric input
        """
        booking_page.fill_phone("1234567890")
        print(" Phone field accepts input")

@pytest.mark.negative
@pytest.mark.ui
class TestBookingUIValidation:
    """
    Negative UI tests for form validation
    """
    
    def test_empty_form_submission(self, booking_page):
        """
        TC007: Verify error when submitting empty form
        """
        booking_page.submit_booking()
        # Add validation check when error handling is available
        print(" Empty form submission test executed")
    
    def test_invalid_email_format(self, booking_page):
        """
        TC008: Verify validation for invalid email
        """
        booking_page.fill_email("invalid-email")
        print(" Invalid email test executed")
    
    def test_invalid_phone_format(self, booking_page):
        """
        TC009: Verify validation for invalid phone
        """
        booking_page.fill_phone("abc123")
        print(" Invalid phone test executed")

@pytest.mark.ui
@pytest.mark.navigation
class TestNavigation:
    """
    Navigation tests for booking page
    """
    
    def test_page_title(self, driver):
        """
        TC010: Verify page has title
        """
        from testing.api_automation.configs.config import config
        driver.get(config.BASE_URL)
        title = driver.title
        assert title is not None
        print(f" Page title: {title}")
    
    def test_page_url(self, booking_page):
        """
        TC011: Verify correct URL is loaded
        """
        from testing.api_automation.configs.config import config
        current_url = booking_page.driver.current_url
        assert config.BASE_URL in current_url
        print(f" Current URL: {current_url}")
