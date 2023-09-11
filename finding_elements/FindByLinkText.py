#<input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByLinkText():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByLinkText = driver.find_element(By.LINK_TEXT,"HOME")
        if elementByLinkText is not None:
            print("Element Found -> By LinkText")

#// input[ @ name = 'show-hide']
        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if elementByPartialLinkText is not None:
            print("Element Found -> By PartialLinkText")

run_tests = FindByLinkText()
run_tests.test()
