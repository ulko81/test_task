import pytest
from pages.bills_page import BillsPage
from settings.project_setting import *
from methods.registration_method import RegistrationMethod
from pages.owner_page import OwnerPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures('get_driver')
class TestRegistration(RegistrationMethod):

    tooltips = {
        'element_created': 'Element created',
        'success_registration': 'You have successfully set your password'
    }

    @pytest.mark.registration
    def test_registration_owner(self):
        bills_page = BillsPage(self.driver)
        owner_page = OwnerPage(self.driver)
        set_password_page = LoginPage(self.driver)
        self.driver.get(TEST_URL)
        self.client_login(self.driver, **client_authorization_data)
        assert bills_page.check_client_panel(TEST_URL + project_pages.get('bills'))
        bills_page.click_owners_button()
        self.owner_registration(self.driver, **owner_registration_data)
        assert self.tooltips.get('element_created') == owner_page.text_tooltip_element_created
        self.driver.get('https://mail.ukr.net/')
        self.click_click_here_in_email(self.driver, mail_setting.get('email'), mail_setting.get('password'))
        self.select_current_window(self.driver)
        self.set_password(self.driver, owner_authorization_data.get('password'))
        assert self.tooltips.get('success_registration') == set_password_page.text_tooltip_success
        self.client_login(self.driver, owner_registration_data.get('email'), owner_authorization_data.get('password'))
        assert bills_page.check_client_panel(TEST_URL + project_pages.get('bills'))
