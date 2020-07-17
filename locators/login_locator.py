from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class LoginLocator(BaseLocator):
    button_submit = By.CSS_SELECTOR, 'button[type = "submit"]'
