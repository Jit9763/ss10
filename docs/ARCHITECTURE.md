# 🏛️ Architecture Documentation (ARCHITECTURE.md)

## 🏗️ 1. Technical Stack & Design Philosophy
- **Core Technologies:** Pure HTML5, Vanilla CSS3, Vanilla JavaScript (ES6+), Dynamic Scalable Vector Graphics (SVG).
- **Zero Heavy Frameworks:** नो React, नो Vue, नो Tailwind, नो भारी नोड पैकेज। यह प्लेटफॉर्म **100% सेल्फ-कंटेन्ड और ऑफलाइन-फ्रेंडली** है, जिसे किसी भी स्कूल के कंप्यूटर, टीवी या मोबाइल ब्राउज़र में केवल डबल-क्लिक करके सीधे खोला जा सकता है।
- **प्रोजेक्टर-ऑप्टिमाइज्ड 16:9 वाइडस्क्रीन स्टैंडर्ड:** सभी इंटरैक्टिव सिमुलेटर `viewBox="0 0 1200 540"` और `aspect-ratio: 1200 / 540` मानक पर डिज़ाइन किए गए हैं।

---

## 🔬 2. Simulator Framework Architecture

### 2.1 सिमुलेटर का DOM स्ट्रक्चर
प्रत्येक सिमुलेटर एक उच्च-स्तरीय कार्ड के रूप में संरचित होता है:
```html
<div class="sim-card" id="simX_Y_box">
  <!-- 1. Header: Icon, Title, 16:9 Badge -->
  <div class="sim-header">
    <div class="sim-title">...</div>
    <span class="sim-badge">16:9 प्रोजेक्टर व्यू 🔬</span>
  </div>

  <!-- 2. Pedagogical Activity Description -->
  <p class="sim-desc">...</p>

  <!-- 3. Interactive Control Buttons Grid -->
  <div class="sim-controls-grid">
    <button class="sim-btn" onclick="simAutoPlay()">▶ संपूर्ण ऑटो-प्ले</button>
    <button class="sim-btn" onclick="simStep(1)">1. चरण 1</button>
    ...
    <button class="sim-btn" onclick="simReset()">🔄 रीसेट</button>
  </div>

  <!-- 4. Progress Bar -->
  <div class="sim-progress-wrap"><div class="sim-progress-bar" id="sXY_pbar"></div></div>

  <!-- 5. 16:9 Stage (Split Screen: Left Lab, Right Observation) -->
  <div class="sim-stage" style="aspect-ratio: 1200 / 540 !important; background: linear-gradient(180deg, #dcfce7 0%, #bbf7d0 100%) !important; border: 3px solid #16a34a !important;">
    <svg viewBox="0 0 1200 540">
      <!-- Left Stage (X: 0 to 720): 3D Workbench, Apparatus, Reactions, Bubbles, Flames -->
      <!-- Right Panel (X: 725 to 1175): Live Status, Chemical Equations, Classification -->
    </svg>
  </div>

  <!-- 6. Bottom Dynamic Status Banner -->
  <div id="sXY_status" class="sim-status-banner">...</div>
</div>
```

---

## ⚡ 3. JavaScript State & Timer Management Engine

### 3.1 टाइमर आइसोलेशन (Timer Isolation System)
सिमुलेटरों में एनिमेशन टाइमर के टकराव को रोकने हेतु केंद्रीय टाइमर मैनेजर:
```javascript
var simTimers = {};
function addSimTimer(simId, timer) {
  if (!simTimers[simId]) simTimers[simId] = [];
  simTimers[simId].push(timer);
}
function clearSimTimers(simId) {
  if (simTimers[simId]) {
    simTimers[simId].forEach(function(t) { clearTimeout(t); });
    simTimers[simId] = [];
  }
}
```

### 3.2 डायनामिक टाइपोग्राफी व स्ट्रोक स्केलर
```javascript
var simTextOffset = 0;
function adjustSimFontSize(amount) {
  simTextOffset += amount;
  if (simTextOffset < -6) simTextOffset = -6;
  if (simTextOffset > 12) simTextOffset = 12;
  applySimTypography();
}
function adjustSimStroke(delta) {
  var svgs = document.querySelectorAll('.sim-stage svg');
  svgs.forEach(function(svg) {
    var lines = svg.querySelectorAll('path, line, rect, circle, ellipse, polygon');
    lines.forEach(function(el) {
      var sw = parseFloat(el.getAttribute('stroke-width'));
      if (!isNaN(sw) && sw > 0) {
        var nsw = Math.max(0.8, +(sw + delta * 0.35).toFixed(2));
        el.setAttribute('stroke-width', nsw);
      }
    });
  });
}
```

---

## 📁 4. File & Repository Structure
```
ss10/
├── docs/                        # Master Project Documentation
│   ├── PRD.md                   # Product Requirements Document
│   ├── ARCHITECTURE.md          # Technical Architecture & Framework
│   ├── RULES.md                 # Strict Guidelines & Coding Protocol
│   ├── DESIGN.md                # Visual System & UI Aesthetics
│   ├── TASKS.md                 # Chapter Tracker & Task Board
│   └── MEMORY.md                # Persistent Memory & Knowledge Base
│
├── images/                      # Generated 16:9 Educational Infographics & Assets
│   └── ch2_salt_chemicals_infographic.jpg
│
├── copy_master_sci1.html        # Chapter 1 Notes & 16 Simulators
├── copy_master_sci2.html        # Chapter 2 Notes & 14 Simulators + Infographic
├── copy_master_sci3.html        # Chapter 3 Notes
│   ...
├── copy_master_sci13.html       # Chapter 13 Notes
│
├── qa_master_sci1.html          # Chapter 1 QA + 5 Years Board Questions
├── qa_master_sci2.html          # Chapter 2 QA + 5 Years Board Questions
│   ...
└── qa_master_sci13.html         # Chapter 13 QA + 5 Years Board Questions
```
