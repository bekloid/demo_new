import time

from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    drag_and_drop = Droppable(browser)
    drag_and_drop.visit()
    action_chains = ActionChains(browser)
    assert drag_and_drop.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(drag_and_drop.drag.find_element(), drag_and_drop.drop.find_element()).perform()
    time.sleep(2)
    assert drag_and_drop.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(2)

    action_chains.drag_and_drop_by_offset(drag_and_drop.drag.find_element(), 700,468).perform()
    time.sleep(3)
    assert drag_and_drop.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
