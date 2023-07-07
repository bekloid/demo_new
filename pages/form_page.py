from pages.base_page import BasePage
from pages.elements_page import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        self.gender_radio_1 = WebElement(driver, "#gender-radio-1")
        self.user_number = WebElement(driver, "#userNumber")
        self.btn_submit = WebElement(driver, "#submit")
        self.btn_state = WebElement(driver,'#state')
        self.modal_dialog = WebElement(driver, "body>div.fade.modal.show>div")
        self.btn_close_modal = WebElement(driver, "#closeLargeModal")
        self.hobbies_btn = WebElement(driver,"#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label")
        self.crnt_address = WebElement(driver, "#currentAddress")
        self.user_form = WebElement(driver,'#userForm')
        self.btn_NCR = WebElement(driver, '//*[contains(text(), "NCR")]', "xpath")
        self.inp_state = WebElement(driver, "#react-select-3-input")
