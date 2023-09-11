from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropDownSelect():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        DropDownElement = driver.find_element(By.ID, "carselect")
        sel = Select(DropDownElement)

        sel.select_by_value('benz')
        print("select Benz by value ")
        time.sleep(2)

        sel.select_by_index("2")
        print("select Honda by index ")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("select BMW by visible text ")
        time.sleep(2)

        sel.select_by_index(2)
        print("select Honda by index ")

dd = DropDownSelect()
dd.test()