from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        login_link = browser.find_element_by_css_selector("#login_link")
        login_link.click()

    # def test_guest_can_go_to_login_page(self, browser):
    #     link = ""
    #     # initialize Page Object and
    #     # pass the driver instance and url address to the constructor
    #     page = MainPage(browser, link)
    #     page.open()
    #     page.go_to_login_page()
    #     login_page = LoginPage(browser, browser.current_url)
    #     login_page.should_be_login_page()

    #def test_gest_should_see_login_link(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/"
        #page = MainPage(browser, link)
        #page.open()
        #page.should_be_login_link()

