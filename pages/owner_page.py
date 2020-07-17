from pages.base_page import BasePage
from locators.owner_locator import OwnerLocator


class OwnerPage(BasePage, OwnerLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_create_owner(self):
        return self.click(self.button_create_owner)

    def input_first_name(self, first_name):
        self.get_web_element(self.field_first_name).send_keys(first_name)

    def input_last_name(self, last_name):
        self.get_web_element(self.field_last_name).send_keys(last_name)

    def input_email(self, email):
        self.get_web_element(self.field_email).send_keys(email)

    def click_select_currency(self):
        self.click(self.currency_select)

    def click_select_balance_start_date(self):
        self.click(self.balance_start_date)

    def click_calendar_ok(self):
        self.get_element_with_text('OK').click()

    def select_currency(self, currency):
        self.get_element_with_text(currency).click()

    def input_balance(self, balance):
        self.get_web_element(self.field_balance).send_keys(balance)

    def click_owner_active(self):
        self.get_web_elements(self.owner_checkboxes)[0].click()

    def click_send_welcome_email(self):
        self.get_web_elements(self.owner_checkboxes)[1].click()

    def click_save(self):
        self.click(self.button_submit)

    @property
    def text_tooltip_element_created(self):
        return self.get_web_element(self.tooltip_element_created).text




