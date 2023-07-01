from pages.text_box import TextBox
import time


def test_text_box(browser):

    text_box = TextBox(browser)
    value_name = 'Hi'
    value_crnt_add = 'Saint-P'
    text_box.visit()
    text_box.name.send_keys(value_name)
    text_box.crnt_add.send_keys(value_crnt_add)
    time.sleep(2)

    text_box.btn_submit.click()
    assert text_box.out_name.get_text() == 'Name:'+ value_name # этот костыль работает
    assert text_box.out_add.get_text() == "Current Address :" + value_crnt_add # это нет(((
 # как правильно провести проверку текста?


