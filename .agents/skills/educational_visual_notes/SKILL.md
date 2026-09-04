---
name: educational_visual_notes
description: Master protocol for generating 16:9 minimalist clean 2D vector educational visuals and embedding them into Hindi textbook notes websites.
---

# Educational Visual Notes Protocol

## 1. Prompt Standard Guidelines
When generating 2-card 16:9 visual teaching cards for NCERT / Educational textbook websites in Gemini:
1. **Single Top Header Only per Card**:
   - Write headers as: `Left card top header: '...'.` and `Right card top header: '...'.`
   - **NEVER use the word "ONCE" in the prompt text**, as AI image models literally print the English word "ONCE" on top of the image!
2. **Zero Card Numbering**:
   - **DO NOT include numbers** (`1.`, `2.`, `१.`, `२.`) in card titles, subheadings, or diagram labels.
3. **Pure Devanagari Hindi Text + International Numerals**:
   - All text labels must be in Hindi Devanagari, with numbers strictly in Hindu-Arabic format (`1, 2, 3...`).
4. **Clean Classroom Aesthetic**:
   - 16:9 minimalist clean 2D vector educational textbook illustration on a pure solid white background.
   - Flat design, bright primary colors, crisp vector graphics.
   - Zero living politicians, zero real party flags.
5. **Point Sub-headings Badge Styling**:
   - Point sub-headings (e.g. `1. संसद में सरकार से सवाल:`, `1. प्रत्येक उम्मीदवार निर्दलीय (Independent) होगा:`) inside `.img-desc b`, `li b`, `.concept-card b`, `.warn-box b`, `.fact-box b` automatically receive Dark Red text (`#991b1b`), pastel red background (`#fee2e2`), crisp border (`#fca5a5`), and rounded badge padding for high visual contrast.

## 2. Direct DOM Canvas Extraction Protocol (No Modals, No Stale Clipboards)
To save images cleanly from Gemini without opening modal lightboxes or copying old stale clipboard images:
1. Connect Playwright over CDP to the running Chrome instance (`http://localhost:9222`).
2. Submit prompt into the active Gemini page:
   - Clear text box (`Control+A` -> `Backspace`).
   - Paste prompt (`Control+V`).
   - Submit prompt **EXACTLY ONCE** (press Enter once or click Send once). Wait 5 seconds for Gemini to register the new query. Do NOT spam or loop submit button.
3. Wait **95-100 seconds** for image generation.
4. Extract the newly generated image **DIRECTLY from the DOM `model-response` container** using Canvas HTML5 Base64:
   ```javascript
   const responses = document.querySelectorAll('model-response, message-content, div.response-container-content');
   const lastResp = responses[responses.length - 1];
   const targetImg = lastResp.querySelector('img');
   const canvas = document.createElement('canvas');
   canvas.width = targetImg.naturalWidth;
   canvas.height = targetImg.naturalHeight;
   const ctx = canvas.getContext('2d');
   ctx.drawImage(targetImg, 0, 0);
   return canvas.toDataURL('image/png');
   ```
5. Save base64 image data directly as WebP file (`quality=95`).
6. Pause **3.5 minutes (210 seconds)** between generations to prevent rate limits.

## 3. Git Boundaries
- Save all images locally in `images/` directory.
- Link images cleanly in HTML files (`copy_master_*.html`).
- **DO NOT run `git push` to GitHub** until explicitly instructed by the user.
