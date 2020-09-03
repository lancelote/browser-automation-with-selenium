from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager

from src.chapter4.base_element import BaseElement


class TrainingGroundPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self) -> None:
        self.driver.get(self.url)

    @property
    def button1(self) -> BaseElement:
        return BaseElement(self.driver, By.ID, "b1")


def main() -> None:
    browser = Firefox(executable_path=GeckoDriverManager().install())
    page = TrainingGroundPage(browser)
    page.go()

    assert page.button1.text == "Button1"

    browser.quit()


if __name__ == "__main__":
    main()
