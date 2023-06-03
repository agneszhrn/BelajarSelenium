import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait   
import baseLogin
from PageObject.locator import elem
from PageObject.data import inputan

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #test cases 1
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        # validasi by url :
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/inventory.html")
    
    def test_success_login2(self): #test cases 2
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.validUser2)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by url :
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/inventory.html")

    def test_success_login3(self): #test cases 3
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.validUser3)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by url :
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/inventory.html")

    def test_success_login4(self): #test cases 4
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.validUser4)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by url :
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/inventory.html")

    def test_login_empty(self): #test cases 5
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by error message :
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputan.reqUsername, error_message)
        
    def test_failed_login_empty_username(self): #test cases 6
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by error message :
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputan.reqUsername, error_message)

    def test_failed_login_empty_pass(self): #test cases 7
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by error message :
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputan.reqPass, error_message)

    def test_failed_login_invalid_userandpass(self): #test cases 8
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.invalidUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.invalidPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by error message :
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputan.reqValidUsernameandPassword, error_message)

    def test_failed_login_invalid_username(self): #test cases 9
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.invalidUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by error message :
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputan.reqValidUsernameandPassword, error_message)

    def test_failed_login_invalid_pass(self): #test cases 10
        driver = self.browser
        # driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.invalidPass)
        driver.find_element(By.NAME, elem.loginButton).click()
        # validasi by error message :
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text
        self.assertIn(inputan.reqValidUsernameandPassword, error_message)

if __name__ == '__main__':
    unittest.main()