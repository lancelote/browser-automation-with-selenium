from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://techstepacademy.com/training-ground")

input_element = browser.find_element_by_css_selector("input[id='ipt1']")
input_element.send_keys("My First Automation")
button_element = browser.find_element_by_css_selector("button[name='butn1']")
button_element.click()
