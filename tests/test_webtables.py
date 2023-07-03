import time

from pages.webtables import WebTables


def test_web_tables(browser):

    web_tables = WebTables(browser)
    assert not web_tables.block.exist()
    for i in range(3):
        web_tables.del_btn.click()

    time.sleep(2)
    assert web_tables.block.exist()
