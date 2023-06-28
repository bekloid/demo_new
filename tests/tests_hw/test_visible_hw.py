from pages.accordian import Accordian
import time


def test_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    accordian_page.text_header.click()
    time.sleep(2)
    assert not accordian_page.text_field.visible()


def test_visible_accordion_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert not accordian_page.hidden_text1.visible()
    assert not accordian_page.hidden_text2.visible()
    assert not accordian_page.hidden_text3.visible()
