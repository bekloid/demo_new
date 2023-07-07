
from pages.demoqa import DemoQa
from pages.accordian import Accordian
from pages.browser_tab import BrowserTab
from pages.allert_file import Allerts
import pytest
import time


@pytest.mark.parametrize('pages', [Accordian, Allerts, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):

    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute("name") =="viewport"