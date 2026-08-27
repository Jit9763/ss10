import urllib.request, json, os, io
from PIL import Image

os.makedirs('images/geo7', exist_ok=True)
headers = {'User-Agent': 'Class10GeoBot/1.0 (contact@example.com)'}

topics_queries = [
    ('ai_geo7_1_golden_quadrilateral', 'Yamuna Expressway India highway'),
    ('ai_geo7_2_indian_railways', 'Vande Bharat Express train India'),
    ('ai_geo7_3_inland_waterways_ganga', 'Ganga river barge vessel'),
    ('ai_geo7_4_major_sea_ports', 'Jawaharlal Nehru Port Mumbai container ship'),
    ('ai_geo7_5_air_transport_northeast', 'Helicopter mountains Nepal Himalaya'),
    ('ai_geo7_6_pipeline_transport', 'Oil pipeline landscape construction'),
    ('ai_geo7_7_communication_satellites', 'INSAT satellite space'),
    ('ai_geo7_8_international_trade', 'Container ship ocean cargo'),
    ('ai_geo7_9_tourism_as_trade', 'Taj Mahal Agra tourists India'),
    ('ai_geo7_10_border_roads_bro', 'Khardung La pass road Ladakh')
]

for name, q in topics_queries:
    out_p = f'images/geo7/{name}.webp'
    url = f'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=10&prop=imageinfo&iiprop=url|size&format=json'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            dl_url = None
            for pid, pinfo in pages.items():
                iinfo = pinfo.get('imageinfo', [{}])[0]
                img_url = iinfo.get('url', '')
                if img_url and any(img_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
                    # Filter out logos/icons
                    if iinfo.get('width', 0) > 400 and iinfo.get('height', 0) > 300:
                        dl_url = img_url
                        break
            if dl_url:
                img_req = urllib.request.Request(dl_url, headers=headers)
                with urllib.request.urlopen(img_req) as img_resp:
                    img_data = img_resp.read()
                    im = Image.open(io.BytesIO(img_data)).convert('RGB')
                    im.save(out_p, 'WEBP', quality=92)
                    print(f'Successfully downloaded REAL PICTURE PHOTO for {name}: {dl_url} ({im.width}x{im.height})')
            else:
                print(f'No photo found for {name}')
    except Exception as e:
        print(f'Error searching/downloading {name}: {e}')

print('Finished downloading topic picture photos!')
