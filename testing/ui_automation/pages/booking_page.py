from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BookingPage(BasePage):
    """
    Page Object for Restful Booker Booking Page
    """
    # Locators - Main elements
    FIRSTNAME_INPUT = (By.ID, "firstname")
    LASTNAME_INPUT = (By.ID, "lastname")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")
    
    # Date fields
    CHECKIN_DATE = (By.NAME, "checkin")
    CHECKOUT_DATE = (By.NAME, "checkout")
    
    # Buttons
    BOOK_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Messages
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_booking_page(self):
        """
        Navigate to booking page
        """
        from testing.api_automation.configs.config import config
        self.navigate_to(config.TEST_URL)
    
    def fill_firstname(self, firstname):
        """
        Fill first name field
        """
        self.send_keys(self.FIRSTNAME_INPUT, firstname)
    
    def fill_lastname(self, lastname):
        """
        Fill last name field
        """
        self.send_keys(self.LASTNAME_INPUT, lastname)
    
    def fill_email(self, email):
        """
        Fill email field
        """
        self.send_keys(self.EMAIL_INPUT, email)
    
    def fill_phone(self, phone):
        """
        Fill phone field
        """
        self.send_keys(self.PHONE_INPUT, phone)
    
    def select_checkin_date(self, date):
        """
        Select check-in date
        """
        self.send_keys(self.CHECKIN_DATE, date)
    
    def select_checkout_date(self, date):
        """
        Select check-out date
        """
        self.send_keys(self.CHECKOUT_DATE, date)
    
    def click_book_button(self):
        """
        Click book button
        """
        self.click_element(self.BOOK_BUTTON)
    
    def submit_booking(self):
        """
        Submit booking form
        """
        self.click_element(self.SUBMIT_BUTTON)
    
    def is_success_message_displayed(self):
        """
        Check if success message is visible
        """
        return self.is_element_visible(self.SUCCESS_MESSAGE, timeout=5)
    
    def get_success_message(self):
        """
        Get success message text
        """
        return self.get_element_text(self.SUCCESS_MESSAGE)
    
    def is_error_message_displayed(self):
        """
        Check if error message is visible
        """
        return self.is_element_visible(self.ERROR_MESSAGE, timeout=5)
    
    def get_error_message(self):
        """
        Get error message text"""
        return self.get_element_text(self.ERROR_MESSAGE)
    
    def create_booking(self, firstname, lastname, email, phone, checkin, checkout):
        """
        Complete booking process - all fields
        """
        self.fill_firstname(firstname)
        self.fill_lastname(lastname)
        self.fill_email(email)
        self.fill_phone(phone)
        self.select_checkin_date(checkin)
        self.select_checkout_date(checkout)
        self.submit_booking()
