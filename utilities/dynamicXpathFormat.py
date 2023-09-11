from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DynamicXpathTest():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        #Login to the practice page
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email_element = driver.find_element(By.ID, "email")
        email_element.send_keys("test@email.com")
        password_element = driver.find_element(By.ID,"login-password")
        password_element.send_keys("abcabc")
        driver.find_element(By.ID,"login").click()
        time.sleep(3)

        #goto Allcourses and search for one course
        driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href='/courses']").click()
        searchbox_element = driver.find_element(By.XPATH,"//form[@id='search']//input[@placeholder='Search Course']")
        searchbox_element.send_keys("JavaScript")
        time.sleep(3)
        driver.find_element(By.XPATH, "//form[@id='search']//i[contains(@class,'fa fa-search')]").click()
        time.sleep(3)

        #select course
        _course = "//div[@id='course-list']//h4[contains(text(),'{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")
        time.sleep(3)

        courseElement = driver.find_element(By.XPATH,_courseLocator)
        courseElement.click()
        time.sleep(3)

df = DynamicXpathTest()
df.test()





