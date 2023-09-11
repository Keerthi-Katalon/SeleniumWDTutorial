#<input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindXpathCSS():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByXpath = driver.find_element(By.XPATH,"// input[ @ id = 'displayed-text']")
        if elementByXpath is not None:
            print("Element Found -> By XPATH")
            #// input[ @ name = 'show-hide']

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSS is not None:
            print("Element Found -> By CSS Selector")

run_tests = FindXpathCSS()
run_tests.test()
