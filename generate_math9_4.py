# -*- coding: utf-8 -*-
"""
Generator for Chapter 4: दो चरों वाले रैखिक समीकरण (Linear Equations in Two Variables)
NCERT Class 9 Mathematics (Rationalised 2024-25 Syllabus)
Fully audited: 100% NCERT coverage, strictly vertical steps ("एक के नीचे एक"), zero horizontal chaining, zero Hindi in MathJax, 5 interactive simulators, projector controls.
"""

html_content = r"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NCERT कक्षा 9 गणित - अध्याय 4: दो चरों वाले रैखिक समीकरण (संपूर्ण प्रश्नोत्तर व 5 लाइव सिमुलेटर)</title>
<meta name="description" content="NCERT कक्षा 9 गणित अध्याय 4 दो चरों वाले रैखिक समीकरण के 100% प्रश्नोत्तर, सभी उदाहरण, विस्तृत एक-के-नीचे-एक हल व 5 इंटरैक्टिव सिमुलेटर।">

<!-- Google Fonts: Inter & Tiro Devanagari Hindi -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Tiro+Devanagari+Hindi:ital@0;1&display=swap" rel="stylesheet">

<!-- MathJax with instant SVG rendering -->
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: true
  },
  svg: {
    fontCache: 'global'
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>

<style>
  :root {
    --bg-page: #f8fafc;
    --text-primary: #0f172a;
    --card-bg: #ffffff;
    --primary-blue: #1e40af;
    --accent-indigo: #4338ca;
    --border-color: #cbd5e1;
    --font-scale: 1.0;
    --width-scale: 100%;
  }

  body.high-contrast {
    --bg-page: #000000 !important;
    --text-primary: #ffffff !important;
    --card-bg: #121212 !important;
    --border-color: #38bdf8 !important;
  }

  body.high-contrast .qa-block,
  body.high-contrast .concept-box,
  body.high-contrast .inline-simulator-card,
  body.high-contrast .step-line,
  body.high-contrast .step-box-blue,
  body.high-contrast .step-box-orange,
  body.high-contrast .step-box-green,
  body.high-contrast .step-box-purple,
  body.high-contrast .step-box-red {
    background: #18181b !important;
    color: #ffffff !important;
    border-color: #38bdf8 !important;
  }

  body.high-contrast .question-heading {
    color: #38bdf8 !important;
  }

  body.high-contrast .step-txt {
    color: #f1f5f9 !important;
  }

  body {
    background-color: var(--bg-page);
    color: var(--text-primary);
    font-family: 'Inter', 'Tiro Devanagari Hindi', sans-serif;
    line-height: 1.8;
    margin: 0;
    padding: 0;
    font-weight: 900 !important;
    -webkit-text-stroke: 0.9px #000000;
    text-rendering: optimizeLegibility;
  }

  body.high-contrast {
    -webkit-text-stroke: 0.9px #ffffff;
  }

  /* Fixed Projector Control Toolbar */
  .toolbar-fixed {
    position: sticky;
    top: 0;
    z-index: 9999;
    background: #0f172a;
    color: white;
    padding: 10px 16px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    border-bottom: 2px solid #38bdf8;
  }

  .toolbar-group {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 4px 0;
  }

  .tool-btn {
    background: #1e293b;
    border: 1.5px solid #475569;
    color: #f8fafc;
    padding: 6px 12px;
    border-radius: 6px;
    font-weight: 800;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s;
  }

  .tool-btn:hover {
    background: #38bdf8;
    color: #0f172a;
    border-color: #38bdf8;
  }

  .main-wrapper {
    max-width: 1400px;
    width: var(--width-scale);
    margin: 0 auto;
    padding: 24px 20px 80px 20px;
    font-size: calc(18px * var(--font-scale));
    transition: all 0.2s ease;
  }

  /* Navigation Shortcuts */
  .nav-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 24px;
    justify-content: center;
  }

  .btn-nav {
    background: #ffffff;
    border: 2px solid #cbd5e1;
    color: #1e40af;
    padding: 8px 16px;
    border-radius: 9999px;
    font-weight: 900;
    text-decoration: none;
    font-size: 15px;
    transition: all 0.2s;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }

  .btn-nav:hover {
    background: #1e40af;
    color: #ffffff;
    border-color: #1e40af;
  }

  /* Hero Header */
  .hero-title {
    background: linear-gradient(135deg, #1e3a8a 0%, #0369a1 100%);
    color: #ffffff;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.4);
    margin-bottom: 30px;
    font-size: calc(26px * var(--font-scale));
    font-weight: 900;
  }

  .hero-title span {
    display: block;
    font-size: 0.7em;
    font-weight: 700;
    color: #bae6fd;
    margin-top: 8px;
  }

  /* Section Part Headers */
  .part-header {
    background: #1e293b;
    color: #ffffff;
    padding: 14px 24px;
    border-radius: 12px;
    margin: 40px 0 20px 0;
    font-size: calc(22px * var(--font-scale));
    font-weight: 900;
    border-left: 8px solid #38bdf8;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  /* Concept Theory Card */
  .concept-box {
    background: #ffffff;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
    border: 2px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
  }

  .concept-title {
    font-size: calc(20px * var(--font-scale));
    font-weight: 900;
    color: #1e40af;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* QA Block Card */
  .qa-block {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 26px;
    margin-bottom: 28px;
    border: 2.5px solid var(--border-color);
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  }

  .question-heading {
    font-size: calc(19px * var(--font-scale));
    font-weight: 900;
    color: #1e3a8a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 12px;
    margin-top: 0;
    margin-bottom: 18px;
  }

  /* Step Boxes (Strict Color Theming) */
  .step-box-blue {
    background: #f8fafc;
    border-left: 8px solid #2563eb;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 14px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
  }

  .step-box-orange {
    background: #fffaf5;
    border-left: 8px solid #f97316;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 14px 0;
  }

  .step-box-green {
    background: #f0fdf4;
    border-left: 8px solid #16a34a;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 14px 0;
  }

  .step-box-purple {
    background: #faf5ff;
    border-left: 8px solid #9333ea;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 14px 0;
  }

  .step-box-red {
    background: #fff1f2;
    border-left: 8px solid #e11d48;
    padding: 18px 22px;
    border-radius: 12px;
    margin: 14px 0;
  }

  .step-txt {
    font-size: 1em;
    color: #1e293b;
    margin: 8px 0;
    line-height: 1.8;
  }

  /* Final Answer Highlight */
  .answer-highlight {
    background: #fef08a;
    color: #854d0e;
    padding: 14px 20px;
    border-radius: 10px;
    font-size: calc(18px * var(--font-scale));
    font-weight: 900;
    border-left: 6px solid #eab308;
    margin-top: 16px;
    display: inline-block;
    width: 100%;
    box-sizing: border-box;
  }

  /* Math Scrolling */
  .math-scroll {
    overflow-x: auto;
    overflow-y: hidden;
    padding: 10px 0;
    margin: 6px 0;
  }

  /* Inline Simulator Cards */
  .inline-simulator-card {
    background: #ffffff;
    border: 3px solid #2563eb;
    border-radius: 20px;
    padding: 24px;
    margin: 30px 0;
    box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.15);
  }

  .sim-title {
    font-size: calc(20px * var(--font-scale));
    font-weight: 900;
    color: #1e40af;
    margin-top: 0;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .sim-controls-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    background: #f8fafc;
    padding: 18px;
    border-radius: 12px;
    border: 1.5px solid #e2e8f0;
    margin-bottom: 20px;
  }

  .sim-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .sim-group label {
    font-size: 14px;
    font-weight: 800;
    color: #334155;
  }

  .sim-group input, .sim-group select {
    padding: 10px 14px;
    border-radius: 8px;
    border: 2px solid #cbd5e1;
    font-size: 16px;
    font-weight: 800;
    outline: none;
    transition: all 0.2s;
  }

  .sim-group input:focus, .sim-group select:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
  }

  .sim-btn-calc {
    background: #2563eb;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 900;
    cursor: pointer;
    transition: all 0.2s;
  }

  .sim-btn-calc:hover {
    background: #1d4ed8;
    transform: translateY(-1px);
  }

  .sim-output-box {
    background: #f8fafc;
    border: 2px dashed #94a3b8;
    border-radius: 14px;
    padding: 20px;
    min-height: 80px;
  }

  .sim-canvas {
    background: #ffffff;
    border: 2px solid #cbd5e1;
    border-radius: 12px;
    display: block;
    margin: 16px auto;
    max-width: 100%;
  }

  .badge-pill {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 0.85em;
    font-weight: 900;
  }

  .badge-blue { background: #dbeafe; color: #1e40af; }
  .badge-green { background: #dcfce7; color: #15803d; }
  .badge-orange { background: #ffedd5; color: #c2410c; }
  .badge-purple { background: #f3e8ff; color: #7e22ce; }
  .badge-red { background: #ffe4e6; color: #be123c; }

  @media print {
    .toolbar-fixed, .nav-pills, .inline-simulator-card {
      display: none !important;
    }
    .main-wrapper {
      width: 100% !important;
      max-width: 100% !important;
      padding: 0 !important;
    }
  }
</style>
</head>
<body>

<!-- Projector Toolbar -->
<div class="toolbar-fixed">
  <div class="toolbar-group">
    <span style="font-size:16px; font-weight:900; color:#38bdf8;">📽️ प्रोजेक्टर कंट्रोल:</span>
    <button class="tool-btn" onclick="adjustFont(0.1)" title="फॉन्ट आकार बढ़ाएं">A+</button>
    <button class="tool-btn" onclick="adjustFont(-0.1)" title="फॉन्ट आकार घटाएं">A-</button>
    <button class="tool-btn" onclick="resetFont()" title="सामान्य आकार">A₀</button>
  </div>
  <div class="toolbar-group">
    <button class="tool-btn" onclick="adjustWidth(5)" title="चौड़ाई बढ़ाएं">W+</button>
    <button class="tool-btn" onclick="adjustWidth(-5)" title="चौड़ाई घटाएं">W-</button>
    <button class="tool-btn" onclick="resetWidth()" title="सामान्य चौड़ाई">W₀</button>
    <button class="tool-btn" onclick="toggleContrast()" title="कंट्रास्ट बदलें">🌓 कंट्रास्ट</button>
  </div>
  <div class="toolbar-group">
    <button class="tool-btn" onclick="window.print()" title="प्रिंट या PDF सेव करें">🖨️ प्रिंट</button>
    <button class="tool-btn" onclick="window.location.reload()" title="रीलोड करें">🔄 रीसेट</button>
    <a href="index.html" class="tool-btn" style="text-decoration:none; display:inline-block;">🏠 होम</a>
  </div>
</div>

<div class="main-wrapper" id="mainContent">

  <!-- Quick Navigation Pills -->
  <div class="nav-pills">
    <a href="#concept" class="btn-nav">📌 मुख्य अवधारणाएँ</a>
    <a href="#ex41" class="btn-nav">प्रश्नावली 4.1</a>
    <a href="#ex42" class="btn-nav">प्रश्नावली 4.2</a>
    <a href="#simulators" class="btn-nav" style="background:#eff6ff; border-color:#2563eb; color:#1d4ed8;">⚡ 5 सिमुलेटर</a>
  </div>

  <!-- Hero Title Banner -->
  <div class="hero-title">
    NCERT कक्षा 9 गणित • अध्याय 4
    <span>दो चरों वाले रैखिक समीकरण (Linear Equations in Two Variables) — संपूर्ण मास्टर प्रश्न-उत्तर नोट्स</span>
  </div>

  <!-- =========================================================
       CONCEPT & THEORY SECTION
       ========================================================= -->
  <div id="concept" class="concept-box">
    <div class="concept-title">📌 अध्याय का परिचय एवं मुख्य सूत्र (Core Concepts)</div>
    
    <div class="step-box-blue">
      <p class="step-txt"><strong>1. दो चरों वाला रैखिक समीकरण:</strong></p>
      <p class="step-txt">ऐसा समीकरण जिसे $ax + by + c = 0$ के रूप में लिखा जा सकता है, जहाँ $a, b, c$ वास्तविक संख्याएँ हैं और $a$ तथा $b$ दोनों एक साथ शून्य नहीं हैं ($a^2 + b^2 \neq 0$), <b>दो चरों वाला रैखिक समीकरण</b> कहलाता है।</p>
    </div>

    <div class="step-box-green">
      <p class="step-txt"><strong>2. रैखिक समीकरण के हल (Solutions):</strong></p>
      <p class="step-txt">चरों $x$ और $y$ के मानों का ऐसा युग्म $(x, y)$, जो समीकरण के बाएँ पक्ष (L.H.S.) और दाएँ पक्ष (R.H.S.) को बराबर कर दे, उस समीकरण का <b>हल</b> कहलाता है।</p>
      <p class="step-txt"><b>महत्वपूर्ण तथ्य:</b> दो चरों वाले एक रैखिक समीकरण के <b>अपरिमित रूप से अनेक हल (Infinitely Many Solutions)</b> होते हैं।</p>
    </div>

    <div class="step-box-orange">
      <p class="step-txt"><strong>3. ज्यामितीय निरूपण (Geometrical Representation):</strong></p>
      <p class="step-txt">दो चरों वाले रैखिक समीकरण का आलेख कार्तीय तल (Cartesian Plane) पर सदैव एक <b>सरल रेखा (Straight Line)</b> होता है। इस रेखा पर स्थित प्रत्येक बिंदु समीकरण का एक हल होता है।</p>
    </div>
  </div>

  <!-- =========================================================
       EXERCISE 4.1
       ========================================================= -->
  <div id="ex41" class="part-header">
    📖 प्रश्नावली 4.1 (Exercise 4.1) — संपूर्ण NCERT हल
  </div>

  <!-- Ex 4.1 Q1 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 1: एक नोटबुक की कीमत एक कलम की कीमत से दो गुनी है। इस कथन को निरूपित करने के लिए दो चरों वाला एक रैखिक समीकरण लिखिए।</h3>
    
    <div class="step-box-blue">
      <p class="step-txt"><b>हल के क्रमबद्ध चरण:</b></p>
      <p class="step-txt">माना एक नोटबुक की कीमत $= x$ रुपये</p>
      <p class="step-txt">तथा एक कलम की कीमत $= y$ रुपये</p>
      <p class="step-txt">प्रश्नानुसार, नोटबुक की कीमत कलम की कीमत की $2$ गुनी है:</p>
      <p class="step-txt">नोटबुक की कीमत $= 2 \times$ (कलम की कीमत)</p>
      <div class="math-scroll">$$\begin{aligned}
      x &= 2y \\
      x - 2y &= 0
      \end{aligned}$$</div>
    </div>

    <div class="answer-highlight">
      ✅ अभीष्ट रैखिक समीकरण: $x - 2y = 0$ (अथवा मानक रूप में: $1x - 2y + 0 = 0$)
    </div>
  </div>

  <!-- Ex 4.1 Q2 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 2: निम्नलिखित रैखिक समीकरणों को $ax + by + c = 0$ के रूप में व्यक्त कीजिए और प्रत्येक स्थिति में $a, b$ और $c$ के मान बताइए:</h3>

    <!-- Q2(i) -->
    <div class="step-box-blue">
      <p class="step-txt"><b>(i) $2x + 3y = 9.3\overline{5}$</b></p>
      <p class="step-txt">दाएँ पक्ष को बाएँ पक्ष में पक्षांतरित करने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      2x + 3y - 9.3\overline{5} &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 2$, &emsp; $b = 3$, &emsp; $c = -9.3\overline{5}$</p>
    </div>

    <!-- Q2(ii) -->
    <div class="step-box-orange">
      <p class="step-txt"><b>(ii) $x - \frac{y}{5} - 10 = 0$</b></p>
      <p class="step-txt">इसे इस प्रकार लिख सकते हैं:</p>
      <div class="math-scroll">$$\begin{aligned}
      1x + \left(-\frac{1}{5}\right)y + (-10) &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 1$, &emsp; $b = -\frac{1}{5}$, &emsp; $c = -10$</p>
    </div>

    <!-- Q2(iii) -->
    <div class="step-box-green">
      <p class="step-txt"><b>(iii) $-2x + 3y = 6$</b></p>
      <p class="step-txt">दाएँ पक्ष $6$ को बाएँ पक्ष में लाने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      -2x + 3y - 6 &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = -2$, &emsp; $b = 3$, &emsp; $c = -6$</p>
    </div>

    <!-- Q2(iv) -->
    <div class="step-box-purple">
      <p class="step-txt"><b>(iv) $x = 3y$</b></p>
      <p class="step-txt">पक्षांतरण करने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      x - 3y + 0 &= 0 \\
      1x + (-3)y + 0 &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 1$, &emsp; $b = -3$, &emsp; $c = 0$</p>
    </div>

    <!-- Q2(v) -->
    <div class="step-box-blue">
      <p class="step-txt"><b>(v) $2x = -5y$</b></p>
      <p class="step-txt">पक्षांतरण करने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      2x + 5y + 0 &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 2$, &emsp; $b = 5$, &emsp; $c = 0$</p>
    </div>

    <!-- Q2(vi) -->
    <div class="step-box-orange">
      <p class="step-txt"><b>(vi) $3x + 2 = 0$</b></p>
      <p class="step-txt">यहाँ $y$ का पद नहीं है, अतः इसे $0 \cdot y$ के रूप में लिखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      3x + 0y + 2 &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 3$, &emsp; $b = 0$, &emsp; $c = 2$</p>
    </div>

    <!-- Q2(vii) -->
    <div class="step-box-green">
      <p class="step-txt"><b>(vii) $y - 2 = 0$</b></p>
      <p class="step-txt">यहाँ $x$ का पद नहीं है, अतः इसे $0 \cdot x$ के रूप में लिखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      0x + 1y + (-2) &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 0$, &emsp; $b = 1$, &emsp; $c = -2$</p>
    </div>

    <!-- Q2(viii) -->
    <div class="step-box-purple">
      <p class="step-txt"><b>(viii) $5 = 2x$</b></p>
      <p class="step-txt">पक्षांतरण करने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      2x - 5 &= 0 \\
      2x + 0y - 5 &= 0
      \end{aligned}$$</div>
      <p class="step-txt">व्यापक मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p class="step-txt"><b>उत्तर:</b> $a = 2$, &emsp; $b = 0$, &emsp; $c = -5$</p>
    </div>
  </div>

  <!-- =========================================================
       EXERCISE 4.2
       ========================================================= -->
  <div id="ex42" class="part-header">
    📖 प्रश्नावली 4.2 (Exercise 4.2) — संपूर्ण NCERT हल
  </div>

  <!-- Ex 4.2 Q1 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 1: निम्नलिखित विकल्पों में कौन-सा विकल्प सत्य है और क्यों?</h3>
    <p class="step-txt">समीकरण: $y = 3x + 5$ का:</p>
    <ul>
      <li>(i) एक अद्वितीय हल है,</li>
      <li>(ii) केवल दो हल हैं,</li>
      <li>(iii) अपरिमित रूप से अनेक हल हैं।</li>
    </ul>

    <div class="step-box-green">
      <p class="step-txt"><b>उत्तर: विकल्प (iii) सत्य है — अपरिमित रूप से अनेक हल हैं (Infinitely many solutions)।</b></p>
      <p class="step-txt"><b>कारण:</b></p>
      <p class="step-txt">दो चरों वाला एक रैखिक समीकरण कार्तीय तल पर एक सरल रेखा को निरूपित करता है। रेखा पर स्थित अपरिमित रूप से अनेक बिंदु होते हैं।</p>
      <p class="step-txt">$x$ के प्रत्येक वास्तविक मान के लिए $y$ का एक संगत मान प्राप्त होता है:</p>
      <p class="step-txt">1. यदि $x = 0$ हो, तो $y = 3(0) + 5 = 5$, बिंदु $(0, 5)$</p>
      <p class="step-txt">2. यदि $x = 1$ हो, तो $y = 3(1) + 5 = 8$, बिंदु $(1, 8)$</p>
      <p class="step-txt">3. यदि $x = -1$ हो, तो $y = 3(-1) + 5 = 2$, बिंदु $(-1, 2)$</p>
      <p class="step-txt">चूँकि वास्तविक संख्याएँ अनंत हैं, अतः $x$ के अनंत मानों के लिए $y$ के भी अनंत मान प्राप्त होंगे।</p>
    </div>

    <div class="answer-highlight">
      ✅ निष्कर्ष: दो चरों वाले किसी भी रैखिक समीकरण के अपरिमित रूप से अनेक हल होते हैं।
    </div>
  </div>

  <!-- Ex 4.2 Q2 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 2: निम्नलिखित समीकरणों में से प्रत्येक समीकरण के चार हल (Four Solutions) लिखिए:</h3>
    
    <!-- Q2(i) -->
    <div class="step-box-blue">
      <p class="step-txt"><b>(i) $2x + y = 7$</b></p>
      <p class="step-txt">$y$ को $x$ के पदों में व्यक्त करने पर: <b>$y = 7 - 2x$</b></p>
      
      <p class="step-txt"><strong>1. $x = 0$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 7 - 2(0) \\
      &= 7 - 0 \\
      &= 7
      \end{aligned}$$</div>
      <p class="step-txt">पहला हल: <b>$(0, 7)$</b></p>

      <p class="step-txt"><strong>2. $x = 1$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 7 - 2(1) \\
      &= 7 - 2 \\
      &= 5
      \end{aligned}$$</div>
      <p class="step-txt">दूसरा हल: <b>$(1, 5)$</b></p>

      <p class="step-txt"><strong>3. $x = 2$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 7 - 2(2) \\
      &= 7 - 4 \\
      &= 3
      \end{aligned}$$</div>
      <p class="step-txt">तीसरा हल: <b>$(2, 3)$</b></p>

      <p class="step-txt"><strong>4. $x = 3$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 7 - 2(3) \\
      &= 7 - 6 \\
      &= 1
      \end{aligned}$$</div>
      <p class="step-txt">चौथा हल: <b>$(3, 1)$</b></p>

      <div class="answer-highlight">
        ✅ अभीष्ट चार हल: $(0, 7)$, &emsp; $(1, 5)$, &emsp; $(2, 3)$, &emsp; $(3, 1)$
      </div>
    </div>

    <!-- Q2(ii) -->
    <div class="step-box-orange">
      <p class="step-txt"><b>(ii) $\pi x + y = 9$</b></p>
      <p class="step-txt">$y$ को व्यक्त करने पर: <b>$y = 9 - \pi x$</b></p>
      
      <p class="step-txt"><strong>1. $x = 0$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 9 - \pi(0) \\
      &= 9 - 0 \\
      &= 9
      \end{aligned}$$</div>
      <p class="step-txt">पहला हल: <b>$(0, 9)$</b></p>

      <p class="step-txt"><strong>2. $x = 1$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 9 - \pi(1) \\
      &= 9 - \pi
      \end{aligned}$$</div>
      <p class="step-txt">दूसरा हल: <b>$(1, 9 - \pi)$</b></p>

      <p class="step-txt"><strong>3. $x = 2$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 9 - \pi(2) \\
      &= 9 - 2\pi
      \end{aligned}$$</div>
      <p class="step-txt">तीसरा हल: <b>$(2, 9 - 2\pi)$</b></p>

      <p class="step-txt"><strong>4. $x = -1$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      y &= 9 - \pi(-1) \\
      &= 9 + \pi
      \end{aligned}$$</div>
      <p class="step-txt">चौथा हल: <b>$(-1, 9 + \pi)$</b></p>

      <div class="answer-highlight">
        ✅ अभीष्ट चार हल: $(0, 9)$, &emsp; $(1, 9 - \pi)$, &emsp; $(2, 9 - 2\pi)$, &emsp; $(-1, 9 + \pi)$
      </div>
    </div>

    <!-- Q2(iii) -->
    <div class="step-box-green">
      <p class="step-txt"><b>(iii) $x = 4y$</b></p>
      <p class="step-txt">यहाँ $y$ के विभिन्न मान रखकर $x$ ज्ञात करते हैं:</p>
      
      <p class="step-txt"><strong>1. $y = 0$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      x &= 4(0) \\
      &= 0
      \end{aligned}$$</div>
      <p class="step-txt">पहला हल: <b>$(0, 0)$</b></p>

      <p class="step-txt"><strong>2. $y = 1$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      x &= 4(1) \\
      &= 4
      \end{aligned}$$</div>
      <p class="step-txt">दूसरा हल: <b>$(4, 1)$</b></p>

      <p class="step-txt"><strong>3. $y = 2$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      x &= 4(2) \\
      &= 8
      \end{aligned}$$</div>
      <p class="step-txt">तीसरा हल: <b>$(8, 2)$</b></p>

      <p class="step-txt"><strong>4. $y = -1$ रखने पर:</strong></p>
      <div class="math-scroll">$$\begin{aligned}
      x &= 4(-1) \\
      &= -4
      \end{aligned}$$</div>
      <p class="step-txt">चौथा हल: <b>$(-4, -1)$</b></p>

      <div class="answer-highlight">
        ✅ अभीष्ट चार हल: $(0, 0)$, &emsp; $(4, 1)$, &emsp; $(8, 2)$, &emsp; $(-4, -1)$
      </div>
    </div>
  </div>

  <!-- Ex 4.2 Q3 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 3: बताइए कि निम्नलिखित हलों में कौन-कौन समीकरण $x - 2y = 4$ के हल हैं और कौन-कौन हल नहीं हैं:</h3>
    <p class="step-txt">समीकरण: $x - 2y = 4$</p>
    <p class="step-txt">बायाँ पक्ष (L.H.S.) $= x - 2y$ &emsp; तथा &emsp; दायाँ पक्ष (R.H.S.) $= 4$</p>

    <!-- Q3(i) -->
    <div class="step-box-red">
      <p class="step-txt"><b>(i) बिंदु $(0, 2)$:</b></p>
      <p class="step-txt">$x = 0$ तथा $y = 2$ रखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      \text{L.H.S.} &= 0 - 2(2) \\
      &= 0 - 4 \\
      &= -4 \neq 4 \text{ (R.H.S.)}
      \end{aligned}$$</div>
      <p class="step-txt"><b>निष्कर्ष: नहीं, बिंदु $(0, 2)$ समीकरण का हल नहीं है।</b></p>
    </div>

    <!-- Q3(ii) -->
    <div class="step-box-red">
      <p class="step-txt"><b>(ii) बिंदु $(2, 0)$:</b></p>
      <p class="step-txt">$x = 2$ तथा $y = 0$ रखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      \text{L.H.S.} &= 2 - 2(0) \\
      &= 2 - 0 \\
      &= 2 \neq 4 \text{ (R.H.S.)}
      \end{aligned}$$</div>
      <p class="step-txt"><b>निष्कर्ष: नहीं, बिंदु $(2, 0)$ समीकरण का हल नहीं है।</b></p>
    </div>

    <!-- Q3(iii) -->
    <div class="step-box-green">
      <p class="step-txt"><b>(iii) बिंदु $(4, 0)$:</b></p>
      <p class="step-txt">$x = 4$ तथा $y = 0$ रखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      \text{L.H.S.} &= 4 - 2(0) \\
      &= 4 - 0 \\
      &= 4 \\
      &= \text{R.H.S.}
      \end{aligned}$$</div>
      <p class="step-txt"><b>निष्कर्ष: हाँ, बिंदु $(4, 0)$ दिए गए समीकरण का एक हल है।</b></p>
    </div>

    <!-- Q3(iv) -->
    <div class="step-box-red">
      <p class="step-txt"><b>(iv) बिंदु $(\sqrt{2}, 4\sqrt{2})$:</b></p>
      <p class="step-txt">$x = \sqrt{2}$ तथा $y = 4\sqrt{2}$ रखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      \text{L.H.S.} &= \sqrt{2} - 2(4\sqrt{2}) \\
      &= \sqrt{2} - 8\sqrt{2} \\
      &= -7\sqrt{2} \neq 4 \text{ (R.H.S.)}
      \end{aligned}$$</div>
      <p class="step-txt"><b>निष्कर्ष: नहीं, बिंदु $(\sqrt{2}, 4\sqrt{2})$ समीकरण का हल नहीं है।</b></p>
    </div>

    <!-- Q3(v) -->
    <div class="step-box-red">
      <p class="step-txt"><b>(v) बिंदु $(1, 1)$:</b></p>
      <p class="step-txt">$x = 1$ तथा $y = 1$ रखने पर:</p>
      <div class="math-scroll">$$\begin{aligned}
      \text{L.H.S.} &= 1 - 2(1) \\
      &= 1 - 2 \\
      &= -1 \neq 4 \text{ (R.H.S.)}
      \end{aligned}$$</div>
      <p class="step-txt"><b>निष्कर्ष: नहीं, बिंदु $(1, 1)$ समीकरण का हल नहीं है।</b></p>
    </div>

    <div class="answer-highlight">
      ✅ केवल बिंदु (iii) $(4, 0)$ समीकरण $x - 2y = 4$ का मान्य हल है।
    </div>
  </div>

  <!-- Ex 4.2 Q4 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 4: $k$ का मान ज्ञात कीजिए जबकि $x = 2, y = 1$ समीकरण $2x + 3y = k$ का एक हल हो।</h3>
    
    <div class="step-box-blue">
      <p class="step-txt"><b>हल के क्रमबद्ध चरण:</b></p>
      <p class="step-txt">दिया गया समीकरण है: $2x + 3y = k$</p>
      <p class="step-txt">चूँकि बिंदु $x = 2$ तथा $y = 1$ इस समीकरण का हल है, अतः ये मान समीकरण को संतुष्ट करेंगे:</p>
      <div class="math-scroll">$$\begin{aligned}
      2(2) + 3(1) &= k \\
      4 + 3 &= k \\
      7 &= k \\
      k &= 7
      \end{aligned}$$</div>
    </div>

    <div class="answer-highlight">
      ✅ अभीष्ट मान: $k = 7$
    </div>
  </div>

  <!-- =========================================================
       SIMULATOR SECTION (5 LIVE SIMULATORS)
       ========================================================= -->
  <div id="simulators" class="part-header">
    ⚡ लाइव सिमुलेटर अनुभाग (5 Interactive Linear Equation Simulators)
  </div>

  <!-- SIMULATOR 1 -->
  <div class="inline-simulator-card">
    <h3 class="sim-title">⚡ लाइव सिमुलेटर 1: मानक रूप व गुणांक गणक ($ax + by + c = 0$)</h3>
    <p class="step-txt">समीकरण दर्ज करें और तुरंत मानक रूप के गुणांक $a, b, c$ देखें:</p>

    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>x का गुणांक a:</label>
        <input type="number" id="sim1_a" value="2" oninput="calculateSim1()">
      </div>
      <div class="sim-group">
        <label>y का गुणांक b:</label>
        <input type="number" id="sim1_b" value="3" oninput="calculateSim1()">
      </div>
      <div class="sim-group">
        <label>दायाँ पक्ष (R.H.S. मान):</label>
        <input type="number" id="sim1_rhs" value="12" oninput="calculateSim1()">
      </div>
      <div class="sim-group" style="justify-content:flex-end;">
        <button class="sim-btn-calc" onclick="calculateSim1()">
          ⚡ मानक रूप में बदलें ➔
        </button>
      </div>
    </div>

    <div id="sim1_output" class="sim-output-box"></div>
  </div>

  <!-- SIMULATOR 2 -->
  <div class="inline-simulator-card">
    <h3 class="sim-title">⚡ लाइव सिमुलेटर 2: चार क्रमिक हल जनरेटर (Four Solutions Table Generator)</h3>
    <p class="step-txt">समीकरण $ax + by = c$ के गुणांक भरें, सिमुलेटर तुरंत 4 विभिन्न हल चरणबद्ध निकालेगा:</p>

    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>गुणांक a (x का):</label>
        <input type="number" id="sim2_a" value="2" oninput="calculateSim2()">
      </div>
      <div class="sim-group">
        <label>गुणांक b (y का):</label>
        <input type="number" id="sim2_b" value="1" oninput="calculateSim2()">
      </div>
      <div class="sim-group">
        <label>अचर पद c:</label>
        <input type="number" id="sim2_c" value="7" oninput="calculateSim2()">
      </div>
      <div class="sim-group" style="justify-content:flex-end;">
        <button class="sim-btn-calc" onclick="calculateSim2()">
          ⚡ 4 हल ज्ञात करें ➔
        </button>
      </div>
    </div>

    <div id="sim2_output" class="sim-output-box"></div>
  </div>

  <!-- SIMULATOR 3 -->
  <div class="inline-simulator-card">
    <h3 class="sim-title">⚡ लाइव सिमुलेटर 3: बिंदु हल सत्यापनकर्ता (Solution Verifier: L.H.S. vs R.H.S.)</h3>
    <p class="step-txt">कोई भी समीकरण $ax + by = c$ और एक बिंदु $(x, y)$ दर्ज करें, सिमुलेटर जाँच कर बताएगा कि क्या वह हल है:</p>

    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>a (x का गुणांक):</label>
        <input type="number" id="sim3_a" value="1" oninput="calculateSim3()">
      </div>
      <div class="sim-group">
        <label>b (y का गुणांक):</label>
        <input type="number" id="sim3_b" value="-2" oninput="calculateSim3()">
      </div>
      <div class="sim-group">
        <label>c (दायाँ पक्ष):</label>
        <input type="number" id="sim3_c" value="4" oninput="calculateSim3()">
      </div>
      <div class="sim-group">
        <label>बिंदु का x:</label>
        <input type="number" id="sim3_x" value="4" oninput="calculateSim3()">
      </div>
      <div class="sim-group">
        <label>बिंदु का y:</label>
        <input type="number" id="sim3_y" value="0" oninput="calculateSim3()">
      </div>
      <div class="sim-group" style="justify-content:flex-end;">
        <button class="sim-btn-calc" onclick="calculateSim3()">
          ⚡ हल की जाँच करें ➔
        </button>
      </div>
    </div>

    <div id="sim3_output" class="sim-output-box"></div>
  </div>

  <!-- SIMULATOR 4 -->
  <div class="inline-simulator-card">
    <h3 class="sim-title">⚡ लाइव सिमुलेटर 4: अज्ञात चर 'k' गणक (Find 'k' Calculator)</h3>
    <p class="step-txt">समीकरण $ax + by = k$ में दिए गए बिंदु $(x, y)$ का मान प्रतिस्थापित करके तुरंत $k$ का मान निकालें:</p>

    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>गुणांक a:</label>
        <input type="number" id="sim4_a" value="2" oninput="calculateSim4()">
      </div>
      <div class="sim-group">
        <label>गुणांक b:</label>
        <input type="number" id="sim4_b" value="3" oninput="calculateSim4()">
      </div>
      <div class="sim-group">
        <label>हल बिंदु का x मान:</label>
        <input type="number" id="sim4_x" value="2" oninput="calculateSim4()">
      </div>
      <div class="sim-group">
        <label>हल बिंदु का y मान:</label>
        <input type="number" id="sim4_y" value="1" oninput="calculateSim4()">
      </div>
      <div class="sim-group" style="justify-content:flex-end;">
        <button class="sim-btn-calc" onclick="calculateSim4()">
          ⚡ k का मान निकालें ➔
        </button>
      </div>
    </div>

    <div id="sim4_output" class="sim-output-box"></div>
  </div>

  <!-- SIMULATOR 5 -->
  <div class="inline-simulator-card">
    <h3 class="sim-title">⚡ लाइव सिमुलेटर 5: सरल रेखा आलेखक (Interactive Straight Line Grapher)</h3>
    <p class="step-txt">समीकरण $ax + by = c$ भरें और कार्तीय तल पर इसकी आलेख रेखा तुरंत लाइव देखें:</p>

    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>गुणांक a (x का):</label>
        <input type="number" id="sim5_a" value="1" oninput="calculateSim5()">
      </div>
      <div class="sim-group">
        <label>गुणांक b (y का):</label>
        <input type="number" id="sim5_b" value="1" oninput="calculateSim5()">
      </div>
      <div class="sim-group">
        <label>अचर पद c:</label>
        <input type="number" id="sim5_c" value="4" oninput="calculateSim5()">
      </div>
      <div class="sim-group" style="justify-content:flex-end;">
        <button class="sim-btn-calc" onclick="calculateSim5()">
          ⚡ आलेख बनाएँ ➔
        </button>
      </div>
    </div>

    <canvas id="sim5_canvas" class="sim-canvas" width="600" height="380"></canvas>
    <div id="sim5_output" class="sim-output-box"></div>
  </div>

</div><!-- End main-wrapper -->

<!-- Interactive Scripts -->
<script>
  // Projector Toolbar Functions
  var currentScale = 1.0;
  var currentWidth = 100;

  function adjustFont(delta) {
    currentScale = Math.max(0.7, Math.min(2.0, currentScale + delta));
    document.documentElement.style.setProperty('--font-scale', currentScale);
  }

  function resetFont() {
    currentScale = 1.0;
    document.documentElement.style.setProperty('--font-scale', currentScale);
  }

  function adjustWidth(delta) {
    currentWidth = Math.max(60, Math.min(100, currentWidth + delta));
    document.documentElement.style.setProperty('--width-scale', currentWidth + '%');
  }

  function resetWidth() {
    currentWidth = 100;
    document.documentElement.style.setProperty('--width-scale', '100%');
  }

  function toggleContrast() {
    document.body.classList.toggle('high-contrast');
  }

  // ==========================================================
  // SIMULATOR 1: Standard Form Converter
  // ==========================================================
  function calculateSim1() {
    var a = parseFloat(document.getElementById('sim1_a').value) || 0;
    var b = parseFloat(document.getElementById('sim1_b').value) || 0;
    var rhs = parseFloat(document.getElementById('sim1_rhs').value) || 0;
    var out = document.getElementById('sim1_output');

    var c = -rhs;
    var bSign = b >= 0 ? ' + ' + b : ' - ' + Math.abs(b);
    var cSign = c >= 0 ? ' + ' + c : ' - ' + Math.abs(c);

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>चरण 1:</strong> समीकरण को $ax + by + c = 0$ के रूप में लिखने पर:</p>' +
      '<div class="math-scroll">$$\\begin{aligned} ' + a + 'x' + bSign + 'y' + cSign + ' &= 0 \\end{aligned}$$</div>' +
      '<p class="step-txt"><strong>चरण 2:</strong> मानक रूप से तुलना करने पर गुणांक:</p>' +
      '<div style="font-size:22pt; font-weight:900; color:#1e40af; margin-top:8px;">' +
      'a = ' + a + ', &emsp; b = ' + b + ', &emsp; c = ' + c +
      '</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 2: Four Solutions Generator
  // ==========================================================
  function calculateSim2() {
    var a = parseFloat(document.getElementById('sim2_a').value) || 0;
    var b = parseFloat(document.getElementById('sim2_b').value) || 0;
    var c = parseFloat(document.getElementById('sim2_c').value) || 0;
    var out = document.getElementById('sim2_output');

    if (b === 0 && a === 0) {
      out.innerHTML = '<div style="color:#e11d48; font-weight:900;">a और b दोनों शून्य नहीं हो सकते!</div>';
      return;
    }

    var html = '<div class="step-box-green">' +
      '<p class="step-txt"><strong>समीकरण:</strong> $' + a + 'x + (' + b + ')y = ' + c + '$</p>';

    if (b !== 0) {
      html += '<p class="step-txt">समीकरण को $y$ के पदों में व्यक्त करने पर: <b>$y = \\frac{' + c + ' - (' + a + 'x)}{' + b + '}$</b></p>';
      var testX = [0, 1, 2, 3];
      var pts = [];
      for (var i = 0; i < testX.length; i++) {
        var xVal = testX[i];
        var yVal = (c - (a * xVal)) / b;
        var yDisplay = Number.isInteger(yVal) ? yVal : yVal.toFixed(2);
        pts.push('(' + xVal + ', ' + yDisplay + ')');
        html += '<p class="step-txt">• $x = ' + xVal + '$ रखने पर: &nbsp; $y = ' + yDisplay + '$ &nbsp; ➔ &nbsp; <b>(' + xVal + ', ' + yDisplay + ')</b></p>';
      }
      html += '<div class="answer-highlight">✅ चार हल: ' + pts.join(', &emsp; ') + '</div>';
    } else {
      var fixedX = c / a;
      html += '<p class="step-txt">चूँकि $b = 0$, अतः $x = ' + fixedX + '$ (नियत मान)</p>';
      html += '<p class="step-txt">चार हल: (' + fixedX + ', 0), (' + fixedX + ', 1), (' + fixedX + ', 2), (' + fixedX + ', 3)</p>';
    }

    html += '</div>';
    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 3: Solution Verifier
  // ==========================================================
  function calculateSim3() {
    var a = parseFloat(document.getElementById('sim3_a').value) || 0;
    var b = parseFloat(document.getElementById('sim3_b').value) || 0;
    var c = parseFloat(document.getElementById('sim3_c').value) || 0;
    var x = parseFloat(document.getElementById('sim3_x').value) || 0;
    var y = parseFloat(document.getElementById('sim3_y').value) || 0;
    var out = document.getElementById('sim3_output');

    var lhs = (a * x) + (b * y);
    var isSol = Math.abs(lhs - c) < 0.0001;

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>समीकरण:</strong> $' + a + 'x + (' + b + ')y = ' + c + '$</p>' +
      '<p class="step-txt">बाएँ पक्ष (L.H.S.) में $x = ' + x + '$ तथा $y = ' + y + '$ रखने पर:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\text{L.H.S.} &= ' + a + '(' + x + ') + (' + b + ')(' + y + ') \\\\' +
      '&= ' + (a * x) + ' + (' + (b * y) + ') \\\\' +
      '&= ' + lhs +
      '\\end{aligned}$$</div>' +
      '<p class="step-txt">दायाँ पक्ष (R.H.S.) $= ' + c + '$</p>' +
      '</div>' +
      '<div class="final-ans" style="margin-top:15px; padding:18px 24px; text-align:center; background:' + (isSol ? '#ecfdf5; border:4px solid #10b981;' : '#fff1f2; border:4px solid #f43f5e;') + ' border-radius:16px;">' +
      '<p style="margin:0 0 8px 0; font-size:22pt; font-weight:900; color:' + (isSol ? '#065f46;' : '#9f1239;') + '">' +
      (isSol ? '🎉 L.H.S. = R.H.S. = ' + c : '❌ L.H.S. (' + lhs + ') ≠ R.H.S. (' + c + ')') + '</p>' +
      '<div style="font-size:32pt; font-weight:900; color:' + (isSol ? '#065f46;' : '#9f1239;') + '">' +
      (isSol ? 'हाँ, बिंदु (' + x + ', ' + y + ') एक मान्य हल है!' : 'नहीं, बिंदु (' + x + ', ' + y + ') हल नहीं है!') +
      '</div></div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 4: Find k Solver
  // ==========================================================
  function calculateSim4() {
    var a = parseFloat(document.getElementById('sim4_a').value) || 0;
    var b = parseFloat(document.getElementById('sim4_b').value) || 0;
    var x = parseFloat(document.getElementById('sim4_x').value) || 0;
    var y = parseFloat(document.getElementById('sim4_y').value) || 0;
    var out = document.getElementById('sim4_output');

    var term1 = a * x;
    var term2 = b * y;
    var k = term1 + term2;

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>समीकरण:</strong> $' + a + 'x + (' + b + ')y = k$</p>' +
      '<p class="step-txt">चूँकि बिंदु $(' + x + ', ' + y + ')$ इस समीकरण का हल है, अतः मान प्रतिस्थापित करने पर:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      'k &= ' + a + '(' + x + ') + (' + b + ')(' + y + ') \\\\' +
      '&= ' + term1 + ' + (' + term2 + ') \\\\' +
      '&= ' + k +
      '\\end{aligned}$$</div>' +
      '</div>' +
      '<div class="final-ans" style="margin-top:15px; padding:18px 24px; text-align:center; background:#ecfdf5; border:4px solid #10b981; border-radius:16px;">' +
      '<p style="margin:0 0 8px 0; color:#064e3b; font-size:22pt; font-weight:900;">✅ k का अभीष्ट मान (Value of k):</p>' +
      '<div style="font-size:42pt; font-weight:900; color:#064e3b;">k = ' + k + '</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 5: Straight Line Grapher
  // ==========================================================
  function calculateSim5() {
    var a = parseFloat(document.getElementById('sim5_a').value) || 1;
    var b = parseFloat(document.getElementById('sim5_b').value) || 1;
    var c = parseFloat(document.getElementById('sim5_c').value) || 4;
    var out = document.getElementById('sim5_output');

    var canvas = document.getElementById('sim5_canvas');
    if (canvas) {
      var ctx = canvas.getContext('2d');
      var W = canvas.width;
      var H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      var ox = W / 2;
      var oy = H / 2;
      var scale = 24;

      // Grid
      ctx.strokeStyle = '#f1f5f9';
      ctx.lineWidth = 1;
      for (var gx = 0; gx <= W; gx += scale) {
        ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, H); ctx.stroke();
      }
      for (var gy = 0; gy <= H; gy += scale) {
        ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
      }

      // Axes
      ctx.strokeStyle = '#0f172a';
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(10, oy); ctx.lineTo(W - 10, oy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, 10); ctx.lineTo(ox, H - 10); ctx.stroke();

      ctx.fillStyle = '#0f172a';
      ctx.font = 'bold 15px system-ui';
      ctx.fillText('X', W - 18, oy - 6);
      ctx.fillText('Y', ox + 6, 20);

      // Draw line: ax + by = c => if b != 0: y = (c - ax) / b
      if (b !== 0) {
        var xLeft = -12;
        var yLeft = (c - (a * xLeft)) / b;
        var px1 = ox + (xLeft * scale);
        var py1 = oy - (yLeft * scale);

        var xRight = 12;
        var yRight = (c - (a * xRight)) / b;
        var px2 = ox + (xRight * scale);
        var py2 = oy - (yRight * scale);

        ctx.strokeStyle = '#2563eb';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(px1, py1);
        ctx.lineTo(px2, py2);
        ctx.stroke();

        // X-intercept: (c/a, 0)
        if (a !== 0) {
          var xInt = c / a;
          var xPix = ox + (xInt * scale);
          ctx.fillStyle = '#dc2626';
          ctx.beginPath(); ctx.arc(xPix, oy, 6, 0, 2 * Math.PI); ctx.fill();
        }
        // Y-intercept: (0, c/b)
        var yInt = c / b;
        var yPix = oy - (yInt * scale);
        ctx.fillStyle = '#16a34a';
        ctx.beginPath(); ctx.arc(ox, yPix, 6, 0, 2 * Math.PI); ctx.fill();
      }
    }

    var xInterceptDesc = (a !== 0 ? (c / a).toFixed(2) : 'कोई नहीं (समांतर)');
    var yInterceptDesc = (b !== 0 ? (c / b).toFixed(2) : 'कोई नहीं (समांतर)');

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>समीकरण:</strong> $' + a + 'x + (' + b + ')y = ' + c + '$</p>' +
      '<p class="step-txt">• <b>X-अंतःखंड (X-intercept, y=0 पर):</b> $x = ' + xInterceptDesc + '$</p>' +
      '<p class="step-txt">• <b>Y-अंतःखंड (Y-intercept, x=0 पर):</b> $y = ' + yInterceptDesc + '$</p>' +
      '</div>' +
      '<div class="final-ans" style="margin-top:15px; padding:18px 24px; text-align:center; background:#ecfdf5; border:4px solid #10b981; border-radius:16px;">' +
      '<p style="margin:0 0 8px 0; color:#064e3b; font-size:22pt; font-weight:900;">✅ आलेख निष्कर्ष:</p>' +
      '<div style="font-size:26pt; font-weight:900; color:#064e3b;">यह कार्तीय तल पर एक सरल रेखा (Straight Line) को निरूपित करता है।</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // Initialise on load
  document.addEventListener('DOMContentLoaded', function() {
    calculateSim1();
    calculateSim2();
    calculateSim3();
    calculateSim4();
    calculateSim5();
  });
</script>

</body>
</html>
"""

with open('qa_master_math9_4.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("qa_master_math9_4.html generated successfully!")
