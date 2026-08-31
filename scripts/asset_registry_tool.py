#!/usr/bin/env python3
"""
Global Asset Registry & Smart Search System for NCERT Social Science (Class 10).
Indexes all high-definition visual assets across Economics, Geography, History, and Civics
so that previously generated & verified visuals can be instantly searched, reused, and cross-referenced.
"""

import json
import re
from pathlib import Path
from PIL import Image

REGISTRY_FILE = Path("GLOBAL_ASSET_REGISTRY.json")

# Metadata mapping for curated assets
ASSET_METADATA = {
    # Economics Chapter 1: Development
    "eco1_real_1_landless_laborer.webp": {
        "chapter": "eco1",
        "title": "भूमिहीन ग्रामीण खेतिहर मजदूर",
        "tags": ["laborer", "agriculture", "farmer", "poverty", "मजदूर", "खेती", "किसान", "विकास", "आय"],
        "category": "Agriculture & Labor"
    },
    "eco1_real_4_tribal_dam_displacement.webp": {
        "chapter": "eco1",
        "title": "विशाल बांध निर्माण एवं आदिवासी विस्थापन",
        "tags": ["dam", "displacement", "tribal", "development_conflict", "बांध", "विस्थापन", "आदिवासी", "जल"],
        "category": "Environment & Infrastructure"
    },
    "eco1_real_8_pds_ration_shop.webp": {
        "chapter": "eco1",
        "title": "सार्वजनिक वितरण प्रणाली (PDS) राशन दुकान",
        "tags": ["pds", "ration", "food_security", "fair_price_shop", "राशन", "खाद्य_सुरक्षा", "जन_कल्याण"],
        "category": "Public Welfare"
    },
    "eco1_real_15_economic_inequality_income.webp": {
        "chapter": "eco1",
        "title": "आर्थिक विषमता एवं प्रति व्यक्ति आय",
        "tags": ["inequality", "income", "wealth_gap", "skyscrapers", "विषमता", "आय", "अमीर_गरीब"],
        "category": "Economy & Inequality"
    },
    "eco1_real_18_maternal_healthcare.webp": {
        "chapter": "eco1",
        "title": "मातृ एवं शिशु स्वास्थ्य देखभाल (Primary Clinic)",
        "tags": ["healthcare", "maternal", "infant", "doctor", "clinic", "स्वास्थ्य", "चिकित्सा", "अस्पताल"],
        "category": "Healthcare"
    },
    
    # Economics Chapter 2: Sectors of Economy
    "eco2_real_1_primary_agriculture.webp": {
        "chapter": "eco2",
        "title": "प्राथमिक क्षेत्रक - कृषि एवं सुनहरी फसल कटाई",
        "tags": ["primary_sector", "agriculture", "wheat", "harvesting", "farming", "प्राथमिक_क्षेत्रक", "कृषि", "फसल"],
        "category": "Agriculture"
    },
    "eco2_real_2_primary_dairy.webp": {
        "chapter": "eco2",
        "title": "प्राथमिक क्षेत्रक - आधुनिक डेयरी एवं पशुपालन",
        "tags": ["primary_sector", "dairy", "cattle", "livestock", "milk", "डेयरी", "पशुपालन", "दूध"],
        "category": "Agriculture & Livestock"
    },
    "eco2_real_3_secondary_factory.webp": {
        "chapter": "eco2",
        "title": "द्वितीयक क्षेत्रक - औद्योगिक वस्त्र विनिर्माण मिल",
        "tags": ["secondary_sector", "factory", "textile", "manufacturing", "industry", "द्वितीयक_क्षेत्रक", "कारखाना", "उद्योग"],
        "category": "Manufacturing & Industry"
    },
    "eco2_real_4_tertiary_it_services.webp": {
        "chapter": "eco2",
        "title": "तृतीयक क्षेत्रक - सूचना प्रौद्योगिकी एवं सॉफ्टवेयर सेवा",
        "tags": ["tertiary_sector", "it", "software", "programming", "services", "तृतीयक_क्षेत्रक", "सेवा_क्षेत्रक", "आईटी", "कंप्यूटर"],
        "category": "Services & IT"
    },
    "eco2_real_5_tertiary_banking.webp": {
        "chapter": "eco2",
        "title": "तृतीयक क्षेत्रक - बैंकिंग एवं वित्तीय सेवाएं",
        "tags": ["tertiary_sector", "banking", "finance", "bank_branch", "credit", "बैंकिंग", "बैंक", "ऋण", "वित्तीय_सेवाएं"],
        "category": "Banking & Finance"
    },
    "eco2_real_6_transport_logistics.webp": {
        "chapter": "eco2",
        "title": "सेवा क्षेत्रक - माल परिवहन एवं लॉजिस्टिक्स",
        "tags": ["transport", "logistics", "freight", "railways", "trucks", "परिवहन", "मालगाड़ी", "लॉजिस्टिक्स"],
        "category": "Transport & Infrastructure"
    },
    "eco2_real_7_final_goods_biscuits.webp": {
        "chapter": "eco2",
        "title": "अंतिम वस्तु बनाम मध्यवर्ती वस्तु - बिस्कुट निर्माण",
        "tags": ["final_goods", "biscuit", "food_processing", "gdp", "अंतिम_वस्तु", "बिस्कुट", "खाद्य_प्रसंस्करण"],
        "category": "Manufacturing"
    },
    "eco2_real_8_disguised_unemployment.webp": {
        "chapter": "eco2",
        "title": "प्रच्छन्न बेरोजगारी - 2 हेक्टेयर खेत पर लक्ष्मी का परिवार",
        "tags": ["disguised_unemployment", "laxmi", "underemployment", "small_farm", "प्रच्छन्न_बेरोजगारी", "अल्प_रोजगार", "लक्ष्मी"],
        "category": "Employment & Labor"
    },
    "eco2_real_9_mgnrega_rural_work.webp": {
        "chapter": "eco2",
        "title": "मनरेगा (MGNREGA 2005) - ग्रामीण तालाब खुदाई कार्य",
        "tags": ["mgnrega", "rural_employment", "job_guarantee", "pond_digging", "मनरेगा", "रोजगार_गारंटी", "तालाब"],
        "category": "Rural Employment"
    },
    "eco2_real_10_rural_irrigation_credit.webp": {
        "chapter": "eco2",
        "title": "ग्रामीण सिंचाई नलकूप एवं जल वितरण",
        "tags": ["irrigation", "tubewell", "pump", "water_canal", "crops", "सिंचाई", "नलकूप", "पानी", "फसल"],
        "category": "Agriculture & Water"
    },
    "eco2_real_11_cold_storage_processing.webp": {
        "chapter": "eco2",
        "title": "आधुनिक कोल्ड स्टोरेज एवं कृषि प्रसंस्करण",
        "tags": ["cold_storage", "potatoes", "agri_business", "warehouse", "कोल्ड_स्टोरेज", "भंडारण", "आलू"],
        "category": "Agri-Business"
    },
    "eco2_real_12_tourism_hospitality.webp": {
        "chapter": "eco2",
        "title": "पर्यटन एवं आतिथ्य सेवा रोजगार",
        "tags": ["tourism", "hospitality", "guide", "heritage", "palace", "पर्यटन", "गाइड", "होटल", "धरोहर"],
        "category": "Tourism & Services"
    },
    "eco2_real_13_organized_office_kanta.webp": {
        "chapter": "eco2",
        "title": "संगठित क्षेत्रक - सुरक्षित कार्यालय (कांता का केस)",
        "tags": ["organized_sector", "kanta", "office", "job_security", "pf", "संगठित_क्षेत्रक", "कांता", "कार्यालय", "नौकरी_सुरक्षा"],
        "category": "Organized Employment"
    },
    "eco2_real_14_unorganized_daily_wage.webp": {
        "chapter": "eco2",
        "title": "असंगठित क्षेत्रक - दैनिक दिहाड़ी मजदूर (कमल का केस)",
        "tags": ["unorganized_sector", "kamal", "daily_wage", "grocery_helper", "असंगठित_क्षेत्रक", "कमल", "दिहाड़ी_मजदूर", "किराना"],
        "category": "Unorganized Employment"
    },
    "eco2_real_15_street_vendor_worker.webp": {
        "chapter": "eco2",
        "title": "असंगठित क्षेत्रक - सड़क सब्जी विक्रेता एवं ठेला",
        "tags": ["street_vendor", "vegetable_cart", "informal_economy", "सड़क_विक्रेता", "ठेला", "सब्जी", "अनौपचारिक"],
        "category": "Informal Economy"
    },
    "eco2_real_16_public_railways_infra.webp": {
        "chapter": "eco2",
        "title": "सार्वजनिक क्षेत्रक - भारतीय रेलवे अवसंरचना",
        "tags": ["public_sector", "railways", "infrastructure", "train", "सार्वजनिक_क्षेत्रक", "भारतीय_रेलवे", "रेल"],
        "category": "Public Infrastructure"
    },
    "eco2_real_17_public_hospital_health.webp": {
        "chapter": "eco2",
        "title": "सार्वजनिक क्षेत्रक - सरकारी AIIMS अस्पताल",
        "tags": ["public_sector", "hospital", "healthcare", "aiims", "doctor", "सरकारी_अस्पताल", "एम्स", "स्वास्थ्य"],
        "category": "Public Healthcare"
    },
    "eco2_real_18_private_industry_tata.webp": {
        "chapter": "eco2",
        "title": "निजी क्षेत्रक - टाटा स्टील भारी औद्योगिक संयंत्र",
        "tags": ["private_sector", "tata_steel", "heavy_industry", "blast_furnace", "निजी_क्षेत्रक", "टाटा_स्टील", "उद्योग"],
        "category": "Private Industry"
    },
    "eco2_real_19_rural_dam_canal_infra.webp": {
        "chapter": "eco2",
        "title": "सार्वजनिक अवसंरचना - विशाल सिंचाई बांध व बैराज",
        "tags": ["dam", "barrage", "canal", "public_infra", "irrigation", "बांध", "बैराज", "नहर", "सिंचाई"],
        "category": "Public Infrastructure"
    },
    "eco2_real_20_skill_training_vocational.webp": {
        "chapter": "eco2",
        "title": "व्यावसायिक कौशल विकास एवं तकनीकी कार्यशाला",
        "tags": ["vocational_training", "skill_development", "iti", "technical", "कौशल_विकास", "आईटीआई", "प्रशिक्षण"],
        "category": "Skill & Education"
    }
}

