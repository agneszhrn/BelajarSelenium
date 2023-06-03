import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from PageObject.locator import elem
from PageObject.data import inputan
# import HtmlTestRunner

class TestCart(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_add_cart(self): #test cases 1
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        driver.find_element(By.CSS_SELECTOR, elem.addCartBackpack).click()
        driver.find_element(By.CLASS_NAME, elem.shoppingCartLink).click()
        # validasi by url :
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/cart.html")
    
    def test_success_remove_add_cart(self): #test cases 2
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        driver.find_element(By.CSS_SELECTOR, elem.addCartBackpack).click()
        driver.find_element(By.CSS_SELECTOR, elem.removeCartBackpack).click()
        # validasi by button cart :
        button = driver.find_element(By.CSS_SELECTOR, elem.addCartBackpack).text
        self.assertIn(inputan.addToCart, button)

    def test_continue_shopping(self): #test cases 3
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        driver.find_element(By.CSS_SELECTOR, elem.addCartBackpack).click()
        driver.find_element(By.CLASS_NAME, elem.shoppingCartLink).click()
        driver.find_element(By.ID, elem.continueShopButton).click()
        # validasi by url :
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/inventory.html")

if __name__ == '__main__':
    unittest.main()

# if want to make a report 
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report'))