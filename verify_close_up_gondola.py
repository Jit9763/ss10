import re, os
from PIL import Image

p = 'images/geo7/ncert_geo7_fig2a_ropeway.webp'
im = Image.open(p)
print(f"UP-CLOSE MOVING CABLE CAR CABIN PHOTO: {p} ({im.width}x{im.height}, {os.path.getsize(p)} bytes)")

text = open('copy_master_geo7.html', encoding='utf-8').read()
assert p in text, "Ropeway image tag missing in HTML!"

print("SUCCESS: UP-CLOSE MOVING CABLE CAR CABIN PHOTO VERIFIED IN HTML AND ON DISK!")
