# 🛡️ Quality Audit & Verification Protocol (AUDIT_PROTOCOL.md)

## 📌 उद्देश्य (Objective)
इस दस्तावेज़ का उद्देश्य कक्षा 10 विज्ञान के प्रत्येक HTML चैप्टर (`copy_master_sci*.html` एवं `qa_master_sci*.html`) के लिए एक कठोर, 4-स्तरीय गुणवत्ता सत्यापन प्रोटोकॉल स्थापित करना है। 

शिक्षक या विद्यार्थी द्वारा किसी भी फाइल को खोलने से पहले निम्नलिखित **4 प्रमुख स्तंभों (Four Pillars of Quality)** का 100% त्रुटिरहित होना अनिवार्य है:
1. **गणित, सूत्र एवं रासायनिक समीकरण (Math, Equations & Formulas)**
2. **जावास्क्रिप्ट एवं कंसोल एरर्स (JavaScript, Events & Timers)**
3. **सिमुलेटर कार्यप्रणाली एवं 16:9 दृश्य (Simulator Execution & Visibility)**
4. **हिंदी वर्तनी, मात्राएं एवं वैज्ञानिक शब्दावली (Spelling & Hindi Terminology)**

---

## 🧮 स्तंभ 1: गणित, समीकरण व MathJax सत्यापन (Math & Equations)

### 1.1 संतुलित रासायनिक समीकरण (Balanced Chemical Equations)
- प्रत्येक रासायनिक समीकरण में अभिकारकों (Reactants) और उत्पादों (Products) के परमाणुओं की संख्या पूर्णतः संतुलित होनी चाहिए।
- भौतिक अवस्थाओं का सही अंकन: ठोस `(s)`, द्रव `(l)`, गैस `(g)`, जलीय विलयन `(aq)`।
- विशेष तीर संकेत:
  - गैस उत्सर्जन: `↑` (उदा. `H₂(g)↑`, `CO₂(g)↑`)
  - अवक्षेप निर्माण: `↓` (उदा. `BaSO₄↓`, `CaCO₃↓`)
  - ताप / उत्प्रेरक: `🔥` या तीर के ऊपर ताप (उदा. `373 K`, `सूर्य का प्रकाश`)।

### 1.2 सबस्क्रिप्ट व सुपरस्क्रिप्ट (Subscripts & Superscripts)
- रासायनिक सूत्रों में आयन आवेश और परमाणुओं की संख्या शुद्ध होनी चाहिए:
  - सही: `H₂SO₄`, `Ca(OH)₂`, `Na₂ZnO₂`, `CuSO₄·5H₂O`, `CaSO₄·½H₂O`
  - गलत: `H2SO4`, `Ca(OH)2`, `CuSO4.5H2O`
  - आयन: `H⁺`, `OH⁻`, `Cl⁻`, `SO₄²⁻`, `Na⁺`, `Cu²⁺`

### 1.3 संख्यात्मक गणनाएं व भौतिकी सूत्र (Physics Numericals)
- विद्युत (अध्याय 11) एवं प्रकाश (अध्याय 9) में:
  - ओम का नियम: `V = IR`, श्रेणीक्रम `R = R₁ + R₂`, पार्श्वक्रम `1/R = 1/R₁ + 1/R₂`
  - दर्पण सूत्र `1/f = 1/v + 1/u`, लेंस सूत्र `1/f = 1/v - 1/u`
  - मात्रक (Units) अनिवार्य: वोल्ट (V), एम्पियर (A), ओम (Ω), जूल (J), वाट (W)।

---

## ⚡ स्तंभ 2: जावास्क्रिप्ट एवं कंसोल एरर सत्यापन (JavaScript & Runtime)

### 2.1 शून्य सिंटैक्स एरर नियम (Zero Syntax Error Mandate)
- किसी भी जावास्क्रिप्ट कोड को HTML में शामिल करने से पहले `node -c` द्वारा टेस्ट किया जाना अनिवार्य है।
- **गंभीर सबक (Quote Escaping Rule):**
  - यदि स्ट्रिंग सिंगल कोट्स `'...'` में है, तो उसके भीतर कभी भी अनएस्केप्ड सिंगल कोट `'` न डालें!
  - ❌ गलत: `'नीली ज्वाला व 💥 'पॉप' (POP) ध्वनि'`  ➔ *Browser SyntaxError: Unexpected identifier 'पॉप'*
  - ✔ सही: `'नीली ज्वाला व 💥 \'पॉप\' (POP) ध्वनि'` या `"नीली ज्वाला व 💥 'पॉप' (POP) ध्वनि"`

