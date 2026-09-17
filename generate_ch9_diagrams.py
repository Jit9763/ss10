# -*- coding: utf-8 -*-
"""
Helper to add high-contrast geometric SVG diagrams (रेखाचित्र / चित्र) to Chapter 9: वृत्त (Circles)
"""

def circle_svg(title, content, w=480, h=260):
    return f'''<div style="margin:20px auto; max-width:{w}px; text-align:center;">
  <div style="font-size:18pt; font-weight:900; color:#1e3a8a; margin-bottom:8px;">📐 रेखाचित्र: {title}</div>
  <svg width="100%" height="{h}" viewBox="0 0 {w} {h}" style="background:#ffffff; border:3px solid #cbd5e1; border-radius:14px; box-shadow:0 6px 18px rgba(0,0,0,0.06); display:block; margin:0 auto;">
    {content}
  </svg>
</div>'''

# Diagram 1: Ex 9.1 Q1 (Two congruent circles)
d_9_1_q1 = circle_svg("सर्वांगसम वृत्तों की बराबर जीवाएँ व केंद्र कोण", '''
  <!-- Circle 1 -->
  <circle cx="130" cy="130" r="85" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <circle cx="130" cy="130" r="4" fill="#000000"/>
  <polygon points="130,130 65,175 195,175" fill="rgba(37,99,235,0.15)" stroke="#1d4ed8" stroke-width="3"/>
  <text x="125" y="120" font-size="16" font-weight="bold" fill="#000000">O</text>
  <text x="45" y="190" font-size="16" font-weight="bold" fill="#000000">A</text>
  <text x="200" y="190" font-size="16" font-weight="bold" fill="#000000">B</text>
  <!-- Circle 2 -->
  <circle cx="350" cy="130" r="85" fill="#f0fdf4" stroke="#16a34a" stroke-width="3.5"/>
  <circle cx="350" cy="130" r="4" fill="#000000"/>
  <polygon points="350,130 285,175 415,175" fill="rgba(22,163,74,0.15)" stroke="#15803d" stroke-width="3"/>
  <text x="345" y="120" font-size="16" font-weight="bold" fill="#000000">O'</text>
  <text x="265" y="190" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="420" y="190" font-size="16" font-weight="bold" fill="#000000">D</text>
''')

# Diagram 2: Ex 9.2 Q1 (Intersecting circles with common chord)
d_9_2_q1 = circle_svg("प्रतिच्छेदी वृत्त (5 सेमी व 3 सेमी) व उभयनिष्ठ जीवा AB", '''
  <circle cx="200" cy="130" r="95" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="3.5"/>
  <circle cx="280" cy="130" r="60" fill="rgba(22,163,74,0.06)" stroke="#16a34a" stroke-width="3.5"/>
  <line x1="280" y1="70" x2="280" y2="190" stroke="#dc2626" stroke-width="4"/>
  <line x1="200" y1="130" x2="280" y2="130" stroke="#000000" stroke-width="3"/>
  <circle cx="200" cy="130" r="4" fill="#000000"/>
  <circle cx="280" cy="130" r="4" fill="#000000"/>
  <text x="180" y="145" font-size="16" font-weight="bold" fill="#000000">O (5cm)</text>
  <text x="290" y="145" font-size="16" font-weight="bold" fill="#000000">O' (3cm)</text>
  <text x="275" y="60" font-size="18" font-weight="bold" fill="#dc2626">A</text>
  <text x="275" y="210" font-size="18" font-weight="bold" fill="#dc2626">B</text>
  <text x="285" y="125" font-size="14" font-weight="bold" fill="#b91c1c">उभयनिष्ठ जीवा = 6 सेमी</text>
''', h=270)

# Diagram 3: Ex 9.2 Q2 (Two equal intersecting chords)
d_9_2_q2 = circle_svg("वृत्त की दो बराबर प्रतिच्छेदी जीवाएँ AB व CD", '''
  <circle cx="240" cy="130" r="100" fill="#f8fafc" stroke="#2563eb" stroke-width="3.5"/>
  <line x1="150" y1="80" x2="330" y2="180" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="150" y1="180" x2="330" y2="80" stroke="#16a34a" stroke-width="3.5"/>
  <circle cx="240" cy="130" r="4" fill="#000000"/>
  <!-- Point of intersection X -->
  <circle cx="240" cy="130" r="5" fill="#b91c1c"/>
  <text x="135" y="75" font-size="16" font-weight="bold" fill="#000000">A</text>
  <text x="340" y="190" font-size="16" font-weight="bold" fill="#000000">B</text>
  <text x="135" y="190" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="340" y="75" font-size="16" font-weight="bold" fill="#000000">D</text>
  <text x="245" y="120" font-size="16" font-weight="bold" fill="#b91c1c">X</text>
''')

