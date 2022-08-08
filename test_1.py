<<<<<<< HEAD
from page import *

=======
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.WebDriver(executable_path="chromedriver")

driver.get("https://habr.com/ru/all/")

# Поиск поля поиска
search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
search_button = driver.find_element(*search_button_locator)
search_button.click()
time.sleep(1)

# вбить текст
search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
search_input = driver.find_element(*search_input_locator)
text_to_search = 'Selenium'
search_input.send_keys(text_to_search)

# нажать на иконку
search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
search_icon = driver.find_element(*search_icon_locator)
search_icon.click()
time.sleep(3)

# посчитать количество записей(20)
article_locator = By.TAG_NAME, 'article'
articles = driver.find_elements(*article_locator)
print(f'Number of articles is {len(articles)}')

# посчитать количество страниц(50)
last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
last_page_number = driver.find_element(*last_page_locator)
element_text = last_page_number.text
print(f'Number of pages is {element_text}')

<<<<<<<< HEAD:first_try.py
driver.quit()
========
>>>>>>> 723a2ea (refactor test blocks, rename tests)

def test_basic_search(driver):
    click_search_form(driver)

    type_text(driver, 'NFT')

    click_search_button(driver)

    count_articles_number(driver)

    count_pages_number(driver)
<<<<<<< HEAD
=======


def count_articles_number(driver):
    count_articles_count(driver)


def count_pages_number(driver):
    last_page_locator = By.XPATH, '(//*[@class="tm-pagination__page"])[last()]'
    last_page_number = driver.find_element(*last_page_locator)
    element_text = last_page_number.text
    print(f'Number of pages is {element_text}')


def count_articles_count(driver):
    article_locator = By.TAG_NAME, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is {len(articles)}')


def click_search_button(driver):
    search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(3)


def type_text(driver, text):
    search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
    search_input = driver.find_element(*search_input_locator)
    text_to_search = text
    search_input.send_keys(text_to_search)


def click_search_form(driver):
    search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(1)


if __name__ == '__main__':
    driver_object = setup()

    try:
        test_basic_search(driver_object)
    except NoSuchElementException as error:
        print(f'Test failed, reason: {error}')

    tear_down(driver_object)
>>>>>>>> 723a2ea (refactor test blocks, rename tests):test_1.py
>>>>>>> 723a2ea (refactor test blocks, rename tests)
