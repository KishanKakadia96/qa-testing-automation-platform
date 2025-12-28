import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from testing.api_automation.configs.config import config

class BasePage:
    """
    Base class for all page objects with common methods
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
    
    def find_element(self, locator):
        """
        Find element with explicit wait
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise
    
    def find_elements(self, locator):
        """
        Find multiple elements
        """
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            return []
    
    def click_element(self, locator):
        """
        Click element with explicit wait, uses JavaScript click as fallback
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            try:
                element = self.find_element(locator)
                self.driver.execute_script("arguments[0].click();", element)
            except:
                raise e
    
    def send_keys(self, locator, text):
        """
        Send keys to element
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise
    
    def get_element_text(self, locator):
        """
        Get text from element
        """
        try:
            element = self.find_element(locator)
            text = element.text
            return text
        except Exception as e:
            return ""
    
    def is_element_visible(self, locator, timeout=None):
        """
        Check if element is visible
        """
        try:
            wait_time = timeout or config.EXPLICIT_WAIT
            wait = WebDriverWait(self.driver, wait_time)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        """
        Scroll to element with offset to avoid fixed headers
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5)  # Wait for scroll animation to complete
    
    def navigate_to(self, url):
        """
        Navigate to URL
        """
        self.driver.get(url)