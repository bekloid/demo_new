from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    page_demo = DemoQa(browser)
    elements_page = ElementsPage(browser)
    page_demo.visit()
    assert page_demo.equal_url()
    page_demo.btn_elements.click()
    assert elements_page.equal_url()

