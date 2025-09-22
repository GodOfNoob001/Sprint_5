from conftest import open_session
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_happy_path_success_logout(open_session):
    open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
    open_session.find_element(*Locators.EXIT_BUTTON).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
    assert open_session.current_url == 'https://stellarburgers.nomoreparties.site/login'
