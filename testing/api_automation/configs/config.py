import os
from dotenv import load_dotenv

load_dotenv()

# Configuration of environment variables for API testing
class Config:
    BASE_URL = os.environ.get("BASE_URL")
    AUTH_ENDPOINT = os.environ.get("AUTH_ENDPOINT")
    BOOKING_ENDPOINT = os.environ.get("BOOKING_ENDPOINT")

    USERNAME = os.environ.get("API_USERNAME")
    PASSWORD = os.environ.get("API_PASSWORD")

    TEST_URL = os.environ.get("TEST_URL")
    SINGLE_ROOM_BOOK_LINK = os.environ.get("SINGLE_ROOM_BOOK_LINK")
    DOUBLE_ROOM_BOOK_LINK = os.environ.get("DOUBLE_ROOM_BOOK_LINK")
    SUITE_ROOM_BOOK_LINK = os.environ.get("SUITE_ROOM_BOOK_LINK")
    BROWSER = os.environ.get("BROWSER")
    IMPLICIT_WAIT = os.environ.get("IMPLICIT_WAIT")
    EXPLICIT_WAIT = os.environ.get("EXPLICIT_WAIT")
    HEADLESS = os.environ.get("HEADLESS")

config = Config()