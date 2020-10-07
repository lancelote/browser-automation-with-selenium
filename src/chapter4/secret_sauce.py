from typing import List

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from lxml import etree


class Listing:
    def __init__(self, listing_div) -> None:
        self.name = listing_div.find("./span/b").text
        self.wealth = int(listing_div.find("./p").text)

    def __lt__(self, other: "Listing") -> bool:
        return self.wealth < other.wealth


class PageWithListings:
    def __init__(self, page_source: str) -> None:
        self.tree = etree.HTML(page_source)

    def get_listings(self) -> List[Listing]:
        locator = ".//div/span/.."
        divs = self.tree.findall(locator)
        return [Listing(div) for div in divs]

    def get_listings_high_to_low(self) -> List[Listing]:
        return sorted(self.get_listings(), reverse=True)

    @property
    def highest_wealth(self) -> str:
        return max(self.get_listings()).name


def main() -> None:
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get("https://techstepacademy.com/trial-of-the-stones")

    page = PageWithListings(browser.page_source)
    print(page.highest_wealth)

    browser.quit()


if __name__ == '__main__':
    main()
