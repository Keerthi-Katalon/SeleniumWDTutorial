from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class TakeScreenshots():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        #goto login page
        loginlink = driver.find_element(By.XPATH, "//a[@href='/login']")
        loginlink.click()

        # enter username
        email_element = driver.find_element(By.ID, "email")
        email_element.send_keys("test@email.com")

        #enter wrong password
        password_element = driver.find_element(By.ID, "login-password")
        password_element.send_keys("abcabc1")

        #click on login
        driver.find_element(By.ID, "login").click()
        time.sleep(5)
        self.take_scrnshot(driver)

    def take_scrnshot(self,driver):
        """
        Takes screenshot of the current open page
        :param driver:
        :return: nothing
        """
        fileName = str(round(time.time()) * 1000) + ".png"
        scrnshot_dir = "/Users/dsaxena/Desktop/"
        destinationFileName = scrnshot_dir + fileName
        try:
            driver.save_screenshot(destinationFileName)
            print("screenshot saved to the directory: ", destinationFileName)
        except NotADirectoryError:
            print("directory issue")

ts = TakeScreenshots()
ts.test()






