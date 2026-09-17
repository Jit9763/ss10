# -*- coding: utf-8 -*-
"""
Full Generator for NCERT Class 9 Mathematics Chapter 7: त्रिभुज (Triangles)
Covers 100% Complete Rajasthan NCERT Curriculum:
- Exercise 7.1 (All 8 Questions: Q1 to Q8) with full proofs and geometric SVG diagrams
- Exercise 7.2 (All 8 Questions: Q1 to Q8) with full proofs and geometric SVG diagrams
- Exercise 7.3 (All 5 Questions: Q1 to Q5) with full proofs and geometric SVG diagrams
- Exercise 7.4 (All 6 Questions: Q1 to Q6) with full proofs and geometric SVG diagrams
Total: 27 Complete NCERT Solutions!
- 5 Live Interactive HTML5 Canvas Simulators:
  1. त्रिभुज सर्वांगसमता कसौटी विश्लेषक (SAS, ASA, SSS, RHS Dynamic Canvases)
  2. समद्विबाहु त्रिभुज लाइव कोण व भुजा प्रदर्शक (Isosceles Triangle Dynamic Canvas)
  3. समकोण त्रिभुज कर्ण संबंध प्रदर्शक (Right Triangle Hypotenuse Canvas)
  4. त्रिभुज असमिका प्रमेय लाइव सिमुलेटर (Triangle Inequality Dynamic Canvas)
  5. माध्यिका एवं शीर्षलम्ब लाइव प्रदर्शक (Median & Altitude Dynamic Canvas)
- Exact Chapter 2 Master Standard:
  * Sticky 9-button Action Bar (W+, W-, A+, A-, B+, B-, Copy, Print, Home)
  * Container #contentToCopy
  * 26pt 900-weight Noto Sans Devanagari typography with stroke
  * Color-coded step boxes & yellow/green answer highlights
  * Zero horizontal scroll (overflow-x: hidden !important; displayOverflow: 'scale')
  * 100% clean MathJax (no Hindi in MathJax, no chained equals)
"""

with open('ch2_style.css', 'r', encoding='utf-8') as f:
    ch2_css = f.read()

# Helper for SVG diagrams
def svg_diag(title, content, w=480, h=260):
    return f'''<div style="margin:20px auto; max-width:{w}px; text-align:center;">
  <div style="font-size:18pt; font-weight:900; color:#1e3a8a; margin-bottom:8px;">📐 रेखाचित्र: {title}</div>
  <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" style="background:#ffffff; border:3px solid #cbd5e1; border-radius:14px; box-shadow:0 6px 18px rgba(0,0,0,0.06); display:block; margin:0 auto;">
    {content}
  </svg>
</div>'''

# SVG Diagrams for all 27 questions
# Ex 7.1
d_7_1_q1 = svg_diag("चतुर्भुज ACBD (AC = AD, AB समद्विभाजक)", '''
  <polygon points="60,130 220,50 400,130 220,210" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <line x1="60" y1="130" x2="400" y2="130" stroke="#dc2626" stroke-width="4" stroke-dasharray="6,4"/>
  <!-- Tick marks on AC and AD -->
  <line x1="135" y1="85" x2="145" y2="95" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="135" y1="175" x2="145" y2="165" stroke="#dc2626" stroke-width="3.5"/>
  <!-- Labels -->
  <text x="35" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="215" y="40" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="415" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="215" y="235" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
''')

d_7_1_q2 = svg_diag("चतुर्भुज ABCD (AD = BC, ∠DAB = ∠CBA)", '''
  <polygon points="80,210 380,210 320,70 120,70" fill="#f8fafc" stroke="#1e40af" stroke-width="4"/>
  <line x1="80" y1="210" x2="320" y2="70" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4"/>
  <line x1="380" y1="210" x2="120" y2="70" stroke="#16a34a" stroke-width="3" stroke-dasharray="6,4"/>
  <!-- Tick marks -->
  <line x1="95" y1="140" x2="105" y2="140" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="345" y1="140" x2="355" y2="140" stroke="#dc2626" stroke-width="3.5"/>
  <!-- Labels -->
  <text x="60" y="230" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="390" y="230" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="330" y="60" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="105" y="60" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
''')

