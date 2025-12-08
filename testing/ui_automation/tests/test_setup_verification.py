from pages.booking_page import BookingPage

class TestSetupVerification:
    """Verify UI automation setup is working"""
    
    def test_driver_setup(self, driver):
        """Test 1: Verify WebDriver is created"""
        assert driver is not None
        print(" WebDriver created successfully")
    
    def test_navigate_to_website(self, driver):
        """Test 2: Verify navigation to website"""
        from testing.api_automation.configs.config import config
        driver.get(config.BASE_URL)
        assert config.BASE_URL in driver.current_url
        print(f"Successfully navigated to: {driver.current_url}")
    
    def test_booking_page_object(self, driver):
        """Test 3: Verify BookingPage object creation"""
        booking_page = BookingPage(driver)
        booking_page.open_booking_page()
        assert driver.current_url is not None
        print("BookingPage object created successfully")
    
    def test_page_title(self, driver):
        """Test 4: Verify page loads and has title"""
        from testing.api_automation.configs.config import config
        driver.get(config.BASE_URL)
        title = driver.title
        assert title is not None
        print(f"Page title: {title}")
