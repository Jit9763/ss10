# -*- coding: utf-8 -*-
"""
Generator for NCERT Class 9 Mathematics Chapter 9: वृत्त (Circles)
File: qa_master_math9_9.html
Strict compliance with:
- Zero horizontal chaining
- Strictly vertical aligned steps
- No Hindi inside MathJax
- Line breaks on long equations to prevent right scrolling
- Safe JS simulator strings (\cdot / ×, no times escape bugs)
- 5 live interactive simulators with projector controls
"""

import sys

content = r'''<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NCERT कक्षा 9 गणित - अध्याय 9: वृत्त (संपूर्ण 100% प्रश्नोत्तर व 5 लाइव सिमुलेटर)</title>

  <!-- Google Fonts & MathJax -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
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
    }
    .question-heading {
      color: #1e3a8a;
      font-size: 24pt;
      font-weight: 900;
      margin: 0 0 16px 0;
      line-height: 1.5;
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
    }

    .step-txt {
      margin: 6px 0;
      font-size: 22pt;
    }

    .math-scroll {
      overflow-x: auto;
      margin: 10px 0;
      padding: 6px 0;
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
    .badge-green {
      background: #dcfce7;
      color: #166534;
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
    }

    svg.geom-canvas {
      display: block;
      margin: 16px auto;
      max-width: 100%;
      height: auto;
      background: #f8fafc;
      border: 2px dashed #94a3b8;
      border-radius: 12px;
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
      <span style="color:#fef08a;">अध्याय 9: वृत्त (Circles)</span>
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
      <h1>अध्याय 9: वृत्त (Circles)</h1>
      <p>NCERT कक्षा 9 गणित (Rationalised Syllabus 2024-25) — संपूर्ण 100% प्रश्नोत्तर, प्रमेय व 5 इंटरैक्टिव लाइव सिमुलेटर</p>
    </div>

    <!-- Core Theorems & Formulas -->
    <div class="section-title">🌟 महत्वपूर्ण प्रमेय एवं मूलभूत अवधारणाएँ (Key Theorems)</div>

    <div class="qa-block">
      <div class="step-box-blue">
        <p><b>1. प्रमेय 9.1:</b> वृत्त की बराबर जीवाएँ केंद्र पर बराबर कोण अंतरित करती हैं।</p>
        <p><b>2. प्रमेय 9.2 (विलोम):</b> यदि केंद्र पर अंतरित कोण बराबर हों, तो जीवाएँ बराबर होती हैं।</p>
        <p><b>3. प्रमेय 9.3:</b> केंद्र से जीवा पर डाला गया लंब जीवा को समद्विभाजित करता है ($AM = MB$) तथा लंब दूरी $d = \sqrt{r^2 - (c/2)^2}$।</p>
        <p><b>4. प्रमेय 9.4 (विलोम):</b> केंद्र से जीवा के मध्य-बिंदु को मिलाने वाली रेखा जीवा पर लंब होती है।</p>
        <p><b>5. प्रमेय 9.5:</b> वृत्त की बराबर जीवाएँ केंद्र से समान दूरी पर होती हैं।</p>
        <p><b>6. प्रमेय 9.6 (दोगुने कोण का प्रमेय):</b> एक चाप द्वारा केंद्र पर अंतरित कोण, वृत्त के शेष भाग के किसी बिंदु पर अंतरित कोण का <b>दोगुना</b> होता है:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle AOB &= 2\angle APB
        \end{aligned}$$</div>
        <p><b>7. प्रमेय 9.7:</b> एक ही वृत्तखंड के कोण परस्पर बराबर होते हैं।</p>
        <p><b>8. प्रमेय 9.8:</b> अर्धवृत्त में बना कोण समकोण ($90^\circ$) होता है।</p>
        <p><b>9. प्रमेय 9.9 (चक्रीय चतुर्भुज):</b> चक्रीय चतुर्भुज के सम्मुख कोणों के प्रत्येक युग्म का योग $180^\circ$ होता है:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A + \angle C &= 180^\circ \\
        \angle B + \angle D &= 180^\circ
        \end{aligned}$$</div>
      </div>
    </div>

    <!-- ========================================================== -->
    <!-- EXERCISE 9.1 -->
    <!-- ========================================================== -->
    <div class="section-title">📝 प्रश्नावली 9.1 (संपूर्ण हल)</div>

    <!-- Ex 9.1 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: याद कीजिए कि दो वृत्त सर्वांगसम होते हैं, यदि उनकी त्रिज्याएँ बराबर हों। सिद्ध कीजिए कि सर्वांगसम वृत्तों की बराबर जीवाएँ उनके केंद्रों पर बराबर कोण अंतरित करती हैं।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">दो सर्वांगसम वृत्त $C(O, r)$ और $C(O', r)$ हैं जिनकी जीवाएँ $AB$ और $CD$ बराबर हैं ($AB = CD$)।</p>
      </div>

      <div class="step-box-orange">
        <span class="badge-blue">सिद्ध करना है</span>
        <div class="math-scroll">$$\begin{aligned}
        \angle AOB &= \angle CO'D
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">$\triangle AOB$ और $\triangle CO'D$ में:</p>
        <p class="step-txt">• <b>भुजा:</b> $OA = O'C$ &emsp; [सर्वांगसम वृत्तों की त्रिज्याएँ]</p>
        <p class="step-txt">• <b>भुजा:</b> $OB = O'D$ &emsp; [सर्वांगसम वृत्तों की त्रिज्याएँ]</p>
        <p class="step-txt">• <b>भुजा:</b> $AB = CD$ &emsp; [दिया है]</p>
        
        <p class="step-txt">अतः <b>SSS सर्वांगसमता नियम</b> से:</p>
        <div class="math-scroll">$$\begin{aligned}
        \triangle AOB &\cong \triangle CO'D
        \end{aligned}$$</div>
        <p class="step-txt">CPCT (सर्वांगसम त्रिभुजों के संगत भाग) द्वारा:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle AOB &= \angle CO'D
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: सर्वांगसम वृत्तों की बराबर जीवाएँ केंद्रों पर बराबर कोण अंतरित करती हैं।</div>
    </div>

    <!-- Ex 9.1 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: सिद्ध कीजिए कि यदि सर्वांगसम वृत्तों की जीवाएँ उनके केंद्रों पर बराबर कोण अंतरित करें, तो जीवाएँ बराबर होती हैं।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">दो सर्वांगसम वृत्त $C(O, r)$ और $C(O', r)$ हैं जिनके केंद्रों पर जीवाओं द्वारा बने कोण बराबर हैं: $\angle AOB = \angle CO'D$।</p>
      </div>

      <div class="step-box-orange">
        <span class="badge-blue">सिद्ध करना है</span>
        <div class="math-scroll">$$\begin{aligned}
        AB &= CD
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">$\triangle AOB$ और $\triangle CO'D$ में:</p>
        <p class="step-txt">• <b>भुजा:</b> $OA = O'C$ &emsp; [समान त्रिज्याएँ]</p>
        <p class="step-txt">• <b>कोण:</b> $\angle AOB = \angle CO'D$ &emsp; [दिया है]</p>
        <p class="step-txt">• <b>भुजा:</b> $OB = O'D$ &emsp; [समान त्रिज्याएँ]</p>
        
        <p class="step-txt">अतः <b>SAS सर्वांगसमता नियम</b> से:</p>
        <div class="math-scroll">$$\begin{aligned}
        \triangle AOB &\cong \triangle CO'D
        \end{aligned}$$</div>
        <p class="step-txt">CPCT द्वारा:</p>
        <div class="math-scroll">$$\begin{aligned}
        AB &= CD
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: केंद्रों पर बराबर कोण अंतरित करने वाली जीवाएँ परस्पर बराबर होती हैं।</div>
    </div>

    <!-- ========================================================== -->
    <!-- EXERCISE 9.2 -->
    <!-- ========================================================== -->
    <div class="section-title">📝 प्रश्नावली 9.2 (संपूर्ण हल)</div>

    <!-- Ex 9.2 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: $5\text{ cm}$ तथा $3\text{ cm}$ त्रिज्या वाले दो वृत्त दो बिंदुओं पर प्रतिच्छेद करते हैं तथा उनके केंद्रों के बीच की दूरी $4\text{ cm}$ है। उभयनिष्ठ जीवा की लंबाई ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>दिया है:</b> बड़े वृत्त की त्रिज्या $r_1 = 5\text{ cm}$, छोटे वृत्त की त्रिज्या $r_2 = 3\text{ cm}$ तथा केंद्रों के बीच की दूरी $OO' = 4\text{ cm}$।</p>
        <p class="step-txt"><b>त्रिभुज $OO'A$ में भुजाओं की जाँच करने पर:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        (O'A)^2 + (OO')^2 &= 3^2 + 4^2 \\
        &= 9 + 16 \\
        &= 25 \\
        &= 5^2 \\
        &= (OA)^2
        \end{aligned}$$</div>
        <p class="step-txt">पाइथागोरस प्रमेय के विलोम से, $\triangle OAO'$ एक समकोण त्रिभुज है, जिसमें:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle OO'A &= 90^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>निष्कर्ष:</b> चूँकि $\angle OO'A = 90^\circ$ है, अतः छोटे वृत्त का केंद्र $O'$ स्वयं उभयनिष्ठ जीवा $AB$ पर स्थित है।</p>
        <p class="step-txt">अर्थात उभयनिष्ठ जीवा $AB$ छोटे वृत्त का <b>व्यास</b> है:</p>
        <div class="math-scroll">$$\begin{aligned}
        AB &= 2 \cdot r_2 \\
        &= 2 \cdot 3 \\
        &= 6\text{ cm}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ उभयनिष्ठ जीवा की अभीष्ट लंबाई = 6 cm</div>
    </div>

    <!-- Ex 9.2 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: यदि एक वृत्त की दो समान जीवाएँ वृत्त के अंदर प्रतिच्छेद करें, तो सिद्ध कीजिए कि एक जीवा के खंड दूसरी जीवा के संगत खंडों के बराबर हैं।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">वृत्त $C(O, r)$ में दो समान जीवाएँ $AB = CD$ बिंदु $X$ पर प्रतिच्छेद करती हैं।</p>
      </div>

      <div class="step-box-orange">
        <span class="badge-blue">रचना (Construction)</span>
        <p class="step-txt">केंद्र $O$ से $OL \perp AB$ और $OM \perp CD$ खींचे तथा $OX$ को मिलाया।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">समान जीवाएँ केंद्र से समदूरस्थ होती हैं, अतः $OL = OM$।</p>
        <p class="step-txt">समकोण त्रिभुजों $\triangle OLX$ और $\triangle OMX$ में:</p>
        <p class="step-txt">• $\angle OLX = \angle OMX = 90^\circ$ &emsp; [रचना से]</p>
        <p class="step-txt">• $OX = OX$ &emsp; [उभयनिष्ठ कर्ण]</p>
        <p class="step-txt">• $OL = OM$ &emsp; [बराबर जीवाएं केंद्र से समदूरस्थ]</p>
        <p class="step-txt">अतः <b>RHS सर्वांगसमता</b> से:</p>
        <div class="math-scroll">$$\begin{aligned}
        \triangle OLX &\cong \triangle OMX
        \end{aligned}$$</div>
        <p class="step-txt">CPCT द्वारा:</p>
        <div class="math-scroll">$$\begin{aligned}
        LX &= MX \qquad \text{...(1)}
        \end{aligned}$$</div>
        
        <p class="step-txt">केंद्र से जीवा पर लंब जीवा को समद्विभाजित करता है:</p>
        <div class="math-scroll">$$\begin{aligned}
        AL &= \frac{1}{2}AB \\
        &= \frac{1}{2}CD \\
        &= CM \qquad \text{...(2)}
        \end{aligned}$$</div>
        
        <p class="step-txt">समीकरण (1) और (2) को जोड़ने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        AL + LX &= CM + MX \\
        AX &= CX
        \end{aligned}$$</div>
        
        <p class="step-txt">अब $AB = CD$ में से $AX = CX$ घटाने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        AB - AX &= CD - CX \\
        XB &= XD
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: संगत खंड परस्पर बराबर हैं ($AX = CX$ तथा $XB = XD$)।</div>
    </div>

    <!-- Ex 9.2 Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: यदि एक वृत्त की दो समान जीवाएँ वृत्त के अंदर प्रतिच्छेद करें, तो सिद्ध कीजिए कि प्रतिच्छेद बिंदु को केंद्र से मिलाने वाली रेखा जीवाओं से बराबर कोण बनाती है।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">समान जीवाएँ $AB = CD$ बिंदु $X$ पर प्रतिच्छेद करती हैं। $OX$ प्रतिच्छेद बिंदु को केंद्र से मिलाती है।</p>
      </div>

      <div class="step-box-orange">
        <span class="badge-blue">सिद्ध करना है</span>
        <p class="step-txt"><b>$\angle OXB = \angle OXD$</b> &emsp; [अर्थात $\angle OXL = \angle OXM$]</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">लंब $OL \perp AB$ और $OM \perp CD$ खींचने पर, $\triangle OLX$ और $\triangle OMX$ में:</p>
        <p class="step-txt">• $\angle OLX = \angle OMX = 90^\circ$</p>
        <p class="step-txt">• $OX = OX$ &emsp; [उभयनिष्ठ]</p>
        <p class="step-txt">• $OL = OM$ &emsp; [समान जीवाएँ केंद्र से समदूरस्थ]</p>
        <div class="math-scroll">$$\begin{aligned}
        \triangle OLX &\cong \triangle OMX \quad \text{[RHS]} \\
        \implies \angle OXL &= \angle OXM \quad \text{[CPCT]}
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: प्रतिच्छेद बिंदु को केंद्र से मिलाने वाली रेखा जीवाओं से बराबर कोण बनाती है।</div>
    </div>

    <!-- Ex 9.2 Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: यदि एक रेखा दो संकेंद्री वृत्तों (एक ही केंद्र वाले वृत्त) को जिनका केंद्र $O$ है, $A, B, C$ और $D$ पर प्रतिच्छेद करे, तो सिद्ध कीजिए $AB = CD$ है।</h3>
      
      <div class="step-box-orange">
        <span class="badge-blue">रचना</span>
        <p class="step-txt">केंद्र $O$ से रेखा $AD$ पर लंब $OM \perp AD$ खींचा।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">चूँकि केंद्र से जीवा पर डाला गया लंब जीवा को समद्विभाजित करता है:</p>
        <p class="step-txt"><b>1. बड़े वृत्त की जीवा $AD$ के लिए:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        AM &= MD \qquad \text{...(1)}
        \end{aligned}$$</div>
        
        <p class="step-txt"><b>2. छोटे वृत्त की जीवा $BC$ के लिए:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        BM &= MC \qquad \text{...(2)}
        \end{aligned}$$</div>
        
        <p class="step-txt">समीकरण (1) में से समीकरण (2) को घटाने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        AM - BM &= MD - MC \\
        AB &= CD
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: $AB = CD$</div>
    </div>

    <!-- Ex 9.2 Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: एक पार्क में बने $5\text{ m}$ त्रिज्या वाले वृत्त पर तीन लड़कियाँ रेशमा, सलमा एवं मनदीप खेल रही हैं। रेशमा एक गेंद को सलमा के पास, सलमा मनदीप के पास तथा मनदीप रेशमा के पास फेंकती है। यदि रेशमा और सलमा के बीच तथा सलमा और मनदीप के बीच की प्रत्येक दूरी $6\text{ m}$ हो, तो रेशमा और मनदीप के बीच की दूरी क्या है?</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>हल:</b> मान लीजिए वृत्त का केंद्र $O$ है। रेशमा, सलमा और मनदीप की स्थितियाँ क्रमशः $R, S$ और $M$ हैं।</p>
        <p class="step-txt">• त्रिज्या $OR = OS = OM = 5\text{ m}$</p>
        <p class="step-txt">• जीवाएँ $RS = SM = 6\text{ m}$</p>
        <p class="step-txt">माना $RM$ और $OS$ का प्रतिच्छेद बिंदु $K$ है। सममितता से $OS \perp RM$ और $RK = KM$।</p>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 1: केंद्र $O$ से जीवा $RS$ पर लंब $OL$ डालने पर:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        RL &= \frac{1}{2}RS \\
        &= \frac{1}{2} \cdot 6 \\
        &= 3\text{ m}
        \end{aligned}$$</div>
        <p class="step-txt">समकोण $\triangle OLR$ में पाइथागोरस प्रमेय से:</p>
        <div class="math-scroll">$$\begin{aligned}
        OL &= \sqrt{OR^2 - RL^2} \\
        &= \sqrt{5^2 - 3^2} \\
        &= \sqrt{25 - 9} \\
        &= \sqrt{16} \\
        &= 4\text{ m}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 2: $\triangle ORS$ का क्षेत्रफल दो प्रकार से निकालने पर:</b></p>
        <p class="step-txt">त्रिभुज का क्षेत्रफल $= \frac{1}{2} \times \text{Base} \times \text{Height}$</p>
        <div class="math-scroll">$$\begin{aligned}
        \frac{1}{2} \cdot OS \cdot RK &= \frac{1}{2} \cdot RS \cdot OL \\
        OS \cdot RK &= RS \cdot OL \\
        5 \cdot RK &= 6 \cdot 4 \\
        5 \cdot RK &= 24 \\
        RK &= \frac{24}{5} \\
        &= 4.8\text{ m}
        \end{aligned}$$</div>
      </div>

      <div class="step-box-orange">
        <p class="step-txt"><b>चरण 3: रेशमा और मनदीप के बीच कुल दूरी $RM$:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        RM &= 2 \cdot RK \\
        &= 2 \cdot 4.8 \\
        &= 9.6\text{ m}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ रेशमा और मनदीप के बीच की अभीष्ट दूरी = 9.6 m</div>
    </div>

    <!-- Ex 9.2 Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: $20\text{ m}$ त्रिज्या का एक गोल पार्क एक कॉलोनी में स्थित है। तीन लड़के अंकुर, सैयद तथा डेविड इसकी परिसीमा पर बराबर दूरी पर बैठे हैं और प्रत्येक के हाथ में एक-दूसरे से बात करने के लिए एक खिलौना टेलीफोन है। प्रत्येक फोन की डोरी की लंबाई ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>हल:</b> तीनों लड़के अंकुर ($A$), सैयद ($S$) और डेविड ($D$) एक समबाहु त्रिभुज $\triangle ASD$ के शीर्षों पर बैठे हैं।</p>
        <p class="step-txt">• परिवृत्त की त्रिज्या $R = 20\text{ m}$</p>
        <p class="step-txt">माना समबाहु त्रिभुज की प्रत्येक भुजा $x\text{ m}$ है (डोरी की लंबाई = $x$)।</p>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 1: समबाहु त्रिभुज की माध्यिका (ऊँचाई) $h$:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        h &= \frac{\sqrt{3}}{2}x
        \end{aligned}$$</div>
        <p class="step-txt">समबाहु त्रिभुज का परिकेंद्र ही उसका केन्द्रक (Centroid) होता है, जो माध्यिका को $2:1$ के अनुपात में विभाजित करता है:</p>
        <div class="math-scroll">$$\begin{aligned}
        R &= \frac{2}{3}h \\
        20 &= \frac{2}{3} \cdot \left(\frac{\sqrt{3}}{2}x\right) \\
        20 &= \frac{\sqrt{3}}{3}x \\
        20 &= \frac{x}{\sqrt{3}} \\
        x &= 20\sqrt{3}\text{ m}
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ प्रत्येक टेलीफोन की डोरी की अभीष्ट लंबाई = $20\sqrt{3}\text{ m} \approx 34.64\text{ m}$</div>
    </div>

    <!-- ========================================================== -->
    <!-- EXERCISE 9.3 -->
    <!-- ========================================================== -->
    <div class="section-title">📝 प्रश्नावली 9.3 (संपूर्ण 12 प्रश्न)</div>

    <!-- Ex 9.3 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: केंद्र $O$ वाले एक वृत्त पर तीन बिंदु $A, B$ और $C$ इस प्रकार हैं कि $\angle BOC = 30^\circ$ तथा $\angle AOB = 60^\circ$ है। यदि चाप $ABC$ के अतिरिक्त वृत्त पर एक बिंदु $D$ है, तो $\angle ADC$ ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: चाप $ABC$ द्वारा केंद्र पर अंतरित कुल कोण $\angle AOC$:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle AOC &= \angle AOB + \angle BOC \\
        &= 60^\circ + 30^\circ \\
        &= 90^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: प्रमेय 9.6 (चाप द्वारा केंद्र पर बना कोण परिधि पर बने कोण का दोगुना होता है):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle AOC &= 2\angle ADC \\
        \angle ADC &= \frac{1}{2}\angle AOC \\
        &= \frac{1}{2} \cdot 90^\circ \\
        &= 45^\circ
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ अभीष्ट कोण: $\angle ADC = 45^\circ$</div>
    </div>

    <!-- Ex 9.3 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: किसी वृत्त की एक जीवा वृत्त की त्रिज्या के बराबर है। जीवा द्वारा लघु चाप के किसी बिंदु पर अंतरित कोण ज्ञात कीजिए तथा दीर्घ चाप के किसी बिंदु पर भी अंतरित कोण ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: केंद्र पर बना कोण:</b></p>
        <p class="step-txt">जीवा $AB = OA = OB = r$ (त्रिज्या)। अतः $\triangle OAB$ एक <b>समबाहु त्रिभुज</b> है:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle AOB &= 60^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: दीर्घ चाप पर स्थित बिंदु $P$ पर कोण:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle APB &= \frac{1}{2}\angle AOB \\
        &= \frac{1}{2} \cdot 60^\circ \\
        &= 30^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: लघु चाप पर स्थित बिंदु $Q$ पर कोण (चक्रीय चतुर्भुज $APBQ$ से):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle APB + \angle AQB &= 180^\circ \\
        30^\circ + \angle AQB &= 180^\circ \\
        \angle AQB &= 180^\circ - 30^\circ \\
        &= 150^\circ
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ दीर्घ चाप पर कोण = $30^\circ$ &emsp; | &emsp; लघु चाप पर कोण = $150^\circ$</div>
    </div>

    <!-- Ex 9.3 Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: आकृति में, $\angle PQR = 100^\circ$ है, जहाँ $P, Q$ तथा $R$ केंद्र $O$ वाले एक वृत्त पर स्थित बिंदु हैं। $\angle OPR$ ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: प्रतिवर्ती केंद्र कोण (Reflex $\angle POR$):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \text{Reflex } \angle POR &= 2 \cdot \angle PQR \\
        &= 2 \cdot 100^\circ \\
        &= 200^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: आंतरिक केंद्र कोण $\angle POR$:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle POR &= 360^\circ - 200^\circ \\
        &= 160^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: समद्विबाहु $\triangle OPR$ में ($OP = OR = r$):</b></p>
        <p class="step-txt">समान भुजाओं के सम्मुख कोण बराबर होते हैं: $\angle OPR = \angle ORP$</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle OPR + \angle ORP + \angle POR &= 180^\circ \\
        2\angle OPR + 160^\circ &= 180^\circ \\
        2\angle OPR &= 180^\circ - 160^\circ \\
        2\angle OPR &= 20^\circ \\
        \angle OPR &= \frac{20^\circ}{2} \\
        &= 10^\circ
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ अभीष्ट कोण: $\angle OPR = 10^\circ$</div>
    </div>

    <!-- Ex 9.3 Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: आकृति में, $\angle ABC = 69^\circ$ और $\angle ACB = 31^\circ$ है, $\angle BDC$ ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: $\triangle ABC$ में कोण योग गुणधर्म से:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle BAC + \angle ABC + \angle ACB &= 180^\circ \\
        \angle BAC + 69^\circ + 31^\circ &= 180^\circ \\
        \angle BAC + 100^\circ &= 180^\circ \\
        \angle BAC &= 180^\circ - 100^\circ \\
        &= 80^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: प्रमेय 9.7 (एक ही वृत्तखंड के कोण बराबर होते हैं):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle BDC &= \angle BAC \\
        &= 80^\circ
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ अभीष्ट कोण: $\angle BDC = 80^\circ$</div>
    </div>

    <!-- Ex 9.3 Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: आकृति में, एक वृत्त पर $A, B, C$ और $D$ चार बिंदु हैं। $AC$ और $BD$ एक बिंदु $E$ पर इस प्रकार प्रतिच्छेद करते हैं कि $\angle BEC = 130^\circ$ तथा $\angle ECD = 20^\circ$ है। $\angle BAC$ ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: रैखिक युग्म से $\angle DEC$:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle DEC + \angle BEC &= 180^\circ \\
        \angle DEC + 130^\circ &= 180^\circ \\
        \angle DEC &= 180^\circ - 130^\circ \\
        &= 50^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: $\triangle DEC$ में कोण योग गुणधर्म से:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle EDC + \angle DEC + \angle ECD &= 180^\circ \\
        \angle EDC + 50^\circ + 20^\circ &= 180^\circ \\
        \angle EDC + 70^\circ &= 180^\circ \\
        \angle EDC &= 180^\circ - 70^\circ \\
        &= 110^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: एक ही वृत्तखंड के कोण ($CD$ जीवा द्वारा):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle BAC &= \angle BDC \\
        &= \angle EDC \\
        &= 110^\circ
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ अभीष्ट कोण: $\angle BAC = 110^\circ$</div>
    </div>

    <!-- Ex 9.3 Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: $ABCD$ एक चक्रीय चतुर्भुज है जिसके विकर्ण एक बिंदु $E$ पर प्रतिच्छेद करते हैं। यदि $\angle DBC = 70^\circ$ और $\angle BAC = 30^\circ$ हो, तो $\angle BCD$ ज्ञात कीजिए। पुन: यदि $AB = BC$ हो, तो $\angle ECD$ ज्ञात कीजिए।</h3>
      
      <div class="step-box-blue">
        <p class="step-txt"><b>चरण 1: एक ही वृत्तखंड के कोण ($BC$ जीवा द्वारा):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle BDC &= \angle BAC \\
        &= 30^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-green">
        <p class="step-txt"><b>चरण 2: $\triangle BCD$ में कोण योग गुणधर्म:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle BCD + \angle DBC + \angle BDC &= 180^\circ \\
        \angle BCD + 70^\circ + 30^\circ &= 180^\circ \\
        \angle BCD + 100^\circ &= 180^\circ \\
        \angle BCD &= 180^\circ - 100^\circ \\
        &= 80^\circ
        \end{aligned}$$</div>
      </div>

      <div class="step-box-purple">
        <p class="step-txt"><b>चरण 3: जब $AB = BC$ हो ($\triangle ABC$ में):</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle BCA &= \angle BAC \\
        &= 30^\circ
        \end{aligned}$$</div>
        <p class="step-txt">अब $\angle ECD$ ज्ञात करने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ECD &= \angle BCD - \angle BCA \\
        &= 80^\circ - 30^\circ \\
        &= 50^\circ
        \end{aligned}$$</div>
      </div>
      <div class="answer-highlight">✅ उत्तर: $\angle BCD = 80^\circ$ &emsp; | &emsp; $\angle ECD = 50^\circ$</div>
    </div>

    <!-- Ex 9.3 Q7 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 7: यदि एक चक्रीय चतुर्भुज के विकर्ण उसके शीर्षों से जाने वाले वृत्त के व्यास हों, तो सिद्ध कीजिए कि वह एक आयत है।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">चक्रीय चतुर्भुज $ABCD$ के विकर्ण $AC$ और $BD$ वृत्त के व्यास हैं।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">चूँकि <b>अर्धवृत्त का कोण समकोण ($90^\circ$) होता है</b>:</p>
        <p class="step-txt">• व्यास $AC$ द्वारा परिधि पर बने कोण:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle B &= 90^\circ \\
        \angle D &= 90^\circ
        \end{aligned}$$</div>
        <p class="step-txt">• व्यास $BD$ द्वारा परिधि पर बने कोण:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A &= 90^\circ \\
        \angle C &= 90^\circ
        \end{aligned}$$</div>
        <p class="step-txt">चूँकि चतुर्भुज के चारों कोण समकोण हैं: <b>$\angle A = \angle B = \angle C = \angle D = 90^\circ$</b></p>
        <p class="step-txt">अतः <b>$ABCD$ एक आयत (Rectangle) है। इति सिद्धम्।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: चारों कोण 90° होने के कारण यह एक आयत है।</div>
    </div>

    <!-- Ex 9.3 Q8 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 8: यदि एक समलंब की असमांतर भुजाएँ बराबर हों, तो सिद्ध कीजिए कि वह चक्रीय है।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">समलंब $ABCD$ में $AB \parallel CD$ तथा असमांतर भुजाएँ $AD = BC$ हैं।</p>
      </div>

      <div class="step-box-orange">
        <span class="badge-blue">रचना</span>
        <p class="step-txt">$AM \perp CD$ और $BN \perp CD$ लंब खींचे।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">समकोण $\triangle AMD$ और $\triangle BNC$ में:</p>
        <p class="step-txt">• $\angle AMD = \angle BNC = 90^\circ$</p>
        <p class="step-txt">• $AD = BC$ &emsp; [दिया है]</p>
        <p class="step-txt">• $AM = BN$ &emsp; [समानांतर रेखाओं के बीच की लंबवत दूरी समान होती है]</p>
        <div class="math-scroll">$$\begin{aligned}
        \triangle AMD &\cong \triangle BNC \quad \text{[RHS]} \\
        \implies \angle D &= \angle C \quad \text{[CPCT]} \qquad \text{...(1)}
        \end{aligned}$$</div>
        
        <p class="step-txt">चूँकि $AB \parallel CD$ है, अंतः कोणों का योग $180^\circ$ होता है:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A + \angle D &= 180^\circ
        \end{aligned}$$</div>
        <p class="step-txt">समीकरण (1) से $\angle D = \angle C$ रखने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A + \angle C &= 180^\circ
        \end{aligned}$$</div>
        <p class="step-txt">चूँकि सम्मुख कोणों का योग $180^\circ$ है, अतः <b>$ABCD$ एक चक्रीय समलंब है। इति सिद्धम्।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: सम्मुख कोणों का योग 180° होने से यह चक्रीय चतुर्भुज है।</div>
    </div>

    <!-- Ex 9.3 Q9 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 9: दो वृत्त दो बिंदुओं $B$ और $C$ पर प्रतिच्छेद करते हैं। $B$ से जाने वाले दो रेखाखंड $ABD$ और $PBQ$ वृत्तों को $A, D$ और $P, Q$ पर क्रमशः प्रतिच्छेद करते हुए खींचे गए हैं। सिद्ध कीजिए कि $\angle ACP = \angle QCD$ है।</h3>
      
      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt"><b>1. पहले वृत्त में चाप $AP$ द्वारा:</b> &emsp; [एक ही वृत्तखंड के कोण]</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ACP &= \angle ABP \qquad \text{...(1)}
        \end{aligned}$$</div>
        
        <p class="step-txt"><b>2. दूसरे वृत्त में चाप $DQ$ द्वारा:</b> &emsp; [एक ही वृत्तखंड के कोण]</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle QCD &= \angle QBD \qquad \text{...(2)}
        \end{aligned}$$</div>
        
        <p class="step-txt"><b>3. शीर्षाभिमुख कोण (Vertically Opposite Angles):</b></p>
        <p class="step-txt">चूँकि $ABD$ और $PBQ$ सीधी रेखाएँ हैं:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ABP &= \angle QBD \qquad \text{...(3)}
        \end{aligned}$$</div>
        
        <p class="step-txt">समीकरण (1), (2) और (3) की तुलना करने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ACP &= \angle QCD
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: $\angle ACP = \angle QCD$</div>
    </div>

    <!-- Ex 9.3 Q10 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 10: यदि किसी त्रिभुज की दो भुजाओं को व्यास मानकर वृत्त खींचे जाएँ, तो सिद्ध कीजिए कि इन वृत्तों का प्रतिच्छेद बिंदु तीसरी भुजा पर स्थित है।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">$\triangle ABC$ की भुजाओं $AB$ और $AC$ को व्यास मानकर दो वृत्त खींचे गए हैं जो परस्पर बिंदु $D$ पर प्रतिच्छेद करते हैं।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">बिंदु $A$ और $D$ को मिलाने पर ($AD$ उभयनिष्ठ जीवा है):</p>
        <p class="step-txt">• चूँकि $AB$ पहले वृत्त का व्यास है, अर्धवृत्त का कोण समकोण होता है:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ADB &= 90^\circ \qquad \text{...(1)}
        \end{aligned}$$</div>
        
        <p class="step-txt">• चूँकि $AC$ दूसरे वृत्त का व्यास है:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ADC &= 90^\circ \qquad \text{...(2)}
        \end{aligned}$$</div>
        
        <p class="step-txt">समीकरण (1) और (2) को जोड़ने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle ADB + \angle ADC &= 90^\circ + 90^\circ \\
        &= 180^\circ
        \end{aligned}$$</div>
        <p class="step-txt">चूँकि दोनों कोणों का योग $180^\circ$ है, अतः $BDC$ एक <b>सीधी रेखा (सरल रेखा)</b> है।</p>
        <p class="step-txt">अतः बिंदु $D$ तीसरी भुजा $BC$ पर स्थित है। <b>इति सिद्धम्।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: प्रतिच्छेद बिंदु D तीसरी भुजा BC पर ही स्थित है।</div>
    </div>

    <!-- Ex 9.3 Q11 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 11: उभयनिष्ठ कर्ण $AC$ वाले दो समकोण त्रिभुज $ABC$ और $ADC$ हैं। सिद्ध कीजिए कि $\angle CAD = \angle CBD$ है।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">उभयनिष्ठ कर्ण $AC$ पर दो समकोण त्रिभुज हैं: $\angle B = 90^\circ$ तथा $\angle D = 90^\circ$।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt">सम्मुख कोणों का योग:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle B + \angle D &= 90^\circ + 90^\circ \\
        &= 180^\circ
        \end{aligned}$$</div>
        <p class="step-txt">अतः चतुर्भुज $ABCD$ एक <b>चक्रीय चतुर्भुज</b> है, जिसके चारों शीर्ष एक ही वृत्त पर स्थित हैं और $AC$ उसका व्यास है।</p>
        <p class="step-txt">अब वृत्त में, जीवा $CD$ द्वारा अंतरित कोण [एक ही वृत्तखंड के कोण बराबर होते हैं]:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle CAD &= \angle CBD
        \end{aligned}$$</div>
        <p class="step-txt"><b>इति सिद्धम् (Hence Proved)।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: $\angle CAD = \angle CBD$</div>
    </div>

    <!-- Ex 9.3 Q12 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 12: सिद्ध कीजिए कि चक्रीय समांतर चतुर्भुज आयत होता है।</h3>
      
      <div class="step-box-blue">
        <span class="badge-blue">दिया है</span>
        <p class="step-txt">$ABCD$ एक चक्रीय समांतर चतुर्भुज है।</p>
      </div>

      <div class="step-box-purple">
        <span class="badge-blue">उपपत्ति (Proof)</span>
        <p class="step-txt"><b>1. समांतर चतुर्भुज के सम्मुख कोण बराबर होते हैं:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A &= \angle C \qquad \text{...(1)}
        \end{aligned}$$</div>
        
        <p class="step-txt"><b>2. चक्रीय चतुर्भुज के सम्मुख कोणों का योग $180^\circ$ होता है:</b></p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A + \angle C &= 180^\circ \qquad \text{...(2)}
        \end{aligned}$$</div>
        
        <p class="step-txt">समीकरण (1) से $\angle C = \angle A$ समीकरण (2) में रखने पर:</p>
        <div class="math-scroll">$$\begin{aligned}
        \angle A + \angle A &= 180^\circ \\
        2\angle A &= 180^\circ \\
        \angle A &= \frac{180^\circ}{2} \\
        &= 90^\circ
        \end{aligned}$$</div>
        <p class="step-txt">इसी प्रकार $\angle B = \angle C = \angle D = 90^\circ$।</p>
        <p class="step-txt">चूँकि समांतर चतुर्भुज का प्रत्येक कोण $90^\circ$ है, अतः <b>$ABCD$ एक आयत है। इति सिद्धम्।</b></p>
      </div>
      <div class="answer-highlight">✅ सिद्ध हुआ: चक्रीय समांतर चतुर्भुज सदैव एक आयत होता है।</div>
    </div>

    <!-- ========================================================== -->
    <!-- 5 INTERACTIVE LIVE SIMULATORS -->
    <!-- ========================================================== -->
    <div class="section-title">⚡ 5 इंटरैक्टिव लाइव सिमुलेटर (Circle Geometry Simulators)</div>

    <!-- SIMULATOR 1: Double Angle Theorem -->
    <div class="sim-card">
      <div class="sim-header">🎯 सिमुलेटर 1: केंद्र पर कोण व परिधि पर कोण (Double Angle Theorem Visualizer)</div>
      <p>परिधि पर बने कोण $\theta$ का मान बदलें और केंद्र पर अंतरित दोगुना कोण ($2\theta$) लाइव देखें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim1_inscribed">परिधि पर कोण $\theta$ (°):</label>
          <input type="number" id="sim1_inscribed" class="sim-input" value="45" min="1" max="179">
        </div>
        <button class="sim-btn" onclick="calculateSim1()">कैलकुलेट करें</button>
      </div>
      <div id="sim1_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 2: Cyclic Quadrilateral Solver -->
    <div class="sim-card">
      <div class="sim-header">🔄 सिमुलेटर 2: चक्रीय चतुर्भुज सम्मुख कोण सॉल्वर (Cyclic Quadrilateral Solver)</div>
      <p>सम्मुख कोणों का योग सदैव $180^\circ$ होता है। $\angle A$ और $\angle B$ दर्ज करें और $\angle C, \angle D$ प्राप्त करें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim2_a">कोण $\angle A$ (°):</label>
          <input type="number" id="sim2_a" class="sim-input" value="70" min="1" max="179">
        </div>
        <div class="sim-input-box">
          <label for="sim2_b">कोण $\angle B$ (°):</label>
          <input type="number" id="sim2_b" class="sim-input" value="100" min="1" max="179">
        </div>
        <button class="sim-btn" onclick="calculateSim2()">सॉल्व करें</button>
      </div>
      <div id="sim2_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 3: Chord-Distance Solver -->
    <div class="sim-card">
      <div class="sim-header">📏 सिमुलेटर 3: जीवा व केंद्र से लंब दूरी कैलकुलेटर (Chord & Distance Solver)</div>
      <p>त्रिज्या $r$ और जीवा की लंबाई $c$ दर्ज करें, केंद्र से लंब दूरी $d = \sqrt{r^2 - (c/2)^2}$ प्राप्त करें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim3_r">त्रिज्या $r$ (cm):</label>
          <input type="number" id="sim3_r" class="sim-input" value="5" min="1">
        </div>
        <div class="sim-input-box">
          <label for="sim3_c">जीवा $c$ (cm):</label>
          <input type="number" id="sim3_c" class="sim-input" value="6" min="1">
        </div>
        <button class="sim-btn" onclick="calculateSim3()">गणना करें</button>
      </div>
      <div id="sim3_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 4: Reshma-Salma-Mandeep Toy Phone Solver -->
    <div class="sim-card">
      <div class="sim-header">🎪 सिमुलेटर 4: समबाहु परिवृत्त टेलीफोन डोरी कैलकुलेटर (Park Toy-Phone Solver)</div>
      <p>पार्क की त्रिज्या $R$ दर्ज करें और समबाहु त्रिभुज के प्रत्येक खिलौना फोन की डोरी $x = R\sqrt{3}$ ज्ञात करें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim4_rad">पार्क त्रिज्या $R$ (m):</label>
          <input type="number" id="sim4_rad" class="sim-input" value="20" min="1">
        </div>
        <button class="sim-btn" onclick="calculateSim4()">हल निकालें</button>
      </div>
      <div id="sim4_output" class="sim-result"></div>
    </div>

    <!-- SIMULATOR 5: Angle in Semicircle -->
    <div class="sim-card">
      <div class="sim-header">📐 सिमुलेटर 5: अर्धवृत्त में कोण परीक्षक (Angle in Semicircle Tester)</div>
      <p>वृत्त के व्यास द्वारा परिधि पर बने किसी भी कोण की स्थिति चुनें और उसका मान $90^\circ$ सत्यापित करें!</p>
      <div class="sim-input-row">
        <div class="sim-input-box">
          <label for="sim5_pos">परिधि पर बिंदु की स्थिति (°):</label>
          <input type="number" id="sim5_pos" class="sim-input" value="60" min="10" max="170">
        </div>
        <button class="sim-btn" onclick="calculateSim5()">सत्यापित करें</button>
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
  // SIMULATOR 1: Double Angle Theorem
  // ==========================================================
  function calculateSim1() {
    var theta = parseFloat(document.getElementById('sim1_inscribed').value) || 45;
    var central = 2 * theta;
    var out = document.getElementById('sim1_output');

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>परिधि पर कोण:</strong> $\\theta = ' + theta + '^\\circ$</p>' +
      '<p class="step-txt"><strong>प्रमेय 9.6:</strong> केंद्र पर बना कोण परिधि पर बने कोण का दोगुना होता है:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\angle AOB &= 2 \\cdot \\theta \\\\' +
      '&= 2 \\cdot ' + theta + '^\\circ \\\\' +
      '&= ' + central + '^\\circ' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ केंद्र कोण $\\angle AOB = ' + central + '^\\circ$</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 2: Cyclic Quadrilateral Solver
  // ==========================================================
  function calculateSim2() {
    var a = parseFloat(document.getElementById('sim2_a').value) || 70;
    var b = parseFloat(document.getElementById('sim2_b').value) || 100;
    var c = 180 - a;
    var d = 180 - b;
    var out = document.getElementById('sim2_output');

    var html = '<div class="step-box-green">' +
      '<p class="step-txt"><strong>चक्रीय चतुर्भुज प्रमेय:</strong> सम्मुख कोणों का योग $180^\\circ$ होता है:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\angle C &= 180^\\circ - \\angle A \\\\' +
      '&= 180^\\circ - ' + a + '^\\circ \\\\' +
      '&= ' + c + '^\\circ' +
      '\\end{aligned}$$</div>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\angle D &= 180^\\circ - \\angle B \\\\' +
      '&= 180^\\circ - ' + b + '^\\circ \\\\' +
      '&= ' + d + '^\\circ' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ अभीष्ट सम्मुख कोण: $\\angle C = ' + c + '^\\circ$ &emsp; | &emsp; $\\angle D = ' + d + '^\\circ$</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 3: Chord Length & Distance Solver
  // ==========================================================
  function calculateSim3() {
    var r = parseFloat(document.getElementById('sim3_r').value) || 5;
    var c = parseFloat(document.getElementById('sim3_c').value) || 6;
    var out = document.getElementById('sim3_output');

    if (c > 2 * r) {
      out.innerHTML = '<div class="step-box-orange"><p style="color:#c2410c;">⚠️ जीवा की लंबाई व्यास ($2r = ' + (2 * r) + '$\\text{ cm}) से अधिक नहीं हो सकती!</p></div>';
      return;
    }

    var halfC = c / 2;
    var dSq = r * r - halfC * halfC;
    var d = Math.sqrt(dSq).toFixed(2);

    var html = '<div class="step-box-purple">' +
      '<p class="step-txt"><strong>त्रिज्या:</strong> $r = ' + r + '$ cm, &emsp; <strong>जीवा:</strong> $c = ' + c + '$ cm</p>' +
      '<p class="step-txt">केंद्र से लंब जीवा को समद्विभाजित करता है: $AM = \\frac{c}{2} = ' + halfC + '$ cm</p>' +
      '<p class="step-txt">समकोण त्रिभुज में पाइथागोरस प्रमेय से:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      'd &= \\sqrt{r^2 - \\left(\\frac{c}{2}\\right)^2} \\\\' +
      '&= \\sqrt{' + r + '^2 - ' + halfC + '^2} \\\\' +
      '&= \\sqrt{' + (r * r) + ' - ' + (halfC * halfC) + '} \\\\' +
      '&= \\sqrt{' + dSq + '} \\\\' +
      '&= ' + d + '\\text{ cm}' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ केंद्र से जीवा की लंबवत दूरी = ' + d + ' cm</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 4: Park Toy-Phone Solver
  // ==========================================================
  function calculateSim4() {
    var R = parseFloat(document.getElementById('sim4_rad').value) || 20;
    var cord = (R * Math.sqrt(3)).toFixed(2);
    var out = document.getElementById('sim4_output');

    var html = '<div class="step-box-orange">' +
      '<p class="step-txt"><strong>पार्क की त्रिज्या:</strong> $R = ' + R + '$ m</p>' +
      '<p class="step-txt">समबाहु त्रिभुज में परिवृत्त की त्रिज्या $R = \\frac{x}{\\sqrt{3}}$ होती है:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      'x &= R \\cdot \\sqrt{3} \\\\' +
      '&= ' + R + '\\sqrt{3}\\text{ m} \\\\' +
      '\\approx ' + cord + '\\text{ m}' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ प्रत्येक फोन की डोरी की लंबाई = $' + R + '\\sqrt{3}\\text{ m} \\approx ' + cord + '\\text{ m}$</div>' +
      '</div>';

    out.innerHTML = html;
    if (window.MathJax) {
      if (MathJax.typesetClear) MathJax.typesetClear([out]);
      if (MathJax.typesetPromise) MathJax.typesetPromise([out]).catch(function(){});
    }
  }

  // ==========================================================
  // SIMULATOR 5: Angle in Semicircle
  // ==========================================================
  function calculateSim5() {
    var pos = parseFloat(document.getElementById('sim5_pos').value) || 60;
    var out = document.getElementById('sim5_output');

    var html = '<div class="step-box-blue">' +
      '<p class="step-txt"><strong>व्यास द्वारा केंद्र पर अंतरित कोण:</strong> $\\angle AOB = 180^\\circ$ (सरल कोण)</p>' +
      '<p class="step-txt"><strong>प्रमेय 9.8 (अर्धवृत्त का कोण):</strong> परिधि के किसी भी बिंदु पर अंतरित कोण:</p>' +
      '<div class="math-scroll">$$\\begin{aligned}' +
      '\\angle APB &= \\frac{1}{2} \\angle AOB \\\\' +
      '&= \\frac{1}{2} \\cdot 180^\\circ \\\\' +
      '&= 90^\\circ' +
      '\\end{aligned}$$</div>' +
      '<div class="answer-highlight">✅ सत्यापित: बिंदु किसी भी स्थिति (' + pos + '°) पर हो, कोण सदैव समकोण (90°) ही होता है!</div>' +
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

with open('qa_master_math9_9.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("qa_master_math9_9.html generated successfully!")
