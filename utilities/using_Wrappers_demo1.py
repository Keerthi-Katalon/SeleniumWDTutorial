from selenium import webdriver
from utilities.handyWrappers import HandyWrappers
import time

class UsingWrappers():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseURL)

        textField = hw.getElement("name")
        textField.send_keys("Text")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

uw = UsingWrappers()
uw.test()