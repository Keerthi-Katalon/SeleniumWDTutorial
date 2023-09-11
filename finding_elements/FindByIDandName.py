#<input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindIdName():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByID = driver.find_element(By.ID,"displayed-text")
        if elementByID is not None:
            print("Element Found -> By ID")

        elementByName = driver.find_element(By.NAME, "show-hide")
        if elementByName is not None:
            print("Element Found -> By Name")

run_tests = FindIdName()
run_tests.test()
