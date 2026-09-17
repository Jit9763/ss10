# -*- coding: utf-8 -*-
"""
Master Hindi Medium Purifier
Replaces English words, proof reasons, buttons, simulator headings,
and technical terminology across ALL 12 Class 9 Mathematics chapters
with pure, natural Hindi (शुद्ध हिंदी माध्यम).
"""

import glob
import re

files = sorted(glob.glob('qa_master_math9_*.html'))

# 1. Action Bar Buttons
button_replacements = {
    '>Copy</button>': '>कॉपी</button>',
    '>Print</button>': '>प्रिंट</button>',
    '>Home</button>': '>होम</button>',
}

# 2. Proof block conversions for Ch 7 & 8 (turn LaTeX aligned blocks into clean Hindi <ul>)
proof_replacements = {
    # Ch 8 Ex 8.1 Q2
    r"""<div class="math-scroll">
        $$\begin{aligned}
        AB &= DC \quad (\text{Opposite sides}) \\
        BC &= CB \quad (\text{Common side}) \\
        AC &= DB \quad (\text{Given})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$AB = DC$ (समांतर चतुर्भुज की सम्मुख भुजाएँ बराबर होती हैं)</li>
        <li>$BC = CB$ (उभयनिष्ठ भुजा)</li>
        <li>$AC = DB$ (विकर्ण बराबर दिए हैं)</li>
      </ul>""",

    # Ch 8 Ex 8.1 Q3
    r"""<div class="math-scroll">
        $$\begin{aligned}
        OA &= OC \quad (\text{Given}) \\
        \angle AOB &= 90^\circ \\ \angle BOC &= 90^\circ \quad (\text{Given}) \\
        OB &= OB \quad (\text{Common side})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$OA = OC$ (विकर्ण परस्पर समद्विभाजित होते हैं)</li>
        <li>$\angle AOB = \angle BOC = 90^\circ$ (विकर्ण परस्पर लम्ब दिए हैं)</li>
        <li>$OB = OB$ (उभयनिष्ठ भुजा)</li>
      </ul>""",

    # Ch 8 Ex 8.1 Q4 (part 1)
    r"""<div class="math-scroll">
        $$\begin{aligned}
        AB &= BA \quad (\text{Common side}) \\
        BC &= AD \quad (\text{Sides of square}) \\
        \angle ABC &= 90^\circ \\ \angle BAD &= 90^\circ
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$AB = BA$ (उभयनिष्ठ भुजा)</li>
        <li>$BC = AD$ (वर्ग की सभी भुजाएँ बराबर होती हैं)</li>
        <li>$\angle ABC = \angle BAD = 90^\circ$ (वर्ग का प्रत्येक कोण समकोण होता है)</li>
      </ul>""",

    # Ch 8 Ex 8.1 Q4 (part 2)
    r"""<div class="math-scroll">
        $$\begin{aligned}
        AB &= AD \quad (\text{Sides of square}) \\
        AO &= AO \quad (\text{Common side}) \\
        OB &= OD \quad (\text{Diagonals bisect})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$AB = AD$ (वर्ग की भुजाएँ)</li>
        <li>$AO = AO$ (उभयनिष्ठ भुजा)</li>
        <li>$OB = OD$ (समांतर चतुर्भुज के विकर्ण परस्पर समद्विभाजित करते हैं)</li>
      </ul>""",

    # Ch 8 Ex 8.1 Q6
    r"""<div class="math-scroll">
        $$\begin{aligned}
        \angle 1 &= \angle 4 \quad (\text{Alternate interior angles}) \\
        \angle 2 &= \angle 3 \quad (\text{Alternate interior angles})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$\angle 1 = \angle 4$ (एकांतर अंतःकोण, चूँकि $AB \parallel CD$)</li>
        <li>$\angle 2 = \angle 3$ (एकांतर अंतःकोण, चूँकि $AD \parallel BC$)</li>
      </ul>""",

    # Ch 8 Ex 8.1 Q9
    r"""<div class="math-scroll">
        $$\begin{aligned}
        AD &= CB \quad (\text{Opposite sides}) \\
        \angle ADP &= \angle CBQ \quad (\text{Alternate angles}) \\
        DP &= BQ \quad (\text{Given})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$AD = CB$ (समांतर चतुर्भुज की सम्मुख भुजाएँ बराबर होती हैं)</li>
        <li>$\angle ADP = \angle CBQ$ (एकांतर अंतःकोण, $AD \parallel BC$)</li>
        <li>$DP = BQ$ (दिया है)</li>
      </ul>""",

    # Ch 8 Ex 8.1 Q10
    r"""<div class="math-scroll">
        $$\begin{aligned}
        \angle APB &= 90^\circ \quad (\text{Perpendicular}) \\
        \angle CQD &= 90^\circ \quad (\text{Perpendicular}) \\
        \angle ABP &= \angle CDQ \quad (\text{Alternate angles}) \\
        AB &= CD \quad (\text{Opposite sides})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$\angle APB = \angle CQD = 90^\circ$ (शीर्षलम्ब दिए हैं)</li>
        <li>$\angle ABP = \angle CDQ$ (एकांतर कोण, $AB \parallel CD$)</li>
        <li>$AB = CD$ (समांतर चतुर्भुज की सम्मुख भुजाएँ बराबर हैं)</li>
      </ul>""",

    # Ch 8 Ex 8.2 Q7
    r"""<div class="math-scroll">
        $$\begin{aligned}
        AD &= CD \quad (\text{D is midpoint}) \\
        \angle ADM &= 90^\circ \\ \angle CDM &= 90^\circ \\
        MD &= MD \quad (\text{Common side})
        \end{aligned}$$
      </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
        <li>$AD = CD$ ($D$, भुजा $AC$ का मध्य-बिंदु है)</li>
        <li>$\angle ADM = \angle CDM = 90^\circ$ ($MD \perp AC$)</li>
        <li>$MD = MD$ (उभयनिष्ठ भुजा)</li>
      </ul>""",

    # Ch 7 Ex 7.1 Q1
    r"""<div class="math-scroll">
          $$\begin{aligned}
          AC &= AD \quad (\text{Given}) \\
          \angle CAB &= \angle DAB \quad (AB \text{ bisects } \angle A) \\
          AB &= AB \quad (\text{Common side})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$AC = AD$ (दिया है)</li>
          <li>$\angle CAB = \angle DAB$ ($AB$, कोण $\angle A$ का समद्विभाजक है)</li>
          <li>$AB = AB$ (उभयनिष्ठ भुजा)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q2
    r"""<div class="math-scroll">
          $$\begin{aligned}
          AD &= BC \quad (\text{Given}) \\
          \angle DAB &= \angle CBA \quad (\text{Given}) \\
          AB &= BA \quad (\text{Common side})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$AD = BC$ (दिया है)</li>
          <li>$\angle DAB = \angle CBA$ (दिया है)</li>
          <li>$AB = BA$ (उभयनिष्ठ भुजा)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q3
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle BOC &= \angle AOD \quad (\text{Vertically opposite angles}) \\
          \angle CBO &= 90^\circ \\
          \angle DAO &= 90^\circ \quad (\text{Given perpendiculars}) \\
          BC &= AD \quad (\text{Given})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle BOC = \angle AOD$ (शीर्षाभिमुख कोण)</li>
          <li>$\angle CBO = \angle DAO = 90^\circ$ (लम्ब दिए हैं)</li>
          <li>$BC = AD$ (बराबर लम्ब दिए हैं)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q4
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle BAC &= \angle DCA \quad (\text{Alternate angles, } AB \parallel DC) \\
          AC &= CA \quad (\text{Common side}) \\
          \angle BCA &= \angle DAC \quad (\text{Alternate angles, } BC \parallel AD)
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle BAC = \angle DCA$ (एकांतर कोण, $AB \parallel DC$)</li>
          <li>$AC = CA$ (उभयनिष्ठ भुजा)</li>
          <li>$\angle BCA = \angle DAC$ (एकांतर कोण, $BC \parallel AD$)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q5
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle APB &= 90^\circ \\
          \angle AQB &= 90^\circ \quad (\text{Given perpendiculars}) \\
          \angle PAB &= \angle QAB \quad (l \text{ bisects } \angle A) \\
          AB &= AB \quad (\text{Common hypotenuse})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle APB = \angle AQB = 90^\circ$ (लम्ब दिए हैं)</li>
          <li>$\angle PAB = \angle QAB$ (रेखा $l$, कोण $\angle A$ की समद्विभाजक है)</li>
          <li>$AB = AB$ (उभयनिष्ठ कर्ण)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q6
    r"""<div class="math-scroll">
          $$\begin{aligned}
          AB &= AD \quad (\text{Given}) \\
          \angle BAC &= \angle DAE \quad (\text{From (1)}) \\
          AC &= AE \quad (\text{Given})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$AB = AD$ (दिया है)</li>
          <li>$\angle BAC = \angle DAE$ (समीकरण 1 से)</li>
          <li>$AC = AE$ (दिया है)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q7
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle PAD &= \angle PBE \quad (\text{Given equal angles}) \\
          AP &= BP \quad (P \text{ is midpoint of } AB) \\
          \angle APD &= \angle BPE \quad (\text{From (1)})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle PAD = \angle PBE$ (बराबर कोण दिए हैं)</li>
          <li>$AP = BP$ ($P$, रेखाखंड $AB$ का मध्य-बिंदु है)</li>
          <li>$\angle APD = \angle BPE$ (समीकरण 1 से)</li>
        </ul>""",

    # Ch 7 Ex 7.1 Q8
    r"""<div class="math-scroll">
          $$\begin{aligned}
          AM &= BM \quad (M \text{ is midpoint of } AB) \\
          \angle AMC &= \angle BMD \quad (\text{Vertically opposite angles}) \\
          CM &= DM \quad (\text{Given})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$AM = BM$ ($M$, कर्ण $AB$ का मध्य-बिंदु है)</li>
          <li>$\angle AMC = \angle BMD$ (शीर्षाभिमुख कोण)</li>
          <li>$CM = DM$ (दिया है)</li>
        </ul>""",

    # Ch 7 Ex 7.2 Q1
    r"""<div class="math-scroll">
          $$\begin{aligned}
          AB &= AC \quad (\text{Given}) \\
          OB &= OC \quad (\text{Proved above}) \\
          AO &= AO \quad (\text{Common side})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$AB = AC$ (दिया है)</li>
          <li>$OB = OC$ (ऊपर सिद्ध किया गया है)</li>
          <li>$AO = AO$ (उभयनिष्ठ भुजा)</li>
        </ul>""",

    # Ch 7 Ex 7.2 Q2
    r"""<div class="math-scroll">
          $$\begin{aligned}
          BD &= CD \quad (D \text{ is midpoint of } BC) \\
          \angle ADB &= 90^\circ \quad (\text{Perpendicular}) \\
          \angle ADC &= 90^\circ \quad (\text{Perpendicular}) \\
          AD &= AD \quad (\text{Common side})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$BD = CD$ ($D$, भुजा $BC$ का मध्य-बिंदु है)</li>
          <li>$\angle ADB = \angle ADC = 90^\circ$ ($AD \perp BC$)</li>
          <li>$AD = AD$ (उभयनिष्ठ भुजा)</li>
        </ul>""",

    # Ch 7 Ex 7.2 Q3
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle AEB &= 90^\circ \quad (\text{Altitude}) \\
          \angle AFC &= 90^\circ \quad (\text{Altitude}) \\
          \angle A &= \angle A \quad (\text{Common angle}) \\
          AB &= AC \quad (\text{Given})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle AEB = \angle AFC = 90^\circ$ (शीर्षलम्ब)</li>
          <li>$\angle A = \angle A$ (उभयनिष्ठ कोण)</li>
          <li>$AB = AC$ (दिया है)</li>
        </ul>""",

    # Ch 7 Ex 7.2 Q4
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle AEB &= 90^\circ \quad (\text{Altitude}) \\
          \angle AFC &= 90^\circ \quad (\text{Altitude}) \\
          \angle A &= \angle A \quad (\text{Common angle}) \\
          BE &= CF \quad (\text{Given})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle AEB = \angle AFC = 90^\circ$ (शीर्षलम्ब)</li>
          <li>$\angle A = \angle A$ (उभयनिष्ठ कोण)</li>
          <li>$BE = CF$ (बराबर शीर्षलम्ब दिए हैं)</li>
        </ul>""",

    # Ch 7 Ex 7.3 Q2
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle ADB &= 90^\circ \quad (\text{Perpendicular}) \\
          \angle ADC &= 90^\circ \quad (\text{Perpendicular}) \\
          AB &= AC \quad (\text{Hypotenuse, given}) \\
          AD &= AD \quad (\text{Common side})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle ADB = \angle ADC = 90^\circ$ ($AD \perp BC$)</li>
          <li>$AB = AC$ (कर्ण, दिया है)</li>
          <li>$AD = AD$ (उभयनिष्ठ भुजा)</li>
        </ul>""",

    # Ch 7 Ex 7.3 Q4
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle BEC &= 90^\circ \\
          \angle CFB &= 90^\circ \quad (\text{Altitudes}) \\
          BC &= CB \quad (\text{Common hypotenuse}) \\
          BE &= CF \quad (\text{Given equal altitudes})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle BEC = \angle CFB = 90^\circ$ (शीर्षलम्ब)</li>
          <li>$BC = CB$ (उभयनिष्ठ कर्ण)</li>
          <li>$BE = CF$ (बराबर शीर्षलम्ब दिए हैं)</li>
        </ul>""",

    # Ch 7 Ex 7.3 Q5
    r"""<div class="math-scroll">
          $$\begin{aligned}
          \angle APB &= 90^\circ \\
          \angle APC &= 90^\circ \quad (AP \perp BC) \\
          AB &= AC \quad (\text{Hypotenuse, given}) \\
          AP &= AP \quad (\text{Common side})
          \end{aligned}$$
        </div>""":
    r"""<ul style="margin:10px 0 15px 30px; line-height:2.2;">
          <li>$\angle APB = \angle APC = 90^\circ$ ($AP \perp BC$)</li>
          <li>$AB = AC$ (कर्ण, दिया है)</li>
          <li>$AP = AP$ (उभयनिष्ठ भुजा)</li>
        </ul>""",
}

