from pages.modal_dialog import ModalDialog
from pages.demoqa import DemoQa
from pages.base_page import BasePage


def test_modal_elements(browser):
    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()
    assert modal_dialog.btn_count.check_count_element(5) #не срабатывает тест. Возможно, неверный локатор


def test_navigation_modal(browser):
    modal_dialog = ModalDialog(browser)
    page_demo = DemoQa(browser)
    modal_dialog.visit()
    modal_dialog.refresh()
    page_demo.icon.click()
    browser.back()
    browser.set_window_size(width=900, height=400)
    browser.forward()
    assert page_demo.equal_url()
    assert browser.title == "DEMOQA"
    browser.set_window_size(width=1000, height=1000)

