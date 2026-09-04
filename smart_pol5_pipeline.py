import os
import sys
import time
import subprocess
import asyncio
import pyautogui
from PIL import Image, ImageGrab
from playwright.async_api import async_playwright

pyautogui.FAILSAFE = False

WORKSPACE_DIR = r"c:\Users\jiten\Desktop\class11\ss10"
POL5_IMG_DIR = os.path.join(WORKSPACE_DIR, "images", "pol5")
os.makedirs(POL5_IMG_DIR, exist_ok=True)

PROMPTS = {
    12: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'सर्वसमावेशी लोकतंत्र (Inclusive Democracy)'. Showing decision making that respects minority views, not just majority rule.
Right card top header: 'हर नागरिक को अवसर (Equal Right to Form Majority)'. Showing changing political majorities based on open elections.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    14: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'वंचित जातियों का सशक्तीकरण (Empowerment of Marginalized Castes)'. Showing dignity and end of discrimination (Article 17).
Right card top header: 'आरक्षण व प्रतिनिधित्व (Reservation & Representation)'. Showing representation in local governance and education.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    15: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top header: 'मौलिक स्वतंत्रताएँ (Fundamental Freedoms)'. Showing freedom of speech, expression, and peaceful assembly.
Right card top header: 'न्यायिक संरक्षण (Judicial Protection)'. Showing Supreme Court emblem protecting fundamental rights.
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

def clear_clipboard():
    try:
        p = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
        p.communicate(input=b'')
    except Exception as e:
        pass

def copy_to_clip(text):
    p = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    p.communicate(input=text.encode('utf-16le'))

def save_clipboard_to_file(out_path):
    img = ImageGrab.grabclipboard()
    if img is None:
        return False
    if isinstance(img, list):
        img = Image.open(img[0])
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save(out_path, format="WEBP", quality=95)
    return os.path.exists(out_path) and os.path.getsize(out_path) > 10000

async def force_close_modal(page):
    for _ in range(3):
        await page.keyboard.press("Escape")
        await asyncio.sleep(0.5)
        await page.evaluate("""() => {
            const closeBtns = document.querySelectorAll('button[aria-label="Close"], button[aria-label="बंद करें"], button[aria-label="close"]');
            closeBtns.forEach(btn => btn.click());
        }""")
        await asyncio.sleep(0.5)

async def process_single_image(page, idx):
    out_file = os.path.join(POL5_IMG_DIR, f"pol5_real_{idx}.webp")
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"Skipping Image {idx}: pol5_real_{idx}.webp already exists.", flush=True)
        return True

    print(f"\n==================================================", flush=True)
    print(f" PROCESSING IMAGE {idx} / 20 (Clean Header Mode)", flush=True)
    print(f"==================================================", flush=True)

    # 1. Clear clipboard before starting
    clear_clipboard()
    await asyncio.sleep(1)

    # 2. Force close any existing modal preview
    await force_close_modal(page)
    await asyncio.sleep(2)

    # 3. Scroll to bottom of chat window
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await asyncio.sleep(2)

    # 4. Copy prompt N to clipboard
    prompt = PROMPTS[idx]
    copy_to_clip(prompt)
    await asyncio.sleep(1)

    # 5. Clear text box & paste prompt via Playwright keyboard commands
    box = page.locator('rich-textarea div[contenteditable="true"], div[contenteditable="true"]').first
    await box.click()
    await page.keyboard.press("Control+a")
    await page.keyboard.press("Backspace")
    await asyncio.sleep(1)
    await page.keyboard.press("Control+v")
    await asyncio.sleep(2)
    print(f" Cleanly pasted Prompt {idx} into Gemini input box!", flush=True)

    # 6. Click Submit
    submitted = await page.evaluate("""() => {
        const sendBtn = document.querySelector('button[aria-label*="Send"], button[aria-label*="भेजें"], button.send-button');
        if (sendBtn) {
            sendBtn.click();
            return true;
        }
        return false;
    }""")
    if not submitted:
        await page.keyboard.press("Enter")

    print(f" Submitted prompt {idx}! Waiting 95 SECONDS for new image generation...", flush=True)
    await asyncio.sleep(95)

    # 7. Scroll down to bottom
    await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await asyncio.sleep(3)

    # 8. Click image inside the LAST model-response container specifically
    img_opened = await page.evaluate("""() => {
        const responses = Array.from(document.querySelectorAll('model-response, message-content, div.response-container-content'));
        if (responses.length === 0) return false;
        
        const lastResp = responses[responses.length - 1];
        const imgs = Array.from(lastResp.querySelectorAll('img')).filter(img => 
            img.src.includes('googleusercontent.com') || img.src.includes('blob:')
        );
        if (imgs.length > 0) {
            const targetImg = imgs[imgs.length - 1];
            targetImg.scrollIntoView({behavior: 'smooth', block: 'center'});
            targetImg.click();
            return true;
        }
        return false;
    }""")

    if not img_opened:
        print(f" Warning: Could not find image in latest model-response container for Image {idx}", flush=True)
        return False

    print(f" Clicked FRESH image in latest model response! Waiting 5s for modal preview...", flush=True)
    await asyncio.sleep(5)

    # 9. Clear clipboard before copying
    clear_clipboard()
    await asyncio.sleep(1)

    # 10. Click Copy Image button 3 TIMES inside modal preview
    print(f" Clicking Copy Image button 3 TIMES...", flush=True)
    for c in range(3):
        copy_clicked = await page.evaluate("""() => {
            const buttons = Array.from(document.querySelectorAll('button'));
            const copyBtn = buttons.find(b => {
                const aria = (b.getAttribute('aria-label') || '').toLowerCase();
                return aria.includes('copy image') || aria.includes('इमेज कॉपी');
            });
            if (copyBtn) {
                copyBtn.click();
                return true;
            }
            return false;
        }""")
        if not copy_clicked:
            pyautogui.click(1820, 50)
        await asyncio.sleep(1.5)

    # 11. Wait 10 SECONDS after copying!
    print(" Waiting 10 SECONDS after copying to capture clipboard...", flush=True)
    await asyncio.sleep(10)

    # 12. Save clipboard image to disk
    success = save_clipboard_to_file(out_file)

    # 13. Force close modal
    await force_close_modal(page)
    await asyncio.sleep(4)

    if success:
        print(f" SUCCESS: Saved unique image for Image {idx} -> pol5_real_{idx}.webp ({os.path.getsize(out_file)} bytes)", flush=True)
        return True
    else:
        print(f" ERROR: Failed to save Image {idx} from clipboard.", flush=True)
        return False

async def main(start_idx=12, end_idx=20):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://localhost:9222')
        context = browser.contexts[0]
        
        gemini_page = None
        for page in context.pages:
            if 'gemini.google.com' in page.url:
                gemini_page = page
                break
                
        if not gemini_page:
            print("FATAL ERROR: Gemini browser tab not found on localhost:9222!", flush=True)
            return

        print(f"==================================================", flush=True)
        print(f" Starting Clean Header Response Pipeline (Images {start_idx} to {end_idx})", flush=True)
        print(f" Connected Tab: {gemini_page.url}", flush=True)
        print(f"==================================================", flush=True)

        for idx in range(start_idx, end_idx + 1):
            if idx == 13: # Already saved
                continue
            res = await process_single_image(gemini_page, idx)
            if not res:
                print(f"Retrying Image {idx} once more...", flush=True)
                await force_close_modal(gemini_page)
                await asyncio.sleep(5)
                await process_single_image(gemini_page, idx)

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    asyncio.run(main(start, end))
