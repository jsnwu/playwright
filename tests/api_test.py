from multiprocessing import Process
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from main import app, accounts


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # setup
    server = Process(target=app.run, args=("127.0.0.1", 8080))
    server.start()
    yield
    # teardown
    server.terminate()
    server.join()


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(base_url="http://127.0.0.1:8080")
    yield request_context
    request_context.dispose()


def test_root(api_request_context: APIRequestContext):
    response = api_request_context.get("/")
    assert response.body().decode("UTF-8") == "Hello World"
    assert response.ok


def test_get_account_by_id(api_request_context: APIRequestContext):
    response = api_request_context.get("accounts/1")
    expected = '{"balance":123.0,"id":1,"name":"John"}\n'
    assert response.body().decode("UTF-8") == expected
    assert response.ok


def test_add_account(api_request_context: APIRequestContext):
    data = {"name": "Tim", "balance": 345.0}
    api_request_context.post("account", data=data)
    print(accounts)
    response = api_request_context.get("accounts/3")
    expected = '{"balance":345.0,"id":3,"name":"Tim"}\n'
    assert response.body().decode("UTF-8") == expected
    assert response.ok
