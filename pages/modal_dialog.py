from pages.base_page import BasePage
from components.components import WebElement


class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_count = WebElement(driver, "div:nth-child(3) > div > ul > li")
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.small_close = WebElement(driver, '#closeSmallModal')
        self.large_close = WebElement(driver, '#closeLargeModal')