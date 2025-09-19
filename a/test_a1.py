from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    # 可以启动不同的浏览器：chromium, firefox, webkit
    browser = p.chromium.launch(headless=False)  # headless=False 表示显示浏览器窗口
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())  # 打印页面标题
    browser.close()


