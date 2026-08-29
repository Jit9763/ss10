#!/usr/bin/env python3
"""
NCERT Social Science GenAI Image Automation Tool
------------------------------------------------
Automates topic-wise image generation using Google GenAI (`google-genai` library)
and inserts them perfectly into NCERT Social Science lesson HTML files.

Usage:
  python ncert_genai_automation_tool.py --html copy_master_hist4.html --subject history --chapter 4
  python ncert_genai_automation_tool.py --html copy_master_geo3.html --subject geography --chapter 3
"""

import os
import sys
import re
import argparse
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

# Try importing google-genai
try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

# Subject Specific Prompt Templates & Visual Guidance
SUBJECT_PROMPT_STYLES = {
    "history": (
        "High-definition educational historical illustration for NCERT History textbook. "
        "Historical authenticity, period-accurate clothing, authentic architectural background, "
        "dramatic realistic museum-style lighting, clear composition, vibrant rich colors, "
        "no text inside image, cinematic archival quality. "
    ),
    "geography": (
        "High-definition geographical visual for NCERT Geography textbook. "
        "Clear physical topography, vibrant natural colors, landscape photography or detailed environmental map diagram, "
        "educational focus, sharp details, no text gibberish, 16:9 widescreen composition. "
    ),
    "civics": (
        "High-definition educational diagram/illustration for NCERT Political Science / Civics textbook. "
        "Clean, modern, clear symbols of democracy, civic engagement, governance, equality, "
        "vector infographics or realistic group interaction visual, bright positive educational palette. "
    ),
    "economics": (
        "High-definition educational visual for NCERT Economics textbook. "
        "Detailed representation of trade, market, currency, production line, banking, or development concept, "
        "clean composition, highly engaging, colorful modern textbook graphic, HD quality. "
    )
}

def clean_slug(text):
    """Generate safe filename slug from topic title."""
    clean = re.sub(r'[^\w\s-]', '', text.lower())
    clean = re.sub(r'[\s_]+', '_', clean).strip('_')
    return clean[:30] if clean else "topic"

def craft_genai_prompt(topic_title, context_text, subject="history", chapter_num=1, topic_idx=1):
    """
    Formulate a precise prompt for Google GenAI Imagen model and a matching Hindi caption.
    """
    style_prefix = SUBJECT_PROMPT_STYLES.get(subject.lower(), SUBJECT_PROMPT_STYLES["history"])
    
    # Extract key English concept if available, or translate context intent
    prompt = f"{style_prefix} Depicting the concept: '{topic_title}'. Context details: {context_text[:200]}. Classroom projector friendly, high resolution, centered subject."
    
    caption = f"चित्र {chapter_num}.{topic_idx}: {topic_title} - पाठ्यक्रमानुसार विषयगत दृश्य।"
    
    return prompt, caption

def generate_image_with_google_genai(prompt, output_path, api_key=None):
    """
    Generate image using `google-genai` Python library (Imagen 3).
    """
    if not HAS_GENAI:
        print("❌ google-genai library is not installed.")
        return False
        
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        print("⚠️ GEMINI_API_KEY environment variable or --api-key flag not set.")
        return False

    try:
        print(f"🎨 Sending prompt to Google GenAI Imagen...")
        client = genai.Client(api_key=key)
        
        result = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                output_mime_type="image/jpeg"
            )
        )
        
        if result.generated_images:
            generated_img = result.generated_images[0]
            # Save raw bytes
            with open(output_path, 'wb') as f:
                f.write(generated_img.image.image_bytes)
            print(f"✅ Image successfully generated and saved to {output_path}")
            return True
        else:
            print("⚠️ No image returned from GenAI model.")
            return False

    except Exception as e:
        print(f"❌ Error generating image via google-genai: {e}")
        return False

