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

config = Config()