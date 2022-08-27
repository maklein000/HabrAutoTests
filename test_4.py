from page import *


def test_pagination_to_last_page(driver):
    page = MainPage(driver)
    page.open()

    page = page.click_search()

    page.search('NFT')

    page.go_to_last_page()

    expected = 'https://habr.com/ru/search/page19/?q=NFT%20&target_type=posts&order=relevance'
    actual = page.current_url

    assert actual == expected
