# 🧪 NCERT Class 10 Science — Lab Simulator Design System
## Master Blueprint v1.0 (Sci Ch.1 + Ch.2 Only)

> **इस MD को किसी भी AI को दो** और कहो:  
> *"इस simulator के लिए `copy_master_sci2.html` में inject होने वाला SVG+JS block बनाओ, SIMULATOR_DESIGN_SYSTEM.md के सभी rules follow करते हुए।"*

---

## 📦 SECTION 0: EXISTING SIMULATORS (Reference)

### Chapter 1 (`copy_master_sci1.html`)
| Box ID | Activity | Type |
|---|---|---|
| `sim1_box` | 1.1 Mg दहन | Static steps image |
| `sim2_box` | 1.2 Pb(NO₃)₂ + KI | Static image |
| `sim12_box` | 1.3 Zn + H₂SO₄ | Static image |
| `sim10_box` | 1.9 CuSO₄ + Fe nail | Static image |
| `sim11_box` | 1.10 Na₂SO₄ + BaCl₂ | Static image |
| `sim13_box` | 1.11 CuO RedOx | Static image |

### Chapter 2 (`copy_master_sci2.html`)
| Box ID | SVG ID | Activity | Animations |
|---|---|---|---|
| `sim2_ind_box` | `sim2_ind_svg` | 2.1 सूचक रंग | Dropper drop, Indicator flash |
| `sim2_olf_box` | `sim2_olf_svg` | 2.2 गंधीय सूचक | Vapor aura |
| `sim2_1_box` | `sim2_1_svg` | 2.3 Zn+H₂SO₄ → H₂ pop | Gas bubbles, tube glow |
| `sim2_zinc_base_box` | – | 2.4 NaOH+Zn → H₂ | Bubbles |
| `sim2_metal_react_box` | `sim2_metal_react_svg` | 2.5 Carbonate+Acid→CO₂ | Bubbles, milky lime water |
| `sim2_carb_box` | – | 2.5B CO₂ test | Lime water |
| `sim2_fire_ext_box` | – | Fire extinguisher CO₂ | Foam spray |
| `sim2_neut_box` | `sim2_neut_svg` | 2.6 Neutralization | Drop, indicator, pH needle |
| `sim2_cuo_box` | `sim2_cuo_svg` | 2.7 CuO+HCl→Blue | Color change |
| `sim2_nonmetal_ox_box` | – | Nonmetal oxide test | |
| `sim2_cond_box` | `sim2_cond_svg` | 2.8 Conductivity | Ions bounce, bulb glow |
| `sim2_dryhcl_box` | – | 2.9 Dry HCl test | |
| `sim2_strong_weak_box` | `sim2_strong_weak_svg` | 2.10 Strong vs Weak Acid | **✅ COMPLETE** Ions bounce, bulb, dropper |
| `sim2_2_box` | `sim2_2_svg` | 2.11 pH Scale | Dropper, pH needle, spectrum |
| `sim2_phtruth_box` | `sim2_phtruth_svg` | 2.11B pH Everyday | Dropdown, dropper, pH reading |
| `sim2_soil_ph_box` | `sim2_soil_svg` | 2.12 Soil pH | Soil beakers, strip dip |
| `sim2_saltfam_box` | `sim2_saltfam_svg` | 2.13 Salt Hydrolysis | pH display, ion animation |
| `sim2_bleach_box` | – | 2.14 Chlor-Alkali | Electrolysis cell |
| `sim2_cryst_box` | – | 2.15 Crystal water CuSO₄ | Color change heating |
| `sim2_pop_setting_box` | – | POP Plaster setting | |

### Chapter 3 (`copy_master_sci3.html`)
| Box ID | SVG ID | Activity | Visual Look & Features |
|---|---|---|---|
| `sim3_oxides_box` | `sim34_olabs_svg` | 3.8 धात्विक (MgO) बनाम अधात्विक (SO₂) ऑक्साइड | **✅ CANONICAL OLABS STANDARD** Light olive wall (`#5a6a34` ➔ `#3c481e`), Certificate frame, Slate table (`#2d3b46` ➔ `#161f26`), 3D Wooden blocks (`#4a301a`), Parchment labels (`#fffff7` ➔ `#eee9ae`), Super-bright glassy borosilicate with 5px white specular strokes (`#ffffff`, 0.88), Electric blue Bunsen flame, Dual mode toggle (`🔬 सिमुलेटर` / `🎬 रियल वीडियो`). |

---

## 🏛️ SECTION 1: CANONICAL OLABS VIRTUAL LAB DESIGN SYSTEM (MANDATORY FOR ALL CHAPTER SIMULATORS)

