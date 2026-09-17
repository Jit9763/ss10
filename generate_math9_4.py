# -*- coding: utf-8 -*-
"""
Generator for Chapter 4: दो चरों वाले रैखिक समीकरण (Linear Equations in Two Variables)
Converts Chapter 4 to the EXACT Chapter 2 Master Standard:
- Sticky Black Action Bar with 9 Projector Buttons (W+, W-, A+, A-, B+, B-, Copy, Print, Home)
- Container #contentToCopy with 26pt 900-weight Noto Sans Devanagari typography
- Rich color-coded step boxes & yellow/green answer highlights
- High-contrast SVG coordinate plane graphs with DARK grid lines and BOLD NUMBERS on X & Y axes
- Simulator 5 Canvas with DARK grid lines, DARK axes, and BOLD NUMBERS on X & Y axes
- 100% verified NCERT Ex 4.1 and Ex 4.2 solutions
"""

from generate_svg_helper import generate_svg_graph

with open('ch2_style.css', 'r', encoding='utf-8') as f:
    ch2_css = f.read()

# Generate SVG graphs for key linear equations
svg_graph_1 = generate_svg_graph(
    "x_plus_y_eq_4",
    [(0, 4), (2, 2), (4, 0)],
    "x + y = 4",
    color="#2563eb",
    x_range=(-4, 6),
    y_range=(-2, 6)
)

svg_graph_2 = generate_svg_graph(
    "2x_plus_y_eq_7",
    [(0, 7), (1, 5), (2, 3), (3, 1)],
    "2x + y = 7",
    color="#dc2626",
    x_range=(-2, 5),
    y_range=(-1, 8)
)

svg_graph_3 = generate_svg_graph(
    "x_eq_4y",
    [(-4, -1), (0, 0), (4, 1)],
    "x = 4y",
    color="#059669",
    x_range=(-5, 5),
    y_range=(-3, 3)
)

svg_graph_4 = generate_svg_graph(
    "x_minus_2y_eq_4",
    [(0, -2), (4, 0), (2, -1)],
    "x - 2y = 4",
    color="#7c3aed",
    x_range=(-2, 6),
    y_range=(-4, 3)
)

html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NCERT कक्षा 9 गणित - अध्याय 4: दो चरों वाले रैखिक समीकरण (संपूर्ण प्रश्नोत्तर व 5 लाइव सिमुलेटर)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700;800;900&display=swap" rel="stylesheet">

<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
    processEscapes: true
  }},
  chtml: {{
    displayOverflow: 'scale'
  }},
  options: {{
    renderActions: {{
      addMenu: []
    }}
  }}
}};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

<style>
{ch2_css}

/* Extra graph & simulator controls styling in Ch 2 theme */
.sim-controls-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 15px;
  margin: 15px 0;
}}
.sim-group {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}
.sim-group label {{
  font-size: 18pt;
  font-weight: 900;
  color: #1e3a8a;
}}
.sim-group input {{
  padding: 10px 14px;
  font-size: 18pt;
  font-weight: 900;
  border: 3px solid #cbd5e1;
  border-radius: 10px;
  background: #ffffff;
}}
.sim-btn-calc {{
  padding: 12px 20px;
  font-size: 18pt;
  font-weight: 900;
  background: #1e3a8a;
  color: #ffffff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
}}
.sim-btn-calc:hover {{
  background: #1d4ed8;
  transform: translateY(-2px);
}}
.sim-canvas {{
  display: block;
  margin: 20px auto;
  background: #ffffff;
  border: 4px solid #cbd5e1;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  max-width: 100%;
}}
</style>
</head>
<body>

