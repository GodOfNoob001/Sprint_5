from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
from locators import Locators
import pytest
from urls import URLS
from data import Data
from conftest import driver, fill_common_fields

class TestStellarsBurgersRegister:
    @pytest.mark.parametrize('password', Data.valid_passwords)
    def test_happy_path_register_with_valid_values_of_name_email_password(self, driver, fill_common_fields, password):
        fill_common_fields(
            name=Data.valid_name,
            email=Data.random_valid_mail,
            password=password
        )
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        assert driver.current_url == URLS.login_url
        driver.quit()

    def test_invalid_path_register_with_empty_name_field(self, driver, fill_common_fields):
        fill_common_fields(
            email=Data.random_valid_mail,
            password=Data.valid_password
        )
        assert driver.current_url != URLS.login_url
        driver.quit()

    def test_invalid_path_register_with_invalid_email_no_domain(self, driver, fill_common_fields):
        fill_common_fields(
            name=Data.valid_name,
            email=Data.random_invalid_mail,
            password=Data.valid_password
        )
        assert driver.current_url != URLS.login_url

    @pytest.mark.parametrize('password', Data.invalid_passwords)
    def test_invalid_path_register_with_invalid_password_no_6_symbols(self, driver, password):
        driver.find_element(*Locators.NAME_INPUT_LOCATOR).send_keys(Data.valid_name)
        driver.find_element(*Locators.EMAIL_INPUT_LOCATOR).send_keys(Data.random_valid_mail)
        driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(Keys.TAB)

        error_element = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.ERROR_FIELD)
        )
        error_text = driver.find_element(*Locators.ERROR_MESSAGE).text
        assert error_element.is_displayed()
        assert error_text == Data.error_text
        driver.quit()
