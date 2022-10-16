from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import submit_button, email_error, message_error, agreement_error, subject_option, subject
from page_objects.base_page import HabrBase
from selenium.webdriver.support.ui import Select


class FeedbackPage(HabrBase):
    url = 'https://habr.com/ru/feedback/'

    @property
    def submit_button(self):
        return self.webdriver.find_element(*submit_button)

    @property
    def email_error_message(self):
        return self.webdriver.find_element(*email_error)

    @property
    def message_error_message(self):
        return self.webdriver.find_element(*message_error)

    @property
    def personal_agreement_error_message(self):
        return self.webdriver.find_element(*agreement_error)

    @property
    def subject(self):
        return Select(self.webdriver.find_element(*subject))

    def count_subject(self):
        elements = self.subject.options

        return len(elements)

    def change_subject(self, index=1):
        self.subject.select_by_index(index)

    def wait_full_page(self):
        wait = WebDriverWait(self.webdriver, 5)

        wait.until(
            presence_of_element_located(subject)
        )

    def open(self):
        super().open()
        self.wait_full_page()
