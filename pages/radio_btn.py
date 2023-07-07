from pages.base_page import BasePage
from components.components import WebElement


class RadioBtn(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        self.yes_btn = WebElement(driver, '#yesRadio')
        self.impressive_btn = WebElement(driver, '#impressiveRadio')
        self.conf_text = WebElement(driver, ' div:nth-child(2) > p > span')
        self.no_btn = WebElement(driver, "#noRadio")
        super().__init__(driver, self.base_url)
