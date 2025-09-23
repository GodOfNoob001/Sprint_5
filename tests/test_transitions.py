from conftest import open_session
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_happy_path_success_transition_from_main_page_to_personal_account(open_session):
    open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
    assert open_session.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

def test_happy_path_success_transition_from_personal_account_to_constructor_by_button(open_session):
    open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
    open_session.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
    assert open_session.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_happy_path_success_transition_from_personal_account_to_constructor_by_logo(open_session):
    open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
    open_session.find_element(*Locators.LOGO).click()
    WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
    assert open_session.current_url == URLS.base_url
