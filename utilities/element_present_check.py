from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handyWrappers import HandyWrappers
import time

class ElementPresentCheck():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        elementResult1 = hw.isElementPresent("//fieldset/input[@id='name']",By.XPATH)
        print(elementResult1)

        elementResult2 = hw.isElementPresent("displayed-text", By.ID)
        print(elementResult2)

        elementResult3 = hw.isElementPresent("namexx", By.ID)
        print(elementResult3)

uw = ElementPresentCheck()
uw.test()