from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: ", parentHandle)

        # Find open window button and click it from the practice page
        openWindowbutton = driver.find_element(By.ID, "openwindow")
        openWindowbutton.click()
        time.sleep(2)

        # Find all handles, there should be two handles after clicking open window button
        handles = driver.window_handles

        # switch to window and search courses
        for handle in handles:
            print("handle: ", handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("switched to window:: ", handle)
                searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # swtich back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.XPATH,"//fieldset/input[@id='name']").send_keys("Test Successful")
        time.sleep(3)

sw = SwitchToWindow()
sw.test()