import os
import sys
import time
import subprocess
import asyncio
from PIL import Image, ImageGrab
from playwright.async_api import async_playwright

WORKSPACE_DIR = r"c:\Users\jiten\Desktop\class11\ss10"
POL5_IMG_DIR = os.path.join(WORKSPACE_DIR, "images", "pol5")
os.makedirs(POL5_IMG_DIR, exist_ok=True)

PROMPTS = {
    10: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'प्रगतिशील कर प्रणाली (Progressive Taxation)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing tax collection scale redistributing resources.
Right card top title: 'अवसरों की समानता (Equal Opportunities)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing equal access to education and jobs for all.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    11: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'सामाजिक विविधताएं (Social Diversity)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing peaceful resolution of differences between diverse cultural groups.
Right card top title: 'बहुसांस्कृतिक सह-अस्तित्व (Multicultural Coexistence)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing harmony among different linguistic and religious communities.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    12: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'सर्वसमावेशी लोकतंत्र (Inclusive Democracy)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing decision making that respects minority views, not just majority rule.
Right card top title: 'हर नागरिक को अवसर (Equal Right to Form Majority)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing changing political majorities based on open elections.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    13: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'महिलाओं की गरिमा (Dignity of Women)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing women participating equally in workforce and parliament.
Right card top title: 'कानूनी व सामाजिक समानता (Legal & Social Equality)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing equal legal rights protection emblem for women.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    14: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'वंचित जातियों का सशक्तीकरण (Empowerment of Marginalized Castes)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing dignity and end of discrimination (Article 17).
Right card top title: 'आरक्षण व प्रतिनिधित्व (Reservation & Representation)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing representation in local governance and education.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    15: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'मौलिक स्वतंत्रताएँ (Fundamental Freedoms)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing freedom of speech, expression, and peaceful assembly.
Right card top title: 'न्यायिक संरक्षण (Judicial Protection)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing Supreme Court emblem protecting fundamental rights.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    16: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'स्वतंत्र मीडिया (Independent Media)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing unbiased journalist reporting and public discourse.
Right card top title: 'जन-बहस व जागरूकता (Public Debate & Awareness)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing informed citizens discussing national issues.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    17: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'भ्रष्टाचार पर नियंत्रण (Control on Corruption)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing transparent anti-corruption audit institution.
Right card top title: 'ई-गवर्नेंस (E-Governance & DBT)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing direct benefit transfer digital services to citizens.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    18: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'स्थानीय स्वशासन (Local Self-Government)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing direct citizen participation in Gram Sabha village meeting.
Right card top title: 'पंचायती राज (Panchayati Raj Leadership)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing elected village woman Sarpanch leading local council.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    19: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'शिकायतें: सफलता का प्रमाण (Complaints: Proof of Success)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing active citizens raising issues to improve democracy.
Right card top title: 'सजग नागरिक (Vigilant & Conscious Citizens)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing citizens voting actively and holding leaders accountable.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    20: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'सशक्त लोकतांत्रिक राष्ट्र (Strong Democratic Nation)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing constitutional supremacy, sovereignty, and rule of law.
Right card top title: 'विश्व का विशालतम लोकतंत्र (World Largest Democracy)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing vibrant multi-ethnic population celebrating democracy.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags."""
}

def copy_to_clip(text):
    p = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    p.communicate(input=text.encode('utf-16le'))

def save_clip_image(out_path):
    img = ImageGrab.grabclipboard()
    if img is None:
        return False
    if isinstance(img, list):
        img = Image.open(img[0])
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save(out_path, format="WEBP", quality=95)
    return True

