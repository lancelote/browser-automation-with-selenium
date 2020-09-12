from typing import NamedTuple
from typing import Optional

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


class Locator(NamedTuple):
    by: By
    value: str


class BaseElement:
    def __init__(self, driver: WebDriver, locator: Locator) -> None:
        self.driver = driver
        self.locator = locator
        self.web_element = self.find()

    def find(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.locator))

    def click(self) -> None:
        element: WebElement = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.locator))
        element.click()

    def input_text(self, text: str) -> None:
        self.web_element.send_keys(text)

    @property
    def text(self) -> str:
        return self.web_element.text


class BasePage:
    url: Optional[str] = None

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def go(self) -> None:
        self.driver.get(self.url)


class TrainingGroundPage(BasePage):
    url = "https://techstepacademy.com/training-ground"

    @property
    def button1(self) -> BaseElement:
        locator = Locator(By.ID, "b1")
        return BaseElement(self.driver, locator)


class TrialPage(BasePage):
    url = "https://techstepacademy.com/trial-of-the-stones"

    @property
    def stone_input(self) -> BaseElement:
        locator = Locator(By.ID, value="r1Input")
        return BaseElement(self.driver, locator)

    @property
    def stone_button(self) -> BaseElement:
        locator = Locator(By.ID, value="r1Btn")
        return BaseElement(self.driver, locator)

    @property
    def stone_password(self) -> BaseElement:
        locator = Locator(By.ID, value="passwordBanner")
        return BaseElement(self.driver, locator)

    @property
    def secrets_input(self) -> BaseElement:
        locator = Locator(By.ID, value="r2Input")
        return BaseElement(self.driver, locator)

    @property
    def secrets_button(self) -> BaseElement:
        locator = Locator(By.ID, value="r2Butn")
        return BaseElement(self.driver, locator)


def main() -> None:
    browser = Firefox(executable_path=GeckoDriverManager().install())
    trial_page = TrialPage(driver=browser)
    trial_page.go()

    trial_page.stone_input.input_text("rock")
    trial_page.stone_button.click()
    assert trial_page.stone_password.text == "bamboo", "unexpected stone password"

    training_page = TrainingGroundPage(driver=browser)
    training_page.go()

    assert training_page.button1.text == "Button1", "unexpected button 1 text"

    browser.quit()


if __name__ == "__main__":
    main()
