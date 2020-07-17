from pages.login_page import LoginPage
from pages.mail_page import MailPage
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class GeneralMethod:

    @staticmethod
    def client_login(driver, username, password):
        login_page = LoginPage(driver)
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_sing_in_button()

    @staticmethod
    def set_password(driver, password):
        login_page = LoginPage(driver)
        login_page.input_password(password)
        login_page.input_confirm_password(password)
        login_page.click_save_button()

    @staticmethod
    def click_click_here_in_email(driver, email, password):
        mail = MailPage(driver)
        mail.input_email(email)
        mail.input_password(password)
        mail.click_enter()
        mail.click_message()
        mail.click_click_here()

    @staticmethod
    def clear_field(driver, locator):
        field = BasePage(driver)
        return field.get_web_element(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)

    @staticmethod
    def select_current_window(driver):
        old_window = driver.current_window_handle
        for handle in driver.window_handles:
            if handle == old_window:
                driver.close()
            else:
                driver.switch_to.window(handle)