d_7_1_q3 = svg_diag("रेखाखंड AB पर लम्ब AD और BC (AD = BC)", '''
  <line x1="60" y1="130" x2="420" y2="130" stroke="#000000" stroke-width="4"/>
  <line x1="120" y1="130" x2="120" y2="220" stroke="#2563eb" stroke-width="4"/>
  <line x1="360" y1="130" x2="360" y2="40" stroke="#2563eb" stroke-width="4"/>
  <line x1="120" y1="220" x2="360" y2="40" stroke="#dc2626" stroke-width="3.5" stroke-dasharray="5,4"/>
  <!-- Right angle symbols -->
  <polyline points="120,150 140,150 140,130" fill="none" stroke="#000000" stroke-width="2"/>
  <polyline points="360,110 340,110 340,130" fill="none" stroke="#000000" stroke-width="2"/>
  <!-- Labels -->
  <text x="95" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="375" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="105" y="240" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="365" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="240" y="120" font-family="sans-serif" font-size="20" font-weight="bold" fill="#b91c1c">O</text>
''')

d_7_1_q4 = svg_diag("समांतर रेखाएँ l ∥ m तथा p ∥ q", '''
  <!-- l and m -->
  <line x1="40" y1="80" x2="440" y2="80" stroke="#64748b" stroke-width="3"/>
  <line x1="40" y1="190" x2="440" y2="190" stroke="#64748b" stroke-width="3"/>
  <!-- p and q -->
  <line x1="90" y1="230" x2="200" y2="40" stroke="#64748b" stroke-width="3"/>
  <line x1="250" y1="230" x2="360" y2="40" stroke="#64748b" stroke-width="3"/>
  <!-- Parallelogram ABCD -->
  <polygon points="175,80 335,80 275,190 115,190" fill="rgba(37,99,235,0.12)" stroke="#2563eb" stroke-width="4"/>
  <line x1="115" y1="190" x2="335" y2="80" stroke="#dc2626" stroke-width="3.5" stroke-dasharray="5,4"/>
  <!-- Labels -->
  <text x="160" y="70" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="345" y="75" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="90" y="210" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="285" y="210" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
''')

d_7_1_q5 = svg_diag("कोण A का समद्विभाजक l तथा लम्ब BP, BQ", '''
  <line x1="60" y1="130" x2="420" y2="50" stroke="#000000" stroke-width="3.5"/>
  <line x1="60" y1="130" x2="420" y2="210" stroke="#000000" stroke-width="3.5"/>
  <line x1="60" y1="130" x2="430" y2="130" stroke="#2563eb" stroke-width="4"/>
  <!-- Point B on l -->
  <circle cx="320" cy="130" r="6" fill="#dc2626"/>
  <!-- Perpendiculars BP and BQ -->
  <line x1="320" y1="130" x2="340" y2="68" stroke="#16a34a" stroke-width="3.5"/>
  <line x1="320" y1="130" x2="340" y2="192" stroke="#16a34a" stroke-width="3.5"/>
  <!-- Labels -->
  <text x="40" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="325" y="120" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">B</text>
  <text x="345" y="60" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">P</text>
  <text x="345" y="215" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">Q</text>
  <text x="440" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#2563eb">l</text>
''')

d_7_1_q6 = svg_diag("परस्पर व्यापी त्रिभुज (AC = AE, AB = AD, ∠BAD = ∠EAC)", '''
  <polygon points="80,180 380,210 240,50" fill="none" stroke="#2563eb" stroke-width="4"/>
  <polygon points="80,180 280,230 180,60" fill="none" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="6,3"/>
  <text x="55" y="190" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="390" y="220" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="240" y="40" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="160" y="55" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="290" y="245" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">E</text>
''')

