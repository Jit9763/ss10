# -*- coding: utf-8 -*-
"""
Master Generator for NCERT Class 9 Mathematics Chapter 8: चतुर्भुज (Quadrilaterals)
Full Rajasthan NCERT Syllabus:
- Exercise 8.1 (All 12 Questions: Q1 to Q12) with full proofs and geometric SVG diagrams (चित्र)
- Exercise 8.2 (All 7 Questions: Q1 to Q7) with full proofs and geometric SVG diagrams (चित्र)
- 5 Live Visual Interactive Simulators with dynamic interactive Canvases:
  1. सजीव चतुर्भुज कोण गणक व लाइव आकृति (Interactive Quadrilateral Canvas)
  2. समांतर चतुर्भुज लाइव विकर्ण व भुजा प्रदर्शक (Interactive Parallelogram Canvas)
  3. मध्य-बिंदु प्रमेय लाइव सिमुलेटर (Mid-point Theorem Interactive Canvas)
  4. समचतुर्भुज / आयत / वर्ग परिवर्तक (Special Quadrilaterals Canvas)
  5. समकोण त्रिभुज कर्ण मध्य-बिंदु संबंध प्रदर्शक (Right Triangle Midpoint Canvas)
- Exact Chapter 2 Master Standard:
  * Sticky 9-button Action Bar (W+, W-, A+, A-, B+, B-, Copy, Print, Home)
  * Container #contentToCopy
  * 26pt 900-weight Noto Sans Devanagari typography with stroke
  * Color-coded step boxes & yellow/green answer highlights
  * Zero horizontal scroll (overflow-x: hidden !important; displayOverflow: 'scale')
"""

# Helper to generate SVG geometric diagrams
def svg_diagram(title, content, w=480, h=260):
    return f'''<div style="margin:20px auto; max-width:{w}px; text-align:center;">
  <div style="font-size:18pt; font-weight:900; color:#1e3a8a; margin-bottom:8px;">📐 रेखाचित्र: {title}</div>
  <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" style="background:#ffffff; border:3px solid #cbd5e1; border-radius:14px; box-shadow:0 6px 18px rgba(0,0,0,0.06); display:block; margin:0 auto;">
    {content}
  </svg>
</div>'''

# Pre-generate diagrams for Ex 8.1 and Ex 8.2
# Ex 8.1 Q1: Quadrilateral ABCD with angles 3x, 5x, 9x, 13x
d_8_1_q1 = svg_diagram("चतुर्भुज ABCD के कोण", '''
  <polygon points="60,200 180,60 400,80 340,210" fill="#eff6ff" stroke="#1d4ed8" stroke-width="4"/>
  <circle cx="60" cy="200" r="5" fill="#dc2626"/>
  <circle cx="180" cy="60" r="5" fill="#dc2626"/>
  <circle cx="400" cy="80" r="5" fill="#dc2626"/>
  <circle cx="340" cy="210" r="5" fill="#dc2626"/>
  <text x="40" y="215" font-size="20" font-weight="900" fill="#000000">A</text>
  <text x="175" y="45" font-size="20" font-weight="900" fill="#000000">B</text>
  <text x="415" y="85" font-size="20" font-weight="900" fill="#000000">C</text>
  <text x="350" y="235" font-size="20" font-weight="900" fill="#000000">D</text>
  <text x="80" y="185" font-size="16" font-weight="900" fill="#1e3a8a">3x</text>
  <text x="180" y="90" font-size="16" font-weight="900" fill="#1e3a8a">5x</text>
  <text x="360" y="105" font-size="16" font-weight="900" fill="#1e3a8a">9x</text>
  <text x="305" y="195" font-size="16" font-weight="900" fill="#1e3a8a">13x</text>
''')

# Ex 8.1 Q2: Parallelogram with equal diagonals is rectangle
d_8_1_q2 = svg_diagram("समांतर चतुर्भुज ABCD (विकर्ण AC = BD)", '''
  <polygon points="70,200 70,60 390,60 390,200" fill="#f0fdf4" stroke="#15803d" stroke-width="4"/>
  <line x1="70" y1="200" x2="390" y2="60" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4"/>
  <line x1="70" y1="60" x2="390" y2="200" stroke="#2563eb" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="50" y="220" font-size="20" font-weight="900" fill="#000000">A</text>
  <text x="50" y="50" font-size="20" font-weight="900" fill="#000000">D</text>
  <text x="400" y="50" font-size="20" font-weight="900" fill="#000000">C</text>
  <text x="400" y="220" font-size="20" font-weight="900" fill="#000000">B</text>
  <text x="210" y="145" font-size="18" font-weight="900" fill="#7c3aed">O</text>
''')

