import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com/login')
        self.driver.maximize_window()
    
    def test_login(self):
        driver = self.driver

        # Filling the login form
        driver.find_element(By.NAME, 'username').send_keys('johndoe')
        driver.find_element(By.NAME, 'password').send_keys('password123')

        # Clicking the login button
        driver.find_element(By.XPATH, '//button[text()="Login"]').click()

        # Waiting for the page to load
        time.sleep(2)

        # Verifying successful login
        user_profile = driver.find_element(By.XPATH, "//a[@href='/profile']")
        self.assertIsNotNone(user_profile)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
