from pages.demoqa import DemoQa
# from pages.elements_page import ElementsPage
from components.components import WebElement
# def test_go_to_page_elements(browser):
#     page_demo = DemoQa(browser)
#     elements_page = ElementsPage(browser)
#     page_demo.visit()
#     assert page_demo.equal_url()
#     page_demo.btn_elements.click()
#     assert elements_page.equal_url()


def test_check_text(browser):
    page_demo = DemoQa(browser)
    # elements_page = ElementsPage(browser)
    text_page = WebElement(browser)
    page_demo.visit()
    # assert
    # text_page.get_text()
    assert page_demo.text.exist()
