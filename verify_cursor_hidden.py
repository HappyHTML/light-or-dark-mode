import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        import os
        path = "file://" + os.path.abspath("index.html")
        await page.goto(path)

        # Move mouse to center
        await page.mouse.move(400, 300)
        await asyncio.sleep(0.5)

        # Check computed style of body and modal
        cursor_style = await page.evaluate("window.getComputedStyle(document.body).cursor")
        modal_cursor_style = await page.evaluate("window.getComputedStyle(document.getElementById('intro-modal')).cursor")

        print(f"Body cursor: {cursor_style}")
        print(f"Modal cursor: {modal_cursor_style}")

        await page.screenshot(path="final_cursor_check.png")
        await browser.close()

asyncio.run(run())
