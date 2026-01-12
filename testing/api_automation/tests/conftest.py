import os
import json
import logging
import pytest
from pathlib import Path

from ..api_client.auth_client import AuthClient
from ..api_client.booking_client import BookingClient
from ..configs.config import config

def load_test_data(filename: str):
    """Load JSON test data from the local data/ directory."""
    tests_dir = Path(__file__).parent
    data_dir = tests_dir / "data" if (tests_dir / "data").exists() else tests_dir.parent / "data"
    data_file = data_dir / filename
    with data_file.open(encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure logging for API automation tests with file and console output."""
    # Create logs/session directory within api_automation folder
    log_dir = Path(__file__).parent.parent / "logs" / "session"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Session log file
    from datetime import datetime
    session_log = log_dir / f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(session_log, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    logging.info(f"API Test session started - Logs: {session_log}")

@pytest.fixture(scope="function", autouse=True)
def setup_api_test_logging(request):
    """Setup module-level logging for each API test file."""
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

@pytest.fixture(scope="session")
def auth_client():
    """Auth client instance, shared for whole session."""
    return AuthClient(config.BASE_URL)

@pytest.fixture(scope="session")
def booking_client():
    """Booking client instance, shared for whole session."""
    return BookingClient(config.BASE_URL)

@pytest.fixture(scope="session")
def auth_token(auth_client):
    """Get authentication token once per session."""
    token = auth_client.login(username=config.USERNAME, password=config.PASSWORD)
    logging.info("Authenticated and obtained token for test session.")
    return token

@pytest.fixture(scope="session")
def sample_booking_data():
    """Load sample booking data for tests."""
    booking_data = {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-12-01",
            "checkout": "2025-12-05"
        },
        "additionalneeds": "Breakfast"

    }
    return booking_data