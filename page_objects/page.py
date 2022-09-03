import time
from locators.locators import *

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class HabrBase:
    url = 'https://habr.com/ru/all/'

    def __init__(self, webdriver):
        self.webdriver = webdriver

    @property
    def last_page_number(self):
        return self.webdriver.find_element(*last_page_locator)

    def count_pages_number(self):
        return int(self.last_page_number.text)

    def go_to_last_page(self):
        self.last_page_number.click()

    @property
    def articles(self):
        return self.webdriver.find_elements(*article_locator)

    def count_articles_number(self):
        return len(self.articles)

    @property
    def current_url(self):
        return self.webdriver.current_url

    def open(self):
        self.webdriver.get(self.url)


class MainPage(HabrBase):
    url = 'https://habr.com/ru/all/'

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_button_locator)

    def click_search(self):
        time.sleep(1)
        self.search_button.click()

        time.sleep(3)

        return SearchPage(self.webdriver)


class SearchPage(HabrBase):
    url = 'https://habr.com/ru/search/'

    @property
    def search_input(self):
        return self.webdriver.find_element(*search_input_locator)

    @property
    def search_button(self):
        return self.webdriver.find_element(*search_icon_locator)

    def search(self, search_text):
        self.search_input.send_keys(search_text)
        self.search_button.click()

        wait = WebDriverWait(self.webdriver, 3)
        wait.until(
            any_of(
                presence_of_element_located(empty_res_locator),
                presence_of_element_located(article_locator)
            ))

        # time.sleep(1)

    @property
    def empty_result_banner(self):
        return self.webdriver.find_element(*empty_res_locator)

    def get_empty_page_text(self):
        return self.empty_result_banner.text