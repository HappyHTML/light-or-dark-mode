import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        import os
        path = "file://" + os.path.abspath("index.html")
        await page.goto(path)

        await page.click("body")
        await asyncio.sleep(1.3)

        # Check if word-entry has no background or box-shadow
        styles = await page.evaluate("""() => {
            const el = document.querySelector('.word-entry');
            const s = window.getComputedStyle(el);
            return {
                boxShadow: s.boxShadow,
                background: s.background
            };
        }""")
        print(f"Word Entry Styles: {styles}")

        # Screenshot of syllable hover
        await page.hover('.syllable:first-child')
        await asyncio.sleep(0.5)
        await page.screenshot(path="final_refined.png")

        await browser.close()

asyncio.run(run())
