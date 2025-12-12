import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from drivers.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.booking_page import BookingPage

@pytest.fixture(scope="function")
def driver():
    """
    Create and quit WebDriver for each test
    """
    driver = DriverFactory.create_driver()
    driver.maximize_window()
    yield driver
    DriverFactory.quit_driver(driver)

@pytest.fixture(scope="function")
def home_page(driver):
    """
    HomePage fixture
    """
    page = HomePage(driver)
    page.open_home_page()
    return page

@pytest.fixture(scope="function")
def booking_page(driver):
    """
    BookingPage fixture
    """
    page = BookingPage(driver)
    page.open_booking_page()
    return page

@pytest.fixture(scope="function")
def sample_booking_data():
    """
    Sample booking data for tests
    """
    return {
        "firstname": "John",
        "lastname": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "checkin": "2025-12-15",
        "checkout": "2025-12-20"
    }

@pytest.fixture(scope="function")
def invalid_booking_data():
    """
    Invalid booking data for negative tests
    """
    return {
        "firstname": "",
        "lastname": "",
        "email": "invalid-email",
        "phone": "abc",
        "checkin": "2025-12-20",
        "checkout": "2025-12-15"
    }
