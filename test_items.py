

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    button = browser.find_element_by_xpath("(//button[contains(@class,'btn btn-lg')])[1]")
    assert button.is_displayed(), "cart button not found"
