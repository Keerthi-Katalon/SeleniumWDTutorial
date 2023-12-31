from traceback import print_stack
from utilities.handyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def waitForElement(self,locator,locatorType="id",timeout=10,pollFrequency=0.5):
        element = None
        byType = self.hw.getByType(locatorType)

        try:
            print("Waiting for maximum:: " + str(timeout) + "::seconds for elements to be visible")
            wait = WebDriverWait(self.driver, timeout= timeout, poll_frequency= pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element