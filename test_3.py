<<<<<<< HEAD
from page import *
=======
from test_1 import *
>>>>>>> 723a2ea (refactor test blocks, rename tests)


def test_main_page(driver):
    count_articles_number(driver)
    count_pages_number(driver)
<<<<<<< HEAD
=======


if __name__ == '__main__':
    driver_object = setup()

    try:
        test_main_page(driver_object)
    except NoSuchElementException as error:
        print(f'Test failed, {error}')

    tear_down(driver_object)
>>>>>>> 723a2ea (refactor test blocks, rename tests)
