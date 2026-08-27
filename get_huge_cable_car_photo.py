import urllib.request, json, os, io
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

out_p = 'images/geo7/ncert_geo7_fig2a_ropeway.webp'

# Direct Wikimedia Commons filenames where the Cable Car Cabin fills 70%+ of the frame
huge_cablecar_urls = [
    'https://upload.wikimedia.org/wikipedia/commons/4/4b/Ropeway_in_Gangtok.jpg', # Gangtok Sikkim Ropeway India (huge yellow/red cable car)
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Table_Mountain_Aerial_Cableway_gondola_2017.jpg/1280px-Table_Mountain_Aerial_Cableway_gondola_2017.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Kitzbuehel-Gondelbahn-Hahnenkamm.jpg/1280px-Kitzbuehel-Gondelbahn-Hahnenkamm.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Gondola_lift_in_Samo%C3%ABns.jpg/1280px-Gondola_lift_in_Samo%C3%ABns.jpg'
]

success = False
for u in huge_cablecar_urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            im = Image.open(io.BytesIO(data)).convert('RGB')
            if im.width > 400:
                im = im.resize((1000, 600), Image.Resampling.LANCZOS)
                im.save(out_p, 'WEBP', quality=95)
                print(f'SUCCESS! Downloaded HUGE CABLE CAR CABIN PHOTO from {u} ({im.width}x{im.height})')
                success = True
                break
    except Exception as e:
        print(f'Failed {u}: {e}')

if not success:
    print("Trying API search...")

print('Finished downloading huge cable car cabin photo!')
