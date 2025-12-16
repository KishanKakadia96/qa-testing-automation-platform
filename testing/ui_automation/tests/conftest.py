import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime
from drivers.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.booking_page import BookingPage

@pytest.fixture(scope="function")
def driver(request):
    """
    Create and quit WebDriver for each test
    """
    driver = DriverFactory.create_driver()
    driver.maximize_window()
    yield driver
    
    # Take screenshot on failure
    if request.node.rep_call.failed:
        screenshot_dir = os.path.join(os.path.dirname(__file__), '../reports/screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")
    
    DriverFactory.quit_driver(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test result for screenshot
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

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
