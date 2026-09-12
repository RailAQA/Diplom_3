from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    ORDERS_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
    INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_POPUP = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]')
    CROSS_POPUP_BUTTON = (By.XPATH, '//button[contains(@class,"close")]')
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/preceding-sibling::div//p[contains(@class, 'counter_counter__num')]")
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")

class OrderPageLocators:
    ORDERS_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX'][@href='/']")
    CURRENT_COUNT_ORDERS_ALL = (By.XPATH, "//div[p[contains(text(), 'Выполнено за все время')]]//p[contains(@class, 'text_type_digits-large')]")
    CURRENT_COUNT_ORDERS_TODAT = (By.XPATH, "//div[p[contains(text(), 'Выполнено за сегодня')]]//p[contains(@class, 'text_type_digits-large')]")
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
