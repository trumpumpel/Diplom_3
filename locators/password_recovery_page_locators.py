from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    BTN_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    BTN_RECOVER = (By.XPATH, "//button[text()='Восстановить']")
    PAS = (By.CSS_SELECTOR, ".input__icon.input__icon-action")
    PAS_ACT = (By.XPATH,
               "//div[@class= 'input pr-6 pl-6 input_type_text input_size_default input_status_active']")
