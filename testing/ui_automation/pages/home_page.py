from testing.api_automation.configs.config import config
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Page Object for Home/Landing Page
    """
    # Header Locators
    LOGO = (By.CSS_SELECTOR, ".hotel-logoUrl, .logo")
    SITE_TITLE = (By.CSS_SELECTOR, "h1, .site-title")
    
    # Room Section
    ROOMS_SECTION = (By.CSS_SELECTOR, ".rooms, #rooms")
    ROOM_CARDS = (By.CSS_SELECTOR, ".room, .room-card")
    FIRST_ROOM = (By.CSS_SELECTOR, ".room:first-child")
    
    # Contact Section
    CONTACT_SECTION = (By.CSS_SELECTOR, "#contact, .contact")
    CONTACT_FORM = (By.CSS_SELECTOR, ".contact-form, form")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open_home_page(self):
        """
        Navigate to home page
        """
        self.navigate_to(config.TEST_URL)
    
    def is_home_page_loaded(self):
        """
        Verify home page is loaded
        """
        return self.is_element_visible(self.ROOM_CARDS, timeout=10)
    
    def get_site_title(self):
        """
        Get site title text
        """
        if self.is_element_visible(self.SITE_TITLE):
            return self.get_element_text(self.SITE_TITLE)
        return ""
    
    def scroll_to_rooms_section(self):
        """
        Scroll to rooms section
        """
        if self.is_element_visible(self.ROOMS_SECTION):
            self.scroll_to_element(self.ROOMS_SECTION)
    
    def scroll_to_contact_section(self):
        """
        Scroll to contact section
        """
        if self.is_element_visible(self.CONTACT_SECTION):
            self.scroll_to_element(self.CONTACT_SECTION)
    
    def get_room_cards_count(self):
        """
        Get number of room cards displayed
        """
        rooms = self.find_elements(self.ROOM_CARDS)
        return len(rooms)
    
    def click_first_room(self):
        """
        Click first room card
        """
        if self.is_element_visible(self.FIRST_ROOM):
            self.click_element(self.FIRST_ROOM)
    
    def is_contact_form_visible(self):
        """
        Check if contact form is visible
        """
        return self.is_element_visible(self.CONTACT_FORM)
