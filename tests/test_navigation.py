from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    page_demo = DemoQa(browser)
    page_demo.visit()
    elements_page = ElementsPage(browser)
    page_demo.btn_elements.click()
    elements_page.refresh() # чтобы понимать от какой страницы вызывается, для понятности кода, так писать всегда
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()
