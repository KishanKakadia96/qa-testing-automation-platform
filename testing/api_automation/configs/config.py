import os
from dotenv import load_dotenv

load_dotenv()

# Configuration of environment variables for API testing
class Config:
    BASE_URL = str(os.environ.get("BASE_URL"))
    AUTH_ENDPOINT = str(os.environ.get("AUTH_ENDPOINT"))
    BOOKING_ENDPOINT = str(os.environ.get("BOOKING_ENDPOINT"))

    USERNAME = str(os.environ.get("API_USERNAME"))
    PASSWORD = str(os.environ.get("API_PASSWORD"))

    TEST_URL = str(os.environ.get("TEST_URL"))
    BROWSER = str(os.environ.get("BROWSER"))
    IMPLICIT_WAIT = int(os.environ.get("IMPLICIT_WAIT"))
    EXPLICIT_WAIT = int(os.environ.get("EXPLICIT_WAIT"))
    HEADLESS = str(os.environ.get("HEADLESS"))
config = Config()