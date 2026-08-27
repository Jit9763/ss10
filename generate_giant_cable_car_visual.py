import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('images/geo7', exist_ok=True)

W, H = 1000, 600
img = Image.new('RGB', (W, H), (135, 206, 250)) # Bright Sky
draw = ImageDraw.Draw(img)

font_bold = r'C:\Windows\Fonts\mangalb.ttf'
try:
    f_title = ImageFont.truetype(font_bold, 34)
    f_sub = ImageFont.truetype(font_bold, 24)
except:
    f_title = ImageFont.load_default()
    f_sub = ImageFont.load_default()

# -------------------------------------------------------------
# 1. HIMALAYAN SNOW MOUNTAINS & GREEN VALLEYS BACKGROUND
# -------------------------------------------------------------
draw.polygon([(0, 450), (200, 150), (450, 450)], fill=(240, 248, 255)) # Mountain 1
draw.polygon([(150, 450), (200, 150), (260, 450)], fill=(210, 225, 245))

draw.polygon([(350, 450), (700, 100), (1000, 450)], fill=(255, 255, 255)) # Mountain 2
draw.polygon([(620, 450), (700, 100), (780, 450)], fill=(190, 215, 240))

# Green hills in lower midground
draw.polygon([(0, 530), (300, 320), (700, 530)], fill=(34, 139, 34))
draw.polygon([(400, 530), (800, 280), (1000, 530)], fill=(46, 139, 87))

# -------------------------------------------------------------
# 2. HEAVY AERIAL CABLE ROPES (Stretching across top half)
# -------------------------------------------------------------
draw.line([(0, 90), (W, 140)], fill=(20, 20, 20), width=8)  # Top main track cable
draw.line([(0, 110), (W, 160)], fill=(50, 50, 50), width=5) # Haulage cable

# -------------------------------------------------------------
# 3. GIANT CABLE CAR CABIN (Fills 70% of Center Screen)
# -------------------------------------------------------------
# Cable Hanger Arm Assembly attached to cable
draw.rectangle([460, 100, 540, 125], fill=(30, 30, 30)) # Double Wheel Trolley on Cable
draw.line([(500, 125), (500, 220)], fill=(10, 10, 10), width=14) # Heavy steel hanger arm
draw.line([(450, 220), (550, 220)], fill=(10, 10, 10), width=12) # Hanger cross-bar

# Main Gondola Cable Car Body (Vivid Crimson Red & Metallic Yellow)
# Top Roof (White & Yellow)
draw.rounded_rectangle([320, 220, 680, 245], radius=10, fill=(254, 240, 138), outline=(0, 0, 0), width=3)

# Main Passenger Cabin Box
draw.rounded_rectangle([330, 245, 670, 450], radius=25, fill=(220, 38, 38), outline=(255, 255, 255), width=5)
draw.rectangle([330, 350, 670, 450], fill=(234, 179, 8)) # Lower yellow accent section

# Windows (Large Glass Panes showing Passengers)
# Left Window
draw.rounded_rectangle([360, 265, 480, 340], radius=12, fill=(191, 219, 254), outline=(0, 0, 0), width=3)
# Right Window
draw.rounded_rectangle([520, 265, 640, 340], radius=12, fill=(191, 219, 254), outline=(0, 0, 0), width=3)

# Passenger Silhouettes inside Cable Car Cabin
draw.ellipse([395, 285, 445, 335], fill=(30, 41, 59)) # Passenger 1 Head
draw.ellipse([555, 285, 605, 335], fill=(30, 41, 59)) # Passenger 2 Head

# Cabin Door Divider Line & Handles
draw.line([(500, 245), (500, 450)], fill=(0, 0, 0), width=4)
draw.rectangle([485, 330, 495, 360], fill=(200, 200, 200), outline=(0, 0, 0), width=2)
draw.rectangle([505, 330, 515, 360], fill=(200, 200, 200), outline=(0, 0, 0), width=2)

# Cable Car Badge Text
draw.text((410, 375), "ROPEWAY CABLE CAR", fill=(0, 0, 0), font=f_sub)

# -------------------------------------------------------------
# 4. BOTTOM TITLE BANNER
# -------------------------------------------------------------
draw.rectangle([0, H-70, W, H], fill=(6, 95, 70))
draw.text((20, H-62), "चित्र 7.2(a): पहाड़ी क्षेत्रों में रज्जू मार्ग (Ropeway / Cable Car Cabin)", fill=(255, 255, 255), font=f_title)

out_p = 'images/geo7/ncert_geo7_fig2a_ropeway.webp'
img.save(out_p, 'WEBP', quality=95)
print(f"SUCCESS! Saved GIANT UNMISTAKABLE CABLE CAR CABIN PHOTO-GRAPHIC to {out_p} ({img.width}x{img.height})")
