import pytest
from selenium import webdriver


@pytest.mark.parametrize('language', ["es", "fr"])
def test_items(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_element_by_xpath("(//button[contains(@class,'btn btn-lg')])[1]")
    assert button.is_displayed()
