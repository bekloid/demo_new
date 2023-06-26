from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        # self.center_text = WebElement(driver, ".row>div:nth-child(2)")
        self.text_please = WebElement(driver, "div.col-12.mt-4.col-md-6")
        self.text_element = WebElement(driver, "div>.main-header")
        self.btn_first = WebElement(driver, "div:nth-child(1) > span > div")
        self.btn_textbox = WebElement(driver, "div:nth-child(1)>div>ul>#item-0>span")
        self.btn_first_checkbox = WebElement(driver, "div:nth-child(1)>div>ul>#item-1>span")

    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     return False