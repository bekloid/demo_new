
from pages.base_page import BasePage
from pages.elements_page import WebElement
import pytest

class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        self.text_field = WebElement(driver,"#section1Content > p ")
        self.text_header = WebElement(driver,"#section1Heading")
        self.hidden_text1 = WebElement(driver,'#section2Content > p:nth-child(1)')
        self.hidden_text2 = WebElement(driver,'#section2Content > p:nth-child(2)')
        self.hidden_text3 = WebElement(driver,'#section3Content > p')

        super().__init__(driver, self.base_url)