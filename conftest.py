"""
Настройка тестового окружения с помощью передачи параметров через командную строку.
Вполняется с помощью встроенной функции pytest_addoption и фикстуры request. 
Сначала добавляем в текущем файле обработчик опции в функции pytest_addoption, 
затем напишем фикстуру, которая будет обрабатывать переданные в опции данные
Добавим выбор браузера и выбор языка.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        # language setting for Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        # launch browser with indicated option
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        # language seting for Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        # launch browser with indicated option
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
