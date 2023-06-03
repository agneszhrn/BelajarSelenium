import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from PageObject.locator import elem
from PageObject.data import inputan

class TestLogout(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_logout(self): #test cases 1
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        driver.find_element(By.ID, elem.burgerMenuButton).click()
        driver.implicitly_wait(10)
        driver.find_element(By.ID, elem.logoutButton).click()
        # # validasi by url :
        # currentUrl = driver.current_url
        # self.assertIn (currentUrl, inputan.baseUrl)

        # # validasi by button login :
        # button = driver.find_element(By.NAME, elem.loginButton).text
        # self.assertIn(inputan.login, button)

if __name__ == '__main__':
    unittest.main()