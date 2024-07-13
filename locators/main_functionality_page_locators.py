from selenium.webdriver.common.by import By


class MainFunctionalityPageLocators:
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    CL_POP_UP = (By.XPATH,
                 "//div[contains(@class, 'P3_V5')]")
    COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1'][text()='2']")
    O_I_P = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    BTN_ENT_PA = (By.XPATH, "//button[text()='Войти в аккаунт']")
