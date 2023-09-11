from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class WindowSize():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        #driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height: ", height)
        print("Width: ", width)

ws =WindowSize()
ws.test()