> [!IMPORTANT]
> **सभी आगामी सिमुलेटरों हेतु स्थायी रूप से सुरक्षित (PERMANENT SPECIFICATION):**
> सभी सिमुलेटरों में बैकग्राउंड, ग्लासवेअर, ज्वाला, लेबल और ड्यूल-मोड का यही प्रामाणिक OLabs वर्चुअल लैब मॉडल लागू रहेगा:
> 1. **Light Olive/Moss Green Wall:** `<linearGradient id="olabs_wall">` (`#5a6a34` ➔ `#4a5928` ➔ `#3c481e`) + गोल्ड फ्रेम में दीवार पर लगा प्रमाण-पत्र (`#b45309`, `#fefce8`)।
> 2. **Charcoal Slate Workbench:** टेबल सतह ग्रेडिएंट `#2d3b46` ➔ `#161f26` + डार्क फ्रंट बेवल किनारा `#0f171d` ➔ `#080c10`।
> 3. **Super-Bright Glassy Apparatus:** क्रिस्टल बोरोसिलिकेट पारदर्शी बॉडी + बाहरी दीवारों पर 5px शुद्ध श्वेत स्पेक्युलर रिफ्लेक्शन आर्क्स (`stroke="#ffffff" stroke-width="5" stroke-linecap="round" opacity="0.88"`), फ्लेयर्ड रिम व लिक्विड मेनिस्कस कर्व।
> 4. **Elevated 3D Wooden Pedestals:** प्रत्येक कांच के उपकरण के नीचे 3D बेवेल्ड डार्क वुड ब्लॉक (`#4a301a` ➔ `#241408`) + टेबल पर 0.45 ड्राप शैडो।
> 5. **Parchment Scroll Paper Labels:** ब्लॉक के नीचे ड्राप-शैडो युक्त क्रीम पार्चमेंट स्क्रॉल बैनर (`#fffff7` ➔ `#eee9ae`, 900 ब्लैक बोल्ड फॉन्ट)।
> 6. **Realistic Dual-Cone Electric Blue Flame:** बर्नर की यथार्थवादी गैस ज्वाला (नीला रूट `#1e3a8a` + इलेक्ट्रिक ब्लू आउटर कोन `#1d4ed8` ➔ `#38bdf8` + चमकदार सायन/श्वेत इनर कोर `#38bdf8` ➔ `#ffffff` + सूक्ष्म GSAP स्केल फ्लिकर)।
> 7. **Dual Mode Standard:** प्रत्येक सिमुलेटर में 16:9 इंटरैक्टिव SVG सिमुलेटर के साथ-साथ HD रियल वीडियो (MP4) टैब स्विच उपलब्ध रहेगा।

---

## 📐 SECTION 1B: STANDARD LAYOUT (हमेशा यही use करो)

### 1.1 SVG Canvas
```
viewBox="0 0 1200 540"

Left Lab Scene:   x=0    to x=718   (718px)
Right Info Panel: x=722  to x=1195  (473px)
```

### 1.2 Zone Map (Left Side 0-718)
```
┌─────────────────────────────────────────────────────────────┐
│  DARK CIRCUIT PANEL  (x=18,y=15, w=682,h=140) #080e08      │  ← bulb/circuit here
├─────────────────────────────────────────────────────────────┤
│                                                              │
│          MAIN LAB AREA  (y=155 to y=448)                    │  ← beaker/apparatus
│          Olive green background                              │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  BENCH TOP    (y=448, h=20)   dark wood                     │
│  BENCH FACE   (y=468, h=72)   darker brown                  │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 Fixed Colors
```
Lab Wall bg:     linearGradient #3d5016 → #4a5c20 → #364a0f  (olive green)
Circuit Panel:   #080e08  opacity=0.92                         (dark = bulb visible)
Panel top line:  #22c55e  h=3px                               (green accent)
Bench top:       #5a3a14 → #2d1e0a
Bench face:      #1a0e04 → #2d1e0a
Shadow under:    fill="#000000" opacity=0.55
```

### 1.4 TEXT RULES (हमेशा — कोई exception नहीं)
```
SVG text:       fill="#000000"   font-weight="900"   (BLACK + BOLD)
Panel labels:   fill="#000000"   font-weight="900"
Bulb label:     fill="#fef08a"   font-weight="900"   (yellow — on dark panel)
Status bar bg:  #f0fdf4          ← LIGHT हमेशा
Status bar text: color:#000000  font-size:19px  font-weight:900
```

### 1.5 HTML Status Bar Template
```html
<div id="[SIM]_status" style="
  margin-top:14px; padding:20px 28px;
  background:#f0fdf4;
  border-left:12px solid #16a34a;
  border-radius:12px;
  font-weight:900; color:#000000;
  font-size:19px; min-height:64px;
  display:flex; align-items:center;
  width:100%; box-sizing:border-box; line-height:1.7;">
  [default status text]
</div>
```

---

## 🔬 SECTION 2: EQUIPMENT SVG LIBRARY

### 2.1 3D GLASS BEAKER (Standard — olive green lab)

**Coordinate Reference:**
```
Center:        cx=310
Left wall:     x=197    Right wall:  x=423
Top rim:       y=200    Bottom:      y=448
Liquid top:    y=300    Liquid bot:  y=445
Cork:          cx=310, cy=196, rx=88, ry=13
L-electrode:   x=269-281, y=88→395
R-electrode:   x=339-351, y=88→395
Ion safe zone: x=215..405, y=318..423  (center of r=15 ion)
Drop tip abs:  (316, 117)  → liquid y=300  → delta=183
```

```svg
<!-- Required defs -->
<linearGradient id="glass3d" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%"   stop-color="#ffffff" stop-opacity="0.75"/>
  <stop offset="8%"   stop-color="#e0f2fe" stop-opacity="0.18"/>
  <stop offset="50%"  stop-color="#bae6fd" stop-opacity="0.06"/>
  <stop offset="88%"  stop-color="#93c5fd" stop-opacity="0.12"/>
  <stop offset="100%" stop-color="#ffffff" stop-opacity="0.50"/>
</linearGradient>
<clipPath id="ionClip_[ID]">
  <rect x="204" y="300" width="212" height="145"/>
</clipPath>

<!-- Beaker shadow -->
<ellipse cx="310" cy="458" rx="125" ry="9" fill="#000000" opacity="0.55"/>

<!-- LIQUID (color/opacity changes by JS) -->
<path id="[ID]_liq" d="M204,300 L204,446 Q310,462 416,446 L416,300 Q310,312 204,300 Z"
      fill="#bae6fd" opacity="0.72"/>
<ellipse id="[ID]_men" cx="310" cy="300" rx="106" ry="12" fill="#bae6fd" opacity="0.88"/>
<ellipse cx="285" cy="298" rx="40" ry="4" fill="#ffffff" opacity="0.28"/>  <!-- shimmer -->

<!-- Glass body -->
<path d="M199,200 L204,446 Q310,462 416,446 L421,200 Q310,218 199,200 Z"
      fill="url(#glass3d)" opacity="1"/>
