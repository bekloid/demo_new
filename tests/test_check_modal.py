import pytest

from pages.demoqa import DemoQa
from pages.modal_dialog import ModalDialog

#@pytest.mark.skipif(True, reson = "страница недоступна")
def test_navigation_modal(browser):

    modal_dialog = ModalDialog(browser)
    # if modal_dialog.code_status():
    #     pytest.skip(reason=f"Страница {modal_dialog.base_url} недоступна")

    modal_dialog.visit()
    assert modal_dialog.small_modal.exist()
    assert modal_dialog.large_modal.exist()
    modal_dialog.small_modal.click()
    assert modal_dialog.small_close.exist()
    modal_dialog.alert().accept()
    assert modal_dialog.large_close.exist()
    modal_dialog.large_modal.click()
    modal_dialog.alert().accept()

