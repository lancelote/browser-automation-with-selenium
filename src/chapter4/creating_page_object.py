from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager

browser = Firefox(executable_path=GeckoDriverManager().install())


class TrainingGroundPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def type_into_input(self, text: str) -> None:
        input_field = self.driver.find_element_by_id("ipt1")
        input_field.clear()
        input_field.send_keys(text)

    def get_input_text(self) -> str:
        input_field = self.driver.find_element_by_id("ipt1")
        return input_field.get_attribute("value")

    def click_button_1(self) -> None:
        button = self.driver.find_element_by_id("b1")
        button.click()
