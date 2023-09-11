from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from utilities.handyWrappers import HandyWrappers
from waittypes.Explicit_wait_type import ExplicitWaitType

class ExplicitWaitdemo2():

    def test(self):
        baseURL = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="//a[@href='/login']", locatorType="xpath")
        element.click()

        time.sleep(3)
        driver.quit()

ew = ExplicitWaitdemo2()
ew.test()