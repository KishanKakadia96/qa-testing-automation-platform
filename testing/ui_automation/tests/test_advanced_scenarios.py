import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.booking_page import BookingPage
from pages.home_page import HomePage


@pytest.mark.smoke
class TestAdvancedScenarios:
    """Advanced test scenarios for UI automation"""
    
    def test_page_load_performance(self, driver):
        """Test page load time is acceptable"""
        start_time = time.time()
        page = HomePage(driver)
        page.open_home_page()
        load_time = time.time() - start_time
        
        assert load_time < 5, f"Page load time {load_time}s exceeds 5s threshold"
        assert page.is_home_page_loaded(), "Home page did not load properly"
    
    def test_multiple_form_submissions(self, driver):
        """Test submitting form multiple times"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        test_data = [
            ("John", "Doe", "john@test.com", "1234567890"),
            ("Jane", "Smith", "jane@test.com", "9876543210"),
            ("Bob", "Wilson", "bob@test.com", "5551234567"),
        ]
        
        for firstname, lastname, email, phone in test_data:
            page.fill_firstname(firstname)
            page.fill_lastname(lastname)
            page.fill_email(email)
            page.fill_phone(phone)
            
            assert page.get_firstname_value() == firstname
            driver.refresh()
            time.sleep(1)
    
    def test_form_field_tab_navigation(self, driver):
        """Test tab navigation between form fields"""
        
        page = BookingPage(driver)
        page.open_booking_page()
        
        # Focus on firstname field
        firstname_field = page.find_element(page.FIRSTNAME_INPUT)
        firstname_field.click()
        firstname_field.send_keys("John")
        
        # Tab to lastname
        firstname_field.send_keys(Keys.TAB)
        time.sleep(0.5)
        
        # Verify lastname is now focused
        active_element = driver.switch_to.active_element
        assert active_element.get_attribute('id') == 'lastname'
    
    def test_browser_back_forward_navigation(self, driver):
        """Test browser back and forward buttons"""
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_url = driver.current_url
        
        booking_page = BookingPage(driver)
        booking_page.open_booking_page()
        booking_url = driver.current_url
        
        # Go back
        driver.back()
        time.sleep(1)
        assert driver.current_url == home_url
        
        # Go forward
        driver.forward()
        time.sleep(1)
        assert driver.current_url == booking_url
    
    def test_page_refresh_clears_form(self, driver):
        """Test that page refresh clears form data"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        page.fill_firstname("John")
        page.fill_lastname("Doe")
        page.fill_email("john@test.com")
        
        # Verify data is present
        assert page.get_firstname_value() == "John"
        
        # Refresh page
        driver.refresh()
        time.sleep(1)
        
        # Verify form is cleared
        assert page.get_firstname_value() == ""
        assert page.get_lastname_value() == ""
    
    def test_window_resize_responsiveness(self, driver):
        """Test form remains functional after window resize"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        # Test at different window sizes
        sizes = [(1920, 1080), (1366, 768), (1024, 768)]
        
        for width, height in sizes:
            driver.set_window_size(width, height)
            time.sleep(0.5)
            
            assert page.is_firstname_visible()
            assert page.is_submit_button_visible()
            
            page.fill_firstname(f"Test_{width}")
            assert page.get_firstname_value() == f"Test_{width}"
            driver.refresh()
            time.sleep(0.5)
    
    def test_element_wait_strategies(self, driver):
        """Test different wait strategies for elements"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        # Explicit wait
        wait = WebDriverWait(driver, 10)
        firstname = wait.until(EC.presence_of_element_located(page.FIRSTNAME_INPUT))
        assert firstname.is_displayed()
        
        # Visibility wait
        submit_btn = wait.until(EC.visibility_of_element_located(page.SUBMIT_BUTTON))
        assert submit_btn.is_displayed()
        
        # Clickable wait
        clickable_btn = wait.until(EC.element_to_be_clickable(page.SUBMIT_BUTTON))
        assert clickable_btn.is_enabled()


@pytest.mark.regression
class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_rapid_field_updates(self, driver):
        """Test rapid updates to form fields"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        # Rapidly update firstname field
        names = ["A", "AB", "ABC", "ABCD", "ABCDE"]
        for name in names:
            page.fill_firstname(name)
            time.sleep(0.1)
        
        assert page.get_firstname_value() == "ABCDE"
    
    def test_special_characters_handling(self, driver):
        """Test form handles special characters"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        special_chars = "Test@#$%"
        page.fill_firstname(special_chars)
        
        # Field may sanitize or accept special chars
        # Just verify no crash occurs
        assert page.get_firstname_value() is not None
    
    def test_unicode_characters(self, driver):
        """Test form handles unicode characters"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        unicode_name = "José María"
        page.fill_firstname(unicode_name)
        
        # Verify unicode is handled
        assert page.get_firstname_value() == unicode_name
    
    def test_very_long_input_strings(self, driver):
        """Test form handles very long input strings"""
        page = BookingPage(driver)
        page.open_booking_page()
        
        long_string = "A" * 200
        page.fill_firstname(long_string)
        
        # Field may truncate or accept long strings
        value = page.get_firstname_value()
        assert value is not None
        assert len(value) <= 200
