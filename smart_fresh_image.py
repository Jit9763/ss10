import os
import sys
import time
import json
import subprocess
import asyncio
import urllib.request
import pyautogui
from PIL import Image, ImageGrab
from playwright.async_api import async_playwright

pyautogui.FAILSAFE = False

WORKSPACE_DIR = r"c:\Users\jiten\Desktop\class11\ss10"
POL5_IMG_DIR = os.path.join(WORKSPACE_DIR, "images", "pol5")
os.makedirs(POL5_IMG_DIR, exist_ok=True)

PROMPTS = {
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

def activate_chrome_window():
    try:
        wins = pyautogui.getWindowsWithTitle('Gemini')
        if wins:
            wins[0].activate()
            time.sleep(1)
    except Exception as e:
        pass

async def generate_in_fresh_chat(idx):
    if idx not in PROMPTS:
        print(f"Error: Prompt {idx} not found in dictionary.", flush=True)
        return False

    out_file = os.path.join(POL5_IMG_DIR, f"pol5_real_{idx}.webp")
    prompt = PROMPTS[idx]

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://localhost:9222')
        context = browser.contexts[0]
        
        gemini_page = context.pages[0] if len(context.pages) > 0 else None
        if not gemini_page:
            print("FATAL ERROR: Chrome page not found on localhost:9222!", flush=True)
            return False

        print(f"\n==================================================", flush=True)
        print(f" FRESH CHAT GENERATION: IMAGE {idx} / 20", flush=True)
        print(f"==================================================", flush=True)

        # Step 1: Navigate to fresh chat URL to reset state completely
        print(" Step 1: Navigating to Fresh Gemini Chat session...", flush=True)
        await gemini_page.goto('https://gemini.google.com/app')
        await asyncio.sleep(4)

        # Step 2: Clear clipboard & copy prompt
        clear_clipboard()
        copy_to_clip(prompt)
        await asyncio.sleep(1)

        # Step 3: Paste prompt cleanly into fresh text box
        box = gemini_page.locator('rich-textarea div[contenteditable="true"], div[contenteditable="true"]').first
        await box.click()
        await gemini_page.keyboard.press("Control+a")
        await gemini_page.keyboard.press("Backspace")
        await asyncio.sleep(1)
        await gemini_page.keyboard.press("Control+v")
        await asyncio.sleep(2)
        await gemini_page.keyboard.press("Enter")
        print(f" Submitted Prompt {idx} in fresh chat! Waiting 95 SECONDS...", flush=True)

        # Step 4: Wait 95 seconds for generation
        await asyncio.sleep(95)

        # Step 5: Click generated image thumbnail in fresh chat (the ONLY image on screen)
        await gemini_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(2)

        clicked = await gemini_page.evaluate("""() => {
            const imgs = Array.from(document.querySelectorAll('img')).filter(i => 
                (i.src.includes('googleusercontent.com') || i.src.includes('blob:')) && i.width > 200
            );
            if (imgs.length > 0) {
                imgs[imgs.length - 1].click();
                return true;
            }
            return false;
        }""")

        if not clicked:
            print(f" Error: Could not locate image thumbnail for Image {idx} in fresh chat", flush=True)
            return False

        print(f" Clicked generated image thumbnail in fresh chat! Waiting 4s for modal view...", flush=True)
        await asyncio.sleep(4)

        # Step 6: Activate Chrome OS Window & Clear clipboard & Click Copy Image
        activate_chrome_window()
        clear_clipboard()
        await asyncio.sleep(1)

        print(f" Clicking Copy Image button 3 TIMES...", flush=True)
        for c in range(3):
            copy_clicked = await gemini_page.evaluate("""() => {
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

        print(" Waiting 10 SECONDS for Windows clipboard capture...", flush=True)
        await asyncio.sleep(10)

        # Step 7: Save image to file
        success = save_clipboard_to_file(out_file)

        if success:
            print(f"\n✨ SUCCESS: Image {idx} saved as pol5_real_{idx}.webp ({os.path.getsize(out_file)} bytes)!", flush=True)
            return True
        else:
            print(f"\n❌ ERROR: Failed to save Image {idx} from clipboard.", flush=True)
            return False

if __name__ == "__main__":
    img_num = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    asyncio.run(generate_in_fresh_chat(img_num))
