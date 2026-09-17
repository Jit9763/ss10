import asyncio
import sys
from playwright.async_api import async_playwright

async def check_file(file_name):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1024, 'height': 800})
        await page.goto(f'file:///c:/Users/jiten/Desktop/class11/ss10/{file_name}')
        await page.wait_for_timeout(4000)

        overflows = await page.evaluate('''() => {
            const container = document.querySelector('.container, .main-wrapper') || document.body;
            const containerRect = container.getBoundingClientRect();
            const results = [];

            const all = document.querySelectorAll('h1, h2, h3, h4, p, div, table, mjx-container, pre, code, blockquote');
            for (let el of all) {
                if (el.classList.contains('container') || el.classList.contains('main-wrapper') || el.closest('.projector-bar') || el.closest('.toolbar-fixed')) continue;
                const r = el.getBoundingClientRect();
                if (r.right > containerRect.right + 2) {
                    let t = (el.innerText || el.textContent || '').trim().replace(/\\s+/g, ' ').substring(0, 70);
                    results.push({
                        tag: el.tagName,
                        cls: String(el.className),
                        diff: Math.round(r.right - containerRect.right),
                        text: t
                    });
                }
            }
            return results;
        }''')

        seen = set()
        deduped = []
        for o in overflows:
            k = o['text'][:35]
            if k and k not in seen:
                seen.add(k)
                deduped.append(o)

        if not deduped:
            print(f"✅ {file_name}: 0 overflows (100% fits container)")
        else:
            print(f"❌ {file_name}: {len(deduped)} overflowing elements:")
            for d in deduped:
                print(f"    +{d['diff']}px: {d['text']}")
        await browser.close()

async def main():
    files = sys.argv[1:] if len(sys.argv) > 1 else ['qa_master_math9_7.html', 'qa_master_math9_8.html']
    for f in files:
        await check_file(f)

if __name__ == '__main__':
    asyncio.run(main())