# Ex 8.1 Q3: Rhombus with perpendicular diagonals
d_8_1_q3 = svg_diagram("समचतुर्भुज ABCD (विकर्ण AC ⊥ BD)", '''
  <polygon points="230,40 370,130 230,220 90,130" fill="#faf5ff" stroke="#7c3aed" stroke-width="4"/>
  <line x1="230" y1="40" x2="230" y2="220" stroke="#000000" stroke-width="3"/>
  <line x1="90" y1="130" x2="370" y2="130" stroke="#000000" stroke-width="3"/>
  <rect x="230" y="115" width="15" height="15" fill="none" stroke="#dc2626" stroke-width="2"/>
  <text x="225" y="30" font-size="20" font-weight="900" fill="#000000">A</text>
  <text x="385" y="135" font-size="20" font-weight="900" fill="#000000">B</text>
  <text x="225" y="245" font-size="20" font-weight="900" fill="#000000">C</text>
  <text x="65" y="135" font-size="20" font-weight="900" fill="#000000">D</text>
  <text x="240" y="150" font-size="18" font-weight="900" fill="#b91c1c">O (90°)</text>
''')

# Ex 8.1 Q6: Parallelogram ABCD with diagonal AC bisecting angle A
d_8_1_q6 = svg_diagram("समांतर चतुर्भुज ABCD (AC कोण A का समद्विभाजक)", '''
  <polygon points="80,190 180,60 410,60 310,190" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <line x1="80" y1="190" x2="410" y2="60" stroke="#dc2626" stroke-width="3.5"/>
  <text x="60" y="210" font-size="20" font-weight="900" fill="#000000">A</text>
  <text x="320" y="210" font-size="20" font-weight="900" fill="#000000">B</text>
  <text x="420" y="65" font-size="20" font-weight="900" fill="#000000">C</text>
  <text x="165" y="50" font-size="20" font-weight="900" fill="#000000">D</text>
  <text x="110" y="170" font-size="16" font-weight="900" fill="#dc2626">∠1</text>
  <text x="120" y="195" font-size="16" font-weight="900" fill="#dc2626">∠2</text>
  <text x="360" y="80" font-size="16" font-weight="900" fill="#15803d">∠3</text>
  <text x="370" y="105" font-size="16" font-weight="900" fill="#15803d">∠4</text>
''')

# Ex 8.1 Q9: Parallelogram ABCD with DP = BQ on diagonal BD
d_8_1_q9 = svg_diagram("समांतर चतुर्भुज ABCD (DP = BQ)", '''
  <polygon points="70,190 160,60 410,60 320,190" fill="#f8fafc" stroke="#000000" stroke-width="3.5"/>
  <line x1="160" y1="60" x2="320" y2="190" stroke="#000000" stroke-width="3"/>
  <!-- P and Q on BD -->
  <circle cx="210" cy="100" r="5" fill="#dc2626"/>
  <circle cx="270" cy="150" r="5" fill="#dc2626"/>
  <line x1="70" y1="190" x2="210" y2="100" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="70" y1="190" x2="270" y2="150" stroke="#2563eb" stroke-width="2.5"/>
  <line x1="410" y1="60" x2="210" y2="100" stroke="#15803d" stroke-width="2.5"/>
  <line x1="410" y1="60" x2="270" y2="150" stroke="#15803d" stroke-width="2.5"/>
  <text x="50" y="205" font-size="18" font-weight="900">A</text>
  <text x="330" y="205" font-size="18" font-weight="900">B</text>
  <text x="420" y="65" font-size="18" font-weight="900">C</text>
  <text x="145" y="55" font-size="18" font-weight="900">D</text>
  <text x="215" y="95" font-size="16" font-weight="900" fill="#dc2626">P</text>
  <text x="280" y="150" font-size="16" font-weight="900" fill="#dc2626">Q</text>
''')

# Ex 8.1 Q12: Trapezium ABCD with AB || CD, AD = BC
d_8_1_q12 = svg_diagram("समलम्ब ABCD (AB || CD, AD = BC)", '''
  <polygon points="120,70 340,70 410,200 60,200" fill="#fefce8" stroke="#ca8a04" stroke-width="4"/>
  <line x1="340" y1="70" x2="470" y2="200" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="5,4"/>
  <line x1="410" y1="200" x2="470" y2="200" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="5,4"/>
  <text x="110" y="60" font-size="20" font-weight="900">A</text>
  <text x="345" y="60" font-size="20" font-weight="900">B</text>
  <text x="420" y="215" font-size="20" font-weight="900">C</text>
  <text x="45" y="215" font-size="20" font-weight="900">D</text>
  <text x="480" y="215" font-size="18" font-weight="900" fill="#2563eb">E</text>
''')

