from pages.base_page import BasePage
from components.components import WebElement


class AddRemEl(BasePage):

    def __init__(self, driver):

        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        self.add_el_btn = WebElement(driver, "#content > div > button")
        self.btn_del = WebElement(driver, 'div>#elements >button')
        super().__init__(driver, self.base_url)