def build_registry():
    registry = []
    root = Path("images")
    
    # 1. First add curated assets
    for filename, meta in ASSET_METADATA.items():
        rel_path = f"images/{meta['chapter']}/{filename}"
        p = Path(rel_path)
        if p.exists():
            im = Image.open(p)
            entry = {
                "id": filename,
                "path": rel_path.replace("\\", "/"),
                "chapter": meta["chapter"],
                "title": meta["title"],
                "tags": meta["tags"],
                "category": meta["category"],
                "dimensions": f"{im.size[0]}x{im.size[1]}",
                "size_kb": p.stat().st_size // 1024
            }
            registry.append(entry)

    # 2. Scan remaining images in images/
    for img_path in sorted(root.glob("**/*.*")):
        if img_path.suffix.lower() in [".webp", ".jpg", ".png", ".svg"]:
            name = img_path.name
            if any(r["id"] == name for r in registry):
                continue
            
            # Generate smart tags from filename
            clean_name = re.sub(r'[\d_.-]+', ' ', name).strip()
            tags = [t.lower() for t in clean_name.split() if len(t) > 2]
            
            dim_str = "SVG"
            if img_path.suffix.lower() != ".svg":
                try:
                    im = Image.open(img_path)
                    dim_str = f"{im.size[0]}x{im.size[1]}"
                except:
                    pass
            
            entry = {
                "id": name,
                "path": str(img_path).replace("\\", "/"),
                "chapter": img_path.parent.name,
                "title": clean_name.title(),
                "tags": tags,
                "category": "General Visual Asset",
                "dimensions": dim_str,
                "size_kb": img_path.stat().st_size // 1024
            }
            registry.append(entry)

    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

    print(f"🎉 Asset Registry built successfully! Total indexed assets: {len(registry)}")

def search_assets(query, limit=5):
    if not REGISTRY_FILE.exists():
        build_registry()
    
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    q = query.lower().strip()
    matches = []
    
    for item in data:
        score = 0
        if q in item["id"].lower():
            score += 10
        if q in item["title"].lower():
            score += 8
        for tag in item["tags"]:
            if q in tag.lower():
                score += 5
        if score > 0:
            matches.append((score, item))
            
    matches.sort(key=lambda x: x[0], reverse=True)
    return [m[1] for m in matches[:limit]]

if __name__ == "__main__":
    build_registry()
    
    # Test search
    print("\n🔍 Test search for 'बैंकिंग':")
    for res in search_assets("बैंकिंग"):
        print(f"  • {res['title']} -> {res['path']} ({res['dimensions']})")

    print("\n🔍 Test search for 'मनरेगा':")
    for res in search_assets("मनरेगा"):
        print(f"  • {res['title']} -> {res['path']} ({res['dimensions']})")
