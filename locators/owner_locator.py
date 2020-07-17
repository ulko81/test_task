from selenium.webdriver.common.by import By
from locators.base_locator import BaseLocator


class OwnerLocator(BaseLocator):
    button_create_owner = By.CSS_SELECTOR, 'a[href = "#/owners/create"]'
    owner_checkboxes = By.CSS_SELECTOR, 'input[type = "checkbox"]'
    field_first_name = By.ID, 'first_name'
    field_last_name = By.ID, 'last_name'
    field_email = By.ID, 'email'
    field_balance = By.NAME, 'start_balance_amount'
    currency_select = By.ID, 'currency_id'
    balance_start_date = By.NAME, 'start_balance_date'
    tooltip_element_created = By.CLASS_NAME, 'MuiSnackbarContent-message'
