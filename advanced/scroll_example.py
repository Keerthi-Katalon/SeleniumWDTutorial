from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class WindowSize():
    def test(self):
        driver = webdriver.Chrome()
        baseURL = "https://www.letskodeit.com/practice"
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        #Scroll down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)

        #Scroll up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)

        #Scroll element into view
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")

        #Native way to scroll element into view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("location: ", location)
        driver.execute_script("window.scrollBy(0,-150);")



ws = WindowSize()
ws.test()
