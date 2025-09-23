from selenium.webdriver.common.by import By

class Locators:
    NAME_INPUT_LOCATOR = (By.XPATH, "//fieldset[1]//input[@class='text input__textfield text_type_main-default']")#Поле ввода имени на странице регистрации
    EMAIL_INPUT_LOCATOR = (By.XPATH, "//fieldset[2]//input[@class='text input__textfield text_type_main-default']")#Поле ввода email на странице регистрации
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//fieldset[3]//input[@class='text input__textfield text_type_main-default']")#Поле ввода пароля на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")#кнопка регистрации на странице регистрации
    ENTER_BUTTON = (By.XPATH, '//button[text() = "Войти"]')#Кнопка входа на странице входа в аккаунт
    ERROR_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_error')]//input[@type='password']")
    ERROR_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']")#Сообщение об ошибке в поле пароль
    ENTER_BUTTON_ON_MAIN_PAGE = (By.XPATH, "//button[text() = 'Войти в аккаунт']")#Кнопка входа в личный аккаунт на главной странице
    EMAIL_LOGIN = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_LOGIN = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    MAKE_AN_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")#Кнопка "Оформить заказ" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")#Кнопка "Личный кабинет" на главной странице
    LOGIN_LINK_BUTTON = (By.XPATH, "//a[text() = 'Войти']")#Кнопка "войти" на странице регистрации и "забыли пароль"
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")#Кнопка выхода из аккаунта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")#Кнопка перехода в конструктор
    LOGO = (By.XPATH, "//a[@href = '/']")#Логотип Stellars burger
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")#Кнопка перехода к соусам в конструкторе
    FIRST_SAUSE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")#Первый отображаемый соус
    BUN_BUTTON = (By.XPATH, "//span[text()='Булки']")#Кнопка перехода к булкам в конструкторе
    FIRST_BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")#Первая отображаемая булка
    TOPPING_BUTTON = (By.XPATH, "//span[text()='Начинки']")#Кнопка перехода к начинкам в конструкторе
    FIRST_TOPPING = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6f']")#Первая отображаемая начинка
    SAUCE_TOP = (By.XPATH, "//h2[text()='Соусы']")
    BUN_TOP = (By.XPATH, "//h2[text()='Булки']")
    TOPPING_TOP = (By.XPATH, "//h2[text()='Начинки']")