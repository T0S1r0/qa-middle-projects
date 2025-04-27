import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSearchFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com')
        self.driver.maximize_window()
    
    def test_search_functionality(self):
        driver = self.driver
        
        # Finding the search bar
        search_box = driver.find_element(By.NAME, 'search')

        # Entering a search term
        search_box.send_keys('laptop')
        search_box.submit()
        
        time.sleep(2)

        # Checking if there are any results on the page
        results = driver.find_elements(By.CSS_SELECTOR, '.product-item')
        self.assertGreater(len(results), 0, "Results not found for search term 'laptop'")
        
        # Verifying that the result contains the word "laptop"
        result_name = results[0].find_element(By.CSS_SELECTOR, '.product-title').text
        self.assertIn('laptop', result_name.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
