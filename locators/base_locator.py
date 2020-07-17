from selenium.webdriver.common.by import By


class BaseLocator:
    button_submit = By.CSS_SELECTOR, 'button[type = "submit"]'
    field_username = By.ID, 'username'
    field_password = By.NAME, 'password'
    field_confirm_password = By.NAME, 'password_confirmation'
    tooltip_element_created = By.CLASS_NAME, 'MuiSnackbarContent-message'