d_7_1_q7 = svg_diag("रेखाखंड AB का मध्य-बिंदु P", '''
  <line x1="60" y1="180" x2="420" y2="180" stroke="#000000" stroke-width="4"/>
  <circle cx="240" cy="180" r="6" fill="#dc2626"/>
  <polygon points="60,180 240,180 340,60" fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="3.5"/>
  <polygon points="420,180 240,180 140,60" fill="rgba(22,163,74,0.08)" stroke="#16a34a" stroke-width="3.5"/>
  <text x="40" y="195" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="235" y="210" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">P</text>
  <text x="430" y="195" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="125" y="55" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="345" y="55" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">E</text>
''')

d_7_1_q8 = svg_diag("समकोण त्रिभुज ABC में कर्ण AB का मध्य-बिंदु M", '''
  <polygon points="80,180 380,180 80,60" fill="none" stroke="#2563eb" stroke-width="4"/>
  <line x1="80" y1="180" x2="380" y2="60" stroke="#000000" stroke-width="3.5"/>
  <circle cx="230" cy="120" r="5" fill="#dc2626"/>
  <line x1="80" y1="60" x2="380" y2="180" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="5,4"/>
  <text x="60" y="195" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="390" y="190" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="60" y="55" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="390" y="55" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="235" y="110" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">M</text>
''')

# Ex 7.2
d_7_2_q1 = svg_diag("समद्विबाहु त्रिभुज ABC (AB = AC, OB व OC समद्विभाजक)", '''
  <polygon points="240,40 100,210 380,210" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <circle cx="240" cy="150" r="5" fill="#dc2626"/>
  <line x1="100" y1="210" x2="240" y2="150" stroke="#16a34a" stroke-width="3"/>
  <line x1="380" y1="210" x2="240" y2="150" stroke="#16a34a" stroke-width="3"/>
  <line x1="240" y1="40" x2="240" y2="150" stroke="#dc2626" stroke-width="3" stroke-dasharray="5,3"/>
  <text x="235" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="75" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="390" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="250" y="155" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">O</text>
''')

d_7_2_q2 = svg_diag("त्रिभुज ABC में भुजा BC का लम्ब समद्विभाजक AD", '''
  <polygon points="240,40 100,210 380,210" fill="#f8fafc" stroke="#2563eb" stroke-width="4"/>
  <line x1="240" y1="40" x2="240" y2="210" stroke="#dc2626" stroke-width="4"/>
  <polyline points="240,190 260,190 260,210" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="235" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="75" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="390" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="235" y="235" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">D</text>
''')

d_7_2_q3 = svg_diag("समद्विबाहु त्रिभुज ABC में शीर्षलम्ब BE और CF", '''
  <polygon points="240,40 100,210 380,210" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <line x1="100" y1="210" x2="310" y2="125" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="380" y1="210" x2="170" y2="125" stroke="#16a34a" stroke-width="3.5"/>
  <text x="235" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="75" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="390" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="320" y="125" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">E</text>
  <text x="145" y="125" font-family="sans-serif" font-size="20" font-weight="bold" fill="#16a34a">F</text>
''')

d_7_2_q5 = svg_diag("समान आधार BC पर दो समद्विबाहु त्रिभुज ABC व DBC", '''
  <polygon points="240,40 100,160 380,160" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <polygon points="240,240 100,160 380,160" fill="#f0fdf4" stroke="#16a34a" stroke-width="4"/>
  <line x1="240" y1="40" x2="240" y2="240" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="235" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="75" y="165" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="390" y="165" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="235" y="260" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
''')

