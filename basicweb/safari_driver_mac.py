import time

from selenium import webdriver

class SafariDriverMac():

    def test(self):
        # instantiate safari browser command
        driver = webdriver.Safari()
        # open the URL provided
        driver.get("https://www.letskodeit.com/")
        time.sleep(3)

sf = SafariDriverMac()
sf.test()
