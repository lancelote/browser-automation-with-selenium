from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://techstepacademy.com/training-ground")

# Accepting an alert
button1 = browser.find_element_by_id("b1")
button1.click()

alert = Alert(browser)
assert alert.text == "You clickedButton1."
alert.accept()

# Waiting for an alert
button1.click()
WebDriverWait(browser, timeout=10).until(alert_is_present())
Alert(browser).accept()

# Selector
selector_element = browser.find_element_by_id("sel1")
selector = Select(selector_element)
assert [item.text for item in selector.options] == ["Bears", "Beets", "Battlestar Galactica"]

selector.select_by_index(2)
assert selector.first_selected_option.text == "Battlestar Galactica"

browser.close()
