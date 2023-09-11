from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioCheckElements():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        time.sleep(3)
        bmwRadioButton = driver.find_element(By.ID, "bmwradio")
        bmwRadioButton.click()

        time.sleep(3)
        benzRadioButton = driver.find_element(By.ID, "benzradio")
        benzRadioButton.click()

        time.sleep(3)
        bmwCheckBox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckBox.click()

        time.sleep(3)
        benzCheckBox = driver.find_element(By.ID, "benzcheck")
        benzCheckBox.click()

        print("is bmw radio button selected? ", bmwRadioButton.is_selected())
        print("is benz radio button selected? ", benzRadioButton.is_selected())
        print("is bmw check box selected? ", bmwCheckBox.is_selected())
        print("is benz check box selected? ", benzCheckBox.is_selected())
        driver.close()

rc = RadioCheckElements()
rc.test()



