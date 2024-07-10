from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='Пароль']")
    SUB_BTN_CLICK_LOG = (By.XPATH, "//button[text()='Войти']")
    BTN_ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BTN = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3 ')]")
