from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://techstepacademy.com/training-ground")

input1_element = browser.find_element_by_css_selector("input[id='ipt1']")
button1_element = browser.find_element_by_xpath("//button[@id='b1']")

input1_element.send_keys("Test text")
button1_element.click()
