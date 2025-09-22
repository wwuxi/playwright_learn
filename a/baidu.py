import re
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#s-usersetting-top").hover()
    page.get_by_role("link",name="搜索设置").wait_for(state="visible")
    page.get_by_role("link", name="搜索设置").click()
    page.locator("#se-settting-1").get_by_role("radio",name="不显示").click()
    page.get_by_role("radio", name="仅简体中文").check()

    #page.get_by_role("link", name="搜索设置").click()

    print("成功")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
