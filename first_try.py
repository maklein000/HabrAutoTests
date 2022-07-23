from selenium.webdriver.chrome import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.WebDriver(executable_path="chromedriver")

driver.get("https://habr.com")


time.sleep(1)

search_button_locator = By.CSS_SELECTOR, '[data-test-id="search-button"]'

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

time.sleep(20)
# посчитать количество записей(20)

# посчитать количество страниц(50)






