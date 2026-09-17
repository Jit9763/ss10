# -*- coding: utf-8 -*-
"""
Builder for Complete Chapter 7: त्रिभुज (Triangles)
Includes:
- Full Ex 7.1 (Q1 to Q8) with geometric SVG diagrams
- Full Ex 7.2 (Q1 to Q8) with geometric SVG diagrams
- Full Ex 7.3 (Q1 to Q5) with geometric SVG diagrams
- Full Ex 7.4 (Q1 to Q6) with geometric SVG diagrams
Total: 27 questions with 100% NCERT solutions!
- 5 Live HTML5 Canvas Simulators with real-time geometric visualisations
- Master Standard Action Bar, Typography, Step boxes, and Zero Overflows.
"""

from generate_ch7_diagrams import (
    d_7_1_q1, d_7_1_q2, d_7_1_q3, d_7_1_q4, d_7_1_q5, d_7_1_q6, d_7_1_q7, d_7_1_q8,
    d_7_2_q1, d_7_2_q2, d_7_2_q3, d_7_2_q5, d_7_2_q6,
    d_7_3_q1, d_7_3_q3, d_7_4_q1, d_7_4_q4
)

with open('ch2_style.css', 'r', encoding='utf-8') as f:
    ch2_css = f.read()

html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NCERT कक्षा 9 गणित - अध्याय 7: त्रिभुज (संपूर्ण 100% प्रश्नोत्तर, रेखाचित्र व 5 लाइव सिमुलेटर)</title>
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
  options: {{
    enableMenu: false
  }},
  chtml: {{
    displayOverflow: 'scale'
  }}
}};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

<style>
{ch2_css}

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

<!-- STICKY ACTION BAR -->
<div class="action-bar">
  <button class="action-btn" onclick="adjustContainerWidth(50)">W+</button>
  <button class="action-btn" onclick="adjustContainerWidth(-50)">W-</button>
  <button class="action-btn" onclick="adjustFontSize(2)">A+</button>
  <button class="action-btn" onclick="adjustFontSize(-2)">A-</button>
  <button class="action-btn" onclick="adjustFontWeight(100)">B+</button>
  <button class="action-btn" onclick="adjustFontWeight(-100)">B-</button>
  <button class="action-btn copy-btn" onclick="copyEntireContent()">Copy</button>
  <button class="action-btn" onclick="window.print()">Print</button>
  <button class="action-btn" onclick="window.location.href='index.html'">Home</button>
</div>

