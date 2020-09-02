from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager


class TrainingGroundPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"

    def go(self) -> None:
        self.driver.get(self.url)

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

    def close(self) -> None:
        self.driver.close()

    def accept_alert(self) -> None:
        Alert(self.driver).accept()


def main() -> None:
    browser = Firefox(executable_path=GeckoDriverManager().install())
    page = TrainingGroundPage(browser)
    page.go()

    page.type_into_input("it worked")
    assert page.get_input_text() == "it worked"

    page.click_button_1()
    page.accept_alert()

    page.close()


if __name__ == "__main__":
    main()
