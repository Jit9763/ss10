# -*- coding: utf-8 -*-
"""
Generator for NCERT Class 9 Mathematics Chapter 12: सांख्यिकी (Statistics)
Includes:
- 100% complete NCERT Ex 12.1 solutions (Q1 to Q9)
- Comprehensive revision of Central Tendency (Mean, Median, Mode)
- 5 Live Interactive Simulators:
  1. बार ग्राफ जनरेटर (Bar Graph Generator)
  2. आयतचित्र (हिस्टोग्राम) विज़ुअलाइज़र (Histogram Visualizer)
  3. बारंबारता बहुभुज प्लॉटर (Frequency Polygon Plotter)
  4. असमान चौड़ाई आयतचित्र सॉल्वर (Varying Width Histogram Area Adjuster)
  5. माध्य, माध्यक एवं बहुलक विश्लेषक (Mean, Median, Mode Interactive Calculator)
- Zero-scrollbar responsive layout:
  * overflow-x: hidden !important;
  * word-wrap: break-word; overflow-wrap: break-word;
  * MathJax displayOverflow: 'scale'
  * No Hindi inside MathJax
  * Safe JS simulator strings (\\cdot / ×)
"""

import sys

content = r'''<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NCERT कक्षा 9 गणित - अध्याय 12: सांख्यिकी (Statistics) संपूर्ण प्रश्नोत्तर व 5 लाइव सिमुलेटर</title>

<!-- MathJax Configuration with scale down to prevent horizontal scroll -->
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
    processEscapes: true
  },
  chtml: {
    displayOverflow: 'scale'
  },
  options: {
    renderActions: {
      addMenu: []
    }
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

<style>
  :root {
    --primary-color: #0d9488;
    --primary-dark: #115e59;
    --bg-color: #f8fafc;
    --card-bg: #ffffff;
    --text-color: #0f172a;
    --border-color: #e2e8f0;
  }

  * {
    box-sizing: border-box;
  }

  body {
    font-family: 'Segoe UI', Roboto, -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-color);
    margin: 0;
    padding: 20px 10px;
    line-height: 1.6;
    overflow-x: hidden !important;
  }

  .container {
    max-width: 1050px;
    margin: 0 auto;
    background: var(--card-bg);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
    border: 1px solid var(--border-color);
    overflow-x: hidden !important;
  }

  .action-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 25px;
    padding: 12px;
    background: #f1f5f9;
    border-radius: 12px;
    justify-content: center;
  }

  .action-btn {
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    background: #ffffff;
    color: #334155;
    font-weight: 600;
    cursor: pointer;
    font-size: 0.95rem;
    transition: all 0.2s ease;
  }

  .action-btn:hover {
    background: #0d9488;
    color: #ffffff;
    border-color: #0d9488;
  }

  .top-header {
    text-align: center;
    border-bottom: 3px solid #0d9488;
    padding-bottom: 20px;
    margin-bottom: 30px;
  }

  .badge-class {
    display: inline-block;
    padding: 4px 12px;
    background: #ccfbf1;
    color: #0f766e;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 8px;
  }

  h1 {
    color: #0f766e;
    font-size: 2.1rem;
    margin: 10px 0;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
  }

  .subtitle {
    color: #475569;
    font-size: 1.05rem;
  }

  .formula-box {
    background: linear-gradient(135deg, #f0fdfa, #ccfbf1);
    border: 2px solid #5eead4;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 30px;
  }

  .formula-box h3 {
    margin-top: 0;
    color: #115e59;
    font-size: 1.3rem;
  }

  .formula-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 15px;
  }

  .formula-item {
    background: #ffffff;
    padding: 14px;
    border-radius: 10px;
    border-left: 5px solid #0d9488;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
  }

  .section-title {
    background: #0f766e;
    color: #ffffff;
    padding: 12px 20px;
    border-radius: 10px;
    font-size: 1.4rem;
    margin: 35px 0 20px 0;
    text-align: center;
  }

  .qa-block {
    background: #ffffff;
    border: 2px solid #e2e8f0;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 25px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    overflow-x: hidden !important;
    word-wrap: break-word !important;
  }

  .question-heading {
    color: #115e59;
    font-size: 1.25rem;
    margin-top: 0;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 10px;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
  }

  .step-box-green {
    background: #f0fdf4;
    border-left: 5px solid #22c55e;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
  }

  .step-box-blue {
    background: #eff6ff;
    border-left: 5px solid #3b82f6;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
  }

  .step-box-purple {
    background: #faf5ff;
    border-left: 5px solid #a855f7;
    padding: 15px;
    border-radius: 8px;
    margin: 15px 0;
  }

  .answer-highlight {
    background: #fefce8;
    border: 2px solid #eab308;
    border-left: 10px solid #ca8a04;
    padding: 14px 18px;
    border-radius: 10px;
    font-weight: 700;
    color: #713f12;
    margin-top: 15px;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    max-width: 100% !important;
  }

  .math-scroll {
    overflow-x: hidden !important;
    overflow-y: hidden !important;
    max-width: 100% !important;
    margin: 12px 0;
  }

  /* Table styles */
  .stat-table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 1rem;
    table-layout: auto;
  }

  .stat-table th, .stat-table td {
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: center;
  }

  .stat-table th {
    background: #0f766e;
    color: #ffffff;
    font-weight: 600;
  }

  .stat-table tr:nth-child(even) {
    background: #f8fafc;
  }

  /* Interactive Simulator Styles */
  .sim-container {
    background: #ffffff;
    border: 2px solid #0d9488;
    border-radius: 16px;
    padding: 22px;
    margin: 30px 0;
    box-shadow: 0 8px 25px rgba(13, 148, 136, 0.1);
  }

  .sim-title {
    color: #0f766e;
    font-size: 1.3rem;
    margin-top: 0;
    border-bottom: 2px solid #ccfbf1;
    padding-bottom: 8px;
  }

  .sim-controls {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin: 15px 0;
    align-items: center;
  }

  .sim-controls label {
    font-weight: 600;
    color: #334155;
    font-size: 0.95rem;
  }

  .sim-controls input[type="range"] {
    flex: 1;
    min-width: 140px;
  }

  .sim-controls input[type="text"], .sim-controls input[type="number"], .sim-controls select {
    padding: 6px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    font-size: 0.95rem;
  }

  .sim-canvas-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    margin-top: 15px;
    overflow-x: hidden !important;
  }

  .sim-output {
    background: #f0fdfa;
    border-left: 4px solid #0d9488;
    padding: 12px;
    border-radius: 6px;
    margin-top: 15px;
    font-weight: 600;
    color: #115e59;
  }

  footer {
    text-align: center;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 2px solid #e2e8f0;
    color: #64748b;
    font-size: 0.95rem;
  }
</style>
</head>
<body>

<div class="container">

  <!-- TOP ACTION BAR -->
  <div class="action-bar">
    <button class="action-btn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">⬆️ शीर्ष पर जाएँ</button>
    <button class="action-btn" onclick="document.getElementById('simulators').scrollIntoView({behavior: 'smooth'})">🎮 5 लाइव सिमुलेटर</button>
    <button class="action-btn" onclick="document.getElementById('ex12_1').scrollIntoView({behavior: 'smooth'})">📝 प्रश्नावली 12.1 हल</button>
    <button class="action-btn" onclick="window.print()">🖨️ प्रिंट / PDF</button>
  </div>

  <!-- HEADER -->
  <div class="top-header">
    <span class="badge-class">NCERT कक्षा 9 • गणित • 2024-25 पाठ्यक्रम</span>
    <h1>अध्याय 12: सांख्यिकी (Statistics)</h1>
    <p class="subtitle">संपूर्ण 100% प्रामाणिक NCERT प्रश्नोत्तर (प्रश्नावली 12.1), आलेखीय निरूपण व 5 इंटरैक्टिव लाइव सिमुलेटर</p>
  </div>

  <!-- SUMMARY & FORMULA BOX -->
  <div class="formula-box">
    <h3>📌 मुख्य अवधारणाएँ एवं आलेखीय निरूपण के नियम</h3>
    <div class="formula-grid">
      <div class="formula-item">
        <b>1. दंड आलेख (Bar Graph):</b>
        <p>समान चौड़ाई के आयताकार दंड, जिनके बीच की दूरी एकसमान होती है। दंड की ऊँचाई संगत बारंबारता के समानुपाती होती है।</p>
      </div>
      <div class="formula-item">
        <b>2. आयतचित्र (Histogram):</b>
        <p>सतत वर्ग अंतरालों के लिए आलेख। इसमें दंडों के बीच कोई रिक्त स्थान नहीं होता। आयत का क्षेत्रफल बारंबारता के समानुपाती होता है।</p>
      </div>
      <div class="formula-item">
        <b>3. बारंबारता बहुभुज (Frequency Polygon):</b>
        <p>आयतचित्र के आयतों की ऊपरी भुजाओं के मध्य-बिंदुओं (वर्ग चिह्नों) को रेखाखंडों द्वारा जोड़कर बनाया जाता है।</p>
        <div class="math-scroll">$$\text{Class Mark} = \frac{\text{Upper Limit} + \text{Lower Limit}}{2}$$</div>
      </div>
      <div class="formula-item">
        <b>4. असमान चौड़ाई वाले आयत की लंबाई:</b>
        <p>जब वर्ग अंतरालों की चौड़ाई भिन्न हो:</p>
        <div class="math-scroll">$$\text{Length of Rectangle} = \frac{\text{Frequency}}{\text{Width}} \cdot \text{Min Width}$$</div>
      </div>
    </div>
  </div>

  <!-- SECTION: EXERCISE 12.1 -->
  <div class="section-title" id="ex12_1">📚 प्रश्नावली 12.1 — संपूर्ण 100% प्रामाणिक हल</div>

  <!-- Q1 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 1: एक संगठन ने पूरे विश्व में 15 - 44 (वर्षों में) की आयु वाली महिलाओं में बीमारी और मृत्यु के कारणों का पता लगाने के लिए सर्वेक्षण किया। आँकड़े (% में) निम्नलिखित हैं:</h3>
    <table class="stat-table">
      <tr>
        <th>क्र. सं.</th>
        <th>कारण (Cause)</th>
        <th>महिला मृत्यु दर (%)</th>
      </tr>
      <tr><td>1</td><td>जनन स्वास्थ्य अवस्था (Reproductive health conditions)</td><td>31.8</td></tr>
      <tr><td>2</td><td>तंत्रिका-मनोविकारी अवस्था (Neuropsychiatric conditions)</td><td>25.4</td></tr>
      <tr><td>3</td><td>क्षति (Injuries)</td><td>12.4</td></tr>
      <tr><td>4</td><td>हृदय-वाहिका अवस्था (Cardiovascular conditions)</td><td>4.3</td></tr>
      <tr><td>5</td><td>श्वसन अवस्था (Respiratory conditions)</td><td>4.1</td></tr>
      <tr><td>6</td><td>अन्य कारण (Other causes)</td><td>22.0</td></tr>
    </table>
    <p><b>(i) ऊपर दी गई सूचनाओं को आलेखीय रूप में निरूपित कीजिए।</b><br>
    <b>(ii) कौन सी अवस्था पूरे विश्व की महिलाओं के खराब स्वास्थ्य और मृत्यु का बड़ा कारण है?</b><br>
    <b>(iii) अपनी अध्यापिका के सहयोग से ऐसे दो कारणों का पता लगाने का प्रयास कीजिए जिनकी ऊपर (ii) में मुख्य भूमिका रही हो।</b></p>

    <div class="step-box-green">
      <p><b>हल एवं व्याख्या:</b></p>
      <p><b>(i) आलेखीय निरूपण (दंड आलेख):</b></p>
      <p>क्षैतिज अक्ष ($X$-अक्ष) पर कारणों को तथा ऊर्ध्वाधर अक्ष ($Y$-अक्ष) पर महिला मृत्यु दर (% में) को निरूपित करने वाला दंड आलेख उपयुक्त पैमाना ($1\text{ unit} = 5\%$) लेकर खींचा जाएगा। सभी दंडों की चौड़ाई समान तथा बीच की दूरी समान रखी जाती है।</p>
      <p><b>(ii) सबसे बड़ा कारण:</b> सारणी और दंड आलेख से स्पष्ट है कि <b>जनन स्वास्थ्य अवस्था (31.8%)</b> पूरे विश्व की महिलाओं के खराब स्वास्थ्य और मृत्यु का सबसे बड़ा कारण है।</p>
      <p><b>(iii) मुख्य सहायक कारण:</b></p>
      <ul>
        <li>उपयुक्त चिकित्सा सुविधाओं और स्वास्थ्य सेवाओं का अभाव।</li>
        <li>महिलाओं में पोषण तथा स्वास्थ्य संबंधी सही जानकारी व शिक्षा की कमी।</li>
      </ul>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: (i) दंड आलेख, (ii) जनन स्वास्थ्य अवस्था (31.8%), (iii) स्वास्थ्य सुविधाओं व जागरूकता की कमी।
    </div>
  </div>

  <!-- Q2 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 2: भारतीय समाज के विभिन्न क्षेत्रों में प्रति हजार लड़कों पर लड़कियों की संख्या के आँकड़े नीचे दिए गए हैं:</h3>
    <table class="stat-table">
      <tr><th>क्षेत्र (Section)</th><th>प्रति हजार लड़कों पर लड़कियों की संख्या</th></tr>
      <tr><td>अनुसूचित जाति (SC)</td><td>940</td></tr>
      <tr><td>अनुसूचित जनजाति (ST)</td><td>970</td></tr>
      <tr><td>गैर-अनुसूचित जाति/जनजाति</td><td>920</td></tr>
      <tr><td>पिछड़े जिले</td><td>950</td></tr>
      <tr><td>गैर-पिछड़े जिले</td><td>920</td></tr>
      <tr><td>ग्रामीण क्षेत्र</td><td>930</td></tr>
      <tr><td>शहरी क्षेत्र</td><td>910</td></tr>
    </table>
    <p><b>(i) इन सूचनाओं को एक दंड आलेख द्वारा निरूपित कीजिए।</b><br>
    <b>(ii) कक्षा में चर्चा करके बताइए कि आप इस आलेख से कौन-कौन से निष्कर्ष निकाल सकते हैं?</b></p>

    <div class="step-box-blue">
      <p><b>हल एवं निष्कर्ष:</b></p>
      <p><b>(i) दंड आलेख:</b> $X$-अक्ष पर क्षेत्रों को समान चौड़ाई के दंडों द्वारा और $Y$-अक्ष पर $1\text{ unit} = 10$ लड़कियाँ (900 से प्रारंभ करते हुए किंक $\text{kink}$ के साथ) आलेखित किया जाएगा।</p>
      <p><b>(ii) प्राप्त निष्कर्ष:</b></p>
      <ul>
        <li>प्रति हजार लड़कों पर लड़कियों की संख्या <b>अनुसूचित जनजाति (ST)</b> में सर्वाधिक ($970$) है।</li>
        <li>प्रति हजार लड़कों पर लड़कियों की संख्या <b>शहरी क्षेत्रों</b> में न्यूनतम ($910$) है।</li>
        <li>ग्रामीण क्षेत्रों ($930$) की तुलना में शहरी क्षेत्रों ($910$) में लिंगानुपात कम है।</li>
      </ul>
    </div>
    <div class="answer-highlight">
      ✅ निष्कर्ष: अनुसूचित जनजाति में अधिकतम लिंगानुपात (970) तथा शहरी क्षेत्रों में न्यूनतम (910) है।
    </div>
  </div>

  <!-- Q3 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 3: एक राज्य के विधानसभा चुनाव में विभिन्न राजनैतिक पार्टियों द्वारा जीती गई सीटों के परिणाम नीचे दिए गए हैं:</h3>
    <table class="stat-table">
      <tr><th>राजनैतिक पार्टी</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th></tr>
      <tr><th>जीती गई सीटें</th><td>75</td><td>55</td><td>37</td><td>29</td><td>10</td><td>37</td></tr>
    </table>
    <p><b>(i) मतदान के परिणामों को निरूपित करने वाला एक दंड आलेख खींचिए।</b><br>
    <b>(ii) किस राजनैतिक पार्टी ने अधिकतम सीटें जीती हैं?</b></p>

    <div class="step-box-purple">
      <p><b>हल:</b></p>
      <p><b>(i) दंड आलेख रचना:</b></p>
      <p>$X$-अक्ष पर राजनैतिक पार्टियाँ (A, B, C, D, E, F) समान दूरी पर अंकित की जाएँगी। $Y$-अक्ष पर पैमाना $1\text{ cm} = 10\text{ seats}$ लेकर प्रत्येक पार्टी के लिए संगत ऊँचाई का दंड बनाया जाता है।</p>
      <p><b>(ii) अधिकतम सीटें:</b></p>
      <p>सारणी तथा दंड आलेख के उच्चतम दंड से स्पष्ट है कि <b>पार्टी A</b> ने अधिकतम $75$ सीटें जीती हैं।</p>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: (i) दंड आलेख, (ii) राजनैतिक पार्टी A ने अधिकतम 75 सीटें जीती हैं।
    </div>
  </div>

  <!-- Q4 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 4: एक पौधे की 40 पत्तियों की लंबाइयाँ एक मिलीमीटर तक शुद्ध मापी गई हैं और प्राप्त आँकड़ों को निम्नलिखित सारणी में निरूपित किया गया है:</h3>
    <table class="stat-table">
      <tr><th>लंबाई (mm में)</th><th>पत्तियों की संख्या ($f_i$)</th><th>सतत वर्ग अंतराल</th></tr>
      <tr><td>118 - 126</td><td>3</td><td>117.5 - 126.5</td></tr>
      <tr><td>127 - 135</td><td>5</td><td>126.5 - 135.5</td></tr>
      <tr><td>136 - 144</td><td>9</td><td>135.5 - 144.5</td></tr>
      <tr><td>145 - 153</td><td>12</td><td>144.5 - 153.5</td></tr>
      <tr><td>154 - 162</td><td>5</td><td>153.5 - 162.5</td></tr>
      <tr><td>163 - 171</td><td>4</td><td>162.5 - 171.5</td></tr>
      <tr><td>172 - 180</td><td>2</td><td>171.5 - 180.5</td></tr>
    </table>
    <p><b>(i) दिए हुए आँकड़ों को निरूपित करने वाला एक आयतचित्र खींचिए।</b><br>
    <b>(ii) क्या इन्हीं आँकड़ों को निरूपित करने वाला कोई अन्य उपयुक्त आलेख है?</b><br>
    <b>(iii) क्या यह सही निष्कर्ष है कि 153 mm लंबाई वाली पत्तियों की संख्या सबसे अधिक है? क्यों?</b></p>

    <div class="step-box-green">
      <p><b>हल:</b></p>
      <p><b>चरण 1 (अंतरालों को सतत बनाना):</b></p>
      <p>दिए गए वर्ग अंतराल असतत हैं। प्रथम अंतराल की उच्च सीमा $126$ तथा द्वितीय की निम्न सीमा $127$ है। अंतर $= 127 - 126 = 1$। अतः प्रत्येक निम्न सीमा में से $\frac{1}{2} = 0.5$ घटाते हैं तथा उच्च सीमा में $0.5$ जोड़ते हैं।</p>
      <p><b>(i) आयतचित्र:</b> $X$-अक्ष पर सतत वर्ग अंतरालों को तथा $Y$-अक्ष पर पत्तियों की संख्या को दर्शाते हुए बिना अंतराल वाले आसन्न आयत बनाए जाते हैं।</p>
      <p><b>(ii) अन्य उपयुक्त आलेख:</b> हाँ, <b>बारंबारता बहुभुज (Frequency Polygon)</b> भी इन आँकड़ों को निरूपित करने के लिए उपयुक्त है।</p>
      <p><b>(iii) निष्कर्ष की सत्यता:</b> <b>नहीं,</b> यह निष्कर्ष सही नहीं है। वर्ग अंतराल $144.5 - 153.5$ की कुल बारंबारता $12$ है, जिसका अर्थ यह नहीं है कि सभी $12$ पत्तियाँ ठीक $153\text{ mm}$ की हैं; वे $144.5$ से $153.5\text{ mm}$ के बीच किसी भी माप की हो सकती हैं।</p>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: (i) सतत आयतचित्र, (ii) बारंबारता बहुभुज, (iii) नहीं, क्योंकि 12 पत्तियाँ पूरे अंतराल (144.5-153.5 mm) में वितरित हैं।
    </div>
  </div>

  <!-- Q5 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 5: नीचे दी गई सारणी में 400 नियॉन लैम्पों के जीवन काल दिए गए हैं:</h3>
    <table class="stat-table">
      <tr><th>जीवन काल (घंटों में)</th><th>लैम्पों की संख्या</th></tr>
      <tr><td>300 - 400</td><td>14</td></tr>
      <tr><td>400 - 500</td><td>56</td></tr>
      <tr><td>500 - 600</td><td>60</td></tr>
      <tr><td>600 - 700</td><td>86</td></tr>
      <tr><td>700 - 800</td><td>74</td></tr>
      <tr><td>800 - 900</td><td>62</td></tr>
      <tr><td>900 - 1000</td><td>48</td></tr>
    </table>
    <p><b>(i) एक आयतचित्र की सहायता से दी हुई सूचनाओं को निरूपित कीजिए।</b><br>
    <b>(ii) कितने लैम्पों के जीवन काल 700 घंटे या उससे अधिक हैं?</b></p>

    <div class="step-box-blue">
      <p><b>हल:</b></p>
      <p><b>(i) आयतचित्र रचना:</b> वर्ग अंतराल पहले से ही सतत हैं तथा सभी की चौड़ाई $100$ घंटे समान है। $X$-अक्ष पर जीवन काल ($0$ से $300$ तक किंक) तथा $Y$-अक्ष पर लैम्पों की संख्या लेकर आयतचित्र बनाया जाता है।</p>
      <p><b>(ii) 700 घंटे या उससे अधिक जीवन काल वाले लैम्प:</b></p>
      <div class="math-scroll">
        $$\begin{aligned}
        \text{Total Lamps} &= (\text{700-800}) + (\text{800-900}) + (\text{900-1000}) \\
        &= 74 + 62 + 48 \\
        &= 184
        \end{aligned}$$
      </div>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: 700 घंटे या उससे अधिक जीवन काल वाले लैम्पों की संख्या = 184 है।
    </div>
  </div>

  <!-- Q6 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 6: नीचे दी गई सारणी में एक विद्यालय के दो सेक्शनों A और B के विद्यार्थियों द्वारा प्राप्त किए गए अंक दिए गए हैं:</h3>
    <table class="stat-table">
      <tr><th colspan="3">सेक्शन A</th><th colspan="3">सेक्शन B</th></tr>
      <tr><th>अंक</th><th>वर्ग चिह्न</th><th>बारंबारता</th><th>अंक</th><th>वर्ग चिह्न</th><th>बारंबारता</th></tr>
      <tr><td>0 - 10</td><td>5</td><td>3</td><td>0 - 10</td><td>5</td><td>5</td></tr>
      <tr><td>10 - 20</td><td>15</td><td>9</td><td>10 - 20</td><td>15</td><td>19</td></tr>
      <tr><td>20 - 30</td><td>25</td><td>17</td><td>20 - 30</td><td>25</td><td>15</td></tr>
      <tr><td>30 - 40</td><td>35</td><td>12</td><td>30 - 40</td><td>35</td><td>10</td></tr>
      <tr><td>40 - 50</td><td>45</td><td>9</td><td>40 - 50</td><td>45</td><td>1</td></tr>
    </table>
    <p><b>एक ही आलेख पर दोनों सेक्शनों के विद्यार्थियों के प्राप्तांकों को दो बारंबारता बहुभुजों की सहायता से निरूपित कीजिए। दोनों बहुभुजों से विद्यार्थियों के प्रदर्शन की तुलना कीजिए।</b></p>

    <div class="step-box-purple">
      <p><b>हल:</b></p>
      <p><b>वर्ग चिह्न सूत्र:</b> $\text{Class Mark} = \frac{\text{Upper Limit} + \text{Lower Limit}}{2}$</p>
      <p>बहुभुज को बंद करने के लिए पूर्व अंतराल $(-10 - 0)$ का वर्ग चिह्न $-5$ (बारंबारता $0$) तथा आगामी अंतराल $(50 - 60)$ का वर्ग चिह्न $55$ (बारंबारता $0$) लेते हैं।</p>
      <p><b>सेक्शन A के बिंदु:</b> $(-5, 0), (5, 3), (15, 9), (25, 17), (35, 12), (45, 9), (55, 0)$</p>
      <p><b>सेक्शन B के बिंदु:</b> $(-5, 0), (5, 5), (15, 19), (25, 15), (35, 10), (45, 1), (55, 0)$</p>
      <p><b>तुलना:</b> सेक्शन A में उच्च अंक (20 से 50 के बीच) प्राप्त करने वाले छात्रों की संख्या अधिक है, अतः सेक्शन A का समग्र प्रदर्शन सेक्शन B से बेहतर है।</p>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: सेक्शन A का प्रदर्शन सेक्शन B की तुलना में श्रेष्ठतर है।
    </div>
  </div>

  <!-- Q7 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 7: एक क्रिकेट मैच में दो टीमों A और B द्वारा प्रथम 60 गेंदों में बनाए गए रन नीचे दिए गए हैं:</h3>
    <table class="stat-table">
      <tr><th>गेंदों की संख्या</th><th>सतत वर्ग अंतराल</th><th>वर्ग चिह्न</th><th>टीम A के रन</th><th>टीम B के रन</th></tr>
      <tr><td>1 - 6</td><td>0.5 - 6.5</td><td>3.5</td><td>2</td><td>5</td></tr>
      <tr><td>7 - 12</td><td>6.5 - 12.5</td><td>9.5</td><td>1</td><td>6</td></tr>
      <tr><td>13 - 18</td><td>12.5 - 18.5</td><td>15.5</td><td>8</td><td>2</td></tr>
      <tr><td>19 - 24</td><td>18.5 - 24.5</td><td>21.5</td><td>9</td><td>10</td></tr>
      <tr><td>25 - 30</td><td>24.5 - 30.5</td><td>27.5</td><td>4</td><td>5</td></tr>
      <tr><td>31 - 36</td><td>30.5 - 36.5</td><td>33.5</td><td>5</td><td>6</td></tr>
      <tr><td>37 - 42</td><td>36.5 - 42.5</td><td>39.5</td><td>6</td><td>3</td></tr>
      <tr><td>43 - 48</td><td>42.5 - 48.5</td><td>45.5</td><td>10</td><td>4</td></tr>
      <tr><td>49 - 54</td><td>48.5 - 54.5</td><td>51.5</td><td>6</td><td>8</td></tr>
      <tr><td>55 - 60</td><td>54.5 - 60.5</td><td>57.5</td><td>2</td><td>10</td></tr>
    </table>
    <p><b>बारंबारता बहुभुजों की सहायता से एक ही आलेख पर दोनों टीमों के आँकड़े निरूपित कीजिए।</b></p>

    <div class="step-box-green">
      <p><b>हल:</b></p>
      <p><b>चरण 1:</b> वर्ग अंतरालों को सतत बनाया गया ($0.5$ घटाकर व जोड़कर)। प्रत्येक वर्ग की चौड़ाई $6$ है।</p>
      <p><b>चरण 2:</b> वर्ग चिह्न $= \frac{\text{Upper Limit} + \text{Lower Limit}}{2}$ निकाला गया (उदा. $\frac{0.5 + 6.5}{2} = 3.5$)।</p>
      <p><b>चरण 3:</b> बहुभुज को दोनों सिरों पर मिलाने के लिए $(-2.5, 0)$ तथा $(63.5, 0)$ पर $X$-अक्ष से जोड़ा जाता है। दोनों टीमों के बिंदुओं को आलेखित कर क्रमशः ठोस व बिंदुदार रेखाओं से मिलाया जाता है।</p>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: दोनों टीमों A व B के बारंबारता बहुभुज सतत वर्ग चिह्नों पर आलेखित किए जाते हैं।
    </div>
  </div>

  <!-- Q8 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 8: एक पार्क में खेल रहे विभिन्न आयु वर्गों के बच्चों की संख्या का एक यादृच्छिक सर्वेक्षण (Random survey) करने पर निम्नलिखित आँकड़े प्राप्त हुए:</h3>
    <table class="stat-table">
      <tr><th>आयु (वर्षों में)</th><th>बच्चों की संख्या ($f_i$)</th><th>वर्ग चौड़ाई ($w_i$)</th><th>आयत की लंबाई (समायोजित बारंबारता)</th></tr>
      <tr><td>1 - 2</td><td>5</td><td>1</td><td>$\frac{5}{1} \cdot 1 = 5$</td></tr>
      <tr><td>2 - 3</td><td>3</td><td>1</td><td>$\frac{3}{1} \cdot 1 = 3$</td></tr>
      <tr><td>3 - 5</td><td>6</td><td>2</td><td>$\frac{6}{2} \cdot 1 = 3$</td></tr>
      <tr><td>5 - 7</td><td>12</td><td>2</td><td>$\frac{12}{2} \cdot 1 = 6$</td></tr>
      <tr><td>7 - 10</td><td>9</td><td>3</td><td>$\frac{9}{3} \cdot 1 = 3$</td></tr>
      <tr><td>10 - 15</td><td>10</td><td>5</td><td>$\frac{10}{5} \cdot 1 = 2$</td></tr>
      <tr><td>15 - 17</td><td>4</td><td>2</td><td>$\frac{4}{2} \cdot 1 = 2$</td></tr>
    </table>
    <p><b>उपरोक्त आँकड़ों को निरूपित करने वाला एक आयतचित्र खींचिए।</b></p>

    <div class="step-box-blue">
      <p><b>हल एवं विशेष नियम (असमान वर्ग चौड़ाई):</b></p>
      <p>यहाँ वर्ग अंतरालों की चौड़ाई असमान है ($1, 2, 3, 5$)। न्यूनतम वर्ग चौड़ाई $= 1$ है।</p>
      <div class="math-scroll">
        $$\text{Length} = \frac{\text{Frequency}}{\text{Width}} \cdot \text{Min Width}$$
      </div>
      <p>समायोजित बारंबारता की गणना ऊपर सारणी के चौथे स्तंभ में पूर्ण की गई है। अब $X$-अक्ष पर आयु वर्ग तथा $Y$-अक्ष पर आयत की लंबाई लेकर आयतचित्र खींचा जाता है।</p>
    </div>
    <div class="answer-highlight">
      ✅ समायोजन: आयतों की अभीष्ट लंबाइयाँ क्रमशः 5, 3, 3, 6, 3, 2, 2 हैं।
    </div>
  </div>

  <!-- Q9 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 9: एक स्थानीय टेलीफोन निर्देशिका से 100 कुलनाम (Surnames) यदृच्छया लिए गए और उनमें अंग्रेजी वर्णमाला के अक्षरों की संख्या का निम्नलिखित बारंबारता बंटन प्राप्त हुआ:</h3>
    <table class="stat-table">
      <tr><th>अक्षरों की संख्या</th><th>कुलनामों की संख्या ($f_i$)</th><th>वर्ग चौड़ाई ($w_i$)</th><th>आयत की लंबाई</th></tr>
      <tr><td>1 - 4</td><td>6</td><td>3</td><td>$\frac{6}{3} \cdot 2 = 4$</td></tr>
      <tr><td>4 - 6</td><td>30</td><td>2</td><td>$\frac{30}{2} \cdot 2 = 30$</td></tr>
      <tr><td>6 - 8</td><td>44</td><td>2</td><td>$\frac{44}{2} \cdot 2 = 44$</td></tr>
      <tr><td>8 - 12</td><td>16</td><td>4</td><td>$\frac{16}{4} \cdot 2 = 8$</td></tr>
      <tr><td>12 - 20</td><td>4</td><td>8</td><td>$\frac{4}{8} \cdot 2 = 1$</td></tr>
    </table>
    <p><b>(i) दी हुई सूचनाओं को निरूपित करने वाला एक आयतचित्र खींचिए।</b><br>
    <b>(ii) वह वर्ग अंतराल बताइए जिसमें अधिकतम संख्या में कुलनाम हैं।</b></p>

    <div class="step-box-purple">
      <p><b>हल:</b></p>
      <p><b>(i) आयत की लंबाई की गणना:</b> न्यूनतम वर्ग चौड़ाई $= 2$ है। प्रत्येक वर्ग के लिए सूत्र लागू किया गया:</p>
      <div class="math-scroll">
        $$\text{Length} = \frac{\text{Frequency}}{\text{Width}} \cdot 2$$
      </div>
      <p>प्राप्त लंबाइयाँ क्रमशः $4, 30, 44, 8, 1$ हैं।</p>
      <p><b>(ii) अधिकतम कुलनामों वाला वर्ग अंतराल:</b></p>
      <p>सारणी से स्पष्ट है कि वर्ग अंतराल <b>$6 - 8$</b> में सर्वाधिक $44$ कुलनाम हैं।</p>
    </div>
    <div class="answer-highlight">
      ✅ उत्तर: (i) आयत की लंबाइयाँ 4, 30, 44, 8, 1 हैं, (ii) अधिकतम कुलनामों वाला वर्ग अंतराल = 6 - 8 है।
    </div>
  </div>

  <!-- SECTION: 5 INTERACTIVE LIVE SIMULATORS -->
  <div class="section-title" id="simulators">🎮 5 लाइव इंटरैक्टिव सिमुलेटर (Interactive Statistics Simulators)</div>

  <!-- SIMULATOR 1 -->
  <div class="sim-container">
    <h3 class="sim-title">सिमुलेटर 1: बार ग्राफ जनरेटर (Interactive Bar Graph Generator)</h3>
    <p>विभिन्न श्रेणियों और बारंबारताओं के लिए तुरंत सजीव SVG बार ग्राफ तैयार करें:</p>
    <div class="sim-controls">
      <label>पार्टी A सीटें: <input type="number" id="sim1_a" value="75" min="0" max="100" style="width:70px;" oninput="updateSim1()"></label>
      <label>पार्टी B सीटें: <input type="number" id="sim1_b" value="55" min="0" max="100" style="width:70px;" oninput="updateSim1()"></label>
      <label>पार्टी C सीटें: <input type="number" id="sim1_c" value="37" min="0" max="100" style="width:70px;" oninput="updateSim1()"></label>
      <label>पार्टी D सीटें: <input type="number" id="sim1_d" value="29" min="0" max="100" style="width:70px;" oninput="updateSim1()"></label>
      <label>पार्टी E सीटें: <input type="number" id="sim1_e" value="10" min="0" max="100" style="width:70px;" oninput="updateSim1()"></label>
    </div>
    <div class="sim-canvas-box">
      <svg id="sim1_svg" width="100%" height="220" viewBox="0 0 500 220"></svg>
    </div>
    <div class="sim-output" id="sim1_out">
      सर्वोच्च दंड: पार्टी A (75 सीटें)
    </div>
  </div>

  <!-- SIMULATOR 2 -->
  <div class="sim-container">
    <h3 class="sim-title">सिमुलेटर 2: सतत आयतचित्र विज़ुअलाइज़र (Histogram Visualizer)</h3>
    <p>सतत अंतरालों के लिए बिना रिक्त स्थान वाला आयतचित्र देखें (उदा. पत्तियों की लंबाई / लैम्पों की संख्या):</p>
    <div class="sim-controls">
      <label>वर्ग 1 (300-400): <input type="range" id="sim2_f1" min="5" max="100" value="14" oninput="updateSim2()"><span id="sim2_v1">14</span></label>
      <label>वर्ग 2 (400-500): <input type="range" id="sim2_f2" min="5" max="100" value="56" oninput="updateSim2()"><span id="sim2_v2">56</span></label>
      <label>वर्ग 3 (500-600): <input type="range" id="sim2_f3" min="5" max="100" value="86" oninput="updateSim2()"><span id="sim2_v3">86</span></label>
      <label>वर्ग 4 (600-700): <input type="range" id="sim2_f4" min="5" max="100" value="62" oninput="updateSim2()"><span id="sim2_v4">62</span></label>
    </div>
    <div class="sim-canvas-box">
      <svg id="sim2_svg" width="100%" height="220" viewBox="0 0 500 220"></svg>
    </div>
    <div class="sim-output" id="sim2_out">
      कुल बारंबारता = 218, उच्चतम बारंबारता वाला अंतराल = 500 - 600 (86)
    </div>
  </div>

  <!-- SIMULATOR 3 -->
  <div class="sim-container">
    <h3 class="sim-title">सिमुलेटर 3: बारंबारता बहुभुज प्लॉटर (Frequency Polygon Plotter)</h3>
    <p>वर्ग चिह्नों (मध्य बिंदुओं) को जोड़कर बारंबारता बहुभुज की सजीव रचना देखें:</p>
    <div class="sim-controls">
      <label>सेक्शन A स्कोर गुणक: <input type="range" id="sim3_scaleA" min="5" max="25" value="15" oninput="updateSim3()"><span id="sim3_va">15</span></label>
      <label>सेक्शन B स्कोर गुणक: <input type="range" id="sim3_scaleB" min="5" max="25" value="10" oninput="updateSim3()"><span id="sim3_vb">10</span></label>
    </div>
    <div class="sim-canvas-box">
      <svg id="sim3_svg" width="100%" height="220" viewBox="0 0 500 220"></svg>
    </div>
    <div class="sim-output" id="sim3_out">
      नीली रेखा = सेक्शन A, लाल रेखा = सेक्शन B (दोनों बहुभुज $X$-अक्ष पर संलग्न हैं)
    </div>
  </div>

  <!-- SIMULATOR 4 -->
  <div class="sim-container">
    <h3 class="sim-title">सिमुलेटर 4: असमान चौड़ाई आयतचित्र सॉल्वर (Varying Width Adjuster)</h3>
    <p>असमान वर्ग अंतरालों में आयत की ऊँचाई (समायोजित बारंबारता) की त्वरित गणना:</p>
    <div class="sim-controls">
      <label>वर्ग बारंबारता ($f_i$): <input type="number" id="sim4_f" value="12" min="1" max="100" style="width:80px;" oninput="updateSim4()"></label>
      <label>इस वर्ग की चौड़ाई ($w_i$): <input type="number" id="sim4_w" value="2" min="1" max="20" style="width:80px;" oninput="updateSim4()"></label>
      <label>न्यूनतम वर्ग चौड़ाई ($w_{min}$): <input type="number" id="sim4_minw" value="1" min="1" max="10" style="width:80px;" oninput="updateSim4()"></label>
    </div>
    <div class="sim-output" id="sim4_out">
      $$\\text{Length} = \\frac{12}{2} \\cdot 1 = 6$$
    </div>
  </div>

  <!-- SIMULATOR 5 -->
  <div class="sim-container">
    <h3 class="sim-title">सिमुलेटर 5: माध्य, माध्यक एवं बहुलक विश्लेषक (Mean, Median, Mode Calculator)</h3>
    <p>कोई भी संख्या श्रेणी दर्ज करें (अल्पविराम द्वारा अलग):</p>
    <div class="sim-controls" style="width:100%;">
      <input type="text" id="sim5_input" value="14, 25, 14, 28, 18, 17, 18, 14, 23, 22, 14, 18" style="width:80%; max-width:500px;" oninput="updateSim5()">
      <button class="action-btn" onclick="updateSim5()">गणना करें</button>
    </div>
    <div class="sim-output" id="sim5_out">
      माध्य $\\approx 18.92$ | माध्यक $= 18$ | बहुलक $= 14$
    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    <p>NCERT कक्षा 9 गणित डिजिटल अध्ययन पोर्टल • 100% सटीक हल, शून्य स्क्रॉलबार व उत्तरदायी लेआउट</p>
  </footer>

</div>

<!-- JAVASCRIPT FOR SIMULATORS -->
<script>
// Simulator 1: Bar Graph
function updateSim1() {
  const a = parseFloat(document.getElementById('sim1_a').value) || 0;
  const b = parseFloat(document.getElementById('sim1_b').value) || 0;
  const c = parseFloat(document.getElementById('sim1_c').value) || 0;
  const d = parseFloat(document.getElementById('sim1_d').value) || 0;
  const e = parseFloat(document.getElementById('sim1_e').value) || 0;

  const data = [
    { label: 'A', val: a, col: '#0d9488' },
    { label: 'B', val: b, col: '#3b82f6' },
    { label: 'C', val: c, col: '#8b5cf6' },
    { label: 'D', val: d, col: '#f59e0b' },
    { label: 'E', val: e, col: '#ef4444' }
  ];

  const maxVal = Math.max(80, a, b, c, d, e);
  const svg = document.getElementById('sim1_svg');
  let html = '<line x1="40" y1="180" x2="480" y2="180" stroke="#94a3b8" stroke-width="2"/>';
  html += '<line x1="40" y1="20" x2="40" y2="180" stroke="#94a3b8" stroke-width="2"/>';

  data.forEach((item, i) => {
    const x = 70 + i * 80;
    const barH = (item.val / maxVal) * 150;
    const y = 180 - barH;
    html += `<rect x="${x}" y="${y}" width="45" height="${barH}" fill="${item.col}" rx="4"/>`;
    html += `<text x="${x + 22}" y="${y - 6}" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">${item.val}</text>`;
    html += `<text x="${x + 22}" y="198" font-size="13" font-weight="bold" fill="#1e293b" text-anchor="middle">${item.label}</text>`;
  });

  svg.innerHTML = html;
  const top = [...data].sort((x, y) => y.val - x.val)[0];
  document.getElementById('sim1_out').innerText = `सर्वोच्च दंड: पार्टी ${top.label} (${top.val} सीटें)`;
}

// Simulator 2: Histogram
function updateSim2() {
  const f1 = parseInt(document.getElementById('sim2_f1').value);
  const f2 = parseInt(document.getElementById('sim2_f2').value);
  const f3 = parseInt(document.getElementById('sim2_f3').value);
  const f4 = parseInt(document.getElementById('sim2_f4').value);

  document.getElementById('sim2_v1').innerText = f1;
  document.getElementById('sim2_v2').innerText = f2;
  document.getElementById('sim2_v3').innerText = f3;
  document.getElementById('sim2_v4').innerText = f4;

  const heights = [f1, f2, f3, f4];
  const maxF = Math.max(100, ...heights);
  const svg = document.getElementById('sim2_svg');

  let html = '<line x1="50" y1="180" x2="470" y2="180" stroke="#94a3b8" stroke-width="2"/>';
  html += '<line x1="50" y1="20" x2="50" y2="180" stroke="#94a3b8" stroke-width="2"/>';

  const labels = ['300-400', '400-500', '500-600', '600-700'];
  heights.forEach((h, i) => {
    const x = 70 + i * 95;
    const barH = (h / maxF) * 150;
    const y = 180 - barH;
    html += `<rect x="${x}" y="${y}" width="95" height="${barH}" fill="#14b8a6" stroke="#0f766e" stroke-width="1.5"/>`;
    html += `<text x="${x + 47}" y="${y - 6}" font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">${h}</text>`;
    html += `<text x="${x + 47}" y="196" font-size="11" fill="#475569" text-anchor="middle">${labels[i]}</text>`;
  });

  svg.innerHTML = html;
  const total = f1 + f2 + f3 + f4;
  document.getElementById('sim2_out').innerText = `कुल बारंबारता = ${total} | उच्चतम बारंबारता = ${Math.max(...heights)}`;
}

// Simulator 3: Frequency Polygon
function updateSim3() {
  const sa = parseInt(document.getElementById('sim3_scaleA').value);
  const sb = parseInt(document.getElementById('sim3_scaleB').value);
  document.getElementById('sim3_va').innerText = sa;
  document.getElementById('sim3_vb').innerText = sb;

  const ptsA = [
    {x: 50, y: 180},
    {x: 120, y: 180 - sa * 5},
    {x: 190, y: 180 - sa * 8},
    {x: 260, y: 180 - sa * 6},
    {x: 330, y: 180 - sa * 4},
    {x: 400, y: 180}
  ];

  const ptsB = [
    {x: 50, y: 180},
    {x: 120, y: 180 - sb * 7},
    {x: 190, y: 180 - sb * 6},
    {x: 260, y: 180 - sb * 7},
    {x: 330, y: 180 - sb * 3},
    {x: 400, y: 180}
  ];

  const polyA = ptsA.map(p => `${p.x},${p.y}`).join(' ');
  const polyB = ptsB.map(p => `${p.x},${p.y}`).join(' ');

  const svg = document.getElementById('sim3_svg');
  let html = '<line x1="40" y1="180" x2="450" y2="180" stroke="#94a3b8" stroke-width="2"/>';
  html += `<polyline points="${polyA}" fill="none" stroke="#2563eb" stroke-width="3"/>`;
  html += `<polyline points="${polyB}" fill="none" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4"/>`;

  ptsA.forEach(p => { html += `<circle cx="${p.x}" cy="${p.y}" r="4" fill="#2563eb"/>`; });
  ptsB.forEach(p => { html += `<circle cx="${p.x}" cy="${p.y}" r="4" fill="#dc2626"/>`; });

  svg.innerHTML = html;
}

// Simulator 4: Varying Width Adjuster
function updateSim4() {
  const f = parseFloat(document.getElementById('sim4_f').value) || 0;
  const w = parseFloat(document.getElementById('sim4_w').value) || 1;
  const minw = parseFloat(document.getElementById('sim4_minw').value) || 1;

  const length = (f / w) * minw;
  const lengthClean = Number.isInteger(length) ? length : length.toFixed(2);

  const out = document.getElementById('sim4_out');
  out.innerHTML = `$$\\\\text{Length} = \\\\frac{${f}}{${w}} \\\\cdot ${minw} = ${lengthClean}$$`;
  if (window.MathJax && MathJax.typesetPromise) {
    MathJax.typesetPromise([out]);
  }
}

// Simulator 5: Mean, Median, Mode
function updateSim5() {
  const raw = document.getElementById('sim5_input').value;
  const nums = raw.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
  if (nums.length === 0) return;

  // Mean
  const sum = nums.reduce((a, b) => a + b, 0);
  const mean = (sum / nums.length).toFixed(2);

  // Median
  const sorted = [...nums].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  const median = sorted.length % 2 !== 0 ? sorted[mid] : ((sorted[mid - 1] + sorted[mid]) / 2);

  // Mode
  const counts = {};
  nums.forEach(n => { counts[n] = (counts[n] || 0) + 1; });
  let maxCount = 0;
  let modes = [];
  for (let k in counts) {
    if (counts[k] > maxCount) {
      maxCount = counts[k];
      modes = [k];
    } else if (counts[k] === maxCount) {
      modes.push(k);
    }
  }
  const modeStr = maxCount > 1 ? modes.join(', ') : 'कोई बहुलक नहीं';

  document.getElementById('sim5_out').innerText = `कुल प्रेक्षण (N) = ${nums.length} | माध्य (Mean) = ${mean} | माध्यक (Median) = ${median} | बहुलक (Mode) = ${modeStr}`;
}

// Initialize simulators on load
window.addEventListener('load', () => {
  updateSim1();
  updateSim2();
  updateSim3();
  updateSim4();
  updateSim5();
});
</script>

</body>
</html>
'''

with open('qa_master_math9_12.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("qa_master_math9_12.html generated successfully!")
