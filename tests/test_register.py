from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import Locators
import pytest
from urls import URLS
from data import Data

class TestStellarsBurgersRegister:
    @pytest.mark.parametrize('password', Data.valid_passwords )
    def test_happy_path_register_with_valid_values_of_name_email_password(self, password):
        driver = webdriver.Chrome()
        driver.get(URLS.register_url)
        driver.find_element(*Locators.NAME_INPUT_LOCATOR).send_keys(Data.valid_name)
        driver.find_element(*Locators.EMAIL_INPUT_LOCATOR).send_keys(Data.random_valid_mail)
        driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        assert driver.current_url == URLS.login_url
        driver.quit()

    def test_invalid_path_register_with_empty_name_field(self):
        driver = webdriver.Chrome()
        driver.get(URLS.register_url)
        driver.find_element(*Locators.EMAIL_INPUT_LOCATOR).send_keys(Data.random_valid_mail)
        driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(Data.valid_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        assert driver.current_url != URLS.login_url
        driver.quit()

def test_invalid_path_register_with_invalid_email_no_domain():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(*Locators.NAME_INPUT_LOCATOR).send_keys("Александр")
    driver.find_element(*Locators.EMAIL_INPUT_LOCATOR).send_keys(f"alexdmiterko30{random.randint(100, 999)}")
    driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys("123456yapraktikum")
    driver.find_element(*Locators.REGISTER_BUTTON).click()
    assert driver.current_url != 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

    @pytest.mark.parametrize('password', Data.invalid_passwords)
    def test_invalid_path_register_with_invalid_password_no_6_symbols(self, password):
        driver = webdriver.Chrome()
        driver.get(URLS.register_url)
        driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(Keys.TAB)
        error_element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ERROR_FIELD))
        error_text = driver.find_element(*Locators.ERROR_MESSAGE).text
        assert error_element.is_displayed()
        assert error_text == Data.error_text
        driver.quit()