### 2.2 ऑनक्लिक हैंडलर सत्यापन (Onclick Handler Integrity)
- HTML के प्रत्येक बटन का `onclick="functionName()"` सीधे जावास्क्रिप्ट में मौजूद होना चाहिए।
- कोई भी अघोषित (undefined) फंक्शन कॉल नहीं होनी चाहिए।

### 2.3 टाइमर आइसोलेशन (Timer Safety)
- किसी भी सिमुलेटर में `setTimeout` का उपयोग होने पर उसे `addSimTimer(simId, timer)` में रजिस्टर करें।
- सिमुलेटर रिसेट होते ही `clearSimTimers(simId)` द्वारा सभी टाइमर समाप्त होने चाहिए ताकि बैकग्राउंड टाइमर दूसरे प्रयोग में बाधा न डालें।

### 2.4 स्क्रिप्ट टैग प्लेसमेंट नियम
- इनलाइन जावास्क्रिप्ट को सदैव पेज के सबसे नीचे स्थित मुख्य `<script>` टैग में रखें।
- `<script src="...">` वाले बाहरी सीडीएन टैग के भीतर कभी भी इनलाइन कोड न डालें।

---

## 🔬 स्तंभ 3: सिमुलेटर कार्यप्रणाली व 16:9 लैब स्टेज (Simulators Execution)

### 3.1 16:9 पैनोरमिक विजुअल स्टेज
- **आस्पेक्ट रेशियो:** `aspect-ratio: 1200 / 540 !important;`
- **न्यूनतम ऊंचाई (Min-Height):** `min-height: 540px !important;` (प्रोजेक्टर और स्मार्ट टीवी पर बड़े और स्पष्ट दृश्य हेतु)।
- **थीम:** `background: linear-gradient(180deg, #dcfce7 0%, #bbf7d0 100%) !important; border: 3px solid #16a34a !important;`

### 3.2 स्प्लिट-स्क्रीन प्रेक्षण पैनल (Split-Screen Apparatus & Observation)
- बायां भाग (0 से 720px): स्पष्ट 3D उपकरण, स्टैंड, परखनली, बीकर, गैस निकास, ज्वाला।
- दायां भाग (725 से 1175px): व्हाइट कार्ड, 450px चौड़ाई, संतुलित समीकरण, रंग परिवर्तन और वैज्ञानिक निष्कर्ष।

### 3.3 इंटरैक्शन सत्यापन (Interaction Check)
- **ऑटो-प्ले बटन:** 1-क्लिक में पूरा प्रयोग चरणबद्ध समय अंतराल पर चलना चाहिए।
- **मैनुअल स्टेप बटन:** प्रत्येक चरण (1, 2, 3...) पर क्लिक करने पर संबंधित घटक (रंग, बुलबुले, आग, पाठ) में दृश्यमान परिवर्तन होना चाहिए।
- **रीसेट बटन:** प्रयोग को तुरंत उसकी मूल प्रारंभिक स्थिति में लौटाना चाहिए।

---

## ✍️ स्तंभ 4: हिंदी वर्तनी, मात्राएं एवं वैज्ञानिक शब्दावली (Hindi Spelling & Typos)

