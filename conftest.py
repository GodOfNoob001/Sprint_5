import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import URLS
from data import Data

@pytest.fixture(scope="function")
def open_session():
    driver = webdriver.Chrome()
    driver.get(URLS.base_url)
    driver.find_element(*Locators.ENTER_BUTTON_ON_MAIN_PAGE).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.EMAIL_LOGIN).send_keys(Data.valid_login)
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(Data.valid_password)
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(URLS.register_url)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def fill_common_fields(driver):
    def _fill_fields(name="", email="", password=""):
        if name:
            driver.find_element(*Locators.NAME_INPUT_LOCATOR).send_keys(name)
        if email:
            driver.find_element(*Locators.EMAIL_INPUT_LOCATOR).send_keys(email)
        if password:
            driver.find_element(*Locators.PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
    return _fill_fields