from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver: WebDriver, by: By, value: str) -> None:
        self.driver = driver
        self.locator = (by, value)
        self.web_element = self.find()

    def find(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.locator))

    def click(self) -> None:
        element: WebElement = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator))
        element.click()

    def text(self) -> str:
        return self.web_element.text
