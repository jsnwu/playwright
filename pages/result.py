from playwright.async_api import Locator


class ResultPage:
    LOC_RESULT_LINKS = 'a[data-testid="result-title-a"]'
    LOC_SEARCH_BUTTON = (
        '#search_button_homepage, button[type="submit"][class^="searchbox"]'
    )
    LOC_SEARCH_INPUT = "#search_form_input_homepage, #searchbox_input"

    def __init__(self, page):
        self.page = page
        self.result_links: Locator = page.locator(self.LOC_RESULT_LINKS)
        self.search_input: Locator = page.locator(self.LOC_SEARCH_INPUT)
        self.search_button: Locator = page.locator(self.LOC_SEARCH_BUTTON)

    def click_result(self, index: int):
        print(self.result_links)
        self.result_links.nth(index).click()
