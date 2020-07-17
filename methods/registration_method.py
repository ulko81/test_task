from pages.owner_page import OwnerPage
from methods.general_method import GeneralMethod
from locators.owner_locator import OwnerLocator


class RegistrationMethod (GeneralMethod):

    def owner_registration(self, driver, first_name, last_name, email, currency, balance, ):
        owner = OwnerPage(driver)
        owner.click_create_owner()
        owner.input_first_name(first_name)
        owner.input_last_name(last_name)
        owner.input_email(email)
        owner.click_select_balance_start_date()
        owner.click_calendar_ok()
        self.clear_field(driver, OwnerLocator.field_balance)
        owner.input_balance(balance)
        owner.click_select_currency()
        owner.select_currency(currency)
        owner.click_owner_active()
        owner.click_send_welcome_email()
        owner.click_save()
