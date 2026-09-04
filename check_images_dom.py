import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://localhost:9222')
        context = browser.contexts[0]
        
        page = None
        for p in context.pages:
            if 'gemini.google.com' in p.url:
                page = p
                break
                
        if not page:
            print("No Gemini page found.")
            return

        print('Connected Page URL:', page.url)
        res = await page.evaluate("""() => {
            const inputs = Array.from(document.querySelectorAll('textarea, div[contenteditable="true"], rich-textarea div[contenteditable="true"]')).map(el => ({
                tag: el.tagName,
                class: el.className
            }));
            const imgs = Array.from(document.querySelectorAll('img')).map(i => ({
                src: i.src.substring(0, 60),
                w: i.width,
                h: i.height
            }));
            return { inputCount: inputs.length, imgCount: imgs.length, images: imgs };
        }""")
        print('DOM Check on https://gemini.google.com/images:', res)

if __name__ == "__main__":
    asyncio.run(main())
