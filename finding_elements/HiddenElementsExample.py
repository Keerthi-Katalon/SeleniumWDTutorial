from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class HiddenElements():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        #Find the state of the text box
        textBoxElement = driver.find_element(By.ID, "displayed-text")
        textBoxState = textBoxElement.is_displayed()
        #Exception if not present in the DOM
        print("Text is visible? ", textBoxState)
        time.sleep(3)

        #click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()
        # find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? ", textBoxState)
        time.sleep(3)

        # click the show button
        driver.find_element(By.ID, "show-textbox").click()
        # find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? ", textBoxState)
        time.sleep(3)

        # Browser close
        driver.quit()

    def testExpedia(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        driver.find_element(By.XPATH, "//div[@id='multi-product-search-form-1']//a[@href='Flights']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='FlightSearchForm_ROUND_TRIP']//button[@data-stid='open-room-picker']").click()
        time.sleep(3)
        dropDownElement = driver.find_element(By.ID,"age-traveler_selector_children_age_selector-0")
        print("is the element found for the child age selector? ", dropDownElement)
        time.sleep(3)
        print("Element visible? ", dropDownElement.is_displayed())
        driver.quit()

he = HiddenElements()
he.test()
he.testExpedia()