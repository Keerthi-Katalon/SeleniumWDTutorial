from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class javaScriptExec():
    def test(self):
        #baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get(baseURL)
        driver.execute_script("window.location= 'https://www.letskodeit.com/practice';")
        driver.implicitly_wait(10)

        #findign element using java script
        element = driver.execute_script("return document.getElementById('name');")
        time.sleep(3)
        element.send_keys("Test")
        time.sleep(4)

jse = javaScriptExec()
jse.test()