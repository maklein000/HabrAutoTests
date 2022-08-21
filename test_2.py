from page import *


def test_empty_search(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('kkgkgk')

    page.count_articles_number()

    page.get_empty_page_text()