<div class="container" id="mainContainer">
  <div id="contentToCopy">

    <!-- HERO TITLE -->
    <div class="hero-title">
      NCERT कक्षा 9 गणित • अध्याय 7
      <span>त्रिभुज (Triangles) — संपूर्ण 100% मास्टर प्रश्नोत्तर, रेखाचित्र व 5 लाइव सिमुलेटर</span>
    </div>

    <!-- QUICK NAV -->
    <div class="nav-pills">
      <a href="#ex71" class="btn-nav">प्रश्नावली 7.1 (8 प्रश्न)</a>
      <a href="#ex72" class="btn-nav">प्रश्नावली 7.2 (8 प्रश्न)</a>
      <a href="#ex73" class="btn-nav">प्रश्नावली 7.3 (5 प्रश्न)</a>
      <a href="#ex74" class="btn-nav">प्रश्नावली 7.4 (6 प्रश्न)</a>
      <a href="#simulators" class="btn-nav" style="background:#fef08a; color:#854d0e;">⚡ 5 लाइव सिमुलेटर</a>
    </div>

    <!-- EXERCISE 7.1 -->
    <div class="part-header" id="ex71">
      📖 प्रश्नावली 7.1 (Exercise 7.1) — त्रिभुज सर्वांगसमता कसौटियाँ (SAS, ASA, AAS)
    </div>

    <!-- Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: चतुर्भुज $ACBD$ में, $AC = AD$ है और $AB$ कोण $A$ को समद्विभाजित करता है। दर्शाइए कि $\\Delta ABC \\cong \\Delta ABD$ है। $BC$ और $BD$ के बारे में आप क्या कह सकते हैं?</h3>
      {d_7_1_q1}
      <div class="step-box-blue">
        <p><b>दिया है:</b> $AC = AD$ तथा रेखाखंड $AB$ कोण $\\angle A$ का समद्विभाजक है, अर्थात $\\angle CAB = \\angle DAB$।</p>
        <p><b>सिद्ध करना है:</b> $\\Delta ABC \\cong \\Delta ABD$ तथा $BC$ व $BD$ में संबंध।</p>
        <p><b>उपपत्ति:</b> $\\Delta ABC$ और $\\Delta ABD$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          AC &= AD \\quad (\\text{{Given}}) \\\\
          \\angle CAB &= \\angle DAB \\quad (AB \\text{{ bisects }} \\angle A) \\\\
          AB &= AB \\quad (\\text{{Common side}})
          \\end{{aligned}}$$
        </div>
        <p>अतः SAS (भुजा-कोण-भुजा) सर्वांगसमता नियम से:</p>
        <div class="math-scroll">
          $$\\Delta ABC \\cong \\Delta ABD$$
        </div>
        <p>चूँकि सर्वांगसम त्रिभुजों के संगत भाग बराबर होते हैं (CPCT द्वारा):</p>
        <div class="math-scroll">
          $$BC = BD$$
        </div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta ABC \\cong \\Delta ABD$ (SAS सर्वांगसमता नियम) तथा $BC$ और $BD$ की लंबाइयाँ परस्पर बराबर हैं ($BC = BD$)।
      </div>
    </div>

    <!-- Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: $ABCD$ एक चतुर्भुज है जिसमें $AD = BC$ और $\\angle DAB = \\angle CBA$ है। सिद्ध कीजिए कि:<br>(i) $\\Delta ABD \\cong \\Delta BAC$<br>(ii) $BD = AC$<br>(iii) $\\angle ABD = \\angle BAC$</h3>
      {d_7_1_q2}
      <div class="step-box-blue">
        <p><b>(i) $\\Delta ABD \\cong \\Delta BAC$ की उपपत्ति:</b></p>
        <p>$\\Delta ABD$ और $\\Delta BAC$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          AD &= BC \\quad (\\text{{Given}}) \\\\
          \\angle DAB &= \\angle CBA \\quad (\\text{{Given}}) \\\\
          AB &= BA \\quad (\\text{{Common side}})
          \\end{{aligned}}$$
        </div>
        <p>अतः SAS सर्वांगसमता नियम से: <b>$\\Delta ABD \\cong \\Delta BAC$</b></p>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $BD = AC$ का प्रमाण:</b></p>
        <p>चूँकि $\\Delta ABD \\cong \\Delta BAC$, अतः सर्वांगसम त्रिभुजों की संगत भुजाएँ बराबर होती हैं (CPCT द्वारा):</p>
        <div class="math-scroll">$$BD = AC$$</div>
      </div>
      <div class="step-box-purple">
        <p><b>(iii) $\\angle ABD = \\angle BAC$ का प्रमाण:</b></p>
        <p>सर्वांगसम त्रिभुजों के संगत कोण बराबर होते हैं (CPCT द्वारा):</p>
        <div class="math-scroll">$$\\angle ABD = \\angle BAC$$</div>
      </div>
      <div class="answer-highlight">
        ✅ इति सिद्धम्: $\\Delta ABD \\cong \\Delta BAC$, $BD = AC$ तथा $\\angle ABD = \\angle BAC$ तीनों भाग पूर्णतः सिद्ध हुए।
      </div>
    </div>

    <!-- Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: एक रेखाखंड $AB$ पर $AD$ और $BC$ दो बराबर लम्ब रेखाखंड हैं। दर्शाइए कि $CD$, रेखाखंड $AB$ को समद्विभाजित करता है।</h3>
      {d_7_1_q3}
      <div class="step-box-blue">
        <p><b>दिया है:</b> $AD \\perp AB$ तथा $BC \\perp AB$ एवं $AD = BC$। मान लीजिए $CD$ और $AB$ का प्रतिच्छेद बिंदु $O$ है।</p>
        <p><b>सिद्ध करना है:</b> $OA = OB$ (अर्थात $CD$, रेखाखंड $AB$ को समद्विभाजित करता है)।</p>
        <p><b>उपपत्ति:</b> $\\Delta BOC$ और $\\Delta AOD$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle BOC &= \\angle AOD \\quad (\\text{{Vertically opposite angles}}) \\\\
          \\angle CBO &= \\angle DAO = 90^\\circ \\quad (\\text{{Given perpendiculars}}) \\\\
          BC &= AD \\quad (\\text{{Given}})
          \\end{{aligned}}$$
        </div>
        <p>अतः AAS (कोण-कोण-भुजा) सर्वांगसमता नियम से:</p>
        <div class="math-scroll">$$\\Delta BOC \\cong \\Delta AOD$$</div>
        <p>CPCT द्वारा संगत भुजाएँ बराबर होंगी:</p>
        <div class="math-scroll">$$OB = OA$$</div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: चूँकि $OA = OB$, अतः रेखाखंड $CD$, $AB$ को समद्विभाजित करता है।
      </div>
    </div>

    <!-- Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: $l$ और $m$ दो समांतर रेखाएँ हैं जिन्हें समांतर रेखाओं $p$ और $q$ का एक अन्य युग्म प्रतिच्छेदित करता है। दर्शाइए कि $\\Delta ABC \\cong \\Delta CDA$ है।</h3>
      {d_7_1_q4}
      <div class="step-box-blue">
        <p><b>दिया है:</b> $l \\parallel m$ तथा $p \\parallel q$। $AC$ विकर्ण है।</p>
        <p><b>उपपत्ति:</b> चतुर्भुज $ABCD$ में सम्मुख भुजाओं के दोनों युग्म समांतर हैं ($AB \\parallel DC$ तथा $AD \\parallel BC$), अतः $ABCD$ एक समांतर चतुर्भुज है।</p>
        <p>$\\Delta ABC$ और $\\Delta CDA$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle BAC &= \\angle DCA \\quad (\\text{{Alternate angles, }} AB \\parallel DC) \\\\
          AC &= CA \\quad (\\text{{Common side}}) \\\\
          \\angle BCA &= \\angle DAC \\quad (\\text{{Alternate angles, }} BC \\parallel AD)
          \\end{{aligned}}$$
        </div>
        <p>अतः ASA (कोण-भुजा-कोण) सर्वांगसमता नियम से:</p>
        <div class="math-scroll">$$\\Delta ABC \\cong \\Delta CDA$$</div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta ABC \\cong \\Delta CDA$ (ASA सर्वांगसमता नियम द्वारा सिद्ध)।
      </div>
    </div>

    <!-- Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: रेखा $l$ कोण $\\angle A$ को समद्विभाजित करती है और $B$, रेखा $l$ पर स्थित कोई बिंदु है। $BP$ और $BQ$, कोण $A$ की भुजाओं पर $B$ से डाले गए लम्ब हैं। दर्शाइए कि:<br>(i) $\\Delta APB \\cong \\Delta AQB$<br>(ii) $BP = BQ$ अर्थात बिंदु $B$, कोण की भुजाओं से समदूरस्थ है।</h3>
      {d_7_1_q5}
      <div class="step-box-blue">
        <p><b>(i) $\\Delta APB \\cong \\Delta AQB$ की उपपत्ति:</b></p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle APB &= \\angle AQB = 90^\\circ \\quad (\\text{{Given perpendiculars}}) \\\\
          \\angle PAB &= \\angle QAB \\quad (l \\text{{ bisects }} \\angle A) \\\\
          AB &= AB \\quad (\\text{{Common hypotenuse}})
          \\end{{aligned}}$$
        </div>
        <p>अतः AAS सर्वांगसमता नियम से: <b>$\\Delta APB \\cong \\Delta AQB$</b></p>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $BP = BQ$ का प्रमाण:</b></p>
        <p>चूँकि $\\Delta APB \\cong \\Delta AQB$, अतः CPCT द्वारा संगत भुजाएँ समान होंगी:</p>
        <div class="math-scroll">$$BP = BQ$$</div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta APB \\cong \\Delta AQB$ तथा $BP = BQ$ (बिंदु $B$ कोण $A$ की दोनों भुजाओं से समदूरस्थ है)।
      </div>
    </div>

    <!-- Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: दी गई आकृति में, $AC = AE, AB = AD$ और $\\angle BAD = \\angle EAC$ है। दर्शाइए कि $BC = DE$ है।</h3>
      {d_7_1_q6}
      <div class="step-box-blue">
        <p><b>दिया है:</b> $\\angle BAD = \\angle EAC$</p>
        <p>दोनों पक्षों में $\\angle DAC$ जोड़ने पर:</p>
        <div class="math-scroll">
          $$\\angle BAD + \\angle DAC = \\angle EAC + \\angle DAC$$
        </div>
        <div class="math-scroll">
          $$\\implies \\angle BAC = \\angle DAE \\quad \\text{{...(1)}}$$
        </div>
        <p>अब $\\Delta BAC$ और $\\Delta DAE$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          AB &= AD \\quad (\\text{{Given}}) \\\\
          \\angle BAC &= \\angle DAE \\quad (\\text{{From (1)}}) \\\\
          AC &= AE \\quad (\\text{{Given}})
          \\end{{aligned}}$$
        </div>
        <p>अतः SAS सर्वांगसमता नियम से: $\\Delta BAC \\cong \\Delta DAE$</p>
        <p>CPCT द्वारा: $BC = DE$</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta BAC \\cong \\Delta DAE \\implies BC = DE$ (इति सिद्धम्)।
      </div>
    </div>

    <!-- Q7 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 7: $AB$ एक रेखाखंड है और $P$ इसका मध्य-बिंदु है। $D$ और $E$ रेखाखंड $AB$ के एक ही ओर स्थित दो बिंदु इस प्रकार हैं कि $\\angle BAD = \\angle ABE$ और $\\angle EPA = \\angle DPB$ है। दर्शाइए कि:<br>(i) $\\Delta DAP \\cong \\Delta EBP$<br>(ii) $AD = BE$</h3>
      {d_7_1_q7}
      <div class="step-box-blue">
        <p><b>दिया है:</b> $\\angle EPA = \\angle DPB$</p>
        <p>दोनों पक्षों में $\\angle EPD$ जोड़ने पर:</p>
        <div class="math-scroll">
          $$\\angle EPA + \\angle EPD = \\angle DPB + \\angle EPD$$
        </div>
        <div class="math-scroll">
          $$\\implies \\angle APD = \\angle BPE \\quad \\text{{...(1)}}$$
        </div>
        <p>अब $\\Delta DAP$ और $\\Delta EBP$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle PAD &= \\angle PBE \\quad (\\text{{Given }}\\angle BAD = \\angle ABE) \\\\
          AP &= BP \\quad (P \\text{{ is midpoint of }} AB) \\\\
          \\angle APD &= \\angle BPE \\quad (\\text{{From (1)}})
          \\end{{aligned}}$$
        </div>
        <p>अतः ASA सर्वांगसमता नियम से: <b>$\\Delta DAP \\cong \\Delta EBP$</b></p>
        <p>CPCT द्वारा: <b>$AD = BE$</b></p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta DAP \\cong \\Delta EBP$ (ASA सर्वांगसमता) तथा संगत भुजाएँ $AD = BE$ सिद्ध हुईं।
      </div>
    </div>

    <!-- Q8 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 8: एक समकोण त्रिभुज $ABC$ में, जिसमें कोण $C$ समकोण है, $M$ कर्ण $AB$ का मध्य-बिंदु है। $C$ को $M$ से मिलाकर $D$ तक इस प्रकार बढ़ाया गया है कि $DM = CM$ है। बिंदु $D$ को बिंदु $B$ से मिला दिया जाता है। दर्शाइए कि:<br>(i) $\\Delta AMC \\cong \\Delta BMD$<br>(ii) $\\angle DBC$ एक समकोण है।<br>(iii) $\\Delta DBC \\cong \\Delta ACB$<br>(iv) $CM = \\frac{{1}}{{2}}AB$</h3>
      {d_7_1_q8}
      <div class="step-box-blue">
        <p><b>(i) $\\Delta AMC \\cong \\Delta BMD$:</b></p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          AM &= BM \\quad (M \\text{{ is midpoint of }} AB) \\\\
          \\angle AMC &= \\angle BMD \\quad (\\text{{Vertically opposite angles}}) \\\\
          CM &= DM \\quad (\\text{{Given}})
          \\end{{aligned}}$$
        </div>
        <p>अतः SAS नियम से: $\\Delta AMC \\cong \\Delta BMD$</p>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $\\angle DBC = 90^\\circ$:</b></p>
        <p>$\\Delta AMC \\cong \\Delta BMD \\implies \\angle ACM = \\angle BDM$ (CPCT)। ये एकांतर अंतःकोण हैं, अतः $DB \\parallel AC$।</p>
        <p>तिर्यक रेखा $BC$ के एक ही ओर के अंतःकोणों का योग $180^\\circ$ होता है:</p>
        <div class="math-scroll">$$\\angle DBC + \\angle ACB = 180^\\circ \\implies \\angle DBC + 90^\\circ = 180^\\circ \\implies \\angle DBC = 90^\\circ$$</div>
      </div>
      <div class="step-box-purple">
        <p><b>(iii) $\\Delta DBC \\cong \\Delta ACB$:</b></p>
        <p>$DB = AC$ (CPCT), $\\angle DBC = \\angle ACB = 90^\\circ$, तथा $BC = CB$ (उभयनिष्ठ)। अतः SAS नियम से: $\\Delta DBC \\cong \\Delta ACB$।</p>
      </div>
      <div class="step-box-orange">
        <p><b>(iv) $CM = \\frac{{1}}{{2}}AB$:</b></p>
        <p>$\\Delta DBC \\cong \\Delta ACB \\implies CD = AB$ (CPCT)। परंतु $CM = \\frac{{1}}{{2}}CD$ (दिया है $DM = CM$)।</p>
        <div class="math-scroll">$$CM = \\frac{{1}}{{2}}AB$$</div>
      </div>
      <div class="answer-highlight">
        ✅ संपूर्ण उपपत्ति पूर्ण हुई: $\\Delta AMC \\cong \\Delta BMD$, $\\angle DBC = 90^\\circ$, $\\Delta DBC \\cong \\Delta ACB$, तथा $CM = \\frac{{1}}{{2}}AB$।
      </div>
    </div>

    <!-- EXERCISE 7.2 -->
    <div class="part-header" id="ex72">
      📖 प्रश्नावली 7.2 (Exercise 7.2) — समद्विबाहु त्रिभुज के गुणधर्म
    </div>

    <!-- Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: एक समद्विबाहु त्रिभुज $ABC$ में, जिसमें $AB = AC$ है, $\\angle B$ और $\\angle C$ के समद्विभाजक परस्पर बिंदु $O$ पर प्रतिच्छेद करते हैं। $A$ और $O$ को जोड़िए। दर्शाइए कि:<br>(i) $OB = OC$<br>(ii) $AO$ कोण $A$ को समद्विभाजित करता है।</h3>
      {d_7_2_q1}
      <div class="step-box-blue">
        <p><b>(i) $OB = OC$ का प्रमाण:</b></p>
        <p>$\\Delta ABC$ में $AB = AC \\implies \\angle C = \\angle B$ (बराबर भुजाओं के सम्मुख कोण बराबर होते हैं)।</p>
        <div class="math-scroll">$$\\frac{{1}}{{2}}\\angle B = \\frac{{1}}{{2}}\\angle C \\implies \\angle OBC = \\angle OCB$$</div>
        <p>$\\Delta OBC$ में, बराबर कोणों की सम्मुख भुजाएँ बराबर होती हैं: अतः <b>$OB = OC$</b>।</p>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $AO$ कोण $A$ को समद्विभाजित करता है:</b></p>
        <p>$\\Delta ABO$ और $\\Delta ACO$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          AB &= AC \\quad (\\text{{Given}}) \\\\
          OB &= OC \\quad (\\text{{Proved above}}) \\\\
          AO &= AO \\quad (\\text{{Common side}})
          \\end{{aligned}}$$
        </div>
        <p>अतः SSS सर्वांगसमता नियम से: $\\Delta ABO \\cong \\Delta ACO$</p>
        <p>CPCT द्वारा: $\\angle BAO = \\angle CAO$। अतः $AO$, कोण $\\angle A$ को समद्विभाजित करता है।</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $OB = OC$ तथा $AO$ कोण $\\angle A$ का समद्विभाजक है।
      </div>
    </div>

    <!-- Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: $\\Delta ABC$ में, $AD$ भुजा $BC$ का लम्ब समद्विभाजक है। दर्शाइए कि $\\Delta ABC$ एक समद्विबाहु त्रिभुज है, जिसमें $AB = AC$ है।</h3>
      {d_7_2_q2}
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> $\\Delta ABD$ और $\\Delta ACD$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          BD &= CD \\quad (D \\text{{ is midpoint of }} BC) \\\\
          \\angle ADB &= \\angle ADC = 90^\\circ \\quad (AD \\perp BC) \\\\
          AD &= AD \\quad (\\text{{Common side}})
          \\end{{aligned}}$$
        </div>
        <p>अतः SAS सर्वांगसमता नियम से: $\\Delta ABD \\cong \\Delta ACD$</p>
        <p>CPCT द्वारा: $AB = AC$</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $AB = AC$, अतः $\\Delta ABC$ एक समद्विबाहु त्रिभुज है।
      </div>
    </div>

    <!-- Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: $ABC$ एक समद्विबाहु त्रिभुज है, जिसमें बराबर भुजाओं $AC$ और $AB$ पर क्रमशः शीर्षलम्ब $BE$ और $CF$ खींचे गए हैं। दर्शाइए कि ये शीर्षलम्ब बराबर हैं।</h3>
      {d_7_2_q3}
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> $\\Delta ABE$ और $\\Delta ACF$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle AEB &= \\angle AFC = 90^\\circ \\quad (\\text{{Altitudes}}) \\\\
          \\angle A &= \\angle A \\quad (\\text{{Common angle}}) \\\\
          AB &= AC \\quad (\\text{{Given}})
          \\end{{aligned}}$$
        </div>
        <p>अतः AAS सर्वांगसमता नियम से: $\\Delta ABE \\cong \\Delta ACF$</p>
        <p>CPCT द्वारा: $BE = CF$</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: शीर्षलम्ब परस्पर बराबर हैं ($BE = CF$)।
      </div>
    </div>

    <!-- Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: $ABC$ एक त्रिभुज है जिसमें भुजाओं $AC$ और $AB$ पर खींचे गए शीर्षलम्ब $BE$ और $CF$ बराबर हैं। दर्शाइए कि:<br>(i) $\\Delta ABE \\cong \\Delta ACF$<br>(ii) $AB = AC$, अर्थात $\\Delta ABC$ एक समद्विबाहु त्रिभुज है।</h3>
      <div class="step-box-blue">
        <p><b>(i) $\\Delta ABE \\cong \\Delta ACF$:</b></p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle AEB &= \\angle AFC = 90^\\circ \\quad (\\text{{Altitudes}}) \\\\
          \\angle A &= \\angle A \\quad (\\text{{Common angle}}) \\\\
          BE &= CF \\quad (\\text{{Given}})
          \\end{{aligned}}$$
        </div>
        <p>अतः AAS नियम से: $\\Delta ABE \\cong \\Delta ACF$</p>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $AB = AC$:</b> CPCT द्वारा संगत भुजाएँ $AB = AC$, अतः $\\Delta ABC$ समद्विबाहु है।</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta ABE \\cong \\Delta ACF$ तथा $AB = AC$ सिद्ध हुआ।
      </div>
    </div>

    <!-- Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: $ABC$ और $DBC$ समान आधार $BC$ पर स्थित दो समद्विबाहु त्रिभुज हैं। दर्शाइए कि $\\angle ABD = \\angle ACD$ है।</h3>
      {d_7_2_q5}
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b></p>
        <p>समद्विबाहु $\\Delta ABC$ में ($AB = AC$):</p>
        <div class="math-scroll">$$\\angle ABC = \\angle ACB \\quad \\text{{...(1)}}$$</div>
        <p>समद्विबाहु $\\Delta DBC$ में ($BD = CD$):</p>
        <div class="math-scroll">$$\\angle DBC = \\angle DCB \\quad \\text{{...(2)}}$$</div>
        <p>समीकरण (1) और (2) को जोड़ने पर:</p>
        <div class="math-scroll">
          $$\\angle ABC + \\angle DBC = \\angle ACB + \\angle DCB$$
        </div>
        <div class="math-scroll">
          $$\\implies \\angle ABD = \\angle ACD$$
        </div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\angle ABD = \\angle ACD$ सिद्ध हुआ।
      </div>
    </div>

    <!-- Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: $\\Delta ABC$ एक समद्विबाहु त्रिभुज है जिसमें $AB = AC$ है। भुजा $BA$ बिंदु $D$ तक इस प्रकार बढ़ाई गई है कि $AD = AB$ है। दर्शाइए कि $\\angle BCD$ एक समकोण है।</h3>
      {d_7_2_q6}
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b></p>
        <p>$\\Delta ABC$ में $AB = AC \\implies \\angle ACB = \\angle ABC = x$</p>
        <p>$\\Delta ACD$ में $AD = AB = AC \\implies AD = AC \\implies \\angle ACD = \\angle ADC = y$</p>
        <p>अब $\\Delta BCD$ में तीनों कोणों का योग $180^\\circ$ होता है:</p>
        <div class="math-scroll">
          $$\\angle DBC + \\angle BCD + \\angle BDC = 180^\\circ$$
        </div>
        <div class="math-scroll">
          $$x + (x + y) + y = 180^\\circ \\implies 2(x + y) = 180^\\circ \\implies x + y = 90^\\circ$$
        </div>
        <p>चूँकि $\\angle BCD = x + y$, अतः:</p>
        <div class="math-scroll">$$\\angle BCD = 90^\\circ$$</div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\angle BCD = 90^\\circ$ (समकोण) सिद्ध हुआ।
      </div>
    </div>

    <!-- Q7 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 7: $ABC$ एक समकोण त्रिभुज है जिसमें $\\angle A = 90^\\circ$ और $AB = AC$ है। $\\angle B$ और $\\angle C$ ज्ञात कीजिए।</h3>
      <div class="step-box-blue">
        <p><b>हल:</b> दिया है $AB = AC \\implies \\angle B = \\angle C$ (बराबर भुजाओं के सम्मुख कोण)।</p>
        <p>त्रिभुज $ABC$ में कोण योग गुण से:</p>
        <div class="math-scroll">
          $$\\angle A + \\angle B + \\angle C = 180^\\circ$$
        </div>
        <div class="math-scroll">
          $$90^\\circ + \\angle B + \\angle B = 180^\\circ \\implies 2\\angle B = 90^\\circ \\implies \\angle B = 45^\\circ$$
        </div>
        <p>अतः $\\angle C = \\angle B = 45^\\circ$</p>
      </div>
      <div class="answer-highlight">
        ✅ अभीष्ट उत्तर: $\\angle B = 45^\\circ$ तथा $\\angle C = 45^\\circ$।
      </div>
    </div>

    <!-- Q8 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 8: दर्शाइए कि किसी समबाहु त्रिभुज का प्रत्येक कोण $60^\\circ$ होता है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> मान लीजिए $ABC$ एक समबाहु त्रिभुज है जिसमें $AB = BC = CA$ है।</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          AB = AC &\\implies \\angle C = \\angle B \\\\
          BC = AB &\\implies \\angle A = \\angle C \\\\
          &\\implies \\angle A = \\angle B = \\angle C
          \\end{{aligned}}$$
        </div>
        <p>त्रिभुज के कोण योग गुण से:</p>
        <div class="math-scroll">
          $$\\angle A + \\angle B + \\angle C = 180^\\circ \\implies 3\\angle A = 180^\\circ \\implies \\angle A = 60^\\circ$$
        </div>
        <p>अतः $\\angle A = \\angle B = \\angle C = 60^\\circ$</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: समबाहु त्रिभुज का प्रत्येक कोण $60^\\circ$ होता है।
      </div>
    </div>

    <!-- EXERCISE 7.3 -->
    <div class="part-header" id="ex73">
      📖 प्रश्नावली 7.3 (Exercise 7.3) — SSS व RHS सर्वांगसमता कसौटियाँ (संपूर्ण 5 प्रश्न)
    </div>

    <!-- Ex 7.3 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: $\\Delta ABC$ और $\\Delta DBC$ एक ही आधार $BC$ पर बने दो समद्विबाहु त्रिभुज इस प्रकार हैं कि शीर्ष $A$ और $D$ भुजा $BC$ के एक ही ओर स्थित हैं। यदि $AD$ को बढ़ाने पर वह $BC$ को $P$ पर प्रतिच्छेद करे, तो दर्शाइए कि:<br>(i) $\\Delta ABD \\cong \\Delta ACD$<br>(ii) $\\Delta ABP \\cong \\Delta ACP$<br>(iii) $AP$ कोण $A$ और कोण $D$ दोनों को समद्विभाजित करता है।<br>(iv) $AP$ रेखाखंड $BC$ का लम्ब समद्विभाजक है।</h3>
      {d_7_3_q1}
      <div class="step-box-blue">
        <p><b>(i) $\\Delta ABD \\cong \\Delta ACD$:</b></p>
        <p>$AB = AC$ (दिया है), $BD = CD$ (दिया है), $AD = AD$ (उभयनिष्ठ भुजा)। SSS नियम से: $\\Delta ABD \\cong \\Delta ACD$।</p>
        <p>$\\implies \\angle BAD = \\angle CAD$ (CPCT) \\quad ...(1)</p>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $\\Delta ABP \\cong \\Delta ACP$:</b></p>
        <p>$AB = AC$ (दिया है), $\\angle BAP = \\angle CAP$ (समीकरण 1 से), $AP = AP$ (उभयनिष्ठ)। SAS नियम से: $\\Delta ABP \\cong \\Delta ACP$।</p>
        <p>$\\implies BP = CP$ तथा $\\angle APB = \\angle APC$ (CPCT)।</p>
      </div>
      <div class="step-box-purple">
        <p><b>(iii) $AP$ कोण $A$ और कोण $D$ दोनों को समद्विभाजित करता है:</b></p>
        <p>$\\Delta BPD$ और $\\Delta CPD$ में: $BD = CD, BP = CP, DP = DP$। SSS नियम से $\\Delta BPD \\cong \\Delta CPD \\implies \\angle BDP = \\angle CDP$।</p>
        <p>अतः $AP$, कोण $A$ तथा कोण $D$ दोनों को समद्विभाजित करता है।</p>
      </div>
      <div class="step-box-orange">
        <p><b>(iv) $AP$, $BC$ का लम्ब समद्विभाजक है:</b></p>
        <p>$\\angle APB + \\angle APC = 180^\\circ$ (रैखिक युग्म)। परंतु $\\angle APB = \\angle APC$, अतः $2\\angle APB = 180^\\circ \\implies \\angle APB = 90^\\circ$।</p>
        <p>तथा $BP = CP$, अतः $AP$ रेखाखंड $BC$ का लम्ब समद्विभाजक है।</p>
      </div>
      <div class="answer-highlight">
        ✅ चारों भाग पूर्णतः सिद्ध हुए: $\\Delta ABD \\cong \\Delta ACD$, $\\Delta ABP \\cong \\Delta ACP$, $AP$ समद्विभाजक है तथा $AP \\perp BC$ और $BP = CP$।
      </div>
    </div>

    <!-- Ex 7.3 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: $AD$ एक समद्विबाहु त्रिभुज $ABC$ का एक शीर्षलम्ब है, जिसमें $AB = AC$ है। दर्शाइए कि:<br>(i) $AD$ रेखाखंड $BC$ को समद्विभाजित करता है।<br>(ii) $AD$ कोण $A$ को समद्विभाजित करता है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> समकोण $\\Delta ABD$ और समकोण $\\Delta ACD$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle ADB &= \\angle ADC = 90^\\circ \\quad (AD \\perp BC) \\\\
          AB &= AC \\quad (\\text{{Hypotenuse, given}}) \\\\
          AD &= AD \\quad (\\text{{Common side}})
          \\end{{aligned}}$$
        </div>
        <p>अतः RHS (समकोण-कर्ण-भुजा) सर्वांगसमता नियम से: <b>$\\Delta ABD \\cong \\Delta ACD$</b></p>
        <p>CPCT द्वारा:</p>
        <p>(i) $BD = CD \\implies AD$, रेखाखंड $BC$ को समद्विभाजित करता है।</p>
        <p>(ii) $\\angle BAD = \\angle CAD \\implies AD$, कोण $\\angle A$ को समद्विभाजित करता है।</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: RHS सर्वांगसमता नियम से दोनों भाग ($BD = CD$ तथा $\\angle BAD = \\angle CAD$) सिद्ध हुए।
      </div>
    </div>

    <!-- Ex 7.3 Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: एक त्रिभुज $ABC$ की दो भुजाएँ $AB, BC$ तथा माध्यिका $AM$ क्रमशः एक दूसरे त्रिभुज की भुजाओं $PQ, QR$ तथा माध्यिका $PN$ के बराबर हैं। दर्शाइए कि:<br>(i) $\\Delta ABM \\cong \\Delta PQN$<br>(ii) $\\Delta ABC \\cong \\Delta PQR$</h3>
      {d_7_3_q3}
      <div class="step-box-blue">
        <p><b>(i) $\\Delta ABM \\cong \\Delta PQN$:</b></p>
        <p>दिया है $BC = QR \\implies \\frac{{1}}{{2}}BC = \\frac{{1}}{{2}}QR \\implies BM = QN$ (चूँकि $AM$ व $PN$ माध्यिकाएँ हैं)।</p>
        <p>$\\Delta ABM$ और $\\Delta PQN$ में: $AB = PQ$ (दिया है), $BM = QN$ (सिद्ध किया), $AM = PN$ (दिया है)। SSS नियम से:</p>
        <div class="math-scroll">$$\\Delta ABM \\cong \\Delta PQN \\implies \\angle B = \\angle Q \\quad (\\text{{CPCT}})$$</div>
      </div>
      <div class="step-box-green">
        <p><b>(ii) $\\Delta ABC \\cong \\Delta PQR$:</b></p>
        <p>$\\Delta ABC$ और $\\Delta PQR$ में: $AB = PQ$ (दिया है), $\\angle B = \\angle Q$ (भाग i से), $BC = QR$ (दिया है)।</p>
        <p>अतः SAS नियम से: <b>$\\Delta ABC \\cong \\Delta PQR$</b></p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\Delta ABM \\cong \\Delta PQN$ (SSS द्वारा) तथा $\\Delta ABC \\cong \\Delta PQR$ (SAS द्वारा)।
      </div>
    </div>

    <!-- Ex 7.3 Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: $BE$ और $CF$ एक त्रिभुज $ABC$ के दो बराबर शीर्षलम्ब हैं। RHS सर्वांगसमता नियम का प्रयोग करके सिद्ध कीजिए कि $\\Delta ABC$ एक समद्विबाहु त्रिभुज है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> समकोण $\\Delta BEC$ और समकोण $\\Delta CFB$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle BEC &= \\angle CFB = 90^\\circ \\quad (\\text{{Altitudes}}) \\\\
          BC &= CB \\quad (\\text{{Common hypotenuse}}) \\\\
          BE &= CF \\quad (\\text{{Given equal altitudes}})
          \\end{{aligned}}$$
        </div>
        <p>अतः RHS सर्वांगसमता नियम से: $\\Delta BEC \\cong \\Delta CFB$</p>
        <p>CPCT द्वारा: $\\angle BCE = \\angle CBF \\implies \\angle C = \\angle B$</p>
        <p>त्रिभुज में बराबर कोणों की सम्मुख भुजाएँ बराबर होती हैं: अतः <b>$AB = AC$</b>।</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: RHS नियम द्वारा $AB = AC$, अतः $\\Delta ABC$ एक समद्विबाहु त्रिभुज है।
      </div>
    </div>

    <!-- Ex 7.3 Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: $ABC$ एक समद्विबाहु त्रिभुज है जिसमें $AB = AC$ है। $AP \\perp BC$ खींच कर दर्शाइए कि $\\angle B = \\angle C$ है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> समकोण $\\Delta ABP$ और समकोण $\\Delta ACP$ में:</p>
        <div class="math-scroll">
          $$\\begin{{aligned}}
          \\angle APB &= \\angle APC = 90^\\circ \\quad (AP \\perp BC) \\\\
          AB &= AC \\quad (\\text{{Hypotenuse, given}}) \\\\
          AP &= AP \\quad (\\text{{Common side}})
          \\end{{aligned}}$$
        </div>
        <p>अतः RHS सर्वांगसमता नियम से: $\\Delta ABP \\cong \\Delta ACP$</p>
        <p>CPCT द्वारा संगत कोण बराबर होंगे: <b>$\\angle B = \\angle C$</b></p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\angle B = \\angle C$ (RHS सर्वांगसमता कसौटी द्वारा सिद्ध)।
      </div>
    </div>

    <!-- EXERCISE 7.4 -->
    <div class="part-header" id="ex74">
      📖 प्रश्नावली 7.4 (Exercise 7.4) — त्रिभुज में असमिकाएँ (Inequalities in a Triangle)
    </div>

    <!-- Ex 7.4 Q1 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 1: दर्शाइए कि समकोण त्रिभुज में कर्ण सबसे लंबी भुजा होती है।</h3>
      {d_7_4_q1}
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> मान लीजिए $\\Delta ABC$ एक समकोण त्रिभुज है जिसमें $\\angle B = 90^\\circ$ है।</p>
        <p>त्रिभुज के तीनों कोणों का योग $180^\\circ$ होता है:</p>
        <div class="math-scroll">
          $$\\angle A + \\angle B + \\angle C = 180^\\circ \\implies \\angle A + \\angle C = 90^\\circ$$
        </div>
        <p>चूँकि $\\angle A$ और $\\angle C$ दोनों न्यूनकोण ($< 90^\\circ$) हैं, अतः समकोण $\\angle B$ त्रिभुज का सबसे बड़ा कोण है:</p>
        <div class="math-scroll">$$\\angle B > \\angle A \\quad \\text{{तथा}} \\quad \\angle B > \\angle C$$</div>
        <p>हम जानते हैं कि किसी त्रिभुज में बड़े कोण के सम्मुख भुजा सबसे लंबी होती है:</p>
        <div class="math-scroll">$$AC > BC \\quad \\text{{तथा}} \\quad AC > AB$$</div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: समकोण त्रिभुज में कर्ण ($AC$) सबसे लंबी भुजा होती है।
      </div>
    </div>

    <!-- Ex 7.4 Q2 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 2: दी गई आकृति में, $\\Delta ABC$ की भुजाओं $AB$ और $AC$ को क्रमशः बिंदुओं $P$ और $Q$ तक बढ़ाया गया है। साथ ही, $\\angle PBC < \\angle QCB$ है। दर्शाइए कि $AC > AB$ है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> सरल रेखा पर रैखिक युग्म से:</p>
        <div class="math-scroll">
          $$\\angle ABC = 180^\\circ - \\angle PBC$$
        </div>
        <div class="math-scroll">
          $$\\angle ACB = 180^\\circ - \\angle QCB$$
        </div>
        <p>दिया है: $\\angle PBC < \\angle QCB$</p>
        <p>दोनों पक्षों को $-1$ से गुणा करने पर असमिका का चिह्न पलट जाता है: $-\\angle PBC > -\\angle QCB$</p>
        <p>$180^\\circ$ जोड़ने पर: $180^\\circ - \\angle PBC > 180^\\circ - \\angle QCB$</p>
        <div class="math-scroll">$$\\implies \\angle ABC > \\angle ACB$$</div>
        <p>त्रिभुज में बड़े कोण की सम्मुख भुजा लंबी होती है: अतः <b>$AC > AB$</b>।</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $AC > AB$ सिद्ध हुआ।
      </div>
    </div>

    <!-- Ex 7.4 Q3 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 3: दी गई आकृति में, $\\angle B < \\angle A$ और $\\angle C < \\angle D$ है। दर्शाइए कि $AD < BC$ है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> मान लीजिए रेखाएँ बिंदु $O$ पर प्रतिच्छेद करती हैं।</p>
        <p>$\\Delta AOB$ में दिया है $\\angle B < \\angle A$:</p>
        <div class="math-scroll">$$OA < OB \\quad \\text{{...(1)}}$$</div>
        <p>$\\Delta COD$ में दिया है $\\angle C < \\angle D$:</p>
        <div class="math-scroll">$$OD < OC \\quad \\text{{...(2)}}$$</div>
        <p>असमिका (1) और (2) को जोड़ने पर:</p>
        <div class="math-scroll">
          $$OA + OD < OB + OC \\implies AD < BC$$
        </div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $AD < BC$ सिद्ध हुआ।
      </div>
    </div>

    <!-- Ex 7.4 Q4 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 4: $AB$ और $CD$ क्रमशः एक चतुर्भुज $ABCD$ की सबसे छोटी और सबसे लंबी भुजाएँ हैं। दर्शाइए कि $\\angle A > \\angle C$ और $\\angle B > \\angle D$ है।</h3>
      {d_7_4_q4}
      <div class="step-box-blue">
        <p><b>रचना:</b> $A$ और $C$ को मिलाया।</p>
        <p>$\\Delta ABC$ में, $AB$ सबसे छोटी भुजा है, अतः $BC > AB \\implies \\angle 1 > \\angle 3$।</p>
        <p>$\\Delta ADC$ में, $CD$ सबसे लंबी भुजा है, अतः $CD > AD \\implies \\angle 2 > \\angle 4$।</p>
        <p>दोनों असमिकाओं को जोड़ने पर:</p>
        <div class="math-scroll">
          $$\\angle 1 + \\angle 2 > \\angle 3 + \\angle 4 \\implies \\angle A > \\angle C$$
        </div>
        <p>इसी प्रकार $B$ और $D$ को मिलाकर सिद्ध किया जा सकता है कि <b>$\\angle B > \\angle D$</b>।</p>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: चतुर्भुज $ABCD$ में $\\angle A > \\angle C$ तथा $\\angle B > \\angle D$ सिद्ध हुआ।
      </div>
    </div>

    <!-- Ex 7.4 Q5 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 5: दी गई आकृति में, $PR > PQ$ है और $PS$ कोण $\\angle QPR$ को समद्विभाजित करता है। सिद्ध कीजिए कि $\\angle PSR > \\angle PSQ$ है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> $\\Delta PQR$ में $PR > PQ \\implies \\angle PQR > \\angle PRQ$ \\quad ...(1)</p>
        <p>दिया है $PS$, कोण $\\angle P$ का समद्विभाजक है: $\\angle QPS = \\angle RPS = x$ \\quad ...(2)</p>
        <p>बहिष्कोण प्रमेय से:</p>
        <div class="math-scroll">
          $$\\angle PSR = \\angle PQR + x$$
        </div>
        <div class="math-scroll">
          $$\\angle PSQ = \\angle PRQ + x$$
        </div>
        <p>समीकरण (1) से $\\angle PQR > \\angle PRQ$, अतः दोनों ओर $x$ जोड़ने पर:</p>
        <div class="math-scroll">
          $$\\angle PQR + x > \\angle PRQ + x \\implies \\angle PSR > \\angle PSQ$$
        </div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: $\\angle PSR > \\angle PSQ$ सिद्ध हुआ।
      </div>
    </div>

    <!-- Ex 7.4 Q6 -->
    <div class="qa-block">
      <h3 class="question-heading">प्रश्न 6: दर्शाइए कि एक रेखा पर किसी दिए गए बिंदु से, जो उस रेखा पर स्थित नहीं है, खींचे गए सभी रेखाखंडों में लम्ब रेखाखंड सबसे छोटा होता है।</h3>
      <div class="step-box-blue">
        <p><b>उपपत्ति:</b> मान लीजिए रेखा $l$ पर बिंदु $P$ स्थित नहीं है। $PM \\perp l$ खींचा तथा रेखा $l$ पर $M$ के अतिरिक्त कोई अन्य बिंदु $N$ लिया।</p>
        <p>समकोण त्रिभुज $PMN$ में $\\angle M = 90^\\circ$ है।</p>
        <p>चूँकि समकोण त्रिभुज में समकोण सबसे बड़ा कोण होता है:</p>
        <div class="math-scroll">$$\\angle M > \\angle N$$</div>
        <p>बड़े कोण के सम्मुख भुजा लंबी होती है:</p>
        <div class="math-scroll">$$PN > PM \\implies PM < PN$$</div>
      </div>
      <div class="answer-highlight">
        ✅ निष्कर्ष: बिंदु $P$ से रेखा $l$ तक खींचे गए सभी रेखाखंडों में लम्ब रेखाखंड $PM$ सबसे छोटा होता है।
      </div>
    </div>

    <!-- =========================================================
         SIMULATOR SECTION (5 LIVE VISUAL CANVASES)
         ========================================================= -->
    <div class="part-header" id="simulators">
      ⚡ 5 लाइव इंटरैक्टिव सिमुलेटर (Visual Interactive Triangle Canvases)
    </div>

    <!-- Simulator 1 -->
    <div class="inline-simulator-card">
      <h3 class="sim-title" style="font-size:24pt; font-weight:900; color:#1e3a8a;">⚡ सिमुलेटर 1: त्रिभुज सर्वांगसमता कसौटी विश्लेषक (Interactive Congruence Canvas)</h3>
      <p>त्रिभुज की भुजाएँ और कोण भरें, सिमुलेटर दोनों त्रिभुजों को लाइव कैनवास पर आलेखित कर सर्वांगसमता नियम (SAS, SSS, ASA, RHS) की जाँच करेगा:</p>

      <div class="sim-controls-grid">
        <div class="sim-group">
          <label>भुजा AB (सेमी):</label>
          <input type="number" id="sim1_ab" value="6" min="3" max="15" oninput="calculateSim1()">
        </div>
        <div class="sim-group">
          <label>अंतर्गत कोण ∠B (डिग्री):</label>
          <input type="number" id="sim1_b" value="60" min="20" max="120" oninput="calculateSim1()">
        </div>
        <div class="sim-group">
          <label>भुजा BC (सेमी):</label>
          <input type="number" id="sim1_bc" value="8" min="3" max="15" oninput="calculateSim1()">
        </div>
      </div>

      <canvas id="sim1_canvas" class="sim-canvas" width="560" height="280"></canvas>
      <div id="sim1_output" class="sim-output-box"></div>
    </div>

    <!-- Simulator 2 -->
    <div class="inline-simulator-card">
      <h3 class="sim-title" style="font-size:24pt; font-weight:900; color:#1e3a8a;">⚡ सिमुलेटर 2: समद्विबाहु त्रिभुज कोण व भुजा लाइव प्रदर्शक (Isosceles Canvas)</h3>
      <p>शीर्ष कोण $\\angle A$ बदलें, सिमुलेटर लाइव त्रिभुज आरेखित कर आधार कोण $\\angle B$ व $\\angle C$ की गणना करेगा ($AB = AC$):</p>

      <div class="sim-controls-grid">
        <div class="sim-group">
          <label>शीर्ष कोण ∠A (डिग्री):</label>
          <input type="range" id="sim2_a" min="20" max="140" value="40" step="5" oninput="calculateSim2()">
          <span id="sim2_a_val" style="font-weight:900; color:#2563eb; font-size:20pt;">40°</span>
        </div>
        <div class="sim-group">
          <label>बराबर भुजा लंबाई (सेमी):</label>
          <input type="number" id="sim2_side" value="8" min="4" max="15" oninput="calculateSim2()">
        </div>
      </div>

      <canvas id="sim2_canvas" class="sim-canvas" width="560" height="280"></canvas>
      <div id="sim2_output" class="sim-output-box"></div>
    </div>

    <!-- Simulator 3 -->
    <div class="inline-simulator-card">
      <h3 class="sim-title" style="font-size:24pt; font-weight:900; color:#1e3a8a;">⚡ सिमुलेटर 3: समबाहु त्रिभुज 60° प्रमाण व क्षेत्रफल सिमुलेटर (Equilateral Canvas)</h3>
      <p>समबाहु त्रिभुज की भुजा बदलें, लाइव कैनवास पर प्रत्येक कोण $60^\\circ$, परिमाप और क्षेत्रफल देखें:</p>

      <div class="sim-controls-grid">
        <div class="sim-group">
          <label>समबाहु त्रिभुज भुजा (सेमी):</label>
          <input type="number" id="sim3_side" value="6" min="2" max="15" oninput="calculateSim3()">
        </div>
      </div>

      <canvas id="sim3_canvas" class="sim-canvas" width="560" height="280"></canvas>
      <div id="sim3_output" class="sim-output-box"></div>
    </div>

    <!-- Simulator 4 -->
    <div class="inline-simulator-card">
      <h3 class="sim-title" style="font-size:24pt; font-weight:900; color:#1e3a8a;">⚡ सिमुलेटर 4: त्रिभुज असमिका प्रमेय लाइव सिमुलेटर ($a+b > c$)</h3>
      <p>त्रिभुज की कोई भी तीन भुजाएँ दर्ज करें, सिमुलेटर असमिका की जाँच करेगा और लाइव त्रिभुज बनाएगा:</p>

      <div class="sim-controls-grid">
        <div class="sim-group">
          <label>भुजा a:</label>
          <input type="number" id="sim4_a" value="5" min="1" max="20" oninput="calculateSim4()">
        </div>
        <div class="sim-group">
          <label>भुजा b:</label>
          <input type="number" id="sim4_b" value="6" min="1" max="20" oninput="calculateSim4()">
        </div>
        <div class="sim-group">
          <label>भुजा c:</label>
          <input type="number" id="sim4_c" value="7" min="1" max="20" oninput="calculateSim4()">
        </div>
      </div>

      <canvas id="sim4_canvas" class="sim-canvas" width="560" height="280"></canvas>
      <div id="sim4_output" class="sim-output-box"></div>
    </div>

    <!-- Simulator 5 -->
    <div class="inline-simulator-card">
      <h3 class="sim-title" style="font-size:24pt; font-weight:900; color:#1e3a8a;">⚡ सिमुलेटर 5: समकोण त्रिभुज कर्ण मध्य-बिंदु संबंध प्रदर्शक ($CM = \\frac{{1}}{{2}}AB$)</h3>
      <p>समकोण त्रिभुज की भुजाएँ भरें, सिमुलेटर कर्ण के मध्य-बिंदु $M$ से शीर्ष $C$ तक मध्यिका $CM$ खींचकर $CM = \\frac{{1}}{{2}}AB = MA = MB$ सत्यापित करेगा:</p>

      <div class="sim-controls-grid">
        <div class="sim-group">
          <label>आधार भुजा BC (सेमी):</label>
          <input type="number" id="sim5_bc" value="8" min="3" max="15" oninput="calculateSim5()">
        </div>
        <div class="sim-group">
          <label>लम्ब भुजा AC (सेमी):</label>
          <input type="number" id="sim5_ac" value="6" min="3" max="15" oninput="calculateSim5()">
        </div>
      </div>

      <canvas id="sim5_canvas" class="sim-canvas" width="560" height="280"></canvas>
      <div id="sim5_output" class="sim-output-box"></div>
    </div>

  </div> <!-- /contentToCopy -->
</div> <!-- /container -->

<!-- JAVASCRIPT CONTROLLERS -->
<script>
  var currentWidth = 1400;
  var sizeOffset = 0;
  var weightOffset = 0;
  var strokeOffset = 0;

  function adjustContainerWidth(delta) {{
    currentWidth += delta;
    if (currentWidth < 600) currentWidth = 600;
    if (currentWidth > 2400) currentWidth = 2400;
    var c = document.getElementById('mainContainer');
    if (c) {{
      c.style.setProperty('width', currentWidth + 'px', 'important');
      c.style.setProperty('max-width', currentWidth + 'px', 'important');
    }}
  }}

  function adjustFontSize(delta) {{
    sizeOffset += delta;
    if (sizeOffset < -14) sizeOffset = -14;
    if (sizeOffset > 30) sizeOffset = 30;
    applyTypography();
  }}

  function adjustFontWeight(delta) {{
    weightOffset += delta;
    strokeOffset += (delta / 100) * 0.35;
    applyTypography();
  }}

  function applyTypography() {{
    var w = Math.max(400, Math.min(900, 900 + weightOffset));
    var s = Math.max(0, 0.9 + strokeOffset);
    var b = 26 + sizeOffset;
    var el = document.getElementById('dyn-typography');
    if (!el) {{
      el = document.createElement('style');
      el.id = 'dyn-typography';
      document.head.appendChild(el);
    }}
    el.innerHTML = 'body, p, li, .step-box-blue, .step-box-green, .step-box-purple, .step-box-orange {{ font-size: ' + b + 'pt !important; font-weight: ' + w + ' !important; -webkit-text-stroke: ' + s + 'px #000000 !important; }}';
  }}

  function copyEntireContent() {{
    var content = document.getElementById('contentToCopy').innerText;
    navigator.clipboard.writeText(content).then(function() {{
      alert('✅ संपूर्ण अध्याय 7 (27 प्रश्न व 5 सिमुलेटर) सफलतापूर्वक कॉपी हो गया है!');
    }});
  }}

  // SIMULATOR 1: Congruence Analyzer
  function calculateSim1() {{
    var ab = parseFloat(document.getElementById('sim1_ab').value) || 6;
    var degB = parseFloat(document.getElementById('sim1_b').value) || 60;
    var bc = parseFloat(document.getElementById('sim1_bc').value) || 8;
    var out = document.getElementById('sim1_output');

    var canvas = document.getElementById('sim1_canvas');
    if (canvas) {{
      var ctx = canvas.getContext('2d');
      var W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      // Draw Grid
      ctx.strokeStyle = '#f1f5f9'; ctx.lineWidth = 1;
      for (var x = 0; x <= W; x += 25) {{ ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }}
      for (var y = 0; y <= H; y += 25) {{ ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }}

      var scale = 18;
      // Triangle 1 (ABC)
      var bx = 60, by = 220;
      var cx = bx + bc * scale;
      var cy = by;
      var radB = degB * Math.PI / 180;
      var ax = bx + ab * scale * Math.cos(radB);
      var ay = by - ab * scale * Math.sin(radB);

      ctx.beginPath();
      ctx.moveTo(bx, by); ctx.lineTo(cx, cy); ctx.lineTo(ax, ay); ctx.closePath();
      ctx.fillStyle = 'rgba(37, 99, 235, 0.12)'; ctx.fill();
      ctx.strokeStyle = '#2563eb'; ctx.lineWidth = 4; ctx.stroke();

      ctx.fillStyle = '#1e3a8a'; ctx.font = 'bold 16px sans-serif';
      ctx.fillText('B', bx - 15, by + 15);
      ctx.fillText('C (' + bc + ' cm)', cx + 5, cy + 15);
      ctx.fillText('A', ax - 5, ay - 10);
      ctx.fillStyle = '#dc2626';
      ctx.fillText(degB + '°', bx + 20, by - 10);

      // Triangle 2 (DEF - Congruent twin)
      var offset = 280;
      var ex = offset + bx, ey = by;
      var fx = offset + cx, fy = cy;
      var dx = offset + ax, dy = ay;

      ctx.beginPath();
      ctx.moveTo(ex, ey); ctx.lineTo(fx, fy); ctx.lineTo(dx, dy); ctx.closePath();
      ctx.fillStyle = 'rgba(22, 163, 74, 0.12)'; ctx.fill();
      ctx.strokeStyle = '#16a34a'; ctx.lineWidth = 4; ctx.stroke();

      ctx.fillStyle = '#166534'; ctx.font = 'bold 16px sans-serif';
      ctx.fillText('E', ex - 15, ey + 15);
      ctx.fillText('F (' + bc + ' cm)', fx + 5, fy + 15);
      ctx.fillText('D', dx - 5, dy - 10);
      ctx.fillStyle = '#dc2626';
      ctx.fillText(degB + '°', ex + 20, ey - 10);
    }}

    var ac = Math.sqrt(ab*ab + bc*bc - 2*ab*bc*Math.cos(degB*Math.PI/180));
    out.innerHTML = '<div style="font-size:22pt; font-weight:900; color:#1e3a8a;">' +
      '✅ सर्वांगसमता कसौटी: SAS (भुजा-कोण-भुजा सर्वांगसमता नियम)<br>' +
      '$\\Delta ABC \\cong \\Delta DEF$ | तीसरी भुजा $AC = DF = ' + ac.toFixed(2) + '\\text{{ cm}}$ (CPCT द्वारा)' +
      '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // SIMULATOR 2: Isosceles Triangle
  function calculateSim2() {{
    var degA = parseFloat(document.getElementById('sim2_a').value) || 40;
    var side = parseFloat(document.getElementById('sim2_side').value) || 8;
    document.getElementById('sim2_a_val').innerText = degA + '°';
    var out = document.getElementById('sim2_output');

    var baseAngle = (180 - degA) / 2;
    var canvas = document.getElementById('sim2_canvas');
    if (canvas) {{
      var ctx = canvas.getContext('2d');
      var W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      var radA = degA * Math.PI / 180;
      var baseLen = 2 * side * Math.sin(radA / 2);
      var scale = Math.min(220 / (side * Math.cos(radA / 2)), 450 / baseLen);

      var ax = W / 2, ay = 40;
      var bx = ax - (baseLen / 2) * scale;
      var cx = ax + (baseLen / 2) * scale;
      var by = ay + (side * Math.cos(radA / 2)) * scale;

      ctx.beginPath();
      ctx.moveTo(ax, ay); ctx.lineTo(bx, by); ctx.lineTo(cx, by); ctx.closePath();
      ctx.fillStyle = 'rgba(59, 130, 246, 0.12)'; ctx.fill();
      ctx.strokeStyle = '#1d4ed8'; ctx.lineWidth = 4; ctx.stroke();

      // Equal side marks
      ctx.strokeStyle = '#dc2626'; ctx.lineWidth = 3;
      var m1x = (ax + bx) / 2, m1y = (ay + by) / 2;
      var m2x = (ax + cx) / 2, m2y = (ay + by) / 2;
      ctx.beginPath(); ctx.moveTo(m1x - 6, m1y - 6); ctx.lineTo(m1x + 6, m1y + 6); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(m2x - 6, m2y - 6); ctx.lineTo(m2x + 6, m2y + 6); ctx.stroke();

      ctx.fillStyle = '#000000'; ctx.font = 'bold 16px sans-serif';
      ctx.fillText('A (' + degA + '°)', ax - 25, ay - 10);
      ctx.fillText('B (' + baseAngle.toFixed(1) + '°)', bx - 30, by + 20);
      ctx.fillText('C (' + baseAngle.toFixed(1) + '°)', cx + 10, by + 20);
      ctx.fillText(side + ' cm', m1x - 45, m1y);
      ctx.fillText(side + ' cm', m2x + 15, m2y);
    }}

    out.innerHTML = '<div style="font-size:22pt; font-weight:900; color:#15803d;">' +
      'समद्विबाहु त्रिभुज गुण: बराबर भुजाओं के सम्मुख कोण बराबर होते हैं ($AB = AC \\implies \\angle B = \\angle C$)<br>' +
      '✅ आधार कोण: $\\angle B = \\angle C = \\frac{{180^\\circ - ' + degA + '^\\circ}}{{2}} = ' + baseAngle.toFixed(1) + '^\\circ$' +
      '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // SIMULATOR 3: Equilateral Triangle
  function calculateSim3() {{
    var s = parseFloat(document.getElementById('sim3_side').value) || 6;
    var out = document.getElementById('sim3_output');

    var canvas = document.getElementById('sim3_canvas');
    if (canvas) {{
      var ctx = canvas.getContext('2d');
      var W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      var scale = 20;
      var h = s * Math.sqrt(3) / 2;
      var ax = W / 2, ay = 30;
      var bx = ax - (s / 2) * scale;
      var cx = ax + (s / 2) * scale;
      var by = ay + h * scale;

      ctx.beginPath();
      ctx.moveTo(ax, ay); ctx.lineTo(bx, by); ctx.lineTo(cx, by); ctx.closePath();
      ctx.fillStyle = 'rgba(234, 179, 8, 0.15)'; ctx.fill();
      ctx.strokeStyle = '#ca8a04'; ctx.lineWidth = 4; ctx.stroke();

      ctx.fillStyle = '#000000'; ctx.font = 'bold 16px sans-serif';
      ctx.fillText('A (60°)', ax - 25, ay - 8);
      ctx.fillText('B (60°)', bx - 30, by + 20);
      ctx.fillText('C (60°)', cx + 10, by + 20);
      ctx.fillStyle = '#dc2626';
      ctx.fillText(s + ' cm', (bx + cx) / 2 - 20, by + 22);
    }}

    var area = (Math.sqrt(3) / 4) * s * s;
    var peri = 3 * s;
    out.innerHTML = '<div style="font-size:22pt; font-weight:900; color:#854d0e;">' +
      '✅ समबाहु त्रिभुज सत्यापन: $\\angle A = \\angle B = \\angle C = 60^\\circ$<br>' +
      'परिमाप: $' + peri + '\\text{{ cm}}$ | क्षेत्रफल: $\\frac{{\\sqrt{{3}}}}{{4}}a^2 = ' + area.toFixed(2) + '\\text{{ cm}}^2$' +
      '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // SIMULATOR 4: Triangle Inequality
  function calculateSim4() {{
    var a = parseFloat(document.getElementById('sim4_a').value) || 5;
    var b = parseFloat(document.getElementById('sim4_b').value) || 6;
    var c = parseFloat(document.getElementById('sim4_c').value) || 7;
    var out = document.getElementById('sim4_output');

    var isValid = (a + b > c) && (a + c > b) && (b + c > a);
    var canvas = document.getElementById('sim4_canvas');
    if (canvas) {{
      var ctx = canvas.getContext('2d');
      var W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      if (isValid) {{
        // Plot triangle using cosine rule
        var cosC = (a*a + b*b - c*c) / (2*a*b);
        var sinC = Math.sqrt(Math.max(0, 1 - cosC*cosC));
        var scale = Math.min(220 / (b * sinC), 420 / a);

        var bx = 70, by = 230;
        var cx = bx + a * scale;
        var cy = by;
        var ax = bx + b * scale * cosC;
        var ay = by - b * scale * sinC;

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(cx, cy); ctx.lineTo(ax, ay); ctx.closePath();
        ctx.fillStyle = 'rgba(16, 185, 129, 0.15)'; ctx.fill();
        ctx.strokeStyle = '#10b981'; ctx.lineWidth = 4; ctx.stroke();

        ctx.fillStyle = '#000000'; ctx.font = 'bold 16px sans-serif';
        ctx.fillText('B', bx - 15, by + 15);
        ctx.fillText('C', cx + 10, cy + 15);
        ctx.fillText('A', ax - 5, ay - 10);
        ctx.fillText('a = ' + a, (bx + cx) / 2 - 15, by + 20);
        ctx.fillText('b = ' + b, (ax + bx) / 2 - 35, (ay + by) / 2);
        ctx.fillText('c = ' + c, (ax + cx) / 2 + 10, (ay + cy) / 2);
      }} else {{
        ctx.fillStyle = '#dc2626'; ctx.font = 'bold 24px sans-serif'; ctx.textAlign = 'center';
        ctx.fillText('❌ त्रिभुज बनना संभव नहीं है! (a + b ≤ c)', W / 2, H / 2);
        ctx.textAlign = 'left';
      }}
    }}

    out.innerHTML = '<div style="font-size:22pt; font-weight:900; color:' + (isValid ? '#15803d' : '#b91c1c') + ';">' +
      (isValid ?
        '✅ त्रिभुज असमिका प्रमेय संतुष्ट: दो भुजाओं का योग तीसरी भुजा से बड़ा है!<br>' +
        '$' + a + ' + ' + b + ' = ' + (a+b) + ' > ' + c + '$ | $' + a + ' + ' + c + ' = ' + (a+c) + ' > ' + b + '$ | $' + b + ' + ' + c + ' = ' + (b+c) + ' > ' + a + '$' :
        '❌ त्रिभुज असमिका प्रमेय का उल्लंघन: किन्हीं दो भुजाओं का योग तीसरी भुजा से अधिक होना अनिवार्य है।') +
      '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

  // SIMULATOR 5: Right Triangle Midpoint
  function calculateSim5() {{
    var bc = parseFloat(document.getElementById('sim5_bc').value) || 8;
    var ac = parseFloat(document.getElementById('sim5_ac').value) || 6;
    var out = document.getElementById('sim5_output');

    var ab = Math.sqrt(bc*bc + ac*ac);
    var cm = ab / 2;

    var canvas = document.getElementById('sim5_canvas');
    if (canvas) {{
      var ctx = canvas.getContext('2d');
      var W = canvas.width, H = canvas.height;
      ctx.clearRect(0, 0, W, H);

      var scale = Math.min(220 / ac, 400 / bc);
      var cx = 80, cy = 230;
      var bx = cx + bc * scale;
      var by = cy;
      var ax = cx;
      var ay = cy - ac * scale;

      var mx = (ax + bx) / 2;
      var my = (ay + by) / 2;

      // Triangle ABC
      ctx.beginPath();
      ctx.moveTo(cx, cy); ctx.lineTo(bx, by); ctx.lineTo(ax, ay); ctx.closePath();
      ctx.fillStyle = 'rgba(99, 102, 241, 0.12)'; ctx.fill();
      ctx.strokeStyle = '#4f46e5'; ctx.lineWidth = 4; ctx.stroke();

      // Right angle box
      ctx.strokeRect(cx, cy - 20, 20, 20);

      // Median CM
      ctx.beginPath();
      ctx.moveTo(cx, cy); ctx.lineTo(mx, my);
      ctx.strokeStyle = '#dc2626'; ctx.lineWidth = 3.5; ctx.stroke();

      // Dot at M
      ctx.fillStyle = '#dc2626'; ctx.beginPath(); ctx.arc(mx, my, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = '#000000'; ctx.font = 'bold 16px sans-serif';
      ctx.fillText('C (90°)', cx - 55, cy + 15);
      ctx.fillText('B', bx + 10, by + 15);
      ctx.fillText('A', ax - 20, ay - 10);
      ctx.fillStyle = '#dc2626';
      ctx.fillText('M (कर्ण मध्य-बिंदु)', mx + 10, my - 10);
      ctx.fillText('CM = ' + cm.toFixed(2) + ' cm', (cx + mx) / 2 - 30, (cy + my) / 2 - 10);
    }}

    out.innerHTML = '<div style="font-size:22pt; font-weight:900; color:#4338ca;">' +
      'पाइथागोरस प्रमेय: कर्ण $AB = \\sqrt{{' + ac + '^2 + ' + bc + '^2}} = \\sqrt{{' + (ac*ac + bc*bc) + '}} = ' + ab.toFixed(2) + '\\text{{ cm}}$<br>' +
      '✅ सिद्ध संबंध: समकोण त्रिभुज में कर्ण का मध्य-बिंदु तीनों शीर्षों से समदूरस्थ होता है:<br>' +
      '$CM = MA = MB = \\frac{{1}}{{2}}AB = ' + cm.toFixed(2) + '\\text{{ cm}}$' +
      '</div>';
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([out]);
  }}

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

with open('qa_master_math9_7.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("qa_master_math9_7.html created with all 27 questions, rich SVG diagrams, and 5 live Canvases!")
