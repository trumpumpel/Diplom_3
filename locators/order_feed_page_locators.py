from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    P_P_O = (By.XPATH,
             "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    NUM_O = (By.XPATH, "//p[@class='text text_type_digits-default']")
    EL_COUNTER = (By.XPATH,
                  "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    P_O_NUM = (By.XPATH,
               "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
    NUM_I_PROG = (By.XPATH,
                  "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]")
