import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime
from drivers.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.booking_page import BookingPage
from testing.api_automation.configs.config import config

def pytest_addoption(parser):
    """
    Add custom command line options for pytest
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, edge"
    )

@pytest.fixture(scope="function")
def driver(request):
    """
    Create and quit WebDriver for each test
    """
    browser = request.config.getoption("--browser")
    os.environ["BROWSER"] = browser
    driver = DriverFactory.create_driver(browser=browser)
    driver.maximize_window()
    yield driver

    current_url = driver.current_url
    print(f"\nCurrent URL at teardown: {current_url}")
    
    # Take screenshot on failure
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
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
        "checkin": "2025-12-28",
        "checkout": "2025-12-29"
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
