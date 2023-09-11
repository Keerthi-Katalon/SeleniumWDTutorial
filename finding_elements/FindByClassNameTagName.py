#<input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByClassNameTagName():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByClassName = driver.find_element(By.CLASS_NAME,"inputs")
        if elementByClassName is not None:
            print("Element Found -> By ClassName")
            elementByClassName.send_keys("Testing")

#// input[ @ name = 'show-hide']
        elementByTagName = driver.find_element(By.TAG_NAME, "a")
        if elementByTagName is not None:
            print("Element Found -> By TagName:", elementByTagName.text)
        time.sleep(5)

run_tests = FindByClassNameTagName()
run_tests.test()