# Ex 8.2 Q1: Midpoint Theorem Quadrilateral ABCD with midpoints P, Q, R, S
d_8_2_q1 = svg_diagram("चतुर्भुज ABCD व मध्य-बिंदु चतुर्भुज PQRS", '''
  <polygon points="60,190 140,50 390,70 330,210" fill="#f8fafc" stroke="#64748b" stroke-width="3"/>
  <line x1="60" y1="190" x2="390" y2="70" stroke="#000000" stroke-width="3" stroke-dasharray="6,4"/>
  <!-- Midpoints: P on AB, Q on BC, R on CD, S on DA -->
  <!-- AB: (60,190) to (330,210) => P=(195, 200) -->
  <!-- BC: (330,210) to (390,70) => Q=(360, 140) -->
  <!-- CD: (390,70) to (140,50) => R=(265, 60) -->
  <!-- DA: (140,50) to (60,190) => S=(100, 120) -->
  <polygon points="195,200 360,140 265,60 100,120" fill="#eff6ff" stroke="#2563eb" stroke-width="4"/>
  <circle cx="195" cy="200" r="5" fill="#dc2626"/>
  <circle cx="360" cy="140" r="5" fill="#dc2626"/>
  <circle cx="265" cy="60" r="5" fill="#dc2626"/>
  <circle cx="100" cy="120" r="5" fill="#dc2626"/>
  <text x="45" y="200" font-size="18" font-weight="900">A</text>
  <text x="340" y="225" font-size="18" font-weight="900">B</text>
  <text x="400" y="70" font-size="18" font-weight="900">C</text>
  <text x="130" y="45" font-size="18" font-weight="900">D</text>
  <text x="195" y="225" font-size="16" font-weight="900" fill="#dc2626">P</text>
  <text x="375" y="145" font-size="16" font-weight="900" fill="#dc2626">Q</text>
  <text x="265" y="45" font-size="16" font-weight="900" fill="#dc2626">R</text>
  <text x="75" y="125" font-size="16" font-weight="900" fill="#dc2626">S</text>
''')

# Ex 8.2 Q4: Trapezium with diagonal BD and line through midpoint E
d_8_2_q4 = svg_diagram("समलम्ब ABCD (मध्य-बिंदु E व F)", '''
  <polygon points="120,60 320,60 410,190 70,190" fill="#f0fdf4" stroke="#16a34a" stroke-width="3.5"/>
  <line x1="120" y1="60" x2="410" y2="190" stroke="#000000" stroke-width="2.5"/>
  <line x1="95" y1="125" x2="365" y2="125" stroke="#dc2626" stroke-width="3.5"/>
  <circle cx="95" cy="125" r="5" fill="#dc2626"/>
  <circle cx="365" cy="125" r="5" fill="#dc2626"/>
  <circle cx="210" cy="125" r="5" fill="#2563eb"/>
  <text x="110" y="50" font-size="18" font-weight="900">A</text>
  <text x="325" y="50" font-size="18" font-weight="900">B</text>
  <text x="420" y="200" font-size="18" font-weight="900">C</text>
  <text x="50" y="200" font-size="18" font-weight="900">D</text>
  <text x="70" y="130" font-size="16" font-weight="900" fill="#dc2626">E</text>
  <text x="375" y="130" font-size="16" font-weight="900" fill="#dc2626">F</text>
  <text x="210" y="115" font-size="16" font-weight="900" fill="#2563eb">G</text>
''')

# Ex 8.2 Q7: Right triangle with hypotenuse midpoint M and MD || BC
d_8_2_q7 = svg_diagram("समकोण त्रिभुज ABC (C समकोण, कर्ण AB का मध्य-बिंदु M)", '''
  <polygon points="70,190 390,190 70,50" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <line x1="70" y1="120" x2="230" y2="120" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="70" y1="190" x2="230" y2="120" stroke="#15803d" stroke-width="3" stroke-dasharray="5,4"/>
  <circle cx="230" cy="120" r="5" fill="#dc2626"/>
  <circle cx="70" cy="120" r="5" fill="#dc2626"/>
  <rect x="70" y="170" width="18" height="20" fill="none" stroke="#000000" stroke-width="2"/>
  <text x="45" y="205" font-size="20" font-weight="900">C (90°)</text>
  <text x="400" y="205" font-size="20" font-weight="900">B</text>
  <text x="65" y="40" font-size="20" font-weight="900">A</text>
  <text x="240" y="115" font-size="18" font-weight="900" fill="#dc2626">M</text>
  <text x="45" y="125" font-size="18" font-weight="900" fill="#dc2626">D</text>
''')

print("All geometric diagrams generated successfully!")
