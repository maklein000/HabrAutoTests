def test_pagination_to_last_page(page):
    page.search('NFT')

    page.go_to_last_page()

    expected = 'https://habr.com/ru/search/page19/?q=NFT&target_type=posts&order=relevance'
    actual = page.current_url
    assert actual == expected