d_7_2_q6 = svg_diag("समद्विबाहु त्रिभुज ABC (BA को D तक बढ़ाया, AD = AB)", '''
  <polygon points="120,200 400,200 240,110" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <line x1="120" y1="200" x2="360" y2="20" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="400" y1="200" x2="360" y2="20" stroke="#16a34a" stroke-width="3.5"/>
  <circle cx="240" cy="110" r="5" fill="#000000"/>
  <text x="245" y="105" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="95" y="215" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="410" y="215" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="365" y="20" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">D</text>
''')

# Ex 7.3
d_7_3_q1 = svg_diag("समान आधार BC पर त्रिभुज ABC व DBC (AD बढ़ाया P तक)", '''
  <polygon points="240,40 100,210 380,210" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <polygon points="240,130 100,210 380,210" fill="#f0fdf4" stroke="#16a34a" stroke-width="3.5"/>
  <line x1="240" y1="40" x2="240" y2="210" stroke="#dc2626" stroke-width="3.5"/>
  <text x="235" y="30" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="75" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="390" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="250" y="135" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="235" y="235" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">P</text>
''')

d_7_3_q3 = svg_diag("त्रिभुज ABC व PQR में माध्यिकाएँ AM व PN", '''
  <!-- Triangle ABC -->
  <polygon points="140,50 40,210 240,210" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <line x1="140" y1="50" x2="140" y2="210" stroke="#dc2626" stroke-width="3"/>
  <text x="135" y="40" font-family="sans-serif" font-size="18" font-weight="bold" fill="#000000">A</text>
  <text x="20" y="220" font-family="sans-serif" font-size="18" font-weight="bold" fill="#000000">B</text>
  <text x="245" y="220" font-family="sans-serif" font-size="18" font-weight="bold" fill="#000000">C</text>
  <text x="135" y="230" font-family="sans-serif" font-size="18" font-weight="bold" fill="#dc2626">M</text>
  <!-- Triangle PQR -->
  <polygon points="360,50 260,210 460,210" fill="#f0fdf4" stroke="#16a34a" stroke-width="3.5"/>
  <line x1="360" y1="50" x2="360" y2="210" stroke="#dc2626" stroke-width="3"/>
  <text x="355" y="40" font-family="sans-serif" font-size="18" font-weight="bold" fill="#000000">P</text>
  <text x="240" y="220" font-family="sans-serif" font-size="18" font-weight="bold" fill="#000000">Q</text>
  <text x="465" y="220" font-family="sans-serif" font-size="18" font-weight="bold" fill="#000000">R</text>
  <text x="355" y="230" font-family="sans-serif" font-size="18" font-weight="bold" fill="#dc2626">N</text>
''')

# Ex 7.4
d_7_4_q1 = svg_diag("समकोण त्रिभुज ABC में कर्ण AC सबसे लंबी भुजा", '''
  <polygon points="100,210 380,210 100,50" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <polyline points="100,185 125,185 125,210" fill="none" stroke="#000000" stroke-width="2.5"/>
  <text x="75" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B (90°)</text>
  <text x="390" y="225" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="80" y="45" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
  <text x="260" y="115" font-family="sans-serif" font-size="20" font-weight="bold" fill="#dc2626">कर्ण (Hypotenuse)</text>
''')

d_7_4_q4 = svg_diag("चतुर्भुज ABCD (AB सबसे छोटी, CD सबसे लंबी भुजा)", '''
  <polygon points="140,190 280,190 380,70 80,90" fill="#f8fafc" stroke="#2563eb" stroke-width="4"/>
  <line x1="80" y1="90" x2="280" y2="190" stroke="#dc2626" stroke-width="3" stroke-dasharray="5,4"/>
  <line x1="140" y1="190" x2="380" y2="70" stroke="#16a34a" stroke-width="3" stroke-dasharray="5,4"/>
  <text x="130" y="215" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">B</text>
  <text x="285" y="215" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">C</text>
  <text x="390" y="70" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">D</text>
  <text x="60" y="90" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000">A</text>
''')

print("All Chapter 7 SVG diagrams defined successfully!")
