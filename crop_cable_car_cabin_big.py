import urllib.request, io
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

u = 'https://upload.wikimedia.org/wikipedia/commons/3/31/Gondola_or_Cable_car_at_Gulmarg%2C_Kashmir%2C_India.jpg'
out_p = 'images/geo7/ncert_geo7_fig2a_ropeway.webp'

req = urllib.request.Request(u, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = resp.read()
    im = Image.open(io.BytesIO(data)).convert('RGB')
    print(f'Original image size: {im.width}x{im.height}')
    
    # Crop right around the cable car cabin hanging on the rope in the center
    # In this high-res image, the yellow/red cable car cabin is in the center-left
    W_orig, H_orig = im.width, im.height
    
    # Let's crop the central 50% region focusing right on the cable car cabin
    left = int(W_orig * 0.15)
    top = int(H_orig * 0.20)
    right = int(W_orig * 0.85)
    bottom = int(H_orig * 0.80)
    
    cabin_crop = im.crop((left, top, right, bottom))
    cabin_crop = cabin_crop.resize((1000, 600), Image.Resampling.LANCZOS)
    cabin_crop.save(out_p, 'WEBP', quality=95)
    print(f'SUCCESS! Cropped BIG & CLEAR CABLE CAR CABIN: {out_p} ({cabin_crop.width}x{cabin_crop.height})')
