import os
import json
import logging
import pytest
from pathlib import Path

from ..api_client.auth_client import AuthClient
from ..api_client.booking_client import BookingClient
from ..configs.config import config

Base_url = config.BASE_URL

def load_test_data(filename: str):
    """Load JSON test data from the local data/ directory."""
    tests_dir = Path(__file__).parent
    data_dir = tests_dir / "data" if (tests_dir / "data").exists() else tests_dir.parent / "data"
    data_file = data_dir / filename
    with data_file.open(encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure basic logging for the whole test session."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Logging configured for test session.")

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