from pages.text_box import TextBox
from components.components import WebElement




def test_placeholder(browser):
    tex_box = TextBox(browser)
    tex_box.visit()
    assert tex_box.name.get_dom_attribute("placeholder") == "Full Name"