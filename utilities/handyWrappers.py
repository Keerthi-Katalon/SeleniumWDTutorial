from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self,driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        else:
            print("this locator type is not supported")
        return False

    def getElement(self,locator,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element is found")
        except:
            print("Element not found")
        return element

    def isElementPresent(self,locator,byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                print("ElementsList not found")
                return False
        except:
            print("Element not found")
            return False

    def elementsPresentCheck(self,locator,byType):
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                print("ElementsList found")
                return True
            else:
                print("ElementsList not found")
                return False
        except:
            print("ElementsList not found")
            return False