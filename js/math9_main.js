/**
 * NCERT Class 9 Mathematics (गणित) Interactive Portal Logic
 * Covers All 12 Chapters (Rationalised Syllabus) with Hindi Medium Focus
 */

const math9Chapters = [
  {
    id: 1,
    num: 1,
    unit: "number",
    unitName: "संख्या पद्धति",
    title: "संख्या पद्धति",
    titleEn: "Number Systems",
    topics: ["परिमेय व अपरिमेय संख्याएँ", "वास्तविक संख्याएँ और दशमलव प्रसार", "संख्या रेखा पर निरूपण", "हर का परिमेयकरण", "घातांक नियम"],
    formulas: [
      "परिमेय संख्या: जिसे p/q के रूप में लिखा जा सके, जहाँ p, q पूर्णांक हैं तथा q ≠ 0",
      "हर का परिमेयकरण: 1/(√a + √b) = (√a - √b) / (a - b)",
      "घातांक नियम: aᵐ × aⁿ = aᵐ⁺ⁿ, \ (aᵐ)ⁿ = aᵐⁿ, \ aᵐ / aⁿ = aᵐ⁻ⁿ, \ aᵐ × bᵐ = (ab)ᵐ",
      "शांत दशमलव प्रसार: यदि q के अभाज्य गुणनखंड 2ⁿ · 5ᵐ रूप के हों"
    ]
  },
  {
    id: 2,
    num: 2,
    unit: "algebra",
    unitName: "बीजगणित",
    title: "बहुपद",
    titleEn: "Polynomials",
    topics: ["एक चर वाले बहुपद", "बहुपद के शून्यक", "शेषफल प्रमेय", "गुणनखंड प्रमेय", "बीजीय सर्वसमिकाएँ"],
    formulas: [
      "रैखिक बहुपद: ax + b का शून्यक x = -b/a",
      "गुणनखंड प्रमेय: यदि p(a) = 0, तो (x - a), p(x) का एक गुणनखंड है",
      "(x + y + z)² = x² + y² + z² + 2xy + 2yz + 2zx",
      "(x + y)³ = x³ + y³ + 3xy(x + y)",
      "(x - y)³ = x³ - y³ - 3xy(x - y)",
      "x³ + y³ + z³ - 3xyz = (x + y + z)(x² + y² + z² - xy - yz - zx)",
      "यदि x + y + z = 0, तो x³ + y³ + z³ = 3xyz"
    ]
  },
  {
    id: 3,
    num: 3,
    unit: "coord",
    unitName: "निर्देशांक ज्यामिति",
    title: "निर्देशांक ज्यामिति",
    titleEn: "Coordinate Geometry",
    topics: ["कार्तीय तल (Cartesian Plane)", "निर्देशांक अक्ष (X व Y अक्ष)", "चतुर्थांश (Quadrants)", "बिंदुओं का आलेखन"],
    formulas: [
      "मूलबिंदु (Origin) के निर्देशांक = (0, 0)",
      "प्रथम चतुर्थांश (I): (+, +), द्वितीय (II): (-, +), तृतीय (III): (-, -), चतुर्थ (IV): (+, -)",
      "X-अक्ष पर किसी बिंदु के निर्देशांक: (x, 0), जहाँ कोटि y = 0",
      "Y-अक्ष पर किसी बिंदु के निर्देशांक: (0, y), जहाँ भुज x = 0",
      "किसी बिंदु (x, y) में: x = भुज (Abscissa), y = कोटि (Ordinate)"
    ]
  },
  {
    id: 4,
    num: 4,
    unit: "algebra",
    unitName: "बीजगणित",
    title: "दो चरों वाले रैखिक समीकरण",
    titleEn: "Linear Equations in Two Variables",
    topics: ["मानक रूप ax + by + c = 0", "समीकरण के अपरिमित रूप से अनेक हल", "रैखिक समीकरण का आलेख", "अक्षों के समांतर रेखाएँ"],
    formulas: [
      "दो चरों वाले रैखिक समीकरण का मानक रूप: ax + by + c = 0 (जहाँ a, b ≠ 0)",
      "दो चरों वाले एक रैखिक समीकरण के अपरिमित रूप से अनेक हल (Infinite Solutions) होते हैं",
      "समीकरण का आलेख सदैव एक सरल रेखा (Straight Line) होता है",
      "x = 0 का आलेख: Y-अक्ष, \ y = 0 का आलेख: X-अक्ष",
      "x = a का आलेख: Y-अक्ष के समांतर रेखा, \ y = b का आलेख: X-अक्ष के समांतर रेखा"
    ]
  },
  {
    id: 5,
    num: 5,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "यूक्लिड की ज्यामिति का परिचय",
    titleEn: "Introduction to Euclid's Geometry",
    topics: ["यूक्लिड की परिभाषाएँ", "अभिगृहीत (Axioms)", "अभिधारणाएँ (Postulates)", "पाँचवीं अभिधारणा के समतुल्य रूप"],
    formulas: [
      "अभिगृहीत 1: वे वस्तुएं जो एक ही वस्तु के बराबर हों, एक दूसरे के बराबर होती हैं",
      "अभिगृहीत 2: यदि बराबरों को बराबरों में जोड़ा जाए, तो पूर्ण भी बराबर होते हैं",
      "अभिगृहीत 3: यदि बराबरों को बराबरों में से घटाया जाए, तो शेषफल भी बराबर होते हैं",
      "अभिगृहीत 4: वे वस्तुएं जो परस्पर संपाती हों, एक दूसरे के बराबर होती हैं",
      "अभिगृहीत 5: पूर्ण अपने भाग से बड़ा होता है",
      "यूक्लिड की 5वीं अभिधारणा: यदि दो रेखाओं पर एक तिर्यक रेखा गिरे और अंतःकोणों का योग 180° से कम हो, तो रेखाएं उसी ओर बढ़ाने पर मिलती हैं"
    ]
  },
  {
    id: 6,
    num: 6,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "रेखाएँ और कोण",
    titleEn: "Lines and Angles",
    topics: ["पूरक व संपूरक कोण", "शीर्षाभिमुख कोण", "समांतर रेखाएँ व तिर्यक रेखा", "संगत व एकांतर कोण", "त्रिभुज का कोण योग गुण"],
    formulas: [
      "पूरक कोण: दो कोण जिनका योग 90° हो (x + y = 90°)",
      "संपूरक कोण: दो कोण जिनका योग 180° हो (x + y = 180°)",
      "रैखिक युग्म अभिगृहीत: आसन्न कोणों का योग 180° होता है",
      "शीर्षाभिमुख कोण परस्पर समान होते हैं",
      "समांतर रेखाओं में: एकांतर अंतःकोण बराबर, संगत कोण बराबर, तथा तिर्यक रेखा के एक ही ओर के अंतःकोणों का योग 180° होता है",
      "त्रिभुज के तीनों अंतःकोणों का योग 180° होता है (∠A + ∠B + ∠C = 180°)",
      "त्रिभुज का बहिष्कोण उसके दोनों सम्मुख अंतःकोणों के योग के बराबर होता है"
    ]
  },
  {
    id: 7,
    num: 7,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "त्रिभुज",
    titleEn: "Triangles",
    topics: ["त्रिभुजों की सर्वांगसमता (Congruence)", "SAS कसौटी", "ASA व AAS कसौटी", "SSS कसौटी", "RHS कसौटी", "समद्विबाहु त्रिभुज प्रमेय"],
    formulas: [
      "सर्वांगसमता: दो आकृतियाँ जिनका आकार और माप समान हो (≅)",
      "CPCT: सर्वांगसम त्रिभुजों के संगत भाग बराबर होते हैं (Corresponding Parts of Congruent Triangles)",
      "SAS: दो भुजाएं और उनके बीच का कोण बराबर हों",
      "ASA: दो कोण और उनके अंतर्गत भुजा बराबर हो",
      "SSS: तीनों संगत भुजाएं बराबर हों",
      "RHS: समकोण, कर्ण और एक भुजा बराबर हो",
      "समद्विबाहु त्रिभुज में बराबर भुजाओं के सम्मुख कोण बराबर होते हैं"
    ]
  },
  {
    id: 8,
    num: 8,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "चतुर्भुज",
    titleEn: "Quadrilaterals",
    topics: ["चतुर्भुज के कोण योग गुण", "समांतर चतुर्भुज के गुण", "आयत, वर्ग व समचतुर्भुज", "मध्य-बिंदु प्रमेय (Mid-point Theorem)"],
    formulas: [
      "चतुर्भुज के चारों अंतःकोणों का योग = 360°",
      "समांतर चतुर्भुज (Parallelogram) के गुण: सम्मुख भुजाएं बराबर, सम्मुख कोण बराबर, विकर्ण एक दूसरे को समद्विभाजित करते हैं",
      "समचतुर्भुज (Rhombus) के विकर्ण परस्पर लंब समद्विभाजक होते हैं",
      "आयत के विकर्ण परस्पर बराबर व समद्विभाजित होते हैं",
      "मध्य-बिंदु प्रमेय: किसी त्रिभुज की दो भुजाओं के मध्य-बिंदुओं को मिलाने वाली रेखा तीसरी भुजा के समांतर और उसकी आधी होती है (DE || BC तथा DE = 1/2 BC)"
    ]
  },
  {
    id: 9,
    num: 9,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "वृत्त",
    titleEn: "Circles",
    topics: ["वृत्त की जीवा और चाप", "केंद्र से जीवा पर लंब", "जीवा द्वारा केंद्र पर अंतरित कोण", "चक्रीय चतुर्भुज (Cyclic Quadrilateral)"],
    formulas: [
      "वृत्त के केंद्र से जीवा पर डाला गया लंब जीवा को समद्विभाजित करता है",
      "वृत्त की बराबर जीवाएँ केंद्र पर बराबर कोण अंतरित करती हैं",
      "एक चाप द्वारा केंद्र पर अंतरित कोण, शेष परिधि पर अंतरित कोण का दुगुना होता है: ∠AOB = 2∠APB",
      "एक ही वृत्तखंड के कोण परस्पर बराबर होते हैं",
      "अर्धवृत्त में बना कोण समकोण (90°) होता है",
      "चक्रीय चतुर्भुज के सम्मुख कोणों का योग 180° होता है: ∠A + ∠C = 180°, \ ∠B + ∠D = 180°"
    ]
  },
  {
    id: 10,
    num: 10,
    unit: "mensuration",
    unitName: "क्षेत्रमिति",
    title: "हीरोन का सूत्र",
    titleEn: "Heron's Formula",
    topics: ["हीरोन का सूत्र का परिचय", "अर्धपरिमाप (Semi-perimeter)", "त्रिभुज का क्षेत्रफल", "समबाहु व समद्विबाहु त्रिभुज का क्षेत्रफल"],
    formulas: [
      "त्रिभुज की भुजाएं a, b, c हों तो अर्धपरिमाप: s = (a + b + c) / 2",
      "हीरोन का सूत्र द्वारा त्रिभुज का क्षेत्रफल: Δ = √[s(s - a)(s - b)(s - c)]",
      "समबाहु त्रिभुज (भुजा a) का क्षेत्रफल = (√3 / 4) × a²",
      "समबाहु त्रिभुज का शीर्षलंब (ऊंचाई) h = (√3 / 2) × a",
      "समकोण त्रिभुज का क्षेत्रफल = 1/2 × आधार × ऊंचाई"
    ]
  },
  {
    id: 11,
    num: 11,
    unit: "mensuration",
    unitName: "क्षेत्रमिति",
    title: "पृष्ठीय क्षेत्रफल और आयतन",
    titleEn: "Surface Areas and Volumes",
    topics: ["लंब वृत्तीय शंकु (Cone)", "गोला (Sphere)", "अर्धगोला (Hemisphere)", "पृष्ठीय क्षेत्रफल व आयतन के अनुप्रयोग"],
    formulas: [
      "शंकु की तिर्यक ऊंचाई: l = √(r² + h²)",
      "शंकु का वक्र पृष्ठीय क्षेत्रफल (CSA) = πrl",
      "शंकु का कुल पृष्ठीय क्षेत्रफल (TSA) = πr(l + r)",
      "शंकु का आयतन = 1/3 πr²h",
      "गोले का पृष्ठीय क्षेत्रफल = 4πr²",
      "गोले का आयतन = 4/3 πr³",
      "अर्धगोले का वक्र पृष्ठीय क्षेत्रफल = 2πr²",
      "अर्धगोले का कुल पृष्ठीय क्षेत्रफल = 3πr²",
      "अर्धगोले का आयतन = 2/3 πr³"
    ]
  },
  {
    id: 12,
    num: 12,
    unit: "stats",
    unitName: "सांख्यिकी",
    title: "सांख्यिकी",
    titleEn: "Statistics",
    topics: ["आंकड़ों का आलेखीय निरूपण", "दंड आलेख (Bar Graph)", "आयत चित्र (Histogram)", "बारंबारता बहुभुज (Frequency Polygon)"],
    formulas: [
      "वर्ग चिह्न (Class Mark) = (उच्च सीमा + निम्न सीमा) / 2",
      "वर्ग माप (Class Width) = उच्च सीमा - निम्न सीमा",
      "परिसर (Range) = अधिकतम मान - न्यूनतम मान",
      "आयत चित्र में आयतों का क्षेत्रफल बारंबारता के समानुपाती होता है",
      "असमान वर्ग अंतराल वाले आयत चित्र में समायोजित बारंबारता = (न्यूनतम वर्ग माप / उस वर्ग की माप) × बारंबारता"
    ]
  }
];

function renderMath9Chapters(filterUnit = "all", searchQuery = "") {
  const container = document.getElementById("math9-chapter-grid");
  if (!container) return;

  const filtered = math9Chapters.filter(ch => {
    const matchesUnit = (filterUnit === "all" || ch.unit === filterUnit);
    const matchesSearch = !searchQuery || 
      ch.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      ch.titleEn.toLowerCase().includes(searchQuery.toLowerCase()) ||
      ch.topics.some(t => t.toLowerCase().includes(searchQuery.toLowerCase()));
    return matchesUnit && matchesSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; color: #94a3b8; font-size: 20pt;">🔍 कोई अध्याय नहीं मिला। कृपया अन्य खोज शब्द का प्रयास करें।</div>';
    return;
  }

  container.innerHTML = filtered.map(ch => {
    const qUrl = 'qa_master_math9_' + ch.num + '.html';
    const topicsHtml = ch.topics.map(t => '<span class="topic-pill">' + t + '</span>').join('');
    const formulaPreview = ch.formulas && ch.formulas.length > 0 ? ch.formulas[0] : '';

    return '<div class="math-card" data-unit="' + ch.unit + '">' +
      '<div class="math-card-header">' +
        '<span class="unit-badge">' + ch.unitName + '</span>' +
        '<span class="chapter-num">अध्याय ' + ch.num + '</span>' +
      '</div>' +
      '<div class="math-card-body">' +
        '<h3 class="math-chapter-title">' + ch.title + '</h3>' +
        '<div class="math-chapter-en">' + ch.titleEn + '</div>' +
        '<div class="topics-wrapper">' + topicsHtml + '</div>' +
        '<div class="formula-preview-box">' +
          '<div class="formula-label">⚡ प्रमुख सूत्र / अवधारणा:</div>' +
          '<div class="formula-text">' + formulaPreview + '</div>' +
        '</div>' +
      '</div>' +
      '<div class="math-card-footer">' +
        '<a href="' + qUrl + '" class="math-action-btn qa-btn">' +
          '<span>📖 मास्टर Q&A नोट्स</span> ➔' +
        '</a>' +
        '<a href="' + qUrl + '#simulators" class="math-action-btn sim-btn" title="लाइव सिमुलेटर">' +
          '<span>⚡ 5 सिमुलेटर</span>' +
        '</a>' +
      '</div>' +
    '</div>';
  }).join('');
}

window.addEventListener('DOMContentLoaded', function() {
  renderMath9Chapters();

  // Unit filter tabs
  const tabs = document.querySelectorAll('.unit-tab-btn');
  tabs.forEach(function(btn) {
    btn.addEventListener('click', function() {
      tabs.forEach(function(b) { b.classList.remove('active'); });
      this.classList.add('active');
      const unit = this.getAttribute('data-unit');
      const searchVal = document.getElementById('math9-search')?.value || '';
      renderMath9Chapters(unit, searchVal);
    });
  });

  // Search filter
  const searchInput = document.getElementById('math9-search');
  if (searchInput) {
    searchInput.addEventListener('input', function() {
      const activeTab = document.querySelector('.unit-tab-btn.active');
      const unit = activeTab ? activeTab.getAttribute('data-unit') : 'all';
      renderMath9Chapters(unit, this.value);
    });
  }
});