# Diagram 4: Ex 9.2 Q4 (Concentric circles)
d_9_2_q4 = circle_svg("संकेंद्री वृत्त व रेखा द्वारा अंतःखंड AB = CD", '''
  <circle cx="240" cy="130" r="105" fill="none" stroke="#2563eb" stroke-width="3.5"/>
  <circle cx="240" cy="130" r="60" fill="none" stroke="#16a34a" stroke-width="3"/>
  <circle cx="240" cy="130" r="4" fill="#000000"/>
  <line x1="80" y1="160" x2="400" y2="160" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="240" y1="130" x2="240" y2="160" stroke="#000000" stroke-width="2.5" stroke-dasharray="4,3"/>
  <text x="235" y="120" font-size="16" font-weight="bold" fill="#000000">O</text>
  <text x="130" y="185" font-size="16" font-weight="bold" fill="#000000">A</text>
  <text x="180" y="185" font-size="16" font-weight="bold" fill="#000000">B</text>
  <text x="290" y="185" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="345" y="185" font-size="16" font-weight="bold" fill="#000000">D</text>
  <text x="245" y="175" font-size="14" font-weight="bold" fill="#000000">M</text>
''')

# Diagram 5: Ex 9.2 Q5 (Reshma, Salma, Mandip)
d_9_2_q5 = circle_svg("रेशमा (R), सलमा (S) और मनदीप (M) वृत्ताकार पथ पर", '''
  <circle cx="240" cy="130" r="95" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <circle cx="240" cy="130" r="4" fill="#000000"/>
  <polygon points="160,80 320,80 240,225" fill="none" stroke="#dc2626" stroke-width="3"/>
  <line x1="160" y1="80" x2="320" y2="80" stroke="#16a34a" stroke-width="4"/>
  <text x="235" y="125" font-size="16" font-weight="bold" fill="#000000">O</text>
  <text x="135" y="80" font-size="16" font-weight="bold" fill="#000000">R (रेशमा)</text>
  <text x="330" y="80" font-size="16" font-weight="bold" fill="#000000">M (मनदीप)</text>
  <text x="235" y="245" font-size="16" font-weight="bold" fill="#000000">S (सलमा)</text>
  <text x="210" y="70" font-size="14" font-weight="bold" fill="#15803d">RM = 9.6 मीटर</text>
''')

# Diagram 6: Ex 9.3 Q1 (Angle subtended at center twice angle at circumference)
d_9_3_q1 = circle_svg("केंद्र पर अंतरित कोण परिधि के कोण का दोगुना (∠AOC = 2∠ADC)", '''
  <circle cx="240" cy="130" r="95" fill="#f8fafc" stroke="#2563eb" stroke-width="3.5"/>
  <circle cx="240" cy="130" r="4" fill="#000000"/>
  <!-- Center Angle AOC -->
  <line x1="240" y1="130" x2="160" y2="185" stroke="#2563eb" stroke-width="3"/>
  <line x1="240" y1="130" x2="320" y2="185" stroke="#2563eb" stroke-width="3"/>
  <line x1="240" y1="130" x2="280" y2="215" stroke="#64748b" stroke-width="2" stroke-dasharray="4,3"/>
  <!-- Inscribed Angle ADC -->
  <line x1="240" y1="35" x2="160" y2="185" stroke="#dc2626" stroke-width="3"/>
  <line x1="240" y1="35" x2="320" y2="185" stroke="#dc2626" stroke-width="3"/>
  <text x="235" y="125" font-size="16" font-weight="bold" fill="#000000">O (90°)</text>
  <text x="145" y="200" font-size="16" font-weight="bold" fill="#000000">A</text>
  <text x="285" y="235" font-size="16" font-weight="bold" fill="#000000">B</text>
  <text x="330" y="200" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="235" y="25" font-size="18" font-weight="bold" fill="#dc2626">D (45°)</text>
''')

