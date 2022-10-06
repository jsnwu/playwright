from playwright.async_api import Locator
from playwright.sync_api import Page


class SearchPage:
    URL = 'https://www.duckduckgo.com'
    LOC_SEARCH_BUTTON = '#search_button_homepage, button[type="submit"][class^="searchbox"]'
    LOC_SEARCH_INPUT = '#search_form_input_homepage, #searchbox_input'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input: Locator = page.locator(self.LOC_SEARCH_INPUT)
        self.search_button: Locator = page.locator(self.LOC_SEARCH_BUTTON)

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, text: str) -> None:
        self.search_input.fill(text)
        self.search_button.click()
