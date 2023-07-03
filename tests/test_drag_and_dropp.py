from pages.droppable import Droppable
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    drag_and_drop = Droppable(browser)
    drag_and_drop.visit()
    action_chains = ActionChains(browser)
    assert action_chains.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop_by_offset(drag_and_drop.find_element(), 700,468).perform()
    assert action_chains.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
