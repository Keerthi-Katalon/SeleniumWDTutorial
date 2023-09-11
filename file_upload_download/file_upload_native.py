from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# driver.maximize_window()
# baseURL = "https://www.plupload.com/examples"
# driver.get(baseURL)
# element = driver.find_element(By.XPATH, "//div[@id='uploader_buttons']/div/input")
# #element = driver.find_element(By.ID,"uploader_browse")
# time.sleep(3)
# element.send_keys("/Users/dsaxena/Downloads/pic.png")

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
baseURL = "https://imgbb.com/upload"
driver.get(baseURL)
#element = driver.find_element(By.XPATH, "//div[@id='uploader_buttons']/div/input")
element = driver.find_element(By.ID,"anywhere-upload-input")
#time.sleep(3)
element.send_keys("/Users/dsaxena/Downloads/pic.png")
