from pages.demoqa import DemoQa
import time


def test_size_window(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
