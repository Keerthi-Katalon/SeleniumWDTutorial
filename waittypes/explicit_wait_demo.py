from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        #driver.get(baseURL)
        driver.implicitly_wait(5)
        driver.execute_script("window.location = 'https://www.letskodeit.com/practice';")
        driver.find_element(By.XPATH, "//a[@href='/login']").click()

        wait = WebDriverWait(driver, timeout=10,poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/login']")))
        element.click()

        time.sleep(3)
        driver.quit()

ew = ExplicitWaitDemo()
ew.test()