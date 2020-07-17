from pages.base_page import BasePage
from locators.bills_locator import BillsLocator


class BillsPage(BasePage, BillsLocator):

    def __init__(self, driver):
        super().__init__(driver)

    def click_owners_button(self):
        return self.click(self.button_owner)

    def check_client_panel(self, url):
        return self.check_page_loaded(url)