<!-- Edge strokes (3D effect) -->
<line x1="199" y1="200" x2="204" y2="447" stroke="#ffffff" stroke-width="3" opacity="0.85"/>
<line x1="421" y1="200" x2="416" y2="447" stroke="#ffffff" stroke-width="2.5" opacity="0.6"/>
<ellipse cx="310" cy="200" rx="111" ry="17" fill="none" stroke="#ffffff" stroke-width="3" opacity="0.9"/>
<ellipse cx="310" cy="447" rx="106" ry="14" fill="none" stroke="#ffffff" stroke-width="2.5" opacity="0.7"/>

<!-- CORK -->
<ellipse cx="310" cy="203" rx="91" ry="16" fill="#000" opacity="0.35"/>
<ellipse cx="310" cy="196" rx="88" ry="13" fill="#6b3a1f"/>
<ellipse cx="310" cy="192" rx="88" ry="9"  fill="#7c4a2a"/>
<ellipse cx="290" cy="190" rx="30" ry="4"  fill="#a05a35" opacity="0.6"/>

<!-- ELECTRODES (through cork) -->
<rect x="269" y="88" width="12" height="290" rx="3" fill="#334155" stroke="#64748b" stroke-width="1.2"/>
<rect x="270" y="88" width="3"  height="290" rx="1" fill="#94a3b8" opacity="0.6"/>
<polygon points="269,378 281,378 275,395" fill="#475569"/>
<rect x="339" y="88" width="12" height="290" rx="3" fill="#334155" stroke="#64748b" stroke-width="1.2"/>
<rect x="340" y="88" width="3"  height="290" rx="1" fill="#94a3b8" opacity="0.6"/>
<polygon points="339,378 351,378 345,395" fill="#475569"/>

<!-- Graduation marks -->
<line x1="406" y1="320" x2="422" y2="320" stroke="#ffffff" stroke-width="2" opacity="0.7"/>
<text x="428" y="325" font-size="12" font-weight="900" fill="#ffffff" opacity="0.9">200</text>
<line x1="406" y1="375" x2="422" y2="375" stroke="#ffffff" stroke-width="2" opacity="0.7"/>
<text x="428" y="380" font-size="12" font-weight="900" fill="#ffffff" opacity="0.9">100</text>

<!-- ION GROUP -->
<g id="[ID]_ions" clip-path="url(#ionClip_[ID])"></g>

