from pages.allert_file import Allerts
import time


def test_alert_text(browser):

    alert_page = Allerts(browser)
    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert().text =="You clicked a botton"
    alert_page.alert().accert()
    assert not alert_page.alert()

def test_confirm(browser):

    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.conf_btn.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.con_res.get_text() == "You selected Cancel"

def test_prompt(browser):
    alert_page = Allerts(browser)
    alert_page.visit()
    alert_page.alert_call_btn.click()
    time.sleep(2)
    alert_page.alert().send_keys("Anna")
    alert_page.alert().accert()
    assert alert_page.prm_res.get_text() == "You entered Anna"
    time.sleep(2)
