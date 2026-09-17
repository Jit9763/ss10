# -*- coding: utf-8 -*-
"""
Generator for NCERT Class 9 Mathematics Chapter 11: पृष्ठीय क्षेत्रफल और आयतन (Surface Areas and Volumes)
File: qa_master_math9_11.html
Strict compliance with:
- Zero horizontal chaining
- Strictly vertical aligned steps
- No Hindi inside MathJax
- Safe JS simulator strings (\cdot / ×)
- Zero scrollbars (wrapped & scaled to fit container)
- 5 live interactive simulators with projector controls
"""

content = r'''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT कक्षा 9 गणित - अध्याय 11: पृष्ठीय क्षेत्रफल और आयतन (संपूर्ण 100% प्रश्नोत्तर व 5 लाइव सिमुलेटर)</title>

  <!-- Google Fonts & MathJax -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true
      },
      chtml: {
        displayOverflow: 'scale'
      },
      startup: {
        pageReady: () => {
          return MathJax.startup.defaultPageReady().then(() => {
            thickenFractionLines();
          });
        }
      }
    };
    function thickenFractionLines() {
      document.querySelectorAll('.mjx-mfrac > .mjx-line').forEach(line => {
        line.style.borderTopWidth = '2.5px';
        line.style.borderTopStyle = 'solid';
      });
    }
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" id="MathJax-script" async></script>

  <style>
    :root {
      --font-base: 22pt;
      --font-weight: 700;
      --primary: #1e3a8a;
      --primary-dark: #172554;
      --accent: #2563eb;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #334155;
      --border: #cbd5e1;
      --shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
      --container-width: 95%;
    }

    * { box-sizing: border-box; }
    body {
      font-family: 'Tiro Devanagari Hindi', serif;
      font-size: var(--font-base);
      font-weight: var(--font-weight);
      line-height: 1.6;
      background: var(--bg);
      color: var(--text);
      margin: 0;
      padding: 0;
      word-wrap: break-word;
    }

    .projector-bar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: #0f172a;
      color: #fff;
      padding: 10px 18px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      z-index: 10000;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
      font-family: 'Outfit', sans-serif;
      font-size: 14pt;
    }
    .projector-bar-title {
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-group {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      align-items: center;
    }
    .proj-btn {
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #475569;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 700;
      font-size: 13pt;
      transition: all 0.2s;
    }
    .proj-btn:hover {
      background: #38bdf8;
      color: #0f172a;
      border-color: #38bdf8;
    }

    .container {
      width: var(--container-width);
      max-width: 1400px;
      margin: 80px auto 40px;
      padding: 24px;
      background: var(--card-bg);
      border-radius: 16px;
      box-shadow: var(--shadow);
      border: 2px solid var(--border);
      overflow-x: hidden;
    }

    .chapter-hero {
      background: linear-gradient(135deg, #1e3a8a, #0369a1);
      color: white;
      padding: 36px 30px;
      border-radius: 14px;
      margin-bottom: 30px;
      text-align: center;
    }
    .chapter-hero h1 {
      margin: 0;
      font-size: 38pt;
      font-family: 'Outfit', sans-serif;
      font-weight: 900;
      letter-spacing: -0.5px;
      color: #f0f9ff;
    }
    .chapter-hero p {
      margin: 10px 0 0;
      font-size: 22pt;
      color: #bae6fd;
    }

    .section-title {
      background: #e0f2fe;
      border-left: 10px solid #0284c7;
      padding: 14px 22px;
      font-size: 28pt;
      font-weight: 900;
      color: #0369a1;
      border-radius: 8px;
      margin: 40px 0 24px;
      font-family: 'Outfit', sans-serif;
    }

    .qa-block {
      background: #ffffff;
      border: 3px solid #e2e8f0;
      border-radius: 14px;
      padding: 24px 28px;
      margin-bottom: 28px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04);
      overflow-x: hidden;
      word-wrap: break-word;
    }
    .question-heading {
      color: #1e3a8a;
      font-size: 24pt;
      font-weight: 900;
      margin: 0 0 16px 0;
      line-height: 1.5;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }

    .step-box-blue {
      background: #eff6ff;
      border-left: 8px solid #2563eb;
      padding: 18px 22px;
      border-radius: 10px;
      margin: 14px 0;
    }
    .step-box-green {
      background: #ecfdf5;
      border-left: 8px solid #10b981;
      padding: 18px 22px;
      border-radius: 10px;
      margin: 14px 0;
    }
    .step-box-purple {
      background: #faf5ff;
      border-left: 8px solid #a855f7;
      padding: 18px 22px;
      border-radius: 10px;
      margin: 14px 0;
    }
    .step-box-orange {
      background: #fff7ed;
      border-left: 8px solid #f97316;
      padding: 18px 22px;
      border-radius: 10px;
      margin: 14px 0;
    }

    .answer-highlight {
      background: #ecfdf5;
      border: 3px solid #059669;
      color: #064e3b;
      padding: 14px 20px;
      border-radius: 10px;
      font-size: 24pt;
      font-weight: 900;
      margin-top: 14px;
      text-align: center;
      word-wrap: break-word;
    }

    .step-txt {
      margin: 6px 0;
      font-size: 22pt;
    }

    .math-scroll {
      overflow-x: hidden !important;
      overflow-y: hidden !important;
      max-width: 100%;
      margin: 10px 0;
      padding: 4px 0;
    }

    .badge-blue {
      background: #dbeafe;
      color: #1e40af;
      padding: 4px 14px;
      border-radius: 8px;
      font-weight: 800;
      display: inline-block;
      margin-bottom: 8px;
      font-family: 'Outfit', sans-serif;
      font-size: 20pt;
    }

    /* Simulator styling */
    .sim-card {
      background: #f0fdfa;
      border: 4px solid #0d9488;
      border-radius: 16px;
      padding: 26px;
      margin: 36px 0;
      box-shadow: 0 8px 24px rgba(13, 148, 136, 0.15);
      overflow-x: hidden;
    }
    .sim-header {
      color: #115e59;
      font-size: 26pt;
      font-weight: 900;
      margin: 0 0 12px 0;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .sim-input-row {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      align-items: center;
      margin: 16px 0;
    }
    .sim-input-box {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 20pt;
      font-weight: 700;
    }
    .sim-input {
      font-family: 'Outfit', sans-serif;
      font-size: 22pt;
      font-weight: 800;
      padding: 8px 14px;
      border: 3px solid #14b8a6;
      border-radius: 10px;
      width: 140px;
      text-align: center;
      background: #ffffff;
      color: #0f172a;
    }
    .sim-btn {
      background: linear-gradient(135deg, #0d9488, #0f766e);
      color: white;
      border: none;
      padding: 12px 28px;
      font-size: 20pt;
      font-weight: 800;
      border-radius: 10px;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(13, 148, 136, 0.3);
      transition: transform 0.1s;
    }
    .sim-btn:hover {
      transform: scale(1.02);
    }
    .sim-result {
      background: #ffffff;
      border: 3px solid #ccfbf1;
      border-radius: 12px;
      padding: 20px;
      margin-top: 16px;
      overflow-x: hidden;
    }

    @media print {
      .projector-bar { display: none; }
      .container { margin: 0; width: 100%; max-width: 100%; border: none; }
    }
  </style>
</head>
<body>

  <!-- Projector Floating Bar -->
  <div class="projector-bar">
    <div class="projector-bar-title">
      <span>📐 कक्षा 9 गणित</span>
      <span style="color:#94a3b8;">|</span>
      <span style="color:#fef08a;">अध्याय 11: पृष्ठीय क्षेत्रफल और आयतन</span>
    </div>
    <div class="btn-group">
      <button class="proj-btn" onclick="adjustWidth(5)" title="चौड़ाई बढ़ाएँ">W+</button>
      <button class="proj-btn" onclick="adjustWidth(-5)" title="चौड़ाई घटाएँ">W-</button>
      <button class="proj-btn" onclick="adjustFontSize(2)" title="फ़ॉन्ट बढ़ाएँ">A+</button>
      <button class="proj-btn" onclick="adjustFontSize(-2)" title="फ़ॉन्ट घटाएँ">A-</button>
      <button class="proj-btn" onclick="adjustFontWeight(100)" title="बोल्डनेस बढ़ाएँ">B+</button>
      <button class="proj-btn" onclick="adjustFontWeight(-100)" title="बोल्डनेस घटाएँ">B-</button>
      <button class="proj-btn" onclick="copyEntireContent()" title="कॉपी करें">📋 कॉपी</button>
      <button class="proj-btn" onclick="window.print()" title="प्रिंट करें">🖨️ प्रिंट</button>
      <a href="index.html" class="proj-btn" style="text-decoration:none;">🏠 मुख्य पृष्ठ</a>
    </div>
  </div>

  <div class="container" id="printable-content">

    <!-- Hero Header -->
    <div class="chapter-hero">
      <h1>अध्याय 11: पृष्ठीय क्षेत्रफल और आयतन</h1>
      <p>NCERT कक्षा 9 गणित (Rationalised Syllabus 2024-25: शंकु एवं गोला) — संपूर्ण 100% प्रश्नोत्तर व 5 लाइव सिमुलेटर</p>
    </div>

    <!-- Core Formulas -->
    <div class="section-title">🌟 महत्वपूर्ण सूत्र एवं अवधारणाएँ (Key Formulas)</div>

    <div class="qa-block">
      <div class="step-box-blue">
        <p><b>1. लम्ब वृत्तीय शंकु (Right Circular Cone):</b> त्रिज्या $r$, ऊँचाई $h$, तिर्यक ऊँचाई $l$</p>
        <div class="math-scroll">$$\begin{aligned}
        l &= \sqrt{r^2 + h^2} \\
        \text{CSA} &= \pi r l \\
        \text{TSA} &= \pi r(l + r)
        \end{aligned}$$</div>

        <p><b>2. गोला (Sphere):</b> त्रिज्या $r$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Surface Area} &= 4\pi r^2
        \end{aligned}$$</div>

        <p><b>3. अर्धगोला (Hemisphere):</b> त्रिज्या $r$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= 2\pi r^2 \\
        \text{TSA} &= 3\pi r^2
        \end{aligned}$$</div>
      </div>
    </div>

    <!-- ========================================================== -->
    <!-- EXERCISE 11.1 -->
    <!-- ========================================================== -->
    <div class="section-title">📝 प्रश्नावली 11.1 (शंकु का पृष्ठीय क्षेत्रफल - संपूर्ण 8 प्रश्न)</div>

    <!-- Ex 11.1 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: एक शंकु के आधार का व्यास $10.5\text{ cm}$ है और इसकी तिर्यक ऊँचाई $10\text{ cm}$ है। इसका वक्र पृष्ठीय क्षेत्रफल ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>दिया है:</b> व्यास $d = 10.5\text{ cm} \implies r = \frac{10.5}{2} = 5.25\text{ cm} = \frac{21}{4}\text{ cm}$</p>
        <p class="step-txt">तिर्यक ऊँचाई $l = 10\text{ cm}$</p>
        <p class="step-txt">शंकु का वक्र पृष्ठीय क्षेत्रफल $\text{CSA} = \pi r l$:</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= \frac{22}{7} \cdot \left(\frac{21}{4}\right) \cdot 10 \\
        &= \frac{22}{7} \cdot \frac{210}{4} \\
        &= \frac{22 \cdot 30}{4} \\
        &= \frac{660}{4} \\
        &= 165\text{ cm}^2
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ शंकु का अभीष्ट वक्र पृष्ठीय क्षेत्रफल = $165\text{ cm}^2$</div>
    </div>

    <!-- Ex 11.1 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: एक शंकु का कुल पृष्ठीय क्षेत्रफल ज्ञात कीजिए, जिसकी तिर्यक ऊँचाई $21\text{ m}$ है और आधार का व्यास $24\text{ m}$ है।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>दिया है:</b> व्यास $d = 24\text{ m} \implies r = 12\text{ m}$, तिर्यक ऊँचाई $l = 21\text{ m}$</p>
        <p class="step-txt">शंकु का कुल पृष्ठीय क्षेत्रफल $\text{TSA} = \pi r(l + r)$:</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{TSA} &= \frac{22}{7} \cdot 12 \cdot (21 + 12) \\
        &= \frac{22}{7} \cdot 12 \cdot 33 \\
        &= \frac{22 \cdot 396}{7} \\
        &= \frac{8712}{7} \\
        &\approx 1244.57\text{ m}^2
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ शंकु का अभीष्ट कुल पृष्ठीय क्षेत्रफल = $\frac{8712}{7}\text{ m}^2 \approx 1244.57\text{ m}^2$</div>
    </div>

    <!-- Ex 11.1 Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: एक शंकु का वक्र पृष्ठीय क्षेत्रफल $308\text{ cm}^2$ है और इसकी तिर्यक ऊँचाई $14\text{ cm}$ है। ज्ञात कीजिए:<br>(i) आधार की त्रिज्या &emsp; (ii) शंकु का कुल पृष्ठीय क्षेत्रफल।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">(i) आधार की त्रिज्या $r$</span>
        <p class="step-txt">सूत्र: $\text{CSA} = \pi r l = 308$</p>
        <div class="math-scroll">$$\begin{aligned}
        \frac{22}{7} \cdot r \cdot 14 &= 308 \\
        22 \cdot 2 \cdot r &= 308 \\
        44r &= 308 \\
        r &= \frac{308}{44} \\
        &= 7\text{ cm}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <span class="badge-blue">(ii) शंकु का कुल पृष्ठीय क्षेत्रफल</span>
        <div class="math-scroll">$$\begin{aligned}
        \text{TSA} &= \text{CSA} + \pi r^2 \\
        &= 308 + \frac{22}{7} \cdot 7^2 \\
        &= 308 + (22 \cdot 7) \\
        &= 308 + 154 \\
        &= 462\text{ cm}^2
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ (i) त्रिज्या = $7\text{ cm}$ &emsp; | &emsp; (ii) कुल पृष्ठीय क्षेत्रफल = $462\text{ cm}^2$</div>
    </div>

    <!-- Ex 11.1 Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: शंकु के आकार का एक तंबू $10\text{ m}$ ऊँचा है और उसके आधार की त्रिज्या $24\text{ m}$ है। ज्ञात कीजिए:<br>(i) तंबू की तिर्यक ऊँचाई &emsp; (ii) तंबू में लगे केनवास की लागत (₹ 70 प्रति $\text{m}^2$ की दर से)।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">(i) तिर्यक ऊँचाई $l$</span>
        <p class="step-txt">$h = 10\text{ m}, \quad r = 24\text{ m}$</p>
        <div class="math-scroll">$$\begin{aligned}
        l &= \sqrt{r^2 + h^2} \\
        &= \sqrt{24^2 + 10^2} \\
        &= \sqrt{576 + 100} \\
        &= \sqrt{676} \\
        &= 26\text{ m}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <span class="badge-blue">(ii) केनवास का क्षेत्रफल व लागत</span>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= \pi r l \\
        &= \frac{22}{7} \cdot 24 \cdot 26 \\
        &= \frac{13728}{7}\text{ m}^2
        \end{aligned}$$</div>
        <p class="step-txt">₹ $70$ प्रति $\text{m}^2$ की दर से कुल लागत:</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Cost} &= \frac{13728}{7} \cdot 70 \\
        &= 13728 \cdot 10 \\
        &= 137280\text{ Rs}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ (i) तिर्यक ऊँचाई = $26\text{ m}$ &emsp; | &emsp; (ii) केनवास की कुल लागत = ₹ 1,37,280</div>
    </div>

    <!-- Ex 11.1 Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: $8\text{ m}$ ऊँचाई और आधार की त्रिज्या $6\text{ m}$ वाले एक शंकु के आकार का तंबू बनाने में $3\text{ m}$ चौड़े तिरपाल की कितनी लंबाई लगेगी? यह मान कर चलिए कि इसकी सिलाई और कटाई में $20\text{ cm}$ अतिरिक्त तिरपाल लगेगा ($\pi = 3.14$)।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: तिर्यक ऊँचाई $l$:</b></p>
        <p class="step-txt">$h = 8\text{ m}, \quad r = 6\text{ m}$</p>
        <div class="math-scroll">$$\begin{aligned}
        l &= \sqrt{6^2 + 8^2} \\
        &= \sqrt{36 + 64} \\
        &= \sqrt{100} \\
        &= 10\text{ m}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: तंबू का वक्र पृष्ठीय क्षेत्रफल:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= \pi r l \\
        &= 3.14 \cdot 6 \cdot 10 \\
        &= 3.14 \cdot 60 \\
        &= 188.4\text{ m}^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: तिरपाल की अभीष्ट लंबाई:</b></p>
        <p class="step-txt">तिरपाल की चौड़ाई $= 3\text{ m}$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Length} &= \frac{\text{Area}}{\text{Width}} \\
        &= \frac{188.4}{3} \\
        &= 62.8\text{ m}
        \end{aligned}$$</div>
        <p class="step-txt">अतिरिक्त सिलाई/कटाई $= 20\text{ cm} = 0.2\text{ m}$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Total Length} &= 62.8 + 0.2 \\
        &= 63\text{ m}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ तिरपाल की कुल अभीष्ट लंबाई = $63\text{ m}$</div>
    </div>

    <!-- Ex 11.1 Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: शंकु के आकार की एक गुंबज की तिर्यक ऊँचाई और आधार व्यास क्रमशः $25\text{ m}$ और $14\text{ m}$ हैं। इसकी वक्र पृष्ठ पर ₹ $210$ प्रति $100\text{ m}^2$ की दर से सफेदी कराने का व्यय ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>दिया है:</b> तिर्यक ऊँचाई $l = 25\text{ m}$, व्यास $d = 14\text{ m} \implies r = 7\text{ m}$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= \pi r l \\
        &= \frac{22}{7} \cdot 7 \cdot 25 \\
        &= 22 \cdot 25 \\
        &= 550\text{ m}^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>सफेदी कराने का व्यय:</b></p>
        <p class="step-txt">दर = ₹ $210$ प्रति $100\text{ m}^2$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Total Cost} &= 550 \cdot \frac{210}{100} \\
        &= 55 \cdot 21 \\
        &= 1155\text{ Rs}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ सफेदी कराने का कुल अभीष्ट व्यय = ₹ 1155</div>
    </div>

    <!-- Ex 11.1 Q7 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 7: एक जोकर की टोपी एक शंकु के आकार की है, जिसके आधार की त्रिज्या $7\text{ cm}$ और ऊँचाई $24\text{ cm}$ है। इसी प्रकार की $10$ टोपियाँ बनाने के लिए आवश्यक गत्ते का क्षेत्रफल ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: तिर्यक ऊँचाई $l$:</b></p>
        <p class="step-txt">$r = 7\text{ cm}, \quad h = 24\text{ cm}$</p>
        <div class="math-scroll">$$\begin{aligned}
        l &= \sqrt{7^2 + 24^2} \\
        &= \sqrt{49 + 576} \\
        &= \sqrt{625} \\
        &= 25\text{ cm}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: 1 टोपी का वक्र पृष्ठीय क्षेत्रफल:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= \pi r l \\
        &= \frac{22}{7} \cdot 7 \cdot 25 \\
        &= 22 \cdot 25 \\
        &= 550\text{ cm}^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: 10 टोपियों के लिए आवश्यक गत्ते का कुल क्षेत्रफल:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Total Area} &= 10 \cdot 550 \\
        &= 5500\text{ cm}^2
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ 10 टोपियों के लिए आवश्यक गत्ते का क्षेत्रफल = $5500\text{ cm}^2$</div>
    </div>

    <!-- Ex 11.1 Q8 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 8: किसी बस स्टॉप को पुराने गत्ते से बने $50$ खोखले शंकुओं द्वारा सड़क से अलग किया हुआ है। प्रत्येक शंकु के आधार का व्यास $40\text{ cm}$ है और ऊँचाई $1\text{ m}$ है। यदि इन शंकुओं के बाहरी पृष्ठों को पेंट करवाना है और पेंट की दर ₹ $12$ प्रति $\text{m}^2$ है, तो इनको पेंट कराने में कितनी लागत आएगी? ($\pi = 3.14, \sqrt{1.04} \approx 1.02$)</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: शंकु की विमाएँ व तिर्यक ऊँचाई $l$:</b></p>
        <p class="step-txt">व्यास $= 40\text{ cm} \implies r = 20\text{ cm} = 0.2\text{ m}$, &emsp; ऊँचाई $h = 1\text{ m}$</p>
        <div class="math-scroll">$$\begin{aligned}
        l &= \sqrt{r^2 + h^2} \\
        &= \sqrt{(0.2)^2 + 1^2} \\
        &= \sqrt{0.04 + 1} \\
        &= \sqrt{1.04} \\
        &\approx 1.02\text{ m}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: 1 शंकु का वक्र पृष्ठीय क्षेत्रफल:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= \pi r l \\
        &= 3.14 \cdot 0.2 \cdot 1.02 \\
        &= 0.64056\text{ m}^2
        \end{aligned}$$</div>
        <p class="step-txt">50 शंकुओं का कुल क्षेत्रफल:</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Total Area} &= 50 \cdot 0.64056 \\
        &= 32.028\text{ m}^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: पेंट कराने की कुल लागत:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Cost} &= 32.028 \cdot 12 \\
        &= 384.336 \\
        &\approx ₹ 384.34
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ पेंट कराने की कुल अभीष्ट लागत = ₹ 384.34</div>
    </div>

    <!-- ========================================================== -->
    <!-- EXERCISE 11.2 -->
    <!-- ========================================================== -->
    <div class="section-title">📝 प्रश्नावली 11.2 (गोला एवं अर्धगोला - संपूर्ण 9 प्रश्न)</div>

    <!-- Ex 11.2 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: निम्न त्रिज्या वाले गोले का पृष्ठीय क्षेत्रफल ज्ञात कीजिए:</h3>
      
      <div class="step-box-blue">
        <p><b>(i) $r = 10.5\text{ cm}$</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Area} &= 4\pi r^2 \\
        &= 4 \cdot \frac{22}{7} \cdot (10.5)^2 \\
        &= 4 \cdot \frac{22}{7} \cdot 110.25 \\
        &= 4 \cdot 22 \cdot 15.75 \\
        &= 88 \cdot 15.75 \\
        &= 1386\text{ cm}^2
        \end{aligned}$$</div>
        <div class="answer-highlight">✅ उत्तर: $1386\text{ cm}^2$</div>
      </div>

      <div class="step-box-orange">
        <p><b>(ii) $r = 5.6\text{ cm}$</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Area} &= 4\pi r^2 \\
        &= 4 \cdot \frac{22}{7} \cdot 5.6 \cdot 5.6 \\
        &= 4 \cdot 22 \cdot 0.8 \cdot 5.6 \\
        &= 88 \cdot 4.48 \\
        &= 394.24\text{ cm}^2
        \end{aligned}$$</div>
        <div class="answer-highlight">✅ उत्तर: $394.24\text{ cm}^2$</div>
      </div>

      <div class="step-box-green">
        <p><b>(iii) $r = 14\text{ cm}$</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Area} &= 4\pi r^2 \\
        &= 4 \cdot \frac{22}{7} \cdot 14 \cdot 14 \\
        &= 4 \cdot 22 \cdot 2 \cdot 14 \\
        &= 88 \cdot 28 \\
        &= 2464\text{ cm}^2
        \end{aligned}$$</div>
        <div class="answer-highlight">✅ उत्तर: $2464\text{ cm}^2$</div>
      </div>
    </div>

    <!-- Ex 11.2 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: निम्न व्यास वाले गोले का पृष्ठीय क्षेत्रफल ज्ञात कीजिए:</h3>
      
      <div class="step-box-blue">
        <p><b>(i) व्यास $= 14\text{ cm} \implies r = 7\text{ cm}$</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Area} &= 4\pi r^2 \\
        &= 4 \cdot \frac{22}{7} \cdot 7 \cdot 7 \\
        &= 4 \cdot 22 \cdot 7 \\
        &= 88 \cdot 7 \\
        &= 616\text{ cm}^2
        \end{aligned}$$</div>
        <div class="answer-highlight">✅ उत्तर: $616\text{ cm}^2$</div>
      </div>

      <div class="step-box-orange">
        <p><b>(ii) व्यास $= 21\text{ cm} \implies r = \frac{21}{2}\text{ cm}$</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Area} &= 4\pi r^2 \\
        &= 4 \cdot \frac{22}{7} \cdot \frac{21}{2} \cdot \frac{21}{2} \\
        &= 4 \cdot \frac{22}{7} \cdot \frac{441}{4} \\
        &= 22 \cdot 63 \\
        &= 1386\text{ cm}^2
        \end{aligned}$$</div>
        <div class="answer-highlight">✅ उत्तर: $1386\text{ cm}^2$</div>
      </div>

      <div class="step-box-green">
        <p><b>(iii) व्यास $= 3.5\text{ m} \implies r = \frac{3.5}{2} = 1.75\text{ m} = \frac{7}{4}\text{ m}$</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Area} &= 4\pi r^2 \\
        &= 4 \cdot \frac{22}{7} \cdot \frac{7}{4} \cdot \frac{7}{4} \\
        &= \frac{22 \cdot 7}{4} \\
        &= \frac{154}{4} \\
        &= 38.5\text{ m}^2
        \end{aligned}$$</div>
        <div class="answer-highlight">✅ उत्तर: $38.5\text{ m}^2$</div>
      </div>
    </div>

    <!-- Ex 11.2 Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: $10\text{ cm}$ त्रिज्या वाले एक अर्धगोले का कुल पृष्ठीय क्षेत्रफल ज्ञात कीजिए ($\pi = 3.14$)।</h3>
      
      <div class="step-box-purple">
        <p class="step-txt">अर्धगोले का कुल पृष्ठीय क्षेत्रफल $\text{TSA} = 3\pi r^2$:</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{TSA} &= 3 \cdot \pi \cdot r^2 \\
        &= 3 \cdot 3.14 \cdot (10)^2 \\
        &= 3 \cdot 3.14 \cdot 100 \\
        &= 3 \cdot 314 \\
        &= 942\text{ cm}^2
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ अर्धगोले का कुल पृष्ठीय क्षेत्रफल = $942\text{ cm}^2$</div>
    </div>

    <!-- Ex 11.2 Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: एक गोलाकार गुब्बारे में हवा भरने पर, उसकी त्रिज्या $7\text{ cm}$ से $14\text{ cm}$ हो जाती है। इन दोनों स्थितियों में गुब्बारे के पृष्ठीय क्षेत्रफलों का अनुपात ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt">प्रारंभिक त्रिज्या $r_1 = 7\text{ cm}$, नई त्रिज्या $r_2 = 14\text{ cm}$</p>
        <p class="step-txt">पृष्ठीय क्षेत्रफलों का अनुपात:</p>
        <div class="math-scroll">$$\begin{aligned}
        \frac{A_1}{A_2} &= \frac{4\pi r_1^2}{4\pi r_2^2} \\
        &= \left(\frac{r_1}{r_2}\right)^2 \\
        &= \left(\frac{7}{14}\right)^2 \\
        &= \left(\frac{1}{2}\right)^2 \\
        &= \frac{1}{4}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ अभीष्ट अनुपात = $1 : 4$</div>
    </div>

    <!-- Ex 11.2 Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: पीतल से बने एक अर्धगोलाकार कटोरे का आंतरिक व्यास $10.5\text{ cm}$ है। ₹ $16$ प्रति $100\text{ cm}^2$ की दर से इसके आंतरिक पृष्ठ पर कलई कराने का व्यय ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: आंतरिक वक्र पृष्ठीय क्षेत्रफल:</b></p>
        <p class="step-txt">व्यास $= 10.5\text{ cm} \implies r = 5.25\text{ cm} = \frac{21}{4}\text{ cm}$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= 2\pi r^2 \\
        &= 2 \cdot \frac{22}{7} \cdot \left(\frac{21}{4}\right) \cdot \left(\frac{21}{4}\right) \\
        &= 2 \cdot 22 \cdot \frac{3}{4} \cdot \frac{21}{4} \\
        &= 44 \cdot \frac{63}{16} \\
        &= \frac{11 \cdot 63}{4} \\
        &= \frac{693}{4} \\
        &= 173.25\text{ cm}^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: कलई कराने का व्यय:</b></p>
        <p class="step-txt">दर = ₹ $16$ प्रति $100\text{ cm}^2$</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Cost} &= 173.25 \cdot \frac{16}{100} \\
        &= \frac{2772}{100} \\
        &= 27.72\text{ Rs}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ कलई कराने का कुल अभीष्ट व्यय = ₹ 27.72</div>
    </div>

    <!-- Ex 11.2 Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: उस गोले की त्रिज्या ज्ञात कीजिए जिसका पृष्ठीय क्षेत्रफल $154\text{ cm}^2$ है।</h3>
      
      <div class="step-box-purple">
        <p class="step-txt">सूत्र: $4\pi r^2 = 154$</p>
        <div class="math-scroll">$$\begin{aligned}
        4 \cdot \frac{22}{7} \cdot r^2 &= 154 \\
        \frac{88}{7} \cdot r^2 &= 154 \\
        r^2 &= \frac{154 \cdot 7}{88} \\
        &= \frac{14 \cdot 7}{8} \\
        &= \frac{7 \cdot 7}{4} \\
        &= \frac{49}{4} \\
        r &= \sqrt{\frac{49}{4}} \\
        &= \frac{7}{2} \\
        &= 3.5\text{ cm}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ गोले की अभीष्ट त्रिज्या = $3.5\text{ cm}$</div>
    </div>

    <!-- Ex 11.2 Q7 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 7: चंद्रमा का व्यास पृथ्वी के व्यास का लगभग एक-चौथाई है। इन दोनों के पृष्ठीय क्षेत्रफलों का अनुपात ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt">माना पृथ्वी का व्यास $= d \implies$ त्रिज्या $r_e = \frac{d}{2}$</p>
        <p class="step-txt">चंद्रमा का व्यास $= \frac{d}{4} \implies$ त्रिज्या $r_m = \frac{d}{8}$</p>
        <p class="step-txt">त्रिज्याओं का अनुपात:</p>
        <div class="math-scroll">$$\begin{aligned}
        \frac{r_m}{r_e} &= \frac{d/8}{d/2} \\
        &= \frac{2}{8} \\
        &= \frac{1}{4}
        \end{aligned}$$</div>
        
        <p class="step-txt">पृष्ठीय क्षेत्रफलों का अनुपात:</p>
        <div class="math-scroll">$$\begin{aligned}
        \frac{S_m}{S_e} &= \frac{4\pi r_m^2}{4\pi r_e^2} \\
        &= \left(\frac{r_m}{r_e}\right)^2 \\
        &= \left(\frac{1}{4}\right)^2 \\
        &= \frac{1}{16}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ चंद्रमा व पृथ्वी के पृष्ठीय क्षेत्रफलों का अभीष्ट अनुपात = $1 : 16$</div>
    </div>

    <!-- Ex 11.2 Q8 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 8: एक अर्धगोलाकार कटोरा $0.25\text{ cm}$ मोटी स्टील से बना है। इस कटोरे की आंतरिक त्रिज्या $5\text{ cm}$ है। कटोरे का बाहरी वक्र पृष्ठीय क्षेत्रफल ज्ञात कीजिए।</h3>
      
      <div class="step-box-green">
        <p class="step-txt">आंतरिक त्रिज्या $r = 5\text{ cm}$, मोटाई $t = 0.25\text{ cm}$</p>
        <p class="step-txt">बाहरी त्रिज्या $R = r + t = 5 + 0.25 = 5.25\text{ cm} = \frac{21}{4}\text{ cm}$</p>
        <p class="step-txt">कटोरे का बाहरी वक्र पृष्ठीय क्षेत्रफल $\text{CSA} = 2\pi R^2$:</p>
        <div class="math-scroll">$$\begin{aligned}
        \text{CSA} &= 2 \cdot \frac{22}{7} \cdot \left(\frac{21}{4}\right) \cdot \left(\frac{21}{4}\right) \\
        &= 44 \cdot \frac{3}{4} \cdot \frac{21}{4} \\
        &= 11 \cdot 3 \cdot \frac{21}{4} \\
        &= \frac{693}{4} \\
        &= 173.25\text{ cm}^2
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ कटोरे का बाहरी वक्र पृष्ठीय क्षेत्रफल = $173.25\text{ cm}^2$</div>
    </div>

    <!-- Ex 11.2 Q9 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 9: एक लम्ब वृत्तीय बेलन त्रिज्या $r$ वाले एक गोले को पूर्णतया घेरे हुए है। ज्ञात कीजिए:<br>(i) गोले का पृष्ठीय क्षेत्रफल &emsp; (ii) बेलन का वक्र पृष्ठीय क्षेत्रफल &emsp; (iii) (i) और (ii) में प्राप्त क्षेत्रफलों का अनुपात।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">(i) गोले का पृष्ठीय क्षेत्रफल</span>
        <div class="math-scroll">$$\begin{aligned}
        S_1 &= 4\pi r^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <span class="badge-blue">(ii) बेलन का वक्र पृष्ठीय क्षेत्रफल</span>
        <p class="step-txt">बेलन की त्रिज्या $= r$, बेलन की ऊँचाई $h =$ गोले का व्यास $= 2r$</p>
        <div class="math-scroll">$$\begin{aligned}
        S_2 &= 2\pi r h \\
        &= 2\pi r \cdot (2r) \\
        &= 4\pi r^2
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">(iii) क्षेत्रफलों का अनुपात</span>
        <div class="math-scroll">$$\begin{aligned}
        \frac{S_1}{S_2} &= \frac{4\pi r^2}{4\pi r^2} \\
        &= \frac{1}{1}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ (i) $4\pi r^2$ &emsp; | &emsp; (ii) $4\pi r^2$ &emsp; | &emsp; (iii) अभीष्ट अनुपात = $1 : 1$</div>
    </div>

    <!-- ========================================================== -->
    <!-- 5 INTERACTIVE LIVE SIMULATORS -->
    <!-- ========================================================== -->
    <div class="section-title">⚡ 5 इंटरैक्टिव लाइव सिमुलेटर (Surface Area Simulators)</div>

    <!-- SIMULATOR 1: Cone Surface Area Solver -->
    <div class="sim-card">
      <div class="sim-header">🍦 सिमुलेटर 1: शंकु वक्र एवं कुल पृष्ठीय क्षेत्रफल कैलकुलेटर (Cone Solver)</div>
      <p>आधार त्रिज्या $r$ और ऊँचाई $h$ दर्ज करें, तिर्यक ऊँचाई $l$, वक्र पृष्ठ ($\pi r l$) तथा कुल पृष्ठ प्राप्त करें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim1_r">त्रिज्या $r$ (cm):</label>
          <input type="number" id="sim1_r" class="sim-input" value="7" min="1">
        </div>
        <div class="sim-input-box">
          <label for="sim1_h">ऊँचाई $h$ (cm):</label>
          <input type="number" id="sim1_h" class="sim-input" value="24" min="1">
        </div>
        <button class="sim-btn" onclick="calculateSim1()">गणना करें</button>
      </div>
      <div id="sim1_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 2: Sphere Surface Area Solver -->
    <div class="sim-card">
      <div class="sim-header">⚽ सिमुलेटर 2: गोला पृष्ठीय क्षेत्रफल कैलकुलेटर (Sphere Area Solver)</div>
      <p>त्रिज्या $r$ दर्ज करें और $4\pi r^2$ के साथ गोले का संपूर्ण पृष्ठीय क्षेत्रफल चरणबद्ध देखें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim2_r">त्रिज्या $r$ (cm):</label>
          <input type="number" id="sim2_r" class="sim-input" value="10.5" min="0.1" step="0.1">
        </div>
        <button class="sim-btn" onclick="calculateSim2()">क्षेत्रफल निकालें</button>
      </div>
      <div id="sim2_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 3: Hemisphere CSA & TSA Solver -->
    <div class="sim-card">
      <div class="sim-header">🥣 सिमुलेटर 3: अर्धगोला वक्र व कुल पृष्ठ कैलकुलेटर (Hemisphere Solver)</div>
      <p>त्रिज्या $r$ दर्ज करें और $2\pi r^2$ (वक्र पृष्ठ) तथा $3\pi r^2$ (कुल पृष्ठ) की तुरंत गणना करें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim3_r">त्रिज्या $r$ (cm):</label>
          <input type="number" id="sim3_r" class="sim-input" value="10" min="0.1">
        </div>
        <button class="sim-btn" onclick="calculateSim3()">हल निकालें</button>
      </div>
      <div id="sim3_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 4: Hemisphere Tin-Plating Cost Solver -->
    <div class="sim-card">
      <div class="sim-header">🪙 सिमुलेटर 4: अर्धगोलाकार कटोरे की कलई लागत कैलकुलेटर (Plating Cost Solver)</div>
      <p>कटोरे का व्यास $d$ और कलई की दर (₹ प्रति $100\text{ cm}^2$) दर्ज कर कुल खर्च निकालें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim4_d">व्यास $d$ (cm):</label>
          <input type="number" id="sim4_d" class="sim-input" value="10.5" min="1" step="0.5">
        </div>
        <div class="sim-input-box">
          <label for="sim4_rate">दर (₹/100 cm²):</label>
          <input type="number" id="sim4_rate" class="sim-input" value="16" min="1">
        </div>
        <button class="sim-btn" onclick="calculateSim4()">लागत निकालें</button>
      </div>
      <div id="sim4_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 5: Moon vs Earth Ratio Solver -->
    <div class="sim-card">
      <div class="sim-header">🌕 सिमुलेटर 5: खगोलीय पिंड व्यास व पृष्ठीय क्षेत्रफल अनुपात विज़ुअलाइज़र</div>
      <p>व्यास का अनुपात (जैसे $1/k$) दर्ज करें और क्षेत्रफलों का वर्ग अनुपात $1/k^2$ सीधे देखें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim5_k">व्यास अनुपात ($1/k$ में $k$):</label>
          <input type="number" id="sim5_k" class="sim-input" value="4" min="2">
        </div>
        <button class="sim-btn" onclick="calculateSim5()">अनुपात निकालें</button>
      </div>
      <div id="sim5_output" class="sim-result"></div>
    </div>

  </div> <!-- End Container -->

  <!-- JavaScript for Projector Toolbar & Simulators -->
  <script>
  function getContainer() {
    return document.getElementById('printable-content');
  }

  function adjustWidth(delta) {
    const c = getContainer();
    let cur = parseInt(window.getComputedStyle(c).width);
    let nw = cur + delta * 20;
    c.style.maxWidth = nw + 'px';
    c.style.width = '98%';
  }

  function adjustFontSize(delta) {
    const b = document.body;
    let cur = parseFloat(window.getComputedStyle(b).fontSize);
    let nw = Math.max(14, Math.min(36, cur + delta));
    b.style.fontSize = nw + 'pt';
  }

  function adjustFontWeight(delta) {
    const b = document.body;
    let cur = parseInt(window.getComputedStyle(b).fontWeight) || 700;
    let nw = Math.max(400, Math.min(900, cur + delta));
    b.style.fontWeight = nw;
  }

  function copyEntireContent() {
    const text = document.getElementById('printable-content').innerText;
    navigator.clipboard.writeText(text).then(() => {
      alert('संपूर्ण पाठ सफलतापूर्वक क्लिपबोर्ड में कॉपी हो गया!');
    }).catch(err => {
      alert('कॉपी करने में त्रुटि: ' + err);
    });
  }

  // ==========================================================
  // SIMULATOR 1: Cone Solver
  // ==========================================================
  function calculateSim1() {
    var r = parseFloat(document.getElementById('sim1_r').value) || 7;
    var h = parseFloat(document.getElementById('sim1_h').value) || 24;
    var l = Math.sqrt(r * r + h * h);
    var csa = (Math.PI * r * l).toFixed(2);
    var tsa = (Math.PI * r * (l + r)).toFixed(2);
    var out = document.getElementById('sim1_output');

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>तिर्यक ऊँचाई:</strong></p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      'l &= \\sqrt{r^2 + h^2} \\\\' +
      '&= \\sqrt{' + r + '^2 + ' + h + '^2} \\\\' +
      '&= ' + l.toFixed(2) + '\\text{ cm}' +
      '\\end{aligned}$$</div>' +
      '<p class="step-txt"><strong>वक्र पृष्ठ (CSA):</strong> $\\pi r l \\approx ' + csa + '\\text{ cm}^2$</p>' +
      '<p class="step-txt"><strong>कुल पृष्ठ (TSA):</strong> $\\pi r(l + r) \\approx ' + tsa + '\\text{ cm}^2$</p>' +
      '<div class="answer-highlight">✅ CSA = ' + csa + ' cm² &emsp; | &emsp; TSA = ' + tsa + ' cm²</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 2: Sphere Solver
  // ==========================================================
  function calculateSim2() {
    var r = parseFloat(document.getElementById('sim2_r').value) || 10.5;
    var area = (4 * Math.PI * r * r).toFixed(2);
    var out = document.getElementById('sim2_output');

    var html = '<div class="step-box-green">' +
      '<p class="step-txt">गोले की त्रिज्या $r = ' + r + '$ cm</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\text{Area} &= 4\\pi r^2 \\\\' +
      '&= 4 \\cdot \\pi \\cdot (' + r + ')^2 \\\\' +
      '\\approx ' + area + '\\text{ cm}^2' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ गोले का कुल पृष्ठीय क्षेत्रफल = ' + area + ' cm²</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 3: Hemisphere Solver
  // ==========================================================
  function calculateSim3() {
    var r = parseFloat(document.getElementById('sim3_r').value) || 10;
    var csa = (2 * Math.PI * r * r).toFixed(2);
    var tsa = (3 * Math.PI * r * r).toFixed(2);
    var out = document.getElementById('sim3_output');

    var html = '<div class="step-box-purple">' +
      '<p class="step-txt">अर्धगोले की त्रिज्या $r = ' + r + '$ cm</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\text{CSA} &= 2\\pi r^2 \\approx ' + csa + '\\text{ cm}^2 \\\\' +
      '\\text{TSA} &= 3\\pi r^2 \\approx ' + tsa + '\\text{ cm}^2' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ वक्र पृष्ठ = ' + csa + ' cm² &emsp; | &emsp; कुल पृष्ठ = ' + tsa + ' cm²</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 4: Plating Cost Solver
  // ==========================================================
  function calculateSim4() {
    var d = parseFloat(document.getElementById('sim4_d').value) || 10.5;
    var rate = parseFloat(document.getElementById('sim4_rate').value) || 16;
    var r = d / 2;
    var csa = (2 * Math.PI * r * r);
    var cost = (csa * rate / 100).toFixed(2);
    var out = document.getElementById('sim4_output');

    var html = '<div class="step-box-orange">' +
      '<p class="step-txt">व्यास $d = ' + d + '$ cm $\\implies r = ' + r.toFixed(2) + '$ cm</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\text{CSA} &= 2\\pi r^2 \\approx ' + csa.toFixed(2) + '\\text{ cm}^2 \\\\' +
      '\\text{Cost} &= ' + csa.toFixed(2) + ' \\cdot \\frac{' + rate + '}{100} \\\\' +
      '&= ₹ ' + cost +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ कलई कराने की कुल लागत = ₹ ' + cost + '</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 5: Ratio Solver
  // ==========================================================
  function calculateSim5() {
    var k = parseFloat(document.getElementById('sim5_k').value) || 4;
    var kSq = k * k;
    var out = document.getElementById('sim5_output');

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt">व्यास का अनुपात $= 1 : ' + k + '$</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\frac{r_1}{r_2} &= \\frac{1}{' + k + '} \\\\' +
      '\\frac{S_1}{S_2} &= \\left(\\frac{r_1}{r_2}\\right)^2 \\\\' +
      '&= \\left(\\frac{1}{' + k + '}\\right)^2 \\\\' +
      '&= \\frac{1}{' + kSq + '}' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ पृष्ठीय क्षेत्रफलों का अनुपात = 1 : ' + kSq + '</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // Initial calculation on page load
  window.addEventListener('DOMContentLoaded', function() {
    calculateSim1();
    calculateSim2();
    calculateSim3();
    calculateSim4();
    calculateSim5();
  });
  </script>
</body>
</html>
'''

with open('qa_master_math9_11.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("qa_master_math9_11.html generated successfully!")
