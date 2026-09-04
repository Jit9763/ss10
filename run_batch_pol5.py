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
POL5_IMG_DIR = os.path.join(WORKSPACE_DIR, "images", "pol5")
os.makedirs(POL5_IMG_DIR, exist_ok=True)

PROMPTS = {
    3: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'उत्तरदायी सरकार (Accountable Government)'. Showing government official explaining public policies to citizens.
Right card top header: 'जवाबदेही व नियम (Responsibility & Rules)'. Showing constitution book and open procedures.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    4: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'पारदर्शिता (Transparency)'. Showing clear open window to government decisions and public documents.
Right card top header: 'सूचना का अधिकार (Right to Information RTI 2005)'. Showing citizen receiving official information document.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    5: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'जन-आवश्यकताओं की पूर्ति (Meeting Public Needs)'. Showing healthcare, education, and water supply services.
Right card top header: 'जनमत का सम्मान (Respecting Public Opinion)'. Showing leaders listening to public feedback in townhall.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    6: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'वैध सरकार (Legitimate Government)'. Showing democratic election process where people elect their representatives.
Right card top header: 'संविधान का शासन (Rule of Law & Constitution)'. Showing constitutional book and judicial balance scales.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    16: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'स्वतंत्र मीडिया (Independent Media)'. Showing unbiased journalist reporting and public discourse.
Right card top header: 'जन-बहस व जागरूकता (Public Debate & Awareness)'. Showing informed citizens discussing national issues.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    17: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'भ्रष्टाचार पर नियंत्रण (Control on Corruption)'. Showing transparent anti-corruption audit institution.
Right card top header: 'ई-गवर्नेंस (E-Governance & DBT)'. Showing direct benefit transfer digital services to citizens.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    18: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'स्थानीय स्वशासन (Local Self-Government)'. Showing direct citizen participation in Gram Sabha village meeting.
Right card top header: 'पंचायती राज (Panchayati Raj Leadership)'. Showing elected village woman Sarpanch leading local council.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    19: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'शिकायतें: सफलता का प्रमाण (Complaints: Proof of Success)'. Showing active citizens raising issues to improve democracy.
Right card top header: 'सजग नागरिक (Vigilant & Conscious Citizens)'. Showing citizens voting actively and holding leaders accountable.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    20: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'सशक्त लोकतांत्रिक राष्ट्र (Strong Democratic Nation)'. Showing constitutional supremacy, sovereignty, and rule of law.
Right card top header: 'विश्व का विशालतम लोकतंत्र (World Largest Democracy)'. Showing vibrant multi-ethnic population celebrating democracy.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags."""
}

def copy_to_clip(text):
    p = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    p.communicate(input=text.encode('utf-16le'))

async def process_image(gemini_page, idx):
    if idx not in PROMPTS:
        print(f"Error: Prompt {idx} not found in dictionary.", flush=True)
        return False

    out_file = os.path.join(POL5_IMG_DIR, f"pol5_real_{idx}.webp")
    prompt = PROMPTS[idx]

    print(f"\n==================================================", flush=True)
    print(f" GENERATING IMAGE {idx} (Direct DOM Canvas Engine)", flush=True)
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

    # 4. Submit & STRICT VERIFICATION of query count increase
    submitted_ok = False
    for submit_attempt in range(5):
        await gemini_page.evaluate("""() => {
            const sendBtn = document.querySelector('button[aria-label*="Send"], button[aria-label*="भेजें"], button.send-button');
            if (sendBtn) sendBtn.click();
        }""")
        await gemini_page.keyboard.press("Enter")
        await asyncio.sleep(3)

        current_queries = await gemini_page.evaluate("document.querySelectorAll('user-query').length")
        if current_queries > initial_counts['queries']:
            submitted_ok = True
            print(f" Verified Prompt {idx} submitted successfully! (Queries: {initial_counts['queries']} -> {current_queries})", flush=True)
            break
        else:
            print(f" Submit attempt {submit_attempt+1}/5: Retrying submit click...", flush=True)
            await asyncio.sleep(2)

    if not submitted_ok:
        print(f" FATAL ERROR: Could not submit prompt for Image {idx}", flush=True)
        return False

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
        print(f"\n✨ SUCCESS: Image {idx} saved as pol5_real_{idx}.webp!", flush=True)
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
        print(f" STARTING DIRECT DOM CANVAS ENGINE FOR IMAGES: {indices}", flush=True)
        print(f" Connected URL: {gemini_page.url}", flush=True)
        print(f"==================================================", flush=True)

        for i, idx in enumerate(indices):
            out_file = os.path.join(POL5_IMG_DIR, f"pol5_real_{idx}.webp")
            if os.path.exists(out_file):
                try:
                    os.remove(out_file)
                    print(f" Removed old pol5_real_{idx}.webp for clean regeneration.", flush=True)
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
        img_indices = [3, 4, 5, 6, 16, 17, 18, 19, 20]
    asyncio.run(main(img_indices))
