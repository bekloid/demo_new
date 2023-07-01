from pages.form_page import FormPage
import time


def test_login_form_validate(browser):

    form_page = FormPage(browser)
    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('pattern') == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    time.sleep(3)
    form_page.btn_submit.click()
    for element in form_page.user_form.find_elements():
        assert element.text == "was-validated"

    #assert form_page.user_form.get_by_type() == "was-validated"