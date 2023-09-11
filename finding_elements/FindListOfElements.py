#<input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListOfElements():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        #elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        elementListByClassName = driver.find_elements_by_class_name("inputs")

        length1 = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Size of the list is: ", length1)

        elementListByTagName = driver.find_elements(By.TAG_NAME, "h1")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("size of the list is: ", length2)

run_tests = FindListOfElements()
run_tests.test()
