import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com')
        self.driver.maximize_window()
    
    def test_add_to_cart(self):
        driver = self.driver

        # Navigating to the product page
        driver.find_element(By.XPATH, "//a[@href='/product/123']").click()
        
        time.sleep(2)
        
        # Clicking the "Add to Cart" button
        driver.find_element(By.ID, 'add-to-cart').click()

        # Navigating to the cart
        driver.find_element(By.ID, 'cart').click()
        
        time.sleep(2)

        # Verifying that the cart is not empty
        cart_items = driver.find_elements(By.CSS_SELECTOR, '.cart-item')
        self.assertGreater(len(cart_items), 0, "Cart is empty!")
        
        # Verifying that the item in the cart is the correct one
        cart_item_name = cart_items[0].find_element(By.CSS_SELECTOR, '.cart-item-title').text
        self.assertEqual(cart_item_name, 'Laptop XYZ')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
