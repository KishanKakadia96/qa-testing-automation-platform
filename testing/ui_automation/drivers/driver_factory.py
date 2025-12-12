from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from testing.api_automation.configs.config import config


class DriverFactory:
    """
    Factory class to create WebDriver instances based on configuration.
    """
    
    @staticmethod
    def create_driver(browser: str = None):
        """
        Create and return WebDriver instance
        """
        browser = browser or config.BROWSER
        
        if browser == "chrome":
            options = ChromeOptions()
            if config.HEADLESS == "true":
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(config.IMPLICIT_WAIT)
            return driver
            
        elif browser == "edge":
            options = EdgeOptions()
            if config.HEADLESS == "true":
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--inprivate")
            options.add_argument("--disable-blink-features=AutomationControlled")
            
            driver = webdriver.Edge(options=options)
            driver.implicitly_wait(config.IMPLICIT_WAIT)
            return driver
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    
    @staticmethod
    def quit_driver(driver):
        """Quit WebDriver safely"""
        if driver:
            driver.quit()