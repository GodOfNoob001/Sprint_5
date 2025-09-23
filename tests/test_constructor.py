from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import open_session

class TestStellaBurgersConstructor:

    def test_happy_path_success_transition_in_constructor_to_sauce_page_on_main_page(self, open_session):

        open_session.find_element(*Locators.SAUCE_BUTTON).click()
        first_sauce = WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.FIRST_SAUSE))
        assert first_sauce.is_displayed()

    def test_happy_path_success_transition_in_constructor_to_bun_page_on_main_page(self, open_session):
        open_session.find_element(*Locators.SAUCE_BUTTON).click()
        open_session.find_element(*Locators.BUN_BUTTON).click()
        first_bun = WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.FIRST_BUN))
        assert first_bun.is_displayed()

    def test_happy_path_success_transition_in_constructor_to_topping_page_on_main_page(self, open_session):
        open_session.find_element(*Locators.TOPPING_BUTTON).click()
        first_topping = WebDriverWait(open_session, 3).until(expected_conditions.visibility_of_element_located(Locators.FIRST_TOPPING))
        assert first_topping.is_displayed()
