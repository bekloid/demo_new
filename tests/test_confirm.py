import time

from pages.allert_file import Allerts


def test_confirm(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.conf_btn.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.con_res.get_text() == "You selected Cancel"