### 4.1 मानक वैज्ञानिक हिंदी शब्दावली (Standard NCERT Terminology)
| अशुद्ध / सामान्य वर्तनी | शुद्ध NCERT मानक वर्तनी | अंग्रेजी पर्याय |
|---|---|---|
| फीनोफ्थलीन / फिनोफथलीन | **फिनॉल्फथलीन** | Phenolphthalein |
| उदासीनीकरन / उदासीनीकरण | **उदासीनीकरण** | Neutralization |
| कृयाकलाप / क्रीयाकलाप | **क्रियाकलाप** | Activity |
| विरंजक चुरण | **विरंजक चूर्ण** | Bleaching Powder |
| क्रिस्टलन का पानी | **क्रिस्टलन का जल** | Water of Crystallization |
| अवछेप / अवक्षेप | **अवक्षेप** | Precipitate |
| हाइड्रोक्लोरिक एसम | **हाइड्रोक्लोरिक अम्ल** | Hydrochloric Acid |
| सल्फ्यूरिक एसम | **सल्फ्यूरिक अम्ल** | Sulphuric Acid |
| बुदबुदाहट / बुदबुदाना | **तीव्र बुदबुदाहट (सनसनाहट)** | Effervescence |
| उभयधर्मी आक्साइड | **उभयधर्मी ऑक्साइड** | Amphoteric Oxide |
| क्लोर-अल्कली / क्लोर-एल्कली | **क्लोर-क्षार प्रक्रिया** | Chlor-Alkali Process |

### 4.2 भाषा व कोष्ठक नियम
- प्रत्येक मुख्य वैज्ञानिक अवधारणा के साथ कोष्ठक में उसका मानक अंग्रेजी नाम लिखा होना चाहिए (उदा: `सोडियम हाइड्रोजनकार्बोनेट (NaHCO₃ / Baking Soda)`).
- संख्याओं के लिए अंतरराष्ट्रीय अंकों (`1, 2, 3...`) का प्रयोग किया जाए ताकि छात्र परीक्षा में आसानी से समझ सकें।

---

## 🛠️ 5. Automated Python Audit Script (स्वचालित ऑडिट कमांड)

प्रत्येक अध्याय को रिलीज़ करने से पहले निम्नलिखित स्वचालित पायथन ऑडिट चलाना अनिवार्य है:

```bash
python -c "
# Automated Chapter Verification Suite
import os, re, subprocess

fpath = r'c:\Users\jiten\Desktop\class11\ss10\copy_master_sci2.html'
with open(fpath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Check JS Syntax with Node
scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', text, re.DOTALL)
main_js = [s for s in scripts if len(s.strip()) > 50][-1]
with open('temp_test.js', 'w', encoding='utf-8') as tf:
    tf.write(main_js)
res = subprocess.run(['node', '-c', 'temp_test.js'], capture_output=True, text=True)
assert res.returncode == 0, f'JS Syntax Error: {res.stderr}'
print('✔ JS Syntax: 100% Clean')

# 2. Check Simulators count & stage size
sims = re.findall(r'class=\"sim-card\"', text)
print(f'✔ Simulators found: {len(sims)}')
assert 'min-height: 540px' in text, 'Simulator min-height must be 540px+'

# 3. Check unescaped quotes
assert not re.search(r'innerHTML\s*=\s*\'[^\']*\'[^\']*\';', text), 'Unescaped quote pattern detected!'
print('✔ Quotes Integrity: Clean')

print('🎉 CHAPTER AUDIT PASSED!')
"
```

---

## 📋 6. Chapter Release Sign-off Checklist (अंतिम सत्यापन चेकलिस्ट)
- [ ] **Math & Equations:** क्या सभी रासायनिक समीकरण संतुलित व सबस्क्रिप्ट युक्त हैं?
- [ ] **JavaScript:** क्या `node -c` में शून्य एरर आया और ब्राउज़र कंसोल 100% शांत है?
- [ ] **Simulators:** क्या सभी सिमुलेटर 16:9 (`1200x540`), बड़े साइज (`min-height: 540px`) और लाइट ग्रीन लैब थीम में हैं?
- [ ] **Onclick Handlers:** क्या सभी बटनों के फंक्शन सही से रेस्पॉन्ड कर रहे हैं?
- [ ] **Spelling & Typos:** क्या फिनॉल्फथलीन, उदासीनीकरण, अवक्षेप जैसे शब्दों की वर्तनी शुद्ध है?
- [ ] **Board QA:** क्या अलग प्रश्नोत्तर फाइल में पिछले 5 वर्षों (2019-2024) के बोर्ड प्रश्न फ्लैग सहित मौजूद हैं?
