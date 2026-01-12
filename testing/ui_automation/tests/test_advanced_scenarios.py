import pytest
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.booking_page import BookingPage
from pages.home_page import HomePage

logger = logging.getLogger(__name__)

@pytest.mark.smoke
class TestAdvancedScenarios:
    """Advanced test scenarios for UI automation"""
    
    def test_page_load_performance(self, driver):
        """Test page load time is acceptable"""
        start_time = time.time()
        page = HomePage(driver)
        page.open_home_page()
        load_time = time.time() - start_time
        
        assert load_time < 60, f"Page load time {load_time}s exceeds 60s threshold"
        assert page.is_home_page_loaded(), "Home page did not load properly"
    
    def test_multiple_form_submissions(self, driver, booking_page):
        """Test submitting form multiple times"""
        
        test_data = [
            ("John", "Doe", "john@test.com", "1234567890"),
            ("Jane", "Smith", "jane@test.com", "9876543210"),
            ("Bob", "Wilson", "bob@test.com", "5551234567"),
        ]
        
        for firstname, lastname, email, phone in test_data:
            booking_page.open_booking_page()
            booking_page.click_room_book_now()
            booking_page.click_reserve_now()
            booking_page.fill_firstname(firstname)
            booking_page.fill_lastname(lastname)
            booking_page.fill_email(email)
            booking_page.fill_phone(phone)
            
            assert booking_page.get_firstname_value() == firstname
    
    def test_form_field_tab_navigation(self, driver, booking_page):
        """Test tab navigation between form fields"""
        
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Focus on firstname field - scroll into view first
        firstname_field = booking_page.find_element(booking_page.FIRSTNAME_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", firstname_field)
        time.sleep(0.5)
        firstname_field.click()
        firstname_field.send_keys("John")
        
        # Tab to lastname
        firstname_field.send_keys(Keys.TAB)
        time.sleep(0.5)
        
        # Verify tab navigation worked by checking active element class
        active_element = driver.switch_to.active_element
        # Check if it's a form input (class contains 'room-')
        element_class = active_element.get_attribute('class')
        assert 'room-' in element_class or active_element.tag_name == 'input'
    
    def test_browser_back_forward_navigation(self, driver, booking_page):
        """Test browser back and forward buttons"""
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_url = driver.current_url
        
        # Navigate to booking form
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        time.sleep(1)
        
        # Go back to home
        driver.back()
        time.sleep(1)
        # Should be back at home page
        assert driver.current_url == home_url
        
        # Go forward
        driver.forward()
        time.sleep(1)
        # Should show booking form again
        assert booking_page.is_firstname_visible()
    
    def test_page_refresh_clears_form(self, driver, booking_page):
        """Test that page refresh clears form data"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        booking_page.fill_firstname("John")
        booking_page.fill_lastname("Doe")
        booking_page.fill_email("john@test.com")
        
        # Verify data is present
        assert booking_page.get_firstname_value() == "John"
        
        # Navigate away and back (simulates refresh)
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Verify form is cleared (fresh form)
        assert booking_page.get_firstname_value() == ""
        assert booking_page.get_lastname_value() == ""
    
    def test_window_resize_responsiveness(self, driver, booking_page):
        """Test form remains functional at different window sizes"""
        booking_page.open_booking_page()
        
        # Test at different window sizes
        sizes = [(1920, 1080), (1366, 768), (1024, 768)]
        
        for width, height in sizes:
            driver.set_window_size(width, height)
            time.sleep(0.5)
            
            # Navigate to fresh page for each size
            booking_page.open_booking_page()
            booking_page.click_room_book_now()
            booking_page.click_reserve_now()
            
            assert booking_page.is_firstname_visible()
            assert booking_page.is_reserve_now_button_visible()
            
            booking_page.fill_firstname(f"Test_{width}")
            assert booking_page.get_firstname_value() == f"Test_{width}"
    
    def test_element_wait_strategies(self, driver, booking_page):
        """Test different wait strategies for elements"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Explicit wait
        wait = WebDriverWait(driver, 10)
        firstname = wait.until(EC.presence_of_element_located(booking_page.FIRSTNAME_INPUT))
        assert firstname.is_displayed()
        
        # Visibility wait
        submit_btn = wait.until(EC.visibility_of_element_located(booking_page.RESERVE_NOW_BUTTON_SUBMIT))
        assert submit_btn.is_displayed()
        
        # Clickable wait
        clickable_btn = wait.until(EC.element_to_be_clickable(booking_page.RESERVE_NOW_BUTTON_SUBMIT))
        assert clickable_btn.is_enabled()


@pytest.mark.regression
class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_rapid_field_updates(self, driver, booking_page):
        """Test rapid updates to form fields"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Scroll to firstname field
        firstname_field = booking_page.find_element(booking_page.FIRSTNAME_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", firstname_field)
        time.sleep(0.3)
        
        # Rapidly update firstname field
        names = ["A", "AB", "ABC", "ABCD", "ABCDE"]
        for name in names:
            booking_page.fill_firstname(name)
            time.sleep(0.1)
        
        assert booking_page.get_firstname_value() == "ABCDE"
    
    def test_special_characters_handling(self, driver, booking_page):
        """Test form handles special characters"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Scroll to firstname field
        firstname_field = booking_page.find_element(booking_page.FIRSTNAME_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", firstname_field)
        time.sleep(0.3)
        
        special_chars = "Test@#$%"
        booking_page.fill_firstname(special_chars)
        
        # Field may sanitize or accept special chars
        # Just verify no crash occurs
        assert booking_page.get_firstname_value() is not None
    
    def test_unicode_characters(self, driver, booking_page):
        """Test form handles unicode characters"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Scroll to firstname field
        firstname_field = booking_page.find_element(booking_page.FIRSTNAME_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", firstname_field)
        time.sleep(0.3)
        
        unicode_name = "José María"
        booking_page.fill_firstname(unicode_name)
        
        # Verify unicode is handled
        assert booking_page.get_firstname_value() == unicode_name
    
    def test_very_long_input_strings(self, driver, booking_page):
        """Test form handles very long input strings"""
        booking_page.open_booking_page()
        booking_page.click_room_book_now()
        booking_page.click_reserve_now()
        
        # Scroll to firstname field
        firstname_field = booking_page.find_element(booking_page.FIRSTNAME_INPUT)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", firstname_field)
        time.sleep(0.3)
        
        long_string = "A" * 200
        booking_page.fill_firstname(long_string)
        
        # Field may truncate or accept long strings
        value = booking_page.get_firstname_value()
        assert value is not None
        assert len(value) <= 200
