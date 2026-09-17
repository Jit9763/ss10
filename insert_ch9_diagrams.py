import re
from generate_ch9_diagrams import (
    d_9_1_q1, d_9_2_q1, d_9_2_q2, d_9_2_q4, d_9_2_q5,
    d_9_3_q1, d_9_3_q3, d_9_3_q4, d_9_3_q6, d_9_3_q12
)

with open('qa_master_math9_9.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Helper to insert diagram right after <h3 class="question-heading">...</h3>
def insert_diagram(html, q_pattern, diagram_svg):
    pos = html.find(q_pattern)
    if pos != -1:
        # find closing </h3>
        h3_close = html.find('</h3>', pos)
        if h3_close != -1:
            h3_end = h3_close + 5
            return html[:h3_end] + '\n' + diagram_svg + html[h3_end:]
    return html

# 1. Ex 9.1 Q1
text = insert_diagram(text, 'याद कीजिए कि दो वृत्त सर्वांगसम होते हैं', d_9_1_q1)

# 2. Ex 9.2 Q1
text = insert_diagram(text, '5\\text{ cm} तथा 3\\text{ cm} त्रिज्या वाले दो वृत्त', d_9_2_q1)

# 3. Ex 9.2 Q2
text = insert_diagram(text, 'यदि एक वृत्त की दो समान जीवाएँ वृत्त के अंदर प्रतिच्छेद करें, तो सिद्ध कीजिए कि एक जीवा के खंड', d_9_2_q2)

# 4. Ex 9.2 Q4
text = insert_diagram(text, 'यदि एक रेखा दो संकेंद्री वृत्तों', d_9_2_q4)

# 5. Ex 9.2 Q5
text = insert_diagram(text, 'एक पार्क में बने 5\\text{ m} त्रिज्या वाले वृत्त पर तीन लड़कियाँ', d_9_2_q5)

# 6. Ex 9.3 Q1
text = insert_diagram(text, 'केंद्र O वाले एक वृत्त पर तीन बिंदु A, B और C इस प्रकार हैं', d_9_3_q1)

# 7. Ex 9.3 Q3
text = insert_diagram(text, 'आकृति में, \\angle PQR = 100^\\circ है', d_9_3_q3)

# 8. Ex 9.3 Q4
text = insert_diagram(text, 'आकृति में, \\angle ABC = 69^\\circ और \\angle ACB = 31^\\circ', d_9_3_q4)

# 9. Ex 9.3 Q6
text = insert_diagram(text, 'ABCD एक चक्रीय चतुर्भुज है जिसके विकर्ण एक बिंदु E पर', d_9_3_q6)

# 10. Ex 9.3 Q12
text = insert_diagram(text, 'सिद्ध कीजिए कि चक्रीय समांतर चतुर्भुज आयत होता है', d_9_3_q12)

with open('qa_master_math9_9.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Chapter 9 SVG diagrams inserted successfully!")
