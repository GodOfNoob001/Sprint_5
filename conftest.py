import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import URLS

@pytest.fixture(scope="function")
def open_session():
    driver = webdriver.Chrome()
    driver.get(URLS.base_url)
    driver.find_element(*Locators.ENTER_BUTTON_ON_MAIN_PAGE).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
    driver.find_element(*Locators.EMAIL_LOGIN).send_keys("alexdmiterko301212@ya.ru")
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys("YaPraktikum123")
    driver.find_element(*Locators.ENTER_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
    yield driver
    driver.quit()
