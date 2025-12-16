import pytest
from drivers.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.booking_page import BookingPage


@pytest.mark.cross_browser
class TestCrossBrowser:
    """Cross-browser compatibility tests"""
    
    @pytest.fixture(params=["chrome", "edge"])
    def cross_browser_driver(self, request):
        """Create driver for different browsers"""
        driver = DriverFactory.create_driver(browser=request.param)
        driver.maximize_window()
        yield driver
        DriverFactory.quit_driver(driver)
    
    def test_home_page_loads_all_browsers(self, cross_browser_driver):
        """Test home page loads correctly in all browsers"""
        page = HomePage(cross_browser_driver)
        page.open_home_page()
        assert page.is_home_page_loaded(), "Home page did not load"
        assert page.get_site_title() != "", "Site title is empty"
    
    def test_booking_page_loads_all_browsers(self, cross_browser_driver):
        """Test booking page loads in all browsers"""
        page = BookingPage(cross_browser_driver)
        page.open_booking_page()
        assert page.is_firstname_visible(), "Firstname field not visible"
        assert page.is_submit_button_visible(), "Submit button not visible"
    
    def test_booking_form_all_browsers(self, cross_browser_driver):
        """Test booking form functionality in all browsers"""
        page = BookingPage(cross_browser_driver)
        page.open_booking_page()
        
        page.fill_firstname("John")
        page.fill_lastname("Doe")
        page.fill_email("john@example.com")
        page.fill_phone("1234567890")
        
        assert page.get_firstname_value() == "John"
        assert page.get_lastname_value() == "Doe"
