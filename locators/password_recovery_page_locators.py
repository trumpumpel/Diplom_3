from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    BTN_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    BTN_RECOVER = (By.XPATH, "//button[text()='Восстановить']")
