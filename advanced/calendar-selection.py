#<input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class CalendarSelection():

    def test(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        #click flights tab

        driver.find_element(By.XPATH, "//div[@id='multi-product-search-form-1']//li[@role='presentation']/a[@href='Flights']").click()
        time.sleep(5)

        #Find departing field
        departingDate = driver.find_element(By.ID,"date_form_field-btn")
        time.sleep(5)

        #click departing field
        departingDate.click()
        time.sleep(5)

        #Find the date to be selected
        datetobeSelected = driver.find_element(By.XPATH,
                                               "//div[@class='uitk-date-picker-month'][position()=1]//button[@data-day='30']")
        time.sleep(5)
        #click the date
        datetobeSelected.click()

        time.sleep(3)
        #driver.quit()



run_tests = CalendarSelection()
run_tests.test()
