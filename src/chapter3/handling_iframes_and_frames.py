from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://techstepacademy.com/iframe-training")

iframe = browser.find_element_by_css_selector("iframe")
browser.switch_to.frame(iframe)

p = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")
assert p.text.startswith("Welcome to the Training Ground")

browser.switch_to.default_content()
title_text = browser.find_element_by_css_selector("div#block-5d3de848045889000188d389 div p").text
assert title_text.startswith(" Training Ground")

browser.close()
