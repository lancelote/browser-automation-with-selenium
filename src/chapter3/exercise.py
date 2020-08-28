from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def answer_stones_riddle(browser: webdriver.Firefox) -> None:
    input1 = browser.find_element_by_id("r1Input")
    input1.send_keys("rock")
    button1 = browser.find_element_by_id("r1Btn")
    button1.click()


def answer_secrets_riddle(browser: webdriver.Firefox) -> None:
    password = browser.find_element_by_xpath("//div[@id='passwordBanner']/h4").text
    input2 = browser.find_element_by_id("r2Input")
    input2.send_keys(password)
    button2 = browser.find_element_by_id("r2Butn")
    button2.click()

    success1 = browser.find_element_by_xpath("//div[@id='successBanner1']/h4").text
    assert success1 == "Success!", "Second riddle failure"


def answer_richest_merchant(browser: webdriver.Firefox) -> None:
    merchants = browser.find_elements_by_xpath("//label[text()='Total Wealth ($):']/..")
    assert len(merchants) == 2, "Cannot find two merchants"

    merchant1_name = merchants[0].find_element_by_tag_name("b").text
    merchant2_name = merchants[1].find_element_by_tag_name("b").text

    merchant1_wealth = int(merchants[0].find_element_by_tag_name("p").text)
    merchant2_wealth = int(merchants[1].find_element_by_tag_name("p").text)

    input3 = browser.find_element_by_id("r3Input")

    if merchant1_wealth > merchant2_wealth:
        input3.send_keys(merchant1_name)
    else:
        input3.send_keys(merchant2_name)

    button3 = browser.find_element_by_id("r3Butn")
    button3.click()


def check_complete_trial(browser: webdriver.Firefox) -> None:
    button4 = browser.find_element_by_id("checkButn")
    button4.click()

    success2 = browser.find_element_by_xpath("//div[@id='trialCompleteBanner']/h4").text
    assert success2 == "Trial Complete", "Trial failure"


def main() -> None:
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get("https://techstepacademy.com/trial-of-the-stones")

    answer_stones_riddle(browser)
    answer_secrets_riddle(browser)
    answer_richest_merchant(browser)

    browser.close()


if __name__ == "__main__":
    main()
