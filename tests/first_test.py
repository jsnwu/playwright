import re

import pytest
from playwright.sync_api import Page, expect
from pages.search import SearchPage
from pages.result import ResultPage


@pytest.mark.parametrize("search_term", ["playwright", "google", "tennis", "kayka"])
def test_search(page: Page, search_term):
    search = SearchPage(page)
    search.load()
    search.search(search_term)
    result = ResultPage(page)
    result.click_result(0)
    page.screenshot(path=f'../reports/screenshots/test_search_{search_term}.png')
    # page.pause()

