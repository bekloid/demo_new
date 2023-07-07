from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.browser_tab import BrowserTab
from pages.allert_file import Allerts
import pytest
import time

def test_seo(browser):
    demo_qa = DemoQa(browser)
    demo_qa.visit()

    assert browser.title == "DEMOQA"


@pytest.mark.parametrize("pages", [Accordian, Allerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
