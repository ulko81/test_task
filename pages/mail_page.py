from pages.base_page import BasePage
from locators.mail_locator import MailLocator


class MailPage(BasePage, MailLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def input_email(self, email):
        self.get_web_element(self.field_email).send_keys(email)

    def input_password(self, password):
        self.get_web_element(self.field_password).send_keys(password)

    def click_enter(self):
        self.click(self.button_submit)

    def click_message(self):
        self.get_web_elements(self.title_message)[0].click()

    def click_click_here(self):
        self.click(self.button_click_here)

