
from pages.demoqa import DemoQa


def test_link(browser):

    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.icon.click()
    assert demo_page.equal_url()
    assert demo_page.icon.exist() #зайти на страницу, проверить иконку

    # browser.get("https://demoqa.com/")
    # link = browser.find_element(By.CSS_SELECTOR, '#app > header >a')
    # if link is None:
    #     print("Элемент не найден")
    # else:
    #     print("Элемент найден")