# 3. Terminology & Subtitle Replacements across all files
general_terms = {
    'Interactive Quadrilateral Canvas': 'सजीव चतुर्भुज आकृति',
    'Interactive Parallelogram Canvas': 'सजीव समांतर चतुर्भुज आकृति',
    'Mid-point Theorem Interactive Canvas': 'मध्य-बिंदु प्रमेय सजीव आकृति',
    'Special Quadrilaterals Explorer': 'विशेष चतुर्भुज परिवर्तक',
    'Special Quadrilaterals Canvas': 'विशेष चतुर्भुज सजीव आकृति',
    'Right Triangle Midpoint Canvas': 'समकोण त्रिभुज कर्ण मध्य-बिंदु सजीव आकृति',
    'Interactive Congruence Canvas': 'सर्वांगसमता कसौटी सजीव आकृति',
    'Isosceles Canvas': 'समद्विबाहु त्रिभुज सजीव आकृति',
    'Equilateral Canvas': 'समबाहु त्रिभुज सजीव आकृति',
    'Interactive Point Plotter': 'कार्तीय तल बिंदु आलेखक',
    'Quadrant & Axis Identifier': 'चतुर्थांश व अक्ष पहचानकर्ता',
    'Distance Formula Solver': 'दूरी सूत्र हलकर्ता',
    'Reflection Solver': 'दर्पण प्रतिबिंब हलकर्ता',
    'Midpoint Calculator': 'मध्य-बिंदु गणक',
    'Four Solutions Table Generator': 'चार क्रमिक हल सारणी जनरेटर',
    'Solution Verifier: L.H.S. vs R.H.S.': 'हल सत्यापनकर्ता (बायाँ पक्ष = दायाँ पक्ष)',
    "Find 'k' Calculator": "'k' का मान गणक",
    'Interactive Straight Line Grapher': 'सरल रेखा ग्राफ आलेखक',
    'Geometric Representation': 'ज्यामितीय निरूपण',
    'Visual Interactive Quadrilateral Canvases': 'सजीव इंटरैक्टिव चतुर्भुज सिमुलेटर',
    'Visual Interactive Triangle Canvases': 'सजीव इंटरैक्टिव त्रिभुज सिमुलेटर',
    '5 LIVE VISUAL INTERACTIVE SIMULATORS (WITH CANVAS)': '⚡ 5 सजीव इंटरैक्टिव सिमुलेटर (लाइव कैनवास सहित)',
    '5 LIVE INTERACTIVE SIMULATORS': '⚡ 5 सजीव इंटरैक्टिव सिमुलेटर',
    'Interactive Linear Equation Simulators': 'रैखिक समीकरण सिमुलेटर',
    'Interactive Coordinate Simulators': 'निर्देशांक ज्यामिति सिमुलेटर',
    'Exercise 8.1': 'प्रश्नावली 8.1',
    'Exercise 8.2': 'प्रश्नावली 8.2',
    'Exercise 7.1': 'प्रश्नावली 7.1',
    'Exercise 7.2': 'प्रश्नावली 7.2',
    'Exercise 7.3': 'प्रश्नावली 7.3',
    'Exercise 7.4': 'प्रश्नावली 7.4',
    'Exercise 3.1': 'प्रश्नावली 3.1',
    'Exercise 3.2': 'प्रश्नावली 3.2',
    'Exercise 3.3': 'प्रश्नावली 3.3',
    'Exercise 4.1': 'प्रश्नावली 4.1',
    'Exercise 4.2': 'प्रश्नावली 4.2',
    'Exercise 4.3': 'प्रश्नावली 4.3',
    'Exercise 6.1': 'प्रश्नावली 6.1',
    'Exercise 6.2': 'प्रश्नावली 6.2',
    'Exercise 6.3': 'प्रश्नावली 6.3',
    'Exercise 9.1': 'प्रश्नावली 9.1',
    'Exercise 9.2': 'प्रश्नावली 9.2',
    'Exercise 9.3': 'प्रश्नावली 9.3',
    'Exercise 10.1': 'प्रश्नावली 10.1',
    'Exercise 10.2': 'प्रश्नावली 10.2',
    'Exercise 11.1': 'प्रश्नावली 11.1',
    'Exercise 11.2': 'प्रश्नावली 11.2',
    'Exercise 12.1': 'प्रश्नावली 12.1',
    '(Rhombus)': '',
    '(Rectangle)': '',
    '(Square)': '',
    '(Only one)': '(केवल एक)',
    '(Midpoint Formula)': '(मध्य-बिंदु सूत्र)',
    '(Distance Formula)': '(दूरी सूत्र)',
    '(Origin)': '(मूलबिंदु)',
    '(Positive X-axis)': '(धनात्मक X-अक्ष)',
    '(Negative X-axis)': '(ऋणात्मक X-अक्ष)',
    '(Positive Y-axis)': '(धनात्मक Y-अक्ष)',
    '(Negative Y-axis)': '(ऋणात्मक Y-अक्ष)',
    '(Quadrant I: +, +)': '(प्रथम चतुर्थांश: +, +)',
    '(Quadrant II: -, +)': '(द्वितीय चतुर्थांश: -, +)',
    '(Quadrant III: -, -)': '(तृतीय चतुर्थांश: -, -)',
    '(Quadrant IV: +, -)': '(चतुर्थ चतुर्थांश: +, -)',
    '(Quadrant I)': '(प्रथम चतुर्थांश)',
    '(Quadrant II)': '(द्वितीय चतुर्थांश)',
    '(Quadrant III)': '(तृतीय चतुर्थांश)',
    '(Quadrant IV)': '(चतुर्थ चतुर्थांश)',
    '(Abscissa / x-निर्देशांक)': '(भुज / x-निर्देशांक)',
    '(Ordinate / y-निर्देशांक)': '(कोटि / y-निर्देशांक)',
    '(Abscissa)': '(भुज)',
    '(Ordinate)': '(कोटि)',
    '(X-axis)': '(X-अक्ष)',
    '(Y-axis)': '(Y-अक्ष)',
    '(Horizontal line)': '(क्षैतिज रेखा)',
    '(Vertical line)': '(ऊर्ध्वाधर रेखा)',
    '(Quadrants)': '(चतुर्थांश)',
    '(Street Plan)': '(सड़क योजना)',
    '(Reference Axes)': '(संदर्भ अक्ष)',
    '(Edges)': '(कोरों)',
    '\\quad \\text{and} \\quad': ' तथा ',
    '\\text{and}': 'तथा',
}

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # Apply button replacements
    for k, v in button_replacements.items():
        content = content.replace(k, v)

    # Apply proof block replacements
    for k, v in proof_replacements.items():
        content = content.replace(k, v)

    # Apply general term replacements
    for k, v in general_terms.items():
        content = content.replace(k, v)

    if content != orig_content:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ {fn}: 100% Purified to Pure Hindi!')
    else:
        print(f'ℹ️ {fn}: No changes needed.')

print("\n🎉 ALL CHAPTERS PURIFIED TO PURE HINDI MEDIUM STANDARDS!")
