import json
import os
import logging
import pytest

def load_test_data(filename):
    filepath = os.path.join(os.path.dirname(__file__), '..', 'data', filename)
    with open(filepath, 'r') as f:
        return json.load(f)

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )