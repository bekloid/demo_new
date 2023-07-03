from components.components import WebElement
from pages.base_page import BasePage

class Allerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.alertButton = WebElement (driver, "#alertButton")
        self.conf_btn = WebElement(driver,"#confirmButton")
        self.con_res = WebElement(driver, "#confirmREsult")
        self.alert_call_btn = WebElement(driver, "#promtButton")
        self.prm_res = WebElement(driver, "#promptResult")
