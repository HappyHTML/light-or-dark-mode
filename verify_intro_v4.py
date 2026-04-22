import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Use absolute path for the local file
        import os
        path = "file://" + os.path.abspath("index.html")
        await page.goto(path)

        # Wait a bit for animations
        await asyncio.sleep(1)

        # Take screenshot of the intro modal
        await page.screenshot(path="intro_v4.png")

        # Check if main is hidden
        main_visible = await page.is_visible("main")
        print(f"Main visible during modal: {main_visible}")

        # Dismiss modal
        await page.click("body")
        await asyncio.sleep(1)

        # Check if main is visible now
        main_visible_after = await page.is_visible("main")
        print(f"Main visible after dismissal: {main_visible_after}")

        await page.screenshot(path="after_dismiss_v4.png")

        await browser.close()

asyncio.run(run())
