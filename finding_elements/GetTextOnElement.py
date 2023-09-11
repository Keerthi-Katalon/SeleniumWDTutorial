from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class GetText():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        OpenTabElement = driver.find_element(By.ID, "opentab")
        OpenTabElementText = OpenTabElement.text
        EnterNameElement = driver.find_element(By.XPATH, "//fieldset/input[@id='name']")
        LabelElementInnerText = driver.find_element(By.XPATH,"//div[@id='radio-btn-example']/fieldset/label[2]")
        EnterNameElement_attr_value1 = EnterNameElement.get_attribute("placeholder")
        EnterNameElement_attr_value2 = EnterNameElement.get_attribute("class")
        EnterNameElement_attr_value3 = LabelElementInnerText.get_attribute("innerText")

        print("Open Tab Element Text is: ", OpenTabElementText)
        time.sleep(1)

        print("Name element's Attribute value for placeholder is: ", EnterNameElement_attr_value1)
        time.sleep(2)

        print("Name element's Attribute value for class is: ", EnterNameElement_attr_value2)
        time.sleep(2)

        print("Name element's Attribute value for inner text is: ", EnterNameElement_attr_value3)
        time.sleep(2)

        driver.quit()

gt = GetText()
gt.test()


