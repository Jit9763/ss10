import os
import sys
import time
import json
import base64
import subprocess
import asyncio
from io import BytesIO
from PIL import Image
from playwright.async_api import async_playwright

WORKSPACE_DIR = r"c:\Users\jiten\Desktop\class11\ss10"
POL4_IMG_DIR = os.path.join(WORKSPACE_DIR, "images", "pol4")
os.makedirs(POL4_IMG_DIR, exist_ok=True)

PROMPTS = {
    13: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'क्षेत्रीय दलों का उभार (Rise of Regional Parties)'. Showing regional state parties flourishing across diverse Indian states.
Right card top header: 'संघवाद का सशक्तीकरण (Strengthening of Federalism)'. Showing national coalition building and balanced power sharing between Center and States.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    14: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'शीर्ष नेताओं का एकाधिकार (Monopoly of Top Leaders)'. Showing a few top leaders holding all decision making power in party headquarters.
Right card top header: 'आंतरिक चुनाव का अभाव (Lack of Internal Elections)'. Showing empty ballot boxes and ordinary party workers left without voice or internal elections.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    15: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'परिवारवाद का प्रभुत्व (Dominance of Family Control)'. Showing leadership position passed down directly within one family lineage.
Right card top header: 'योग्यता की उपेक्षा (Neglect of Hardworking Cadre)'. Showing hardworking grassroot party workers passed over for family members.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    16: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'धन-बल का अनुचित प्रभाव (Influence of Money Power)'. Showing wealthy donors and corporate funds influencing party nomination tickets.
Right card top header: 'अपराधिक तत्त्वों का प्रवेश (Entry of Criminal Elements)'. Showing muscle power and intimidation tactics during election campaigns.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    17: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'समान नीतियां (Ideological Convergence)'. Showing different political parties offering almost identical economic policies.
Right card top header: 'विकल्पहीनता (Lack of Distinct Choice)'. Showing confused voters searching for genuine policy choices on ballot paper.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    18: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'दल-बदल विरोधी कानून (Anti-Defection Law)'. Showing constitution law restricting elected MLAs and MPs from changing parties opportunistically.
Right card top header: 'शपथ पत्र (Affidavit of Assets & Cases)'. Showing candidate submitting legal affidavit declaring property assets and criminal cases to Election Commission.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    19: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'सांगठनिक चुनाव व आयकर ऑडिट (Internal Elections & Tax Audit)'. Showing mandatory organizational elections and audited income tax returns for political parties.
Right card top header: 'महिला आरक्षण व स्टेट फंडिंग (Women Quota & State Funding)'. Showing 33% election ticket quota for women candidates and state funding of election supplies.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    20: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'जनता का दबाव (Public Pressure & Movements)'. Showing active citizens, media, and petitions pressuring political parties for reforms.
Right card top header: 'सक्रिय सहभागिता (Active Citizen Participation)'. Showing conscious reform-minded citizens joining political parties to improve governance from within.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags."""
}

def copy_to_clip(text):
    p = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    p.communicate(input=text.encode('utf-16le'))

async def process_image(gemini_page, idx):
    if idx not in PROMPTS:
        print(f"Error: Prompt {idx} not found in dictionary.", flush=True)
        return False

    out_file = os.path.join(POL4_IMG_DIR, f"pol4_real_{idx}.webp")
    prompt = PROMPTS[idx]

    print(f"\n==================================================", flush=True)
    print(f" GENERATING CHAPTER 4 IMAGE {idx} (Direct DOM Canvas Engine)", flush=True)
    print(f"==================================================", flush=True)

    # 1. Scroll to bottom
    await gemini_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await asyncio.sleep(2)

    # Count initial user queries & model responses
    initial_counts = await gemini_page.evaluate("""() => {
        return {
            queries: document.querySelectorAll('user-query').length,
            responses: document.querySelectorAll('model-response, message-content, div.response-container-content').length
        };
    }""")
    print(f" Initial DOM counts: {initial_counts}", flush=True)

    # 2. Copy prompt N to clipboard
    copy_to_clip(prompt)
    await asyncio.sleep(1)

    # 3. Clean text box & paste prompt
    box = gemini_page.locator('rich-textarea div[contenteditable="true"], div[contenteditable="true"], textarea').first
    await box.click()
    await gemini_page.keyboard.press("Control+a")
    await gemini_page.keyboard.press("Backspace")
    await asyncio.sleep(1)
    await gemini_page.keyboard.press("Control+v")
    await asyncio.sleep(2)

    # 4. Submit prompt EXACTLY ONCE (Send button click OR Enter key, never both)
    print(f" Submitting Prompt {idx} (single submission)...", flush=True)
    click_success = await gemini_page.evaluate("""() => {
        const sendBtn = document.querySelector('button[aria-label*="Send"], button[aria-label*="भेजें"], button.send-button');
        if (sendBtn && !sendBtn.disabled) {
            sendBtn.click();
            return true;
        }
        return false;
    }""")
    if not click_success:
        await gemini_page.keyboard.press("Enter")
    
    await asyncio.sleep(5)
    current_queries = await gemini_page.evaluate("document.querySelectorAll('user-query').length")
    print(f" Prompt {idx} submitted! (DOM Queries: {initial_counts['queries']} -> {current_queries})", flush=True)

    # 5. Patient wait for NEW response & NEW image generation (100 seconds)
    print(f" Waiting 100 SECONDS for new image generation...", flush=True)
    await asyncio.sleep(100)

    # 6. Extract image directly from newest model-response container via Canvas
    saved_ok = False
    for poll in range(6):
        await gemini_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(2)

        base64_data = await gemini_page.evaluate("""async (initRespCount) => {
            const responses = Array.from(document.querySelectorAll('model-response, message-content, div.response-container-content'));
            if (responses.length <= initRespCount) return null;
            
            const lastResp = responses[responses.length - 1];
            const imgs = Array.from(lastResp.querySelectorAll('img')).filter(img => 
                (img.src.includes('googleusercontent.com') || img.src.includes('blob:'))
            );
            if (imgs.length === 0) return null;
            const targetImg = imgs[imgs.length - 1];

            if (!targetImg.complete || targetImg.naturalWidth === 0) {
                await new Promise(r => targetImg.onload = r);
            }

            const canvas = document.createElement('canvas');
            canvas.width = targetImg.naturalWidth || targetImg.width;
            canvas.height = targetImg.naturalHeight || targetImg.height;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(targetImg, 0, 0);
            return canvas.toDataURL('image/png');
        }""", initial_counts['responses'])

        if base64_data and ',' in base64_data:
            header, encoded = base64_data.split(',', 1)
            raw_bytes = base64.b64decode(encoded)
            img = Image.open(BytesIO(raw_bytes))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(out_file, format='WEBP', quality=95)
            file_sz = os.path.getsize(out_file)
            if file_sz > 20000:
                saved_ok = True
                print(f" Direct DOM Canvas Extract SUCCESS for Image {idx}! Size: {img.size}, File: {file_sz} bytes", flush=True)
                break
        
        print(f" Poll {poll+1}/6: Response image not ready, waiting 5s...", flush=True)
        await asyncio.sleep(5)

    if saved_ok:
        print(f"\n✨ SUCCESS: Image {idx} saved as pol4_real_{idx}.webp!", flush=True)
        return True
    else:
        print(f"\n❌ ERROR: Failed to extract Image {idx} from DOM.", flush=True)
        return False

async def main(indices):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://localhost:9222')
        context = browser.contexts[0]
        
        gemini_page = None
        for page in context.pages:
            if 'gemini.google.com' in page.url:
                gemini_page = page
                break
                
        if not gemini_page:
            print("FATAL ERROR: Gemini page not found on localhost:9222!", flush=True)
            return

        print(f"==================================================", flush=True)
        print(f" STARTING CHAPTER 4 REGENERATION FOR IMAGES: {indices}", flush=True)
        print(f" Settings: Direct DOM Canvas Engine + 3.5 Minute Gap", flush=True)
        print(f" Connected URL: {gemini_page.url}", flush=True)
        print(f"==================================================", flush=True)

        for i, idx in enumerate(indices):
            out_file = os.path.join(POL4_IMG_DIR, f"pol4_real_{idx}.webp")
            if os.path.exists(out_file):
                try:
                    os.remove(out_file)
                    print(f" Removed old pol4_real_{idx}.webp for clean regeneration.", flush=True)
                except Exception as e:
                    pass

            res = await process_image(gemini_page, idx)
            if not res:
                print(f" Retrying Image {idx} once more after 20s pause...", flush=True)
                await asyncio.sleep(20)
                await process_image(gemini_page, idx)

            if i < len(indices) - 1:
                print(f"\n⏳ PATIENT PAUSE: Waiting 3.5 MINUTES (210 seconds) before starting Image {indices[i+1]}...", flush=True)
                await asyncio.sleep(210)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_indices = [int(x) for x in sys.argv[1:]]
    else:
        img_indices = [13, 14, 15, 16, 17, 18, 19, 20]
    asyncio.run(main(img_indices))
