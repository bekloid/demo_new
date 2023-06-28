from pages.base_page import BasePage
from components.components import WebElement


class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_count = WebElement(driver, "div > div > div: nth - child(3) > div") # возможно, неверный локатор
