import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service

class RunChromeTests():

    def test(self):
        #old syntax
        #chrome_service = ChromeService(executable_path="/Users/dsaxena/PycharmProjects/SeleniumWDTutorial/drivers/chromedriver")
        #new syntax
        #service = Service(executable_path="/Users/dsaxena/PycharmProjects/SeleniumWDTutorial/drivers/chromedriver")
        #Instantiate browser
        driver = webdriver.Chrome()
        #open provided URL
        driver.get("https://www.letskodeit.com")
        time.sleep(5)

run_tests = RunChromeTests()
run_tests.test()