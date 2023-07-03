from pages.base_page import BasePage
from components.components import WebElement


class Hkuapp(BasePage):

    def __init__(self, driver):

        self.base_url = "http://the-internet.herokuapp.com/"
        self.link = WebElement(driver, "//*[@id='content']/ul/li[2]/a", "xpath")
        super().__init__(driver, self.base_url)