# Diagram 7: Ex 9.3 Q3 (Angle PQR = 100°)
d_9_3_q3 = circle_svg("चक्रीय कोण ∠PQR = 100° व केंद्र कोण", '''
  <circle cx="240" cy="130" r="95" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <circle cx="240" cy="130" r="4" fill="#000000"/>
  <polyline points="160,185 240,40 320,185" fill="none" stroke="#dc2626" stroke-width="3.5"/>
  <line x1="240" y1="130" x2="160" y2="185" stroke="#2563eb" stroke-width="3"/>
  <line x1="240" y1="130" x2="320" y2="185" stroke="#2563eb" stroke-width="3"/>
  <line x1="160" y1="185" x2="320" y2="185" stroke="#64748b" stroke-width="2.5" stroke-dasharray="4,3"/>
  <text x="235" y="125" font-size="16" font-weight="bold" fill="#000000">O</text>
  <text x="145" y="200" font-size="16" font-weight="bold" fill="#000000">P</text>
  <text x="235" y="30" font-size="16" font-weight="bold" fill="#dc2626">Q (100°)</text>
  <text x="330" y="200" font-size="16" font-weight="bold" fill="#000000">R</text>
  <text x="175" y="175" font-size="14" font-weight="bold" fill="#1e3a8a">∠OPR = 10°</text>
''')

# Diagram 8: Ex 9.3 Q4 (Same segment angles ∠BDC = ∠BAC = 80°)
d_9_3_q4 = circle_svg("एक ही वृत्तखंड के कोण बराबर होते हैं (∠BDC = ∠BAC = 80°)", '''
  <circle cx="240" cy="130" r="95" fill="#f8fafc" stroke="#2563eb" stroke-width="3.5"/>
  <polygon points="160,190 320,190 190,45" fill="rgba(37,99,235,0.08)" stroke="#2563eb" stroke-width="3"/>
  <polyline points="160,190 290,45 320,190" fill="none" stroke="#16a34a" stroke-width="3.5"/>
  <text x="145" y="205" font-size="16" font-weight="bold" fill="#000000">B</text>
  <text x="330" y="205" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="180" y="35" font-size="16" font-weight="bold" fill="#1d4ed8">A (80°)</text>
  <text x="290" y="35" font-size="16" font-weight="bold" fill="#15803d">D (80°)</text>
''')

# Diagram 9: Ex 9.3 Q6 (Cyclic Quadrilateral ABCD)
d_9_3_q6 = circle_svg("चक्रीय चतुर्भुज ABCD व विकर्ण प्रतिच्छेद E", '''
  <circle cx="240" cy="130" r="95" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <polygon points="170,60 310,65 330,190 150,175" fill="rgba(22,163,74,0.08)" stroke="#16a34a" stroke-width="3.5"/>
  <line x1="170" y1="60" x2="330" y2="190" stroke="#dc2626" stroke-width="3" stroke-dasharray="5,3"/>
  <line x1="310" y1="65" x2="150" y2="175" stroke="#dc2626" stroke-width="3" stroke-dasharray="5,3"/>
  <circle cx="240" cy="120" r="4" fill="#000000"/>
  <text x="155" y="55" font-size="16" font-weight="bold" fill="#000000">A</text>
  <text x="320" y="60" font-size="16" font-weight="bold" fill="#000000">B</text>
  <text x="340" y="200" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="135" y="190" font-size="16" font-weight="bold" fill="#000000">D</text>
  <text x="245" y="115" font-size="16" font-weight="bold" fill="#dc2626">E</text>
''')

# Diagram 10: Ex 9.3 Q12 (Cyclic Parallelogram is Rectangle)
d_9_3_q12 = circle_svg("चक्रीय समांतर चतुर्भुज एक आयत होता है", '''
  <circle cx="240" cy="130" r="95" fill="#eff6ff" stroke="#2563eb" stroke-width="3.5"/>
  <rect x="173" y="66" width="134" height="128" fill="rgba(37,99,235,0.12)" stroke="#1d4ed8" stroke-width="4"/>
  <circle cx="240" cy="130" r="4" fill="#000000"/>
  <text x="235" y="125" font-size="16" font-weight="bold" fill="#000000">O</text>
  <text x="155" y="60" font-size="16" font-weight="bold" fill="#000000">A</text>
  <text x="315" y="60" font-size="16" font-weight="bold" fill="#000000">B</text>
  <text x="315" y="210" font-size="16" font-weight="bold" fill="#000000">C</text>
  <text x="155" y="210" font-size="16" font-weight="bold" fill="#000000">D</text>
  <text x="210" y="145" font-size="14" font-weight="bold" fill="#15803d">∠A = ∠C = 90°</text>
''')

print("All Chapter 9 circle diagrams generated!")
