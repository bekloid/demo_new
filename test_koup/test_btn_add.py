from pages.herokuapp import Hkuapp
from pages.add_remo_el import AddRemEl


def test_btn_add(browser):

    hkuapp = Hkuapp(browser)
    ad_rem_el = AddRemEl(browser)
    hkuapp.visit()
    assert hkuapp.link.exist()
    hkuapp.link.click()
    assert ad_rem_el.equal_url()

    assert ad_rem_el.add_el_btn.exist()
    assert ad_rem_el.add_el_btn.get_dom_attribute('onclick') == "addElement()"

    for i in range(4):
        ad_rem_el.add_el_btn.click()

    assert ad_rem_el.btn_del.check_count_element(4)
    for element in ad_rem_el.btn_del.find_elements():
        assert element.text == "Delete"

    while ad_rem_el.btn_del.exist():
        ad_rem_el.btn_del.click()
    assert not ad_rem_el.btn_del.exist()
