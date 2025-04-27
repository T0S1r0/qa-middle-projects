import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestContactForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com/contact')
        self.driver.maximize_window()
    
    def test_contact_form_submission(self):
        driver = self.driver

        # Filling in the contact form
        driver.find_element(By.NAME, 'name').send_keys('John Doe')
        driver.find_element(By.NAME, 'email').send_keys('johndoe@example.com')
        driver.find_element(By.NAME, 'message').send_keys('This is a test message.')

        # Submitting the form
        driver.find_element(By.XPATH, '//button[text()="Send Message"]').click()

        # Waiting for the success message
        time.sleep(2)

        # Verifying that the success message is displayed
        success_message = driver.find_element(By.XPATH, "//div[@class='success-message']")
        self.assertIsNotNone(success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
