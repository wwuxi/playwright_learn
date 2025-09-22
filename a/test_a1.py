from time import sleep

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").type("abc",delay=100)
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    Todo=page.get_by_role("link",name="TodoMVC",exact=True).get_attribute("href")
    print(Todo)
    assert Todo =="http://todomvc.com"  # 打印页面标题