<div class="container" id="contentToCopy">

  <!-- Top Action Bar (Sticky 9 Projector Buttons) -->
  <div class="action-bar">
    <button class="action-btn" onclick="adjustWidth(100)">↔️ W+</button>
    <button class="action-btn" onclick="adjustWidth(-100)">↔️ W-</button>
    <button class="action-btn" onclick="adjustFontSize(2)">🔍 A+</button>
    <button class="action-btn" onclick="adjustFontSize(-2)">🔍 A-</button>
    <button class="action-btn" onclick="adjustFontWeight(100)">✒️ B+</button>
    <button class="action-btn" onclick="adjustFontWeight(-100)">✒️ B-</button>
    <button class="action-btn action-btn-copy" onclick="copyEntireContent()">📋 कॉपी</button>
    <button class="action-btn" onclick="window.print()">🖨️ प्रिंट</button>
    <a href="math9.html" class="action-btn action-btn-home">🏠 मुख्य पोर्टल</a>
  </div>

  <!-- Top Header -->
  <div class="top-header">
    <span class="class-badge">NCERT कक्षा 9 गणित (Mathematics)</span>
    <div style="font-size: 32pt; font-weight: 900; color: #0f172a; margin-top: 8px;">
      अध्याय 4: दो चरों वाले रैखिक समीकरण (Linear Equations in Two Variables) • संपूर्ण 100% अभ्यास हल व 5 लाइव सिमुलेटर
    </div>
    <div style="font-size: 20pt; font-weight: 700; color: #475569; margin-top: 10px;">
      प्रश्नावली 4.1 व 4.2 के सभी प्रश्न, आलेखीय निरूपण, पूर्ण चरणबद्ध हल एवं इंटरैक्टिव प्रोजेक्टर टूल्स
    </div>
  </div>

  <!-- Key Concepts / Formula Box -->
  <div class="formula-box" style="background:#eff6ff; border:4px solid #3b82f6; border-radius:18px; padding:25px; margin:30px 0;">
    <div style="font-size: 24pt; font-weight: 900; color: #1e3a8a; margin-bottom: 15px; border-bottom: 3px solid #bfdbfe; padding-bottom: 10px;">
      📌 मुख्य सूत्र एवं अवधारणाएँ (Key Formulas & Concepts)
    </div>
    <ul style="font-size: 20pt; font-weight: 800; line-height: 1.8; color: #1e293b; padding-left: 25px;">
      <li><b>मानक रूप (Standard Form):</b> $ax + by + c = 0$, जहाँ $a, b, c$ वास्तविक संख्याएँ हैं तथा $a$ और $b$ दोनों शून्य नहीं हैं ($a^2 + b^2 \\neq 0$)।</li>
      <li><b>अपरिमित हल (Infinitely Many Solutions):</b> दो चरों वाले एक रैखिक समीकरण के अपरिमित रूप से अनेक हल होते हैं। प्रत्येक हल $(x, y)$ आलेख पर स्थित एक बिंदु होता है।</li>
      <li><b>आलेखीय निरूपण (Graphical Representation):</b> दो चरों वाले रैखिक समीकरण का आलेख सदैव एक <b>सरल रेखा (Straight Line)</b> होती है।</li>
      <li><b>अक्षों के समीकरण:</b>
        <ul>
          <li>$X$-अक्ष का समीकरण: $y = 0$</li>
          <li>$Y$-अक्ष का समीकरण: $x = 0$</li>
          <li>$Y$-अक्ष के समांतर रेखा: $x = a$</li>
          <li>$X$-अक्ष के समांतर रेखा: $y = b$</li>
        </ul>
      </li>
    </ul>
  </div>

  <!-- =========================================================
       EXERCISE 4.1
       ========================================================= -->
  <div class="part-header">
    📖 प्रश्नावली 4.1 (Exercise 4.1) — संपूर्ण 100% NCERT हल
  </div>

  <!-- Q1 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 1: एक नोटबुक की कीमत एक कलम की कीमत से दो गुनी है। इस कथन को निरूपित करने के लिए दो चरों वाला एक रैखिक समीकरण लिखिए।</h3>
    <div class="step-box-green">
      <p><b>चरण 1: चरों को मानना</b></p>
      <p>मान लीजिए कि एक नोटबुक की कीमत $= x$ रुपये</p>
      <p>तथा एक कलम की कीमत $= y$ रुपये</p>
      <p><b>चरण 2: प्रश्नानुसार संबंध स्थापित करना</b></p>
      <p>प्रश्नानुसार, नोटबुक की कीमत कलम की कीमत की दो गुनी है:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        x &= 2y \\\\
        x - 2y &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ में तुलना करने पर: $1x + (-2)y + 0 = 0$</p>
    </div>
    <div class="answer-highlight">
      ✅ अभीष्ट दो चरों वाला रैखिक समीकरण: $x - 2y = 0$
    </div>
  </div>

  <!-- Q2 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 2: निम्नलिखित रैखिक समीकरणों को $ax + by + c = 0$ के रूप में व्यक्त कीजिए और प्रत्येक स्थिति में $a, b$ और $c$ के मान बताइए:</h3>

    <!-- (i) -->
    <div class="step-box-blue">
      <p><b>(i) $2x + 3y = 9.3\\bar{{5}}$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        2x + 3y - 9.3\\bar{{5}} &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 2$, $b = 3$, $c = -9.3\\bar{{5}}$</b></p>
    </div>

    <!-- (ii) -->
    <div class="step-box-purple">
      <p><b>(ii) $x - \\frac{{y}}{{5}} - 10 = 0$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        1x + \\left(-\\frac{{1}}{{5}}\\right)y + (-10) &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 1$, $b = -\\frac{{1}}{{5}}$, $c = -10$</b></p>
    </div>

    <!-- (iii) -->
    <div class="step-box-green">
      <p><b>(iii) $-2x + 3y = 6$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        -2x + 3y - 6 &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = -2$, $b = 3$, $c = -6$</b></p>
    </div>

    <!-- (iv) -->
    <div class="step-box-orange">
      <p><b>(iv) $x = 3y$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        1x - 3y + 0 &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 1$, $b = -3$, $c = 0$</b></p>
    </div>

    <!-- (v) -->
    <div class="step-box-blue">
      <p><b>(v) $2x = -5y$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        2x + 5y + 0 &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 2$, $b = 5$, $c = 0$</b></p>
    </div>

    <!-- (vi) -->
    <div class="step-box-purple">
      <p><b>(vi) $3x + 2 = 0$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        3x + 0y + 2 &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 3$, $b = 0$, $c = 2$</b></p>
    </div>

    <!-- (vii) -->
    <div class="step-box-green">
      <p><b>(vii) $y - 2 = 0$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        0x + 1y - 2 &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 0$, $b = 1$, $c = -2$</b></p>
    </div>

    <!-- (viii) -->
    <div class="step-box-orange">
      <p><b>(viii) $5 = 2x$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        2x + 0y - 5 &= 0
        \\end{{aligned}}$$
      </div>
      <p>मानक रूप $ax + by + c = 0$ से तुलना करने पर:</p>
      <p><b>$a = 2$, $b = 0$, $c = -5$</b></p>
    </div>

    <div class="answer-highlight">
      ✅ निष्कर्ष: प्रत्येक रैखिक समीकरण को $ax + by + c = 0$ में व्यवस्थित कर $a, b, c$ के मान सरलता से ज्ञात किए जा सकते हैं।
    </div>
  </div>

  <!-- =========================================================
       EXERCISE 4.2
       ========================================================= -->
  <div class="part-header">
    📖 प्रश्नावली 4.2 (Exercise 4.2) — संपूर्ण 100% NCERT हल व आलेख
  </div>

  <!-- Q1 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 1: निम्नलिखित विकल्पों में कौन-सा विकल्प सत्य है और क्यों?<br>$y = 3x + 5$ का:<br>(i) एक अद्वितीय हल है,<br>(ii) केवल दो हल हैं,<br>(iii) अपरिमित रूप से अनेक हल हैं।</h3>
    <div class="step-box-green">
      <p><b>कारण एवं विस्तृत व्याख्या:</b></p>
      <p>विकल्प <b>(iii) अपरिमित रूप से अनेक हल हैं</b> सत्य है।</p>
      <p><b>कारण:</b> समीकरण $y = 3x + 5$ दो चरों वाला एक रैखिक समीकरण है। इसमें $x$ के प्रत्येक वास्तविक मान के लिए $y$ का एक निश्चित संगत मान प्राप्त होता है:</p>
      <ul>
        <li>यदि $x = 0$, तो $y = 3(0) + 5 = 5$ $\\implies (0, 5)$</li>
        <li>यदि $x = 1$, तो $y = 3(1) + 5 = 8$ $\\implies (1, 8)$</li>
        <li>यदि $x = -1$, तो $y = 3(-1) + 5 = 2$ $\\implies (-1, 2)$</li>
      </ul>
      <p>चूँकि $x$ के अनंत मान संभव हैं, अतः $y$ के भी अनंत मान प्राप्त होंगे। इसलिए एक रैखिक समीकरण के <b>अपरिमित रूप से अनेक हल (Infinitely Many Solutions)</b> होते हैं।</p>
    </div>
    <div class="answer-highlight">
      ✅ सही उत्तर: विकल्प (iii) — अपरिमित रूप से अनेक हल हैं।
    </div>
  </div>

  <!-- Q2 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 2: निम्नलिखित समीकरणों में से प्रत्येक समीकरण के चार हल (Four Solutions) लिखिए तथा उनका आलेखीय निरूपण समझिए:</h3>

    <!-- (i) -->
    <div class="step-box-blue">
      <p><b>(i) $2x + y = 7$</b></p>
      <p>समीकरण को $y$ के रूप में लिखने पर: $y = 7 - 2x$</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        x &= 0 \\implies y = 7 - 2(0) = 7 \\implies (0, 7) \\\\
        x &= 1 \\implies y = 7 - 2(1) = 5 \\implies (1, 5) \\\\
        x &= 2 \\implies y = 7 - 2(2) = 3 \\implies (2, 3) \\\\
        x &= 3 \\implies y = 7 - 2(3) = 1 \\implies (3, 1)
        \\end{{aligned}}$$
      </div>
      <p><b>चार हल:</b> $(0, 7), (1, 5), (2, 3), (3, 1)$</p>
      {svg_graph_2}
    </div>

    <!-- (ii) -->
    <div class="step-box-purple">
      <p><b>(ii) $\\pi x + y = 9$</b></p>
      <p>समीकरण को $y$ के रूप में लिखने पर: $y = 9 - \\pi x$</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        x &= 0 \\implies y = 9 - \\pi(0) = 9 \\implies (0, 9) \\\\
        x &= 1 \\implies y = 9 - \\pi(1) = 9 - \\pi \\implies (1, 9 - \\pi) \\\\
        x &= 2 \\implies y = 9 - \\pi(2) = 9 - 2\\pi \\implies (2, 9 - 2\\pi) \\\\
        x &= -1 \\implies y = 9 - \\pi(-1) = 9 + \\pi \\implies (-1, 9 + \\pi)
        \\end{{aligned}}$$
      </div>
      <p><b>चार हल:</b> $(0, 9), (1, 9 - \\pi), (2, 9 - 2\\pi), (-1, 9 + \\pi)$</p>
    </div>

    <!-- (iii) -->
    <div class="step-box-green">
      <p><b>(iii) $x = 4y$</b></p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        y &= 0 \\implies x = 4(0) = 0 \\implies (0, 0) \\\\
        y &= 1 \\implies x = 4(1) = 4 \\implies (4, 1) \\\\
        y &= 2 \\implies x = 4(2) = 8 \\implies (8, 2) \\\\
        y &= -1 \\implies x = 4(-1) = -4 \\implies (-4, -1)
        \\end{{aligned}}$$
      </div>
      <p><b>चार हल:</b> $(0, 0), (4, 1), (8, 2), (-4, -1)$</p>
      {svg_graph_3}
    </div>

    <!-- Graph example: x + y = 4 -->
    <div class="step-box-orange">
      <p><b>विशेष आलेख उदाहरण: $x + y = 4$</b></p>
      <p>समीकरण $y = 4 - x$ के लिए हल सारणी:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        x &= 0 \\implies y = 4 \\implies (0, 4) \\\\
        x &= 2 \\implies y = 2 \\implies (2, 2) \\\\
        x &= 4 \\implies y = 0 \\implies (4, 0)
        \\end{{aligned}}$$
      </div>
      {svg_graph_1}
    </div>

    <div class="answer-highlight">
      ✅ उत्तर: प्रत्येक रैखिक समीकरण के अपरिमित हल होते हैं, जिनमें से कोई भी चार अभीष्ट हल हो सकते हैं।
    </div>
  </div>

  <!-- Q3 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 3: बताइए कि निम्नलिखित हलों में कौन-कौन समीकरण $x - 2y = 4$ के हल हैं और कौन-कौन हल नहीं हैं:</h3>
    <p>दिया गया समीकरण: $x - 2y = 4$ (यहाँ $\\text{{L.H.S.}} = x - 2y$ तथा $\\text{{R.H.S.}} = 4$)</p>

    <!-- (i) -->
    <div class="step-box-blue">
      <p><b>(i) $(0, 2)$:</b> $x = 0, y = 2$ रखने पर:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        \\text{{L.H.S.}} &= 0 - 2(2) \\\\
        &= -4 \\neq 4 (\\text{{R.H.S.}})
        \\end{{aligned}}$$
      </div>
      <p><b>अतः $(0, 2)$ इस समीकरण का हल नहीं है।</b></p>
    </div>

    <!-- (ii) -->
    <div class="step-box-purple">
      <p><b>(ii) $(2, 0)$:</b> $x = 2, y = 0$ रखने पर:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        \\text{{L.H.S.}} &= 2 - 2(0) \\\\
        &= 2 \\neq 4 (\\text{{R.H.S.}})
        \\end{{aligned}}$$
      </div>
      <p><b>अतः $(2, 0)$ इस समीकरण का हल नहीं है।</b></p>
    </div>

    <!-- (iii) -->
    <div class="step-box-green">
      <p><b>(iii) $(4, 0)$:</b> $x = 4, y = 0$ रखने पर:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        \\text{{L.H.S.}} &= 4 - 2(0) \\\\
        &= 4 = \\text{{R.H.S.}}
        \\end{{aligned}}$$
      </div>
      <p><b>अतः $(4, 0)$ इस समीकरण का एक हल है।</b></p>
    </div>

    <!-- (iv) -->
    <div class="step-box-orange">
      <p><b>(iv) $(\\sqrt{{2}}, 4\\sqrt{{2}})$:</b> $x = \\sqrt{{2}}, y = 4\\sqrt{{2}}$ रखने पर:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        \\text{{L.H.S.}} &= \\sqrt{{2}} - 2(4\\sqrt{{2}}) \\\\
        &= \\sqrt{{2}} - 8\\sqrt{{2}} \\\\
        &= -7\\sqrt{{2}} \\neq 4 (\\text{{R.H.S.}})
        \\end{{aligned}}$$
      </div>
      <p><b>अतः $(\\sqrt{{2}}, 4\\sqrt{{2}})$ हल नहीं है।</b></p>
    </div>

    <!-- (v) -->
    <div class="step-box-blue">
      <p><b>(v) $(1, 1)$:</b> $x = 1, y = 1$ रखने पर:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        \\text{{L.H.S.}} &= 1 - 2(1) \\\\
        &= -1 \\neq 4 (\\text{{R.H.S.}})
        \\end{{aligned}}$$
      </div>
      <p><b>अतः $(1, 1)$ हल नहीं है।</b></p>
    </div>

    {svg_graph_4}

    <div class="answer-highlight">
      ✅ उत्तर: केवल (iii) $(4, 0)$ समीकरण $x - 2y = 4$ का एक हल है।
    </div>
  </div>

  <!-- Q4 -->
  <div class="qa-block">
    <h3 class="question-heading">प्रश्न 4: $k$ का मान ज्ञात कीजिए जबकि $x = 2, y = 1$ समीकरण $2x + 3y = k$ का एक हल हो।</h3>
    <div class="step-box-green">
      <p><b>चरण 1: समीकरण में मान प्रतिस्थापित करना</b></p>
      <p>दिया गया समीकरण: $2x + 3y = k$</p>
      <p>चूँकि $x = 2$ और $y = 1$ इस समीकरण का एक हल है, अतः यह समीकरण को संतुष्ट करेगा:</p>
      <div class="math-scroll">
        $$\\begin{{aligned}}
        2(2) + 3(1) &= k \\\\
        4 + 3 &= k \\\\
        k &= 7
        \\end{{aligned}}$$
      </div>
    </div>
    <div class="answer-highlight">
      ✅ अभीष्ट उत्तर: $k = 7$
    </div>
  </div>

  <!-- =========================================================
       5 LIVE INTERACTIVE SIMULATORS
       ========================================================= -->
  <div class="part-header" id="simulators">
    ⚡ लाइव सिमुलेटर अनुभाग (5 Interactive Linear Equation Simulators)
  </div>

  <!-- Simulator 1 -->
  <div class="inline-simulator-card">
    <h3 style="font-size:24pt; font-weight:900; color:#1e3a8a; margin-top:0;">⚡ लाइव सिमुलेटर 1: मानक रूप व गुणांक गणक ($ax + by + c = 0$)</h3>
    <p style="font-size:18pt; font-weight:700; color:#334155;">समीकरण के गुणांक दर्ज करें और मानक रूप व प्रकृतियाँ लाइव देखें:</p>
    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>गुणांक a (x का):</label>
        <input type="number" id="sim1_a" value="2" oninput="calculateSim1()">
      </div>
      <div class="sim-group">
        <label>गुणांक b (y का):</label>
        <input type="number" id="sim1_b" value="3" oninput="calculateSim1()">
      </div>
      <div class="sim-group">
        <label>अचर c:</label>
        <input type="number" id="sim1_c" value="-7" oninput="calculateSim1()">
      </div>
    </div>
    <div id="sim1_output" class="sim-output-box"></div>
  </div>

  <!-- Simulator 2 -->
  <div class="inline-simulator-card">
    <h3 style="font-size:24pt; font-weight:900; color:#1e3a8a; margin-top:0;">⚡ लाइव सिमुलेटर 2: चार क्रमिक हल जनरेटर (Four Solutions Table Generator)</h3>
    <p style="font-size:18pt; font-weight:700; color:#334155;">समीकरण $ax + by = c$ के लिए चार क्रमिक हल $(x, y)$ तालिका तुरंत प्राप्त करें:</p>
    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>गुणांक a:</label>
        <input type="number" id="sim2_a" value="2" oninput="calculateSim2()">
      </div>
      <div class="sim-group">
        <label>गुणांक b:</label>
        <input type="number" id="sim2_b" value="1" oninput="calculateSim2()">
      </div>
      <div class="sim-group">
        <label>अचर c:</label>
        <input type="number" id="sim2_c" value="7" oninput="calculateSim2()">
      </div>
    </div>
    <div id="sim2_output" class="sim-output-box"></div>
  </div>

  <!-- Simulator 3 -->
  <div class="inline-simulator-card">
    <h3 style="font-size:24pt; font-weight:900; color:#1e3a8a; margin-top:0;">⚡ लाइव सिमुलेटर 3: बिंदु हल सत्यापनकर्ता (Point Solution Verifier)</h3>
    <p style="font-size:18pt; font-weight:700; color:#334155;">जाँचें कि क्या कोई बिंदु $(x, y)$ समीकरण $ax + by = c$ को संतुष्ट करता है:</p>
    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>बिंदु का भुज (x):</label>
        <input type="number" id="sim3_x" value="4" oninput="calculateSim3()">
      </div>
      <div class="sim-group">
        <label>बिंदु की कोटि (y):</label>
        <input type="number" id="sim3_y" value="0" oninput="calculateSim3()">
      </div>
      <div class="sim-group">
        <label>समीकरण (a, b, c):</label>
        <div style="display:flex; gap:6px;">
          <input type="number" id="sim3_a" value="1" style="width:33%;" oninput="calculateSim3()">
          <input type="number" id="sim3_b" value="-2" style="width:33%;" oninput="calculateSim3()">
          <input type="number" id="sim3_c" value="4" style="width:33%;" oninput="calculateSim3()">
        </div>
      </div>
    </div>
    <div id="sim3_output" class="sim-output-box"></div>
  </div>

  <!-- Simulator 4 -->
  <div class="inline-simulator-card">
    <h3 style="font-size:24pt; font-weight:900; color:#1e3a8a; margin-top:0;">⚡ लाइव सिमुलेटर 4: अज्ञात चर 'k' गणक (Find 'k' Calculator)</h3>
    <p style="font-size:18pt; font-weight:700; color:#334155;">यदि $(x_0, y_0)$ समीकरण $ax + by = k$ का हल है, तो $k$ का मान तुरंत ज्ञात करें:</p>
    <div class="sim-controls-grid">
      <div class="sim-group">
        <label>हल x:</label>
        <input type="number" id="sim4_x" value="2" oninput="calculateSim4()">
      </div>
      <div class="sim-group">
        <label>हल y:</label>
        <input type="number" id="sim4_y" value="1" oninput="calculateSim4()">
      </div>
      <div class="sim-group">
        <label>गुणांक a व b:</label>
        <div style="display:flex; gap:8px;">
          <input type="number" id="sim4_a" value="2" style="width:50%;" oninput="calculateSim4()">
          <input type="number" id="sim4_b" value="3" style="width:50%;" oninput="calculateSim4()">
        </div>
      </div>
    </div>
    <div id="sim4_output" class="sim-output-box"></div>
  </div>

  <!-- Simulator 5 with DARK GRAPH & AXIS NUMBERS -->
  <div class="inline-simulator-card">
    <h3 style="font-size:24pt; font-weight:900; color:#1e3a8a; margin-top:0;">⚡ लाइव सिमुलेटर 5: सरल रेखा आलेखक (Interactive Straight Line Grapher)</h3>
    <p style="font-size:18pt; font-weight:700; color:#334155;">समीकरण $ax + by = c$ भरें और डार्क ग्रिड व अंकित अक्षों पर लाइव रेखा आलेख देखें:</p>
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
        <label>अचर c:</label>
        <input type="number" id="sim5_c" value="4" oninput="calculateSim5()">
      </div>
      <div class="sim-group" style="justify-content:flex-end;">
        <button class="sim-btn-calc" onclick="calculateSim5()">⚡ आलेख अपडेट करें</button>
      </div>
    </div>
    <canvas id="sim5_canvas" class="sim-canvas" width="600" height="380"></canvas>
    <div id="sim5_output" class="sim-output-box"></div>
  </div>

