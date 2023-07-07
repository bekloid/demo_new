from pages.demoqa import DemoQa
from components.components import WebElement
from pages.radio_btn import RadioBtn
import pytest

@pytest.mark.skip
def test_decor(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    assert demo_page.h5.check_count_element(6)
    for elements in demo_page.h5.find_element():
        assert elements.text != " "


@pytest.mark.skipif(True, reason='Потому что я могу !')
def test_radio_btn(browser):

    radio_btn = RadioBtn(browser)
    if radio_btn.code_status():
        pytest.skip(reason=f"Страница {radio_btn.base_url} недоступна")
    radio_btn.visit()

    radio_btn.yes_btn.click()
    assert radio_btn.conf_text.get_text() == "Yes"
    radio_btn.impressive_btn.click()
    assert radio_btn.conf_text.get_text() == "Impressive"
    assert 'disabled' in radio_btn.no_btn.get_by_type('class')
    assert radio_btn.code_status()
