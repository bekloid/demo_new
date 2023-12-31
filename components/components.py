from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement():
    def __init__(self, driver, locator=""):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def visible(self):
        return self.find_element().is_displayed()

    def exist(self):

        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # def get_text(self):
    #     if self.find_element().text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.":
    #        return str(self.find_element().text)

    def get_text(self):
        return str(self.find_element().text)

    def check_count_element(self, count: int) -> bool:
        return len(self.find_elements()) == count

    def send_keys(self, value):
        self.find_element().send_keys(value)
