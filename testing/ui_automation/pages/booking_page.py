from testing.api_automation.configs.config import config
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BookingPage(BasePage):
    """
    Page Object for Restful Booker Booking Page
    """
    # Form input fields (appear after clicking Reserve Now)
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input.room-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input.room-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.room-email")
    PHONE_INPUT = (By.CSS_SELECTOR, "input.room-phone")
    
    # Date fields
    CHECKIN_DATE = (By.NAME, "checkin")
    CHECKOUT_DATE = (By.NAME, "checkout")
    
    # Room selection - Book now links
    SINGLE_ROOM_BOOK_LINK = (By.XPATH, "//h5[contains(text(), 'Single')]/ancestor::div[contains(@class, 'card')]//a[contains(text(), 'Book now')]")
    DOUBLE_ROOM_BOOK_LINK = (By.XPATH, "//h5[contains(text(), 'Double')]/ancestor::div[contains(@class, 'card')]//a[contains(text(), 'Book now')]")
    SUITE_ROOM_BOOK_LINK = (By.XPATH, "//h5[contains(text(), 'Suite')]/ancestor::div[contains(@class, 'card')]//a[contains(text(), 'Book now')]")
    
    # Reservation page buttons
    RESERVE_NOW_BUTTON_FIRST = (By.ID, "doReservation")  # Opens form after date selection
    RESERVE_NOW_BUTTON_SUBMIT = (By.XPATH, "//button[contains(text(), 'Reserve Now') and contains(@class, 'btn-primary')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")
    
    # Booking Confirmation elements
    BOOKING_CONFIRMED_TITLE = (By.XPATH, "//h2[contains(text(), 'Booking Confirmed')]")
    BOOKING_CONFIRMED_CARD = (By.CSS_SELECTOR, ".booking-card")
    BOOKING_CONFIRMED_DATES = (By.XPATH, "//p[@class='text-center pt-2']/strong")
    RETURN_HOME_BUTTON = (By.XPATH, "//a[contains(text(), 'Return home')]")
    
    # Messages
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_booking_page(self):
        """
        Navigate to booking page
        """
        self.navigate_to(config.TEST_URL)
    
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
    
    def click_single_room_book_now(self):
        """
        Click 'Book now' link for Single room
        """
        self.scroll_to_element(self.SINGLE_ROOM_BOOK_LINK)
        self.click_element(self.SINGLE_ROOM_BOOK_LINK)
    
    def click_double_room_book_now(self):
        """
        Click 'Book now' link for Double room
        """
        self.scroll_to_element(self.DOUBLE_ROOM_BOOK_LINK)
        self.click_element(self.DOUBLE_ROOM_BOOK_LINK)
    
    def click_suite_room_book_now(self):
        """
        Click 'Book now' link for Suite room
        """
        self.scroll_to_element(self.SUITE_ROOM_BOOK_LINK)
        self.click_element(self.SUITE_ROOM_BOOK_LINK)
    
    def click_reserve_now(self):
        """
        Click 'Reserve Now' button on reservation page (first button - opens form)
        This button appears after selecting dates for any room type
        """
        self.click_element(self.RESERVE_NOW_BUTTON_FIRST)
    
    def click_submit_reservation(self):
        """
        Click 'Reserve Now' button to submit the booking form (second button - submits form)
        This button appears after filling in personal details
        """
        self.click_element(self.RESERVE_NOW_BUTTON_SUBMIT)
    
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
    
    def is_firstname_visible(self):
        """
        Check if firstname input is visible
        """
        return self.is_element_visible(self.FIRSTNAME_INPUT, timeout=5)
    
    def is_reserve_now_button_visible(self):
        """
        Check if Reserve Now submit button is visible
        """
        return self.is_element_visible(self.RESERVE_NOW_BUTTON_SUBMIT, timeout=5)
    
    def get_firstname_value(self):
        """Get firstname field value"""
        return self.find_element(self.FIRSTNAME_INPUT).get_attribute('value')
    
    def get_lastname_value(self):
        """Get lastname field value"""
        return self.find_element(self.LASTNAME_INPUT).get_attribute('value')
    
    def get_email_value(self):
        """Get email field value"""
        return self.find_element(self.EMAIL_INPUT).get_attribute('value')
    
    def get_phone_value(self):
        """Get phone field value"""
        return self.find_element(self.PHONE_INPUT).get_attribute('value')
    
    def is_booking_confirmed(self):
        """
        Check if booking confirmation screen is displayed
        Returns: True if booking confirmed, False otherwise
        """
        return self.is_element_visible(self.BOOKING_CONFIRMED_TITLE, timeout=10)
    
    def get_booking_confirmation_title(self):
        """
        Get booking confirmation title text
        Returns: Title text (should be "Booking Confirmed")
        """
        return self.get_element_text(self.BOOKING_CONFIRMED_TITLE)
    
    def get_confirmed_dates(self):
        """
        Get confirmed booking dates from confirmation screen
        Returns: Dates string
        """
        return self.get_element_text(self.BOOKING_CONFIRMED_DATES)
    
    def click_return_home(self):
        """
        Click 'Return home' button on confirmation screen
        """
        self.click_element(self.RETURN_HOME_BUTTON)
        self.navigate_to(config.TEST_URL)
