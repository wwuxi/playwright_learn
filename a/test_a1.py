from time import sleep

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    # 可以启动不同的浏览器：chromium, firefox, webkit
    browser = p.chromium.launch(headless=False)  # headless=False 表示显示浏览器窗口
    page = browser.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").type("abc",delay=100)
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    Todo=page.get_by_role("link",name="TodoMVC",exact=True).get_attribute("href")
    print(Todo)
    sleep(5)
    print(page.title())  # 打印页面标题
    browser.close()