def generate_fallback_diagram(topic_title, caption, output_path):
    """
    Fallback diagram generator using PIL if GenAI key is unavailable or fails.
    Ensures 100% uninterrupted file generation without breaking website workflow.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = Image.new('RGB', (820, 460), color=(15, 23, 42)) # Dark navy modern theme
    draw = ImageDraw.Draw(img)
    
    # Outer decorative border
    draw.rectangle([10, 10, 810, 450], outline=(59, 130, 246), width=4)
    draw.rectangle([20, 20, 800, 440], outline=(30, 58, 138), width=2)
    
    # Header text banner inside diagram
    draw.text((410, 80), "NCERT Social Science Educational Visual", fill=(224, 231, 255), anchor="mm")
    draw.text((410, 210), topic_title, fill=(96, 165, 250), anchor="mm")
    draw.text((410, 350), caption[:50] + ("..." if len(caption)>50 else ""), fill=(148, 163, 184), anchor="mm")
    
    img.save(output_path, quality=95)
    print(f"ℹ️ Fallback diagram generated at {output_path}")
    return True

def process_html_file(html_path, subject="history", chapter_num=1, api_key=None, force_replace=False):
    """
    Parses lesson HTML, identifies topic headers, generates images for each topic,
    and inserts standard `.img-box` figure containers automatically.
    """
    path = Path(html_path)
    if not path.exists():
        print(f"❌ File not found: {html_path}")
        return False

    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Prepare images directory
    img_dir_name = f"{subject[:4]}{chapter_num}"
    images_folder = Path("images") / img_dir_name
    images_folder.mkdir(parents=True, exist_ok=True)

    # Find topic headers (.topic-header, .part-header, h2, h3)
    headers = soup.find_all(class_=re.compile(r'(topic-header|part-header|section-header)'))
    if not headers:
        headers = soup.find_all(['h2', 'h3'])

    print(f"📍 Found {len(headers)} topics/sections in {path.name}")
    
    images_created = 0
    for idx, header in enumerate(headers, 1):
        topic_title = header.get_text(strip=True)
        
        # Get next sibling text for context
        context_p = header.find_next_sibling('p')
        context_text = context_p.get_text(strip=True) if context_p else topic_title
        
        slug = clean_slug(topic_title)
        img_filename = f"genai_{img_dir_name}_topic{idx}_{slug}.jpg"
        img_full_path = images_folder / img_filename
        relative_img_src = f"images/{img_dir_name}/{img_filename}"
        
        # Check if next element is already an img-box
        next_sibling = header.find_next_sibling()
        if next_sibling and next_sibling.get('class') and 'img-box' in next_sibling.get('class') and not force_replace:
            print(f"⏩ Image box already exists for Topic {idx}: '{topic_title[:25]}...'. Skipping.")
            continue

        print(f"\n--- Processing Topic {idx}/{len(headers)}: {topic_title} ---")
        prompt, caption = craft_genai_prompt(topic_title, context_text, subject, chapter_num, idx)
        
        success = False
        if api_key or os.environ.get("GEMINI_API_KEY"):
            success = generate_image_with_google_genai(prompt, img_full_path, api_key)
            
        if not success:
            generate_fallback_diagram(topic_title, caption, img_full_path)

        # Build standard .img-box HTML container
        img_box = soup.new_tag('div', attrs={'class': 'img-box'})
        img_tag = soup.new_tag('img', attrs={
            'src': relative_img_src,
            'alt': f"चित्र {chapter_num}.{idx}: {topic_title}",
            'loading': 'lazy'
        })
        caption_div = soup.new_tag('div', attrs={'class': 'img-caption'})
        caption_div.string = caption

        img_box.append(img_tag)
        img_box.append(caption_div)

        # Insert after topic header
        header.insert_after(img_box)
        images_created += 1

    # Save updated HTML file
    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))

    print(f"\n🎉 Successfully updated {path.name}! Inserted {images_created} topic images into website.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GenAI NCERT Image Generator & HTML Inserter")
    parser.add_argument("--html", required=True, help="Path to lesson HTML file")
    parser.add_argument("--subject", default="history", choices=["history", "geography", "civics", "economics"], help="Subject type")
    parser.add_argument("--chapter", type=int, default=1, help="Chapter number")
    parser.add_argument("--api-key", default=None, help="Google GenAI API Key")
    parser.add_argument("--force", action="store_true", help="Force replace existing image boxes")
    
    args = parser.parse_args()
    process_html_file(args.html, args.subject, args.chapter, args.api_key, args.force)
