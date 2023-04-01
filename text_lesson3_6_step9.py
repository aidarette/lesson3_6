from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_items(browser):
    browser.get(link)
    time.sleep(3)
    buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(buttons) > 0, 'button not found'