<<<<<<< HEAD
from page import *
=======
from test_1 import *
>>>>>>> 723a2ea (refactor test blocks, rename tests)


def test_empty_search(driver):
    click_search_form(driver)

    type_text(driver, 'kkgkgk')

    click_search_button(driver)

    count_articles_number(driver)

    check_empty_page_text(driver)
<<<<<<< HEAD
=======


def check_empty_page_text(driver):
    # проверяем текст
    empty_res_locator = By.XPATH, '//*[@data-test-id="empty-placeholder-text"]'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')


if __name__ == '__main__':
    driver_object = setup()
    try:
        test_empty_search(driver_object)
    except NoSuchElementException as error:
        print(f'Test failed, {error}')

    tear_down(driver_object)
>>>>>>> 723a2ea (refactor test blocks, rename tests)
