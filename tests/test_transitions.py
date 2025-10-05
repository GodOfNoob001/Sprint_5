from conftest import open_session
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import URLS

class TestStellarsBurgersTransitions:
    def test_happy_path_success_transition_from_main_page_to_personal_account(self, open_session):
        open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        assert open_session.current_url == URLS.profile_url

    def test_happy_path_success_transition_from_personal_account_to_constructor_by_button(self, open_session):
        open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        open_session.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
        assert open_session.current_url == URLS.base_url

    def test_happy_path_success_transition_from_personal_account_to_constructor_by_logo(self, open_session):
        open_session.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        open_session.find_element(*Locators.LOGO).click()
        WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.MAKE_AN_ORDER_BUTTON))
        assert open_session.current_url == URLS.base_url
