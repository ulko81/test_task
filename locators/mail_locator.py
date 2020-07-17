from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class MailLocator(BaseLocator):
    title_message = By.XPATH, '//a[contains(text(),"Welcome email message")]'
    button_click_here = By.XPATH, '//a[contains(text(),"Click here")]'
    field_email = By.CSS_SELECTOR, 'input[type = "text"]'
    field_password = By.CSS_SELECTOR, 'input[type = "password"]'
