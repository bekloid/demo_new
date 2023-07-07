from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        self.btn_submit = WebElement(driver, "#submit")
        self.email = WebElement(driver, "#userEmail")
        self.crnt_add = WebElement(driver, "#currentAddress")
        self.out_name = WebElement(driver,"p#name.mb-1")
        self.out_add = WebElement(driver,"p#currentAddress.mb-1")

        self.name = WebElement(driver, "#userName")
        super().__init__(driver, self.base_url)
