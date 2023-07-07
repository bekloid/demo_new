from selenium.webdriver import Keys

from pages.form_page import FormPage
import time
from components.components import WebElement
from pages.modal_dialog import ModalDialog


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testerovich")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("9992223344")

    assert form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.btn_state.click_force()
    form_page.hobbies_btn.click()
    form_page.crnt_address.send_keys("So many signs")
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


def test_new_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.btn_state.scroll_to_element()
    time.sleep(2)
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)