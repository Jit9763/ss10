# 🏛️ Architecture Documentation (ARCHITECTURE.md)

## 🏗️ 1. Technical Stack & Design Philosophy
- **Core Technologies:** Pure HTML5, Vanilla CSS3, Vanilla JavaScript (ES6+), Dynamic Scalable Vector Graphics (SVG).
- **Interactive Animation Engine:** GSAP (GreenSock) for high-performance physics, particle bubbling, and gas delivery dynamics.
- **Acoustic Audio System:** Native Web Audio API (`window.AudioContext`) synthesizing zero-asset realistic sound effects (e.g. 460Hz to 75Hz acoustic POP burst, liquid bubbling sound).
- **Zero Heavy Frameworks:** नो React, नो Vue, नो Tailwind। 100% सेल्फ-कंटेन्ड और ऑफलाइन-फ्रेंडली।
- **प्रोजेक्टर-ऑप्टिमाइज्ड 16:9 वाइडस्क्रीन स्टैंडर्ड:** सभी इंटरैक्टिव सिमुलेटर `viewBox="0 0 1200 540"` और `aspect-ratio: 1200 / 540` मानक पर।

---

## 🔬 2. High-Efficiency Simulator DOM Architecture
```html
<div class="sim-card" id="simX_Y_box">
  <div class="sim-header">
    <div class="sim-title" style="font-size: 24px; font-weight: 800; color: #0f172a;">...</div>
    <span class="sim-badge" style="font-size: 15px; font-weight: 700;">16:9 प्रोजेक्टर व्यू 🔬</span>
  </div>
  <p class="sim-desc" style="font-size: 19px; font-weight: 700; color: #1e293b;">...</p>
  <div class="sim-controls-grid">...</div>
  <div class="sim-progress-wrap"><div class="sim-progress-bar" id="sXY_pbar"></div></div>
  <div class="sim-stage" style="aspect-ratio: 1200 / 540; background: linear-gradient(180deg, #dcfce7 0%, #bbf7d0 100%); border: 3px solid #16a34a;">
    <svg viewBox="0 0 1200 540">
      <!-- Left Apparatus Stage (X: 0 to 710) -->
      <!-- Right Projector-Grade Live Panel (X: 720 to 1180): Font-weight 800-900, High Contrast Dark Text -->
    </svg>
  </div>
  <div id="sXY_status" class="sim-status-banner" style="font-size: 19px; font-weight: 800;">...</div>
</div>
```

---

## 🧰 3. Proven Open-Source Patterns Integration
- **PhET Acid-Base Dynamics (`phetsims/acid-base-solutions`):** Particle emission for bubbling, equilibrium color shades, universal indicator color maps.
- **Virtua-Chem Lab Apparatus (`sufyanaslam44/Virtua-Chem-Sim`):** Real-world glassware dimensions, delivery tubes, test tube stands, Bunsen burners.
