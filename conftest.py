import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
user_language = None
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def language(request, user_language):
    user_language = request.config.getoption("language")
    if user_language == "es":
        print("\nstart chrome browser for test..")
    elif user_language == "fr":
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser():
    # browser = webdriver.Chrome()
    # browser.implicitly_wait(60)
    yield browser
    browser.quit()