async def run_automation(start_idx=10, end_idx=20):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://localhost:9222')
        context = browser.contexts[0]
        
        gemini_page = None
        for page in context.pages:
            if 'gemini.google.com' in page.url:
                gemini_page = page
                break
                
        if not gemini_page:
            print("Error: Gemini tab not found!")
            return

        print(f"Connected to Gemini Tab: {gemini_page.url}")

        for idx in range(start_idx, end_idx + 1):
            out_file = os.path.join(POL5_IMG_DIR, f"pol5_real_{idx}.webp")
            if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
                print(f"Skipping pol5_real_{idx}.webp (already exists).")
                continue

            print(f"\n==========================================")
            print(f" Processing Image {idx} / {end_idx}...")
            print(f"==========================================")

            # Copy prompt
            prompt = PROMPTS[idx]
            copy_to_clip(prompt)
            print(f"Prompt {idx} copied to clipboard.")

            # Close any open modal
            await gemini_page.evaluate("""() => {
                const closeBtn = document.querySelector('button[aria-label="Close"], button[aria-label="बंद करें"]');
                if (closeBtn) closeBtn.click();
            }""")
            await asyncio.sleep(1)

            # Focus text box in Gemini via evaluate JS
            focused = await gemini_page.evaluate("""() => {
                const el = document.querySelector('div[contenteditable="true"], rich-textarea div[contenteditable="true"]');
                if (el) {
                    el.focus();
                    return true;
                }
                return false;
            }""")
            
            if not focused:
                print("Fallback clicking prompt box...")
                await gemini_page.mouse.click(600, 880)
            await asyncio.sleep(1)

            # Paste
            await gemini_page.keyboard.press("Control+v")
            await asyncio.sleep(2)

            # Submit
            submitted = await gemini_page.evaluate("""() => {
                const btn = document.querySelector('button[aria-label*="Send"], button[aria-label*="भेजें"], .send-button');
                if (btn) {
                    btn.click();
                    return true;
                }
                return false;
            }""")
            
            if not submitted:
                await gemini_page.keyboard.press("Enter")

            print(f"Submitted prompt {idx}. Waiting 42 seconds for generation...")
            await asyncio.sleep(42)

            # Click last generated image or copy button directly via JS evaluation
            clicked_copy = await gemini_page.evaluate("""() => {
                // Check if copy button exists on the page
                const allButtons = Array.from(document.querySelectorAll('button'));
                const copyButtons = allButtons.filter(b => {
                    const aria = (b.getAttribute('aria-label') || '').toLowerCase();
                    const tooltip = (b.getAttribute('data-tooltip') || '').toLowerCase();
                    return aria.includes('copy') || tooltip.includes('copy') || aria.includes('कॉपी');
                });
                if (copyButtons.length > 0) {
                    const lastCopyBtn = copyButtons[copyButtons.length - 1];
                    lastCopyBtn.click();
                    return "clicked_last_copy_btn";
                }

                // If no copy button directly visible, click the last generated image to open modal
                const images = Array.from(document.querySelectorAll('img')).filter(img => 
                    img.src.includes('googleusercontent.com') || img.src.includes('blob:')
                );
                if (images.length > 0) {
                    images[images.length - 1].click();
                    return "clicked_image_modal";
                }
                return "none";
            }""")

            print(f"JS action result: {clicked_copy}")
            await asyncio.sleep(2)

            if clicked_copy == "clicked_image_modal":
                # Now click copy button inside open modal
                await gemini_page.evaluate("""() => {
                    const allButtons = Array.from(document.querySelectorAll('button'));
                    const copyButtons = allButtons.filter(b => {
                        const aria = (b.getAttribute('aria-label') || '').toLowerCase();
                        return aria.includes('copy') || aria.includes('कॉपी');
                    });
                    if (copyButtons.length > 0) {
                        copyButtons[copyButtons.length - 1].click();
                    }
                }""")
                await asyncio.sleep(2)

            # Save from clipboard
            if save_clip_image(out_file):
                print(f"SUCCESS: Saved pol5_real_{idx}.webp!")
            else:
                print(f"WARNING: Clipboard grab failed for Image {idx}")

            # Close modal if opened
            await gemini_page.evaluate("""() => {
                const closeBtn = document.querySelector('button[aria-label="Close"], button[aria-label="बंद करें"]');
                if (closeBtn) closeBtn.click();
            }""")
            await asyncio.sleep(2)

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    asyncio.run(run_automation(start, end))
