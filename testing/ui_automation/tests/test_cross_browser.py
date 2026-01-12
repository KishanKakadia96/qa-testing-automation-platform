import pytest
import logging
from drivers.driver_factory import DriverFactory
from pages.home_page import HomePage

logger = logging.getLogger(__name__)

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
    
    def test_booking_page_loads_all_browsers(self, booking_page):
        """Test booking page loads in all browsers"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        assert booking_page.is_firstname_visible(), "Firstname field not visible"
        assert booking_page.is_reserve_now_button_visible(), "reserve now button not visible"
    
    def test_booking_form_all_browsers(self, booking_page):
        """Test booking form functionality in all browsers"""
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        booking_page.fill_firstname("John")
        booking_page.fill_lastname("Doe")
        booking_page.fill_email("john@example.com")
        booking_page.fill_phone("1234567890")
        
        assert booking_page.get_firstname_value() == "John"
        assert booking_page.get_lastname_value() == "Doe"
