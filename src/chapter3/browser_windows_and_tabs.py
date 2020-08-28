from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser1 = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser2 = webdriver.Firefox(executable_path=GeckoDriverManager().install())

url = "https://techstepacademy.com/training-ground"

browser1.get(url)
browser2.get("https://google.com")

# get the different page
browser2.get("https://amazon.com")
browser2.close()

# open multiple tabs
browser1.execute_script('window.open(url, "_blank");')
browser1.execute_script('window.open("https://google.com", "_blank");')
browser1.execute_script('window.open("https://yahoo.com", "_blank");')
browser1.execute_script('window.open("https://google.com", "_blank");')

handles = browser1.window_handles
assert len(handles) == 5

# note: handles are not in open order
browser1.switch_to.window(handles[0])

browser1.close()
