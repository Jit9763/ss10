import re, os
from PIL import Image

p = 'images/geo7/ai_geo7_6_pipeline_transport.webp'
im = Image.open(p)
print(f"HVJ PIPELINE MAP FILE: {p} ({im.width}x{im.height}, {os.path.getsize(p)} bytes)")

text = open('copy_master_geo7.html', encoding='utf-8').read()
assert p in text, "HVJ Pipeline Map image tag missing in HTML!"
assert 'हजीरा-विजयपुर-जगदीशपुर अंतरराज्यीय प्राकृतिक गैस पाइपलाइन मानचित्र' in text, "HVJ Pipeline Map caption missing in HTML!"

print("SUCCESS: OFFICIAL HINDI HVJ PIPELINE MAP VERIFIED IN HTML AND ON DISK!")
