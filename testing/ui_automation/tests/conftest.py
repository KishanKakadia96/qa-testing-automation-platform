import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import logging
from datetime import datetime
from pathlib import Path
from drivers.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.booking_page import BookingPage
from testing.api_automation.configs.config import config

def pytest_configure(config):
    """
    Configure logging for UI automation tests
    Creates testing/ui_automation/logs directory with session and module-level logs
    """
    # Create logs/session directory within ui_automation folder
    log_dir = Path(__file__).parent.parent / "logs" / "session"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Session log file
    session_log = log_dir / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(session_log, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    logging.info(f"UI Test session started - Logs: {session_log}")

@pytest.fixture(scope="function", autouse=True)
def setup_test_logging(request):
    """
    Setup module-level logging for each test file
    """
    log_dir = Path(__file__).parent.parent / "logs" / "tests"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Get test module name
    module_name = request.node.module.__name__.split('.')[-1]
    module_log = log_dir / f"{module_name}.log"
    
    # Create file handler for this module
    file_handler = logging.FileHandler(module_log, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Add handler to root logger
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    
    yield
    
    # Remove handler after test
    logger.removeHandler(file_handler)
    file_handler.close()

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
