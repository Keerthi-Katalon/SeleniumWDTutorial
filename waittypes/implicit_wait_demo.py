from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        # Login to the practice page
        loginlink = driver.find_element(By.XPATH, "//a[@href='/login']")
        loginlink.click()

        email_element = driver.find_element(By.ID, "email")
        email_element.send_keys("test@email.com")

        password_element = driver.find_element(By.ID, "login-password")
        password_element.send_keys("abcabc")

        time.sleep(3)

iw = ImplicitWaitDemo()
iw.test()