</div><!-- End container #contentToCopy -->

<!-- Projector Control & Simulator Scripts -->
<script>
  // Projector Controller
  var currentWidth = 1350;
  var sizeOffset = 0;
  var weightOffset = 0;
  var strokeOffset = 0;

  function getContainer() {{
    return document.getElementById('contentToCopy') || document.querySelector('.container');
  }}

  function adjustWidth(amount) {{
    currentWidth += amount;
    if (currentWidth < 600) currentWidth = 600;
    if (currentWidth > 3500) currentWidth = 3500;
    var c = getContainer();
    if (c) {{
      c.style.setProperty('width', currentWidth + 'px', 'important');
      c.style.setProperty('max-width', currentWidth + 'px', 'important');
    }}
  }}

  function adjustFontSize(amount) {{
    sizeOffset += amount;
    if (sizeOffset < -16) sizeOffset = -16;
    if (sizeOffset > 30) sizeOffset = 30;
    applyTypography();
  }}

  function adjustFontWeight(amount) {{
    weightOffset += amount;
    if (weightOffset < -300) weightOffset = -300;
    if (weightOffset > 200) weightOffset = 200;
    applyTypography();
  }}

  function applyTypography() {{
    var basePt = 26 + sizeOffset;
    var currentWeight = Math.min(900, Math.max(400, 900 + weightOffset));
    var currentStroke = Math.max(0.4, 0.9 + (weightOffset / 400));

    var el = document.getElementById('dyn-typography');
    if (!el) {{
      el = document.createElement('style');
      el.id = 'dyn-typography';
      document.head.appendChild(el);
    }}
    el.innerHTML =
      'body, .container, p, div, span, li, td, th {{ font-size: ' + basePt + 'pt !important; }}' +
      '.question-heading {{ font-size: ' + (basePt + 4) + 'pt !important; }}' +
      '.answer-highlight {{ font-size: ' + (basePt + 2) + 'pt !important; }}' +
      'body, .container, p, div, span, li, h1, h2, h3, h4, .question-heading, .answer-highlight, ' +
      'strong, b, mjx-container, mjx-math, mjx-c, .MathJax {{ ' +
      'font-weight: ' + currentWeight + ' !important; ' +
      '-webkit-text-stroke: ' + currentStroke + 'px currentColor !important; }}';
  }}

  function copyEntireContent() {{
    var container = getContainer();
    if (!container) return;
    var text = container.innerText || container.textContent;
    navigator.clipboard.writeText(text).then(function() {{
      alert('📋 संपूर्ण अध्याय सफलतापूर्वक कॉपी हो गया है!');
    }}).catch(function() {{
      alert('कॉपी विफल रही, कृपया स्वयं टेक्स्ट का चयन करें।');
    }});
  }}

  // Simulator 1: Standard Form
  function calculateSim1() {{
    var a = parseFloat(document.getElementById('sim1_a').value) || 0;
    var b = parseFloat(document.getElementById('sim1_b').value) || 0;
    var c = parseFloat(document.getElementById('sim1_c').value) || 0;
    var out = document.getElementById('sim1_output');
    var eq = (a !== 0 ? (a + 'x ') : '') + (b >= 0 ? ('+ ' + b + 'y ') : ('- ' + Math.abs(b) + 'y ')) + (c >= 0 ? ('+ ' + c) : ('- ' + Math.abs(c))) + ' = 0';
    out.innerHTML = '<div style="font-size:20pt; font-weight:900; color:#1e3a8a;">' +
      'मानक रूप: $' + eq + '$<br>' +
      'गुणांक: $a = ' + a + '$, $b = ' + b + '$, $c = ' + c + '$</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // Simulator 2: 4 Solutions
  function calculateSim2() {{
    var a = parseFloat(document.getElementById('sim2_a').value) || 0;
    var b = parseFloat(document.getElementById('sim2_b').value) || 0;
    var c = parseFloat(document.getElementById('sim2_c').value) || 0;
    var out = document.getElementById('sim2_output');
    if (b === 0 && a === 0) {{
      out.innerHTML = 'अमान्य समीकरण (a और b दोनों शून्य नहीं हो सकते)।';
      return;
    }}
    var pts = [];
    if (b !== 0) {{
      for (var x = 0; x < 4; x++) {{
        var y = (c - (a * x)) / b;
        var yStr = Number.isInteger(y) ? y : y.toFixed(2);
        pts.push('(' + x + ', ' + yStr + ')');
      }}
    }} else {{
      var xFixed = c / a;
      var xStr = Number.isInteger(xFixed) ? xFixed : xFixed.toFixed(2);
      for (var y = 0; y < 4; y++) pts.push('(' + xStr + ', ' + y + ')');
    }}
    out.innerHTML = '<div style="font-size:20pt; font-weight:900; color:#065f46;">' +
      'चार क्रमिक हल:<br>' + pts.map(function(p) {{ return '$' + p + '$'; }}).join(', ') + '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // Simulator 3: Verifier
  function calculateSim3() {{
    var x = parseFloat(document.getElementById('sim3_x').value) || 0;
    var y = parseFloat(document.getElementById('sim3_y').value) || 0;
    var a = parseFloat(document.getElementById('sim3_a').value) || 0;
    var b = parseFloat(document.getElementById('sim3_b').value) || 0;
    var c = parseFloat(document.getElementById('sim3_c').value) || 0;
    var out = document.getElementById('sim3_output');

    var lhs = (a * x) + (b * y);
    var isSol = Math.abs(lhs - c) < 0.0001;
    out.innerHTML = '<div style="font-size:20pt; font-weight:900; color:' + (isSol ? '#15803d' : '#b91c1c') + ';">' +
      'L.H.S. = $' + a + '(' + x + ') + (' + b + ')(' + y + ') = ' + lhs + '$<br>' +
      'R.H.S. = $' + c + '$<br>' +
      (isSol ? '✅ बिंदु $(' + x + ', ' + y + ')$ इस समीकरण का एक हल है!' : '❌ बिंदु $(' + x + ', ' + y + ')$ इस समीकरण का हल नहीं है।') +
      '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // Simulator 4: Find k
  function calculateSim4() {{
    var x = parseFloat(document.getElementById('sim4_x').value) || 0;
    var y = parseFloat(document.getElementById('sim4_y').value) || 0;
    var a = parseFloat(document.getElementById('sim4_a').value) || 0;
    var b = parseFloat(document.getElementById('sim4_b').value) || 0;
    var out = document.getElementById('sim4_output');

    var k = (a * x) + (b * y);
    out.innerHTML = '<div style="font-size:22pt; font-weight:900; color:#1e3a8a;">' +
      'मानक गणना: $k = ' + a + '(' + x + ') + ' + b + '(' + y + ') = ' + k + '$<br>' +
      '✅ अभीष्ट मान: $k = ' + k + '$</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // Simulator 5: Canvas Straight Line with DARK GRID & AXIS NUMBERS
  function calculateSim5() {{
    var a = parseFloat(document.getElementById('sim5_a').value) || 1;
    var b = parseFloat(document.getElementById('sim5_b').value) || 1;
    var c = parseFloat(document.getElementById('sim5_c').value) || 4;
    var out = document.getElementById('sim5_output');

    var canvas = document.getElementById('sim5_canvas');
    if (canvas) {{
      var ctx = canvas.getContext('2d');
      var W = canvas.width;
      var H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      var ox = W / 2;
      var oy = H / 2;
      var scale = 26;

      // 1. Dark Visible Grid Lines
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 1.2;
      for (var gx = 0; gx <= W; gx += scale) {{
        ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, H); ctx.stroke();
      }}
      for (var gy = 0; gy <= H; gy += scale) {{
        ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
      }}

      // 2. Solid Black Axes
      ctx.strokeStyle = '#000000';
      ctx.lineWidth = 4;
      ctx.beginPath(); ctx.moveTo(5, oy); ctx.lineTo(W - 5, oy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ox, 5); ctx.lineTo(ox, H - 5); ctx.stroke();

      // 3. Numbers on X and Y Axes
      ctx.fillStyle = '#000000';
      ctx.font = 'bold 13px system-ui, -apple-system, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'top';

      // X Numbers
      for (var xi = -11; xi <= 11; xi++) {{
        if (xi === 0) continue;
        var px = ox + xi * scale;
        if (px > 15 && px < W - 15) {{
          ctx.beginPath(); ctx.moveTo(px, oy - 4); ctx.lineTo(px, oy + 4); ctx.stroke();
          ctx.fillText(xi, px, oy + 5);
        }}
      }}

      // Y Numbers
      ctx.textAlign = 'right';
      ctx.textBaseline = 'middle';
      for (var yi = -7; yi <= 7; yi++) {{
        if (yi === 0) continue;
        var py = oy - yi * scale;
        if (py > 15 && py < H - 15) {{
          ctx.beginPath(); ctx.moveTo(ox - 4, py); ctx.lineTo(ox + 4, py); ctx.stroke();
          ctx.fillText(yi, ox - 6, py);
        }}
      }}

      // Origin 'O'
      ctx.textAlign = 'right';
      ctx.textBaseline = 'top';
      ctx.fillText('0', ox - 4, oy + 4);

      // Axis names X, Y
      ctx.font = 'bold 16px system-ui, -apple-system, sans-serif';
      ctx.fillText('X', W - 10, oy - 20);
      ctx.fillText('Y', ox + 18, 10);

      // 4. Draw Line ax + by = c
      ctx.strokeStyle = '#2563eb';
      ctx.lineWidth = 4.5;
      if (b !== 0) {{
        var xLeft = -12;
        var yLeft = (c - (a * xLeft)) / b;
        var px1 = ox + (xLeft * scale);
        var py1 = oy - (yLeft * scale);

        var xRight = 12;
        var yRight = (c - (a * xRight)) / b;
        var px2 = ox + (xRight * scale);
        var py2 = oy - (yRight * scale);

        ctx.beginPath(); ctx.moveTo(px1, py1); ctx.lineTo(px2, py2); ctx.stroke();

        // Plot 2 sample points
        [0, 2].forEach(function(xp) {{
          var yp = (c - (a * xp)) / b;
          var pxx = ox + (xp * scale);
          var pyy = oy - (yp * scale);
          ctx.fillStyle = '#dc2626';
          ctx.beginPath(); ctx.arc(pxx, pyy, 6, 0, Math.PI * 2); ctx.fill();
          ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 2; ctx.stroke();
        }});
      }} else if (a !== 0) {{
        var xFixed = c / a;
        var pxx = ox + (xFixed * scale);
        ctx.beginPath(); ctx.moveTo(pxx, 0); ctx.lineTo(pxx, H); ctx.stroke();
      }}
    }}

    var eqStr = a + 'x + (' + b + ')y = ' + c;
    out.innerHTML = '<div style="font-size:20pt; font-weight:900; color:#1e3a8a;">' +
      'आलेख समीकरण: $' + eqStr + '$<br>' +
      'सरल रेखा डार्क ग्रिड और अंकीय अक्षों पर सफलतापूर्वक आलेखित की गई है।</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // Auto initialize on load
  window.addEventListener('load', function() {{
    calculateSim1();
    calculateSim2();
    calculateSim3();
    calculateSim4();
    calculateSim5();
  }});
</script>

</body>
</html>
"""

with open('qa_master_math9_4.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("qa_master_math9_4.html generated successfully with Chapter 2 master template, dark SVG graphs, and numbered canvas axes!")
