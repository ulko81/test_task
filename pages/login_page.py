from pages.base_page import BasePage
from locators.login_locator import LoginLocator


class LoginPage(BasePage, LoginLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        self.get_web_element(self.field_username).send_keys(username)

    def input_password(self, password):
        self.get_web_element(self.field_password).send_keys(password)

    def input_confirm_password(self, password):
        self.get_web_element(self.field_confirm_password).send_keys(password)

    def click_save_button(self):
        self.click(self.button_submit)

    def click_sing_in_button(self):
        self.click(self.button_submit)

    @property
    def text_tooltip_success(self):
        return self.get_web_element(self.tooltip_element_created).text