<!-- BEAKER LABEL -->
<rect x="218" y="460" width="184" height="38" rx="7" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
<text id="[ID]_bk1" x="310" y="479" font-size="13" font-weight="900" fill="#000000" text-anchor="middle">लेबल</text>
<text id="[ID]_bk2" x="310" y="492" font-size="10" font-weight="900" fill="#000000" text-anchor="middle">sublabel</text>
```

---

### 2.2 BATTERY + SWITCH + BULB CIRCUIT

**Coordinate Reference:**
```
Dark Panel:   x=18,y=15, w=682,h=140
Battery:      x=44,y=38, w=88,h=52   (+pin: x=132,y=64)  (-pin: x=44,y=64)
Switch:       cx=222, cy=64
Bulb:         cx=480, cy=64
+ wire:       (132,64)→(222,64)→(237,64)→(465,64)  [red #ef4444]
bulb→R-elec:  (495,64)→(540,64)→(540,116)→(351,116)→(351,88)  [red]
- wire:       (44,64)→(24,64)→(24,116)→(264,116)→(264,88)  [gray #94a3b8]
```

```svg
<!-- Required defs -->
<radialGradient id="bulbHalo" cx="50%" cy="50%" r="50%">
  <stop offset="0%"   stop-color="#fef08a" stop-opacity="0.85"/>
  <stop offset="70%"  stop-color="#fbbf24" stop-opacity="0.30"/>
  <stop offset="100%" stop-color="#fef08a" stop-opacity="0"/>
</radialGradient>
<filter id="bloom" x="-80%" y="-80%" width="260%" height="260%">
  <feGaussianBlur stdDeviation="14"/>
</filter>

<!-- Dark panel -->
<rect x="18" y="15" width="682" height="140" rx="10" fill="#080e08" opacity="0.92"/>
<rect x="18" y="15" width="682" height="3"   rx="2"  fill="#22c55e" opacity="0.5"/>

<!-- Battery -->
<rect x="44" y="38" width="88" height="52" rx="7" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
<line x1="68" y1="52" x2="68" y2="78" stroke="#ef4444" stroke-width="3.5"/>
<line x1="60" y1="59" x2="76" y2="59" stroke="#ef4444" stroke-width="2.5"/>
<line x1="60" y1="70" x2="76" y2="70" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="82" y1="52" x2="82" y2="78" stroke="#ef4444" stroke-width="3.5"/>
<text x="110" y="61" font-size="13" font-weight="900" fill="#f1f5f9">6V</text>
<text x="110" y="78" font-size="11" font-weight="900" fill="#f1f5f9">बैटरी</text>
<text x="38"  y="36" font-size="18" font-weight="900" fill="#ef4444">+</text>
<text x="126" y="36" font-size="18" font-weight="900" fill="#94a3b8">−</text>

<!-- Switch -->
<circle cx="222" cy="64" r="15" fill="#1e293b" stroke="#4ade80" stroke-width="2.5"/>
<text x="222" y="69" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">SW</text>
<line x1="207" y1="64" x2="237" y2="64" stroke="#4ade80" stroke-width="2.5"/>

<!-- Wires -->
<polyline points="132,64 222,64"  fill="none" stroke="#ef4444" stroke-width="3.5"/>
<polyline points="237,64 465,64"  fill="none" stroke="#ef4444" stroke-width="3.5"/>
<polyline points="495,64 540,64 540,116 351,116 351,88" fill="none" stroke="#ef4444" stroke-width="3.5"/>
<polyline points="44,64 24,64 24,116 264,116 264,88"    fill="none" stroke="#94a3b8" stroke-width="3.5"/>

<!-- Bulb halo (GSAP opacity) -->
<circle id="[ID]_halo" cx="480" cy="64" r="62" fill="url(#bulbHalo)" opacity="0.95" filter="url(#bloom)"/>
<!-- Bulb glass -->
<path id="[ID]_bgl"
      d="M462,68 C462,45 498,45 498,68 C498,82 492,88 490,97 L470,97 C468,88 462,82 462,68 Z"
      fill="#fef08a" stroke="#ca8a04" stroke-width="2.2"/>
<path d="M470,84 Q475,75 480,84 Q485,75 490,84" fill="none" stroke="#f59e0b" stroke-width="2.2"/>
<rect x="469" y="97" width="22" height="16" rx="3" fill="#64748b"/>
<rect x="471" y="113" width="18" height="6"  rx="2" fill="#475569"/>
<text id="[ID]_blbl" x="480" y="30" font-size="14" font-weight="900" fill="#fef08a" text-anchor="middle">बल्ब: अत्यंत तीव्र 💡💡</text>
```

---

### 2.3 DROPPER / PIPETTE
```
Group position: translate(296, 32)
Tip local: (20, 85)  →  Absolute: (316, 117)
Liquid surface y=300  →  DROP DELTA y = 183
```

```svg
<g id="[ID]_drp" transform="translate(296,32)">
  <ellipse cx="20" cy="-18" rx="20" ry="15" fill="#7dd3fc" stroke="#0284c7" stroke-width="2"/>
  <rect x="11" y="-3" width="18" height="62" rx="7" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <polygon points="13,59 27,59 24,85 16,85" fill="#7dd3fc" stroke="#0284c7" stroke-width="1.5"/>
  <rect x="-8" y="-42" width="60" height="23" rx="5" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.5"/>
  <text id="[ID]_dlbl" x="20" y="-25" font-size="11" font-weight="900" fill="#000000" text-anchor="middle">HCl अम्ल</text>
</g>
<!-- Drop: tip abs=(316,117), liquid y=300, DELTA=183 -->
<ellipse id="[ID]_drop" cx="316" cy="117" rx="5" ry="9" fill="#60a5fa" opacity="0"
         style="transform-box:fill-box;transform-origin:center;"/>
```

---

### 2.4 pH METER + SPECTRUM BAR
```
Position: translate(140,75)  — inside left lab scene
pH bar x: 0=pH0, 350=pH14  → needle cx = 15 + (pH/14)*350
```

```svg
<g transform="translate(140,75)">
  <rect x="0" y="0" width="380" height="110" rx="12" fill="#ffffff" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="15" y="12" width="350" height="52" rx="8" fill="#f1f5f9" stroke="#94a3b8" stroke-width="2"/>
  <text id="[ID]_phval" x="35" y="50" font-size="34" font-weight="900" fill="#22c55e">pH 7.0</text>
  <text id="[ID]_phname" x="225" y="47" font-size="16" font-weight="800" fill="#0ea5e9">उदासीन</text>
  <!-- pH spectrum: red→green→purple -->
  <defs>
    <linearGradient id="phSpec" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#ef4444"/>
      <stop offset="25%"  stop-color="#fbbf24"/>
      <stop offset="50%"  stop-color="#22c55e"/>
      <stop offset="75%"  stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
  </defs>
  <rect x="15" y="75" width="350" height="16" rx="4" fill="url(#phSpec)"/>
  <!-- Needle (GSAP cx: 15→365) -->
  <circle id="[ID]_needle" cx="190" cy="83" r="7" fill="#ffffff" stroke="#000000" stroke-width="2"/>
  <text x="15"  y="102" font-size="10" font-weight="900" fill="#ef4444">0 (अम्ल)</text>
  <text x="175" y="102" font-size="10" font-weight="900" fill="#22c55e">7</text>
  <text x="308" y="102" font-size="10" font-weight="900" fill="#7c3aed">14 (क्षार)</text>
</g>
```

---

### 2.5 OBSERVATION PANEL (Right Side 722-1195)
```
translate(722,15)
Panel: w=462, h=516, rx=14
Header green: h=52
Card 1: y=62,  h=94  — selected substance
Card 2: y=166, h=94  — equation/reading
Card 3: y=270, h=94  — observation/result
Card 4: y=374, h=134 — NCERT fact box
```

```svg
<g transform="translate(722,15)">
  <rect x="0" y="0" width="462" height="516" rx="14" fill="#ffffff" stroke="#15803d" stroke-width="3"/>
  <rect x="0" y="0"  width="462" height="52" rx="14" fill="#15803d"/>
  <rect x="0" y="38" width="462" height="14"          fill="#15803d"/>
  <text x="231" y="34" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle">📋 [Panel Title]</text>

  <!-- Card 1 -->
  <g transform="translate(14,62)">
    <rect id="[ID]_c1bg" x="0" y="0" width="434" height="94" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="2.2"/>
    <text x="14" y="26" font-size="14" font-weight="900" fill="#000000">[Card1 Title]</text>
    <text id="[ID]_c1b" x="14" y="57" font-size="17" font-weight="900" fill="#000000">[Main line]</text>
    <text id="[ID]_c1s" x="14" y="80" font-size="13" font-weight="900" fill="#000000">[Sub line]</text>
  </g>

  <!-- Card 2 -->
  <g transform="translate(14,166)">
    <rect id="[ID]_c2bg" x="0" y="0" width="434" height="94" rx="10" fill="#fefce8" stroke="#fde047" stroke-width="2.2"/>
    <text x="14" y="26" font-size="14" font-weight="900" fill="#000000">[Card2 Title]</text>
    <text id="[ID]_c2b" x="14" y="57" font-size="17" font-weight="900" fill="#000000">[Main line]</text>
    <text id="[ID]_c2s" x="14" y="80" font-size="13" font-weight="900" fill="#000000">[Sub line]</text>
  </g>

  <!-- Card 3 -->
  <g transform="translate(14,270)">
    <rect id="[ID]_c3bg" x="0" y="0" width="434" height="94" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="2.2"/>
    <text x="14" y="26" font-size="14" font-weight="900" fill="#000000">[Card3 Title]</text>
    <text id="[ID]_c3b" x="14" y="57" font-size="17" font-weight="900" fill="#000000">[Main line]</text>
    <text id="[ID]_c3s" x="14" y="80" font-size="13" font-weight="900" fill="#000000">[Sub line]</text>
  </g>

  <!-- NCERT Facts Card 4 -->
  <g transform="translate(14,374)">
    <rect x="0" y="0" width="434" height="134" rx="10" fill="#fff7ed" stroke="#fed7aa" stroke-width="2.2"/>
    <text x="217" y="26" font-size="15" font-weight="900" fill="#000000" text-anchor="middle">⭐ [Facts Title]</text>
    <text x="14" y="54"  font-size="13" font-weight="900" fill="#000000">• [Fact 1]</text>
    <text x="14" y="78"  font-size="13" font-weight="900" fill="#000000">• [Fact 2]</text>
    <text x="14" y="102" font-size="13" font-weight="900" fill="#000000">• [Fact 3]</text>
    <text x="14" y="126" font-size="13" font-weight="900" fill="#000000">• [Fact 4]</text>
  </g>
</g>
```

---

## ⚡ SECTION 3: ANIMATION LIBRARY (GSAP — Scratch code मत लिखो)

### 3.1 ION BOUNCE (GSAP ticker — beaker walls bounce)
```javascript
/* ── ION BOUNCE PHYSICS ─────────────────────────────────────────
   Safe center zone (r=15 ion): x=215..405, y=318..423
   GSAP ticker runs every frame → updates position → bounces at walls
   ─────────────────────────────────────────────────────────────── */
var BOUNDS = {x1:215, x2:405, y1:318, y2:423};
var ionObjs=[], bTicker=null;

function spawnIons(ionData, groupId) {
  var g=document.getElementById(groupId);
  if(!g) return;
  while(g.firstChild) g.removeChild(g.firstChild);
  ionObjs=[];
  var ns='http://www.w3.org/2000/svg';
  var cols=4, total=ionData.length;
  var bW=BOUNDS.x2-BOUNDS.x1, bH=BOUNDS.y2-BOUNDS.y1;
  ionData.forEach(function(ion,i){
    var col=i%cols, row=Math.floor(i/cols);
    var cw=bW/cols, rh=bH/Math.ceil(total/cols);
    var px=BOUNDS.x1+col*cw+cw*0.2+Math.random()*cw*0.6;
    var py=BOUNDS.y1+row*rh+rh*0.2+Math.random()*rh*0.6;
    px=Math.max(BOUNDS.x1,Math.min(BOUNDS.x2,px));
    py=Math.max(BOUNDS.y1,Math.min(BOUNDS.y2,py));
    var spd=0.4+Math.random()*0.5, ang=Math.random()*Math.PI*2;
    var g2=document.createElementNS(ns,'g');
    g2.setAttribute('transform','translate('+px.toFixed(1)+','+py.toFixed(1)+')');
    g2.setAttribute('opacity','0');
    // glow bg
    var gw=document.createElementNS(ns,'circle');
    gw.setAttribute('r','20'); gw.setAttribute('fill',ion.c); gw.setAttribute('opacity','0.25');
    g2.appendChild(gw);
    // main circle
    var ci=document.createElementNS(ns,'circle');
    ci.setAttribute('r','15'); ci.setAttribute('fill',ion.c);
    ci.setAttribute('stroke','#ffffff'); ci.setAttribute('stroke-width','2.2');
    g2.appendChild(ci);
    // label
    var tx=document.createElementNS(ns,'text');
    tx.setAttribute('x','0'); tx.setAttribute('y','5');
    tx.setAttribute('font-size',ion.s.length>=4?'8':'12');
    tx.setAttribute('font-weight','900'); tx.setAttribute('fill','#ffffff');
    tx.setAttribute('text-anchor','middle'); tx.textContent=ion.s;
    g2.appendChild(tx);
    g.appendChild(g2);
    gsap.to(g2,{opacity:1,duration:0.4,delay:i*0.06,ease:'power2.out'});
    ionObjs.push({el:g2,x:px,y:py,vx:Math.cos(ang)*spd,vy:Math.sin(ang)*spd});
  });
  if(bTicker) gsap.ticker.remove(bTicker);
  bTicker=function(){
    ionObjs.forEach(function(ion){
      ion.x+=ion.vx; ion.y+=ion.vy;
      if(ion.x<BOUNDS.x1){ion.x=BOUNDS.x1;ion.vx=Math.abs(ion.vx);}
      if(ion.x>BOUNDS.x2){ion.x=BOUNDS.x2;ion.vx=-Math.abs(ion.vx);}
      if(ion.y<BOUNDS.y1){ion.y=BOUNDS.y1;ion.vy=Math.abs(ion.vy);}
      if(ion.y>BOUNDS.y2){ion.y=BOUNDS.y2;ion.vy=-Math.abs(ion.vy);}
      ion.el.setAttribute('transform','translate('+ion.x.toFixed(2)+','+ion.y.toFixed(2)+')');
    });
  };
  gsap.ticker.add(bTicker);
}

function killIons(groupId) {
  if(bTicker&&window.gsap){gsap.ticker.remove(bTicker);bTicker=null;}
  ionObjs=[];
  var g=document.getElementById(groupId);
  if(g) while(g.firstChild) g.removeChild(g.firstChild);
}
```

---

### 3.2 DROP FALL (Dropper tip → Liquid)
```javascript
/* DROP_DELTA = liquid_surface_y - dropper_tip_abs_y
   Standard: tip=(316,117), liquid_y=300 → DELTA=183 */
function animDrop(dropId, color, delta, cb) {
  var dr=document.getElementById(dropId);
  if(!dr||!window.gsap){if(cb)cb();return;}
  dr.setAttribute('fill',color);
  gsap.killTweensOf(dr);
  gsap.set(dr,{attr:{cy:117},y:0,scaleX:0.28,scaleY:0.28,opacity:0});
  gsap.timeline()
    .to(dr,{opacity:1,scaleX:1,scaleY:1.5,duration:0.14,ease:'power1.out'})
    .to(dr,{y:delta,duration:0.44,ease:'power2.in'})
    .to(dr,{opacity:0,scaleY:0.08,scaleX:2.5,duration:0.06,
        onComplete:function(){gsap.set(dr,{y:0});if(cb)cb();}});
}
function loopDrop(dropId,color,delta,n){
  if(n<=0)return;
  animDrop(dropId,color,delta,function(){
    setTimeout(function(){loopDrop(dropId,color,delta,n-1);},780);
  });
}
```

---

### 3.3 BULB BRIGHTNESS
```javascript
/* haloOp: 0.95=bright (strong), 0.10=dim (weak), 0.02=off */
function setBulb(haloId, bglId, lblId, haloOp, bglColor, lblText) {
  var h=document.getElementById(haloId);
  var b=document.getElementById(bglId);
  var l=document.getElementById(lblId);
  if(h&&window.gsap) gsap.to(h,{opacity:haloOp,duration:0.8,ease:'power2.out'});
  else if(h) h.style.opacity=haloOp;
  if(b&&window.gsap) gsap.to(b,{attr:{fill:bglColor},duration:0.55});
  else if(b) b.setAttribute('fill',bglColor);
  if(l) l.textContent=lblText;
}
```

---

### 3.4 pH NEEDLE MOVE
```javascript
/* px = 15 + (pH/14)*350   (bar goes from x=15 to x=365) */
function movePHNeedle(needleId, valId, nameId, pH, name) {
  var nx=15+(pH/14)*350;
  var el=document.getElementById(needleId);
  var vl=document.getElementById(valId);
  var nm=document.getElementById(nameId);
  if(el&&window.gsap) gsap.to(el,{attr:{cx:nx},duration:0.8,ease:'elastic.out(1,0.6)'});
  else if(el) el.setAttribute('cx',nx);
  if(vl) vl.textContent='pH '+pH.toFixed(1);
  if(nm) nm.textContent=name;
}
```

---

### 3.5 LIQUID COLOR CHANGE
```javascript
function changeLiquid(liqId, menId, color, opacity) {
  var liq=document.getElementById(liqId);
  var men=document.getElementById(menId);
  opacity=opacity||0.72;
  if(liq&&window.gsap) gsap.to(liq,{attr:{fill:color,'fill-opacity':opacity},duration:0.7});
  else if(liq) liq.setAttribute('fill',color);
  if(men&&window.gsap) gsap.to(men,{attr:{fill:color},duration:0.7});
  else if(men) men.setAttribute('fill',color);
}
```

---

### 3.6 BUBBLE RISE (Gas evolution)
```javascript
function startBubbles(groupId, fromY, toY, count) {
  var g=document.getElementById(groupId);
  if(!g||!window.gsap) return;
  var ns='http://www.w3.org/2000/svg';
  for(var i=0;i<count;i++){
    (function(d){
      var bx=230+Math.random()*160;
      var ci=document.createElementNS(ns,'circle');
      ci.setAttribute('cx',bx); ci.setAttribute('cy',fromY);
      ci.setAttribute('r',4+Math.random()*5);
      ci.setAttribute('fill','none'); ci.setAttribute('stroke','rgba(255,255,255,0.7)');
      ci.setAttribute('stroke-width','1.5'); ci.setAttribute('opacity','0');
      g.appendChild(ci);
      gsap.timeline({repeat:-1,delay:d})
        .set(ci,{attr:{cy:fromY},opacity:0})
        .to(ci,{opacity:0.8,duration:0.2})
        .to(ci,{attr:{cy:toY},duration:1.4+Math.random(),ease:'power1.inOut'})
        .to(ci,{opacity:0,scale:1.5,duration:0.15,transformOrigin:'center'});
    })(i*0.4+Math.random()*0.3);
  }
}
```

---

### 3.7 THERMOMETER RISE
```javascript
/* y=350=cold(0°C), y=165=hot(100°C), maxH=185px */
function setTemp(thermId, celsius) {
  var el=document.getElementById(thermId);
  if(!el) return;
  var h=Math.min(185,(celsius/100)*185);
  var y=350-h;
  if(window.gsap) gsap.to(el,{attr:{y:y,height:h},duration:1.2,ease:'power1.inOut'});
  else{el.setAttribute('y',y);el.setAttribute('height',h);}
}
```

---

### 3.8 INDICATOR FLASH (Phenolphthalein endpoint)
```javascript
function indicatorFlash(liqId, fromColor, toColor) {
  if(!window.gsap) return;
  var el=document.getElementById(liqId);
  gsap.to(el,{attr:{fill:toColor},duration:0.25,repeat:3,yoyo:true,
    onComplete:function(){gsap.to(el,{attr:{fill:toColor},duration:0.8});}});
}
```

---

## 📋 SECTION 4: ACTIVITY CONFIGS

### 4.1 Conductivity Test (`sim2_cond_box`)
```javascript
var condData = {
  hcl:  { ions:[{s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},
                {s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},
                {s:'Cl⁻',c:'#b91c1c'},{s:'Cl⁻',c:'#b91c1c'},{s:'Cl⁻',c:'#b91c1c'},{s:'Cl⁻',c:'#b91c1c'},
                {s:'Cl⁻',c:'#b91c1c'},{s:'Cl⁻',c:'#b91c1c'},{s:'Cl⁻',c:'#b91c1c'},{s:'Cl⁻',c:'#b91c1c'}],
          haloOp:0.95, liqColor:'#bae6fd', bglFill:'#fef08a', bulbText:'तीव्र 💡💡' },
  ch3cooh: { ions:[{s:'H⁺',c:'#1d4ed8'},{s:'H⁺',c:'#1d4ed8'},{s:'Ac⁻',c:'#b45309'},{s:'Ac⁻',c:'#b45309'},
                   {s:'HAc',c:'#78350f'},{s:'HAc',c:'#78350f'},{s:'HAc',c:'#78350f'}],
             haloOp:0.10, liqColor:'#fef9c3', bglFill:'#fef3c7', bulbText:'मंद 🕯️' },
  naoh:  { ions:[{s:'Na⁺',c:'#6d28d9'},{s:'Na⁺',c:'#6d28d9'},{s:'Na⁺',c:'#6d28d9'},{s:'Na⁺',c:'#6d28d9'},
                 {s:'Na⁺',c:'#6d28d9'},{s:'Na⁺',c:'#6d28d9'},{s:'Na⁺',c:'#6d28d9'},{s:'Na⁺',c:'#6d28d9'},
                 {s:'OH⁻',c:'#15803d'},{s:'OH⁻',c:'#15803d'},{s:'OH⁻',c:'#15803d'},{s:'OH⁻',c:'#15803d'},
                 {s:'OH⁻',c:'#15803d'},{s:'OH⁻',c:'#15803d'},{s:'OH⁻',c:'#15803d'},{s:'OH⁻',c:'#15803d'}],
          haloOp:0.95, liqColor:'#dcfce7', bglFill:'#fef08a', bulbText:'तीव्र 💡💡' },
  glucose:{ ions:[], haloOp:0.02, liqColor:'rgba(240,240,200,0.5)', bglFill:'#374151', bulbText:'नहीं जलता ❌' }
};
```

### 4.2 Strong vs Weak Acid (`sim2_strong_weak_box`) ✅ DONE
```
Buttons: HCl (16 ions, bright) / CH₃COOH (7 ions, dim) / NaOH (16 ions, bright) / Reset
Already implemented in file.
```

### 4.3 pH Scale / Everyday (`sim2_2_box`, `sim2_phtruth_box`)
```javascript
var phSubstances = [
  {name:'HCl (तनु)',     pH:1.0, color:'#ef4444', nature:'प्रबल अम्ल',    dropC:'#fca5a5'},
  {name:'नींबू रस',      pH:2.5, color:'#f97316', nature:'दुर्बल अम्ल',   dropC:'#fef08a'},
  {name:'सिरका (Vinegar)',pH:3.0, color:'#fb923c', nature:'दुर्बल अम्ल',  dropC:'#fed7aa'},
  {name:'कॉफ़ी',         pH:5.0, color:'#facc15', nature:'दुर्बल अम्ल',   dropC:'#78350f'},
  {name:'शुद्ध जल',      pH:7.0, color:'#22c55e', nature:'उदासीन',        dropC:'#60a5fa'},
  {name:'रक्त (Blood)',  pH:7.4, color:'#4ade80', nature:'हल्का क्षारीय',  dropC:'#dc2626'},
  {name:'दूध (Milk)',    pH:6.5, color:'#a3e635', nature:'हल्का अम्लीय',   dropC:'#f8fafc'},
  {name:'NaOH (तनु)',    pH:13.0,color:'#7c3aed', nature:'प्रबल क्षारक',   dropC:'#86efac'},
];
```

### 4.4 Salt Hydrolysis (`sim2_saltfam_box`)
```javascript
var saltData = [
  {name:'NaCl',   pH:7.0,  color:'#22c55e', nature:'उदासीन',    hydrolysis:'नहीं'},
  {name:'Na₂CO₃', pH:11.5, color:'#7c3aed', nature:'क्षारीय',   hydrolysis:'CO₃²⁻ + H₂O → HCO₃⁻ + OH⁻'},
  {name:'NH₄Cl',  pH:5.5,  color:'#f97316', nature:'अम्लीय',    hydrolysis:'NH₄⁺ + H₂O → NH₃ + H₃O⁺'},
  {name:'CH₃COONa',pH:9.0, color:'#a855f7', nature:'हल्का क्षार',hydrolysis:'CH₃COO⁻ + H₂O → CH₃COOH + OH⁻'},
];
```

---

## 🎨 SECTION 5: COLOR REFERENCE

### Liquid Colors
| पदार्थ | Fill | Opacity |
|---|---|---|
| HCl | `#bae6fd` | 0.72 |
| H₂SO₄ | `#fca5a5` | 0.60 |
| CH₃COOH | `#fef9c3` | 0.72 |
| NaOH | `#dcfce7` | 0.72 |
| Phenolphthalein+base | `#fbcfe8` | 0.75 |
| Litmus acid | `#ef4444` | 0.65 |
| Litmus base | `#3b82f6` | 0.65 |
| Blood | `#dc2626` | 0.75 |
| Milk | `#f8fafc` | 0.90 |
| Lime water milky | `#e2e8f0` | 0.90 |
| CO₂ in limewater | `rgba(226,232,240,0.95)` | 0.95 |

### Ion Colors
| Ion | Color |
|---|---|
| H⁺ | `#1d4ed8` (blue) |
| Cl⁻ | `#b91c1c` (red) |
| OH⁻ | `#15803d` (green) |
| Na⁺ | `#6d28d9` (purple) |
| CH₃COO⁻ | `#b45309` (amber) |
| SO₄²⁻ | `#0891b2` (cyan) |
| NH₄⁺ | `#0d9488` (teal) |
| Ca²⁺ | `#d97706` (gold) |

### pH to Color (JS function)
```javascript
function phColor(pH){
  if(pH<=1) return '#ef4444';   if(pH<=2) return '#f97316';
  if(pH<=3) return '#fb923c';   if(pH<=4) return '#fbbf24';
  if(pH<=5) return '#facc15';   if(pH<=6) return '#a3e635';
  if(pH<=7) return '#22c55e';   if(pH<=8) return '#38bdf8';
  if(pH<=9) return '#0ea5e9';   if(pH<=10) return '#6366f1';
  if(pH<=11) return '#8b5cf6';  if(pH<=12) return '#a855f7';
  if(pH<=13) return '#7c3aed';  return '#581c87';
}
```

---

## 🐍 SECTION 6: PYTHON PATCH SCRIPT PROTOCOL

```python
"""patch_[name].py — Simulator: [Activity Name]"""
import re, subprocess

HTML = r'c:\Users\jiten\Desktop\class11\ss10\copy_master_sci2.html'
with open(HTML,'r',encoding='utf-8') as f: content=f.read()

# ── 1. Find and replace SVG ──
SVG_ID = '[your_svg_id_here]'
s = content.find('<svg id="'+SVG_ID+'"')
tag_end = content.find('>',s)+1
e = tag_end + content[tag_end:tag_end+15000].find('</svg>') + 6
print(f'SVG: {s}–{e} ({e-s} chars)')

NEW_SVG = content[s:tag_end] + r"""
[... complete SVG content per Section 2 templates ...]
</svg>"""
content = content[:s] + NEW_SVG + content[e:]

# ── 2. Find and replace JS ──
JS_MARKER_START = '[exact first line of old JS block]'
JS_MARKER_END   = '[exact first line of NEXT simulator JS block]'
js_s = content.find(JS_MARKER_START)
js_e = content.find(JS_MARKER_END, js_s+50) if js_s!=-1 else -1
if js_s!=-1 and js_e!=-1:
    content = content[:js_s] + NEW_JS.strip() + '\n\n    ' + content[js_e:]
    print('JS replaced')

# ── 3. Update status bar (LIGHT bg ALWAYS) ──
st = content.find('id="[SIM]_status"')
if st!=-1:
    div_s = content.rfind('<div',0,st)
    div_e = content.find('</div>',st)+6
    content = content[:div_s] + NEW_STATUS + content[div_e:]

# ── 4. Save + check ──
with open(HTML,'w',encoding='utf-8') as f: f.write(content)
m = re.search(r'<script[^>]*>(.*?)</script>',content,re.DOTALL)
if m:
    with open('_chk.js','w',encoding='utf-8') as f: f.write(m.group(1))
    r = subprocess.run(['node','--check','_chk.js'],capture_output=True,text=True)
    print('JS OK!' if r.returncode==0 else 'ERR: '+r.stderr[:300])
```

---

## 📝 SECTION 7: AI PROMPT TEMPLATE

### किसी भी नए simulator के लिए AI को यह दो:

```
तुम्हें NCERT Class 10 Science का एक lab simulator बनाना है।
`SIMULATOR_DESIGN_SYSTEM.md` के सभी rules follow करो।

== SIMULATOR SPEC ==
File:     copy_master_sci2.html
Box ID:   sim2_[name]_box
SVG ID:   sim2_[name]_svg
Activity: [NCERT Activity Number + Name in Hindi]
Chapter:  [1 या 2]

Equipment: (Section 2 से choose करो)
  [ ] Beaker 3D (2.1)          [ ] Battery+Circuit (2.2)
  [ ] Dropper (2.3)            [ ] pH Meter (2.4)
  [ ] Observation Panel (2.5)  [ ] Test tube
  [ ] Bunsen burner            [ ] Thermometer

Animations: (Section 3 से choose करो)
  [ ] Ion Bounce (3.1)         [ ] Drop Fall (3.2)
  [ ] Bulb Glow (3.3)          [ ] pH Needle (3.4)
  [ ] Liquid Color (3.5)       [ ] Bubbles (3.6)
  [ ] Thermometer (3.7)        [ ] Indicator Flash (3.8)

Buttons: [list button names]
Data: [paste data config from Section 4 or write your own]

MANDATORY RULES:
- Status bar: background:#f0fdf4, color:#000000  (LIGHT bg, DARK text)
- All SVG text: fill="#000000" font-weight="900"
- Lab wall: olive green gradient (Section 1.3)
- Dark circuit panel #080e08 if bulb present
- Ion bounce: GSAP ticker (3.1) — never scratch physics loop
- Drop delta: CALCULATE from coordinates — dont guess

Output: Complete Python patch script (Section 6 protocol)
== END SPEC ==
```

---

## ⚠️ SECTION 8: COMMON MISTAKES

| ❌ गलत | ✅ सही |
|---|---|
| Status bar: `background:#1e293b` dark | Status bar: `background:#f0fdf4` light |
| SVG text: `fill="#ffffff"` | SVG text: `fill="#000000"` |
| Ions overflow beaker (unbounded random) | Grid spawn + BOUNDS clamping + `clipPath` |
| GSAP float `±10-12px` | GSAP ticker bounce velocity reversal |
| Drop delta wrong / guessed | Calculate: `delta = liquid_y - tip_abs_y` |
| Bulb invisible on light bg | Dark panel `#080e08` behind circuit always |
| Title banner inside SVG | No SVG banner — title goes in HTML above |
| Wire through beaker body | Wires route above cork level only |
| Scratch physics loop | `gsap.ticker.add(fn)` always |
| `font-weight="800"` | `font-weight="900"` maximum bold |
| Ions radius `r=18` with `±10px` float | Ion `r=15` with `±5px` max velocity |

---

*File: `SIMULATOR_DESIGN_SYSTEM.md`*  
*Project: Class 10 NCERT Science — `copy_master_sci1.html` & `copy_master_sci2.html`*  
*Last Updated: 2026-09-20*
