from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.block = WebElement(driver, "div.rt-noData")
        self.del_btn = WebElement(driver, '[title="Delete"]')
        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.pen_btn = WebElement(driver, '#edit-record-1') #кнопок несколько    .mr-2
        self.submit_btn = WebElement(driver, '#submit')
        self.frst_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.u_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.reg_form = WebElement(driver, 'div.fade.modal.show > div > div')
        self.new_line_edit_btn = WebElement(driver, '#edit-record-4 > svg')
        self.new_strip = WebElement(driver, 'div.rt-table > div.rt-tbody > div:nth-child(4)')
        self. del_str_btn = WebElement(driver, '#delete-record-4 > svg > path')
        self.prev_btn = WebElement(driver, 'div.-previous > button')
        self.next_btn = WebElement(driver, "div.-next > button")
