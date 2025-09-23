from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import URLS

class TestStellarsBurgerLogin:
    def test_happy_path_success_login_from_main_page_with_valid_values(self):
        driver = webdriver.Chrome()
        driver.get(URLS.base_url)
        driver.find_element(*Locators.ENTER_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Data.valid_login)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Data.valid_password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_AN_ORDER_BUTTON).is_displayed()
        driver.quit()


    def test_happy_path_success_login_from_personal_account_button_with_valid_values(self):
        driver = webdriver.Chrome()
        driver.get(URLS.base_url)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Data.valid_login)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Data.valid_password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_AN_ORDER_BUTTON).is_displayed()
        driver.quit()


    def test_happy_path_success_login_from_register_page_with_valid_values(self):
        driver = webdriver.Chrome()
        driver.get(URLS.register_url)
        driver.find_element(*Locators.LOGIN_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Data.valid_login)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Data.valid_password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_AN_ORDER_BUTTON).is_displayed()
        driver.quit()


    def test_happy_path_success_login_from_forgot_password_page_with_valid_values(self):
        driver = webdriver.Chrome()
        driver.get(URLS.forgot_password_url)
        driver.find_element(*Locators.LOGIN_LINK_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Data.valid_login)
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Data.valid_password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_AN_ORDER_BUTTON).is_displayed()
        driver.quit()

