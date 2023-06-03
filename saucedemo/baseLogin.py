import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.data import inputan

def test_success_login(driver): #test cases 2
    driver.get(inputan.baseUrl)
    driver.find_element(By.ID, elem.username).send_keys(inputan.validUser)
    driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
    driver.find_element(By.NAME, elem.loginButton).click()
