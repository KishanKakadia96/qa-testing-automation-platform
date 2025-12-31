from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from testing.api_automation.configs.config import config
import os


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
        # Auto-enable headless mode in CI environment
        is_ci = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"
        is_headless = config.HEADLESS == "true" or is_ci
        
        if browser == "chrome":
            options = ChromeOptions()
            if is_headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(config.IMPLICIT_WAIT)
            return driver
            
        elif browser == "edge":
            options = EdgeOptions()
            if is_headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--inprivate")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.page_load_strategy = 'normal'
            
            driver = webdriver.Edge(options=options)
            driver.implicitly_wait(config.IMPLICIT_WAIT)
            driver.set_page_load_timeout(30)
            return driver
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    
    @staticmethod
    def quit_driver(driver):
        """Quit WebDriver safely"""
        if driver:
            driver.quit()