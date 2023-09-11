import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService

class RunFFTests():

    def test(self):
        #ff_service = FFService(executable_path="/Users/dsaxena/PycharmProjects/SeleniumWDTutorial/drivers/geckodriver")
        #Instantiate browser
        driver = webdriver.Firefox()
        #open provided URL
        driver.get("https://www.letskodeit.com")
        time.sleep(5)
        driver.close()

run_tests = RunFFTests()
run_tests.test()