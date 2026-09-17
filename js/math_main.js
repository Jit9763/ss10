/**
 * NCERT Class 10 Mathematics (गणित) Interactive Portal Logic
 * Covers All 14 Chapters (Rationalised Syllabus) with Hindi Medium Focus
 */

const mathChapters = [
  {
    id: 1,
    num: 1,
    unit: "number",
    unitName: "संख्या पद्धति",
    title: "वास्तविक संख्याएँ",
    titleEn: "Real Numbers",
    topics: ["अंकगणित की आधारभूत प्रमेय", "अपरिमेय संख्याओं का सत्यापन", "HCF और LCM संबंध", "दशमलव प्रसार"],
    formulas: [
      "दो संख्याओं a और b के लिए: HCF(a, b) × LCM(a, b) = a × b",
      "अंकगणित की आधारभूत प्रमेय: प्रत्येक भाज्य संख्या को अभाज्य गुणनखंडों के गुणनफल के रूप में अद्वितीय रूप से व्यक्त किया जा सकता है।",
      "यदि p एक अभाज्य संख्या है और p, a² को विभाजित करता है, तो p, a को भी विभाजित करेगा।"
    ]
  },
  {
    id: 2,
    num: 2,
    unit: "algebra",
    unitName: "बीजगणित",
    title: "बहुपद",
    titleEn: "Polynomials",
    topics: ["द्विघात बहुपद के शून्यक", "शून्यकों व गुणांकों में संबंध", "शून्यकों का ज्यामितीय अर्थ"],
    formulas: [
      "द्विघात बहुपद ax² + bx + c के शून्यक α और β हों तो:",
      "शून्यकों का योग (α + β) = -b/a = -(x का गुणांक)/(x² का गुणांक)",
      "शून्यकों का गुणनफल (α · β) = c/a = अचर पद/(x² का गुणांक)",
      "द्विघात बहुपद: k[x² - (α + β)x + αβ]"
    ]
  },
  {
    id: 3,
    num: 3,
    unit: "algebra",
    unitName: "बीजगणित",
    title: "दो चर वाले रैखिक समीकरण युग्म",
    titleEn: "Pair of Linear Equations in Two Variables",
    topics: ["ग्राफीय निरूपण", "प्रतिस्थापन विधि", "विलोपन विधि", "संगत व असंगत निकाय"],
    formulas: [
      "रैखिक युग्म: a₁x + b₁y + c₁ = 0 तथा a₂x + b₂y + c₂ = 0",
      "प्रतिच्छेदी रेखाएं (अद्वितीय हल): a₁/a₂ ≠ b₁/b₂ (संगत)",
      "संपाती रेखाएं (अपरिमित हल): a₁/a₂ = b₁/b₂ = c₁/c₂ (आश्रित संगत)",
      "समांतर रेखाएं (कोई हल नहीं): a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (असंगत)"
    ]
  },
  {
    id: 4,
    num: 4,
    unit: "algebra",
    unitName: "बीजगणित",
    title: "द्विघात समीकरण",
    titleEn: "Quadratic Equations",
    topics: ["गुणनखंडन विधि", "द्विघाती सूत्र (श्रीधराचार्य)", "विविक्तकर (D)", "मूलों की प्रकृति"],
    formulas: [
      "मानक रूप: ax² + bx + c = 0 (a ≠ 0)",
      "द्विघाती सूत्र (श्रीधराचार्य): x = [-b ± √(b² - 4ac)] / (2a)",
      "विविक्तकर D = b² - 4ac",
      "D > 0: दो भिन्न वास्तविक मूल | D = 0: दो बराबर वास्तविक मूल | D < 0: कोई वास्तविक मूल नहीं"
    ]
  },
  {
    id: 5,
    num: 5,
    unit: "algebra",
    unitName: "बीजगणित",
    title: "समांतर श्रेढ़ियाँ (A.P.)",
    titleEn: "Arithmetic Progressions",
    topics: ["प्रथम पद (a) व सार्व अंतर (d)", "nवाँ पद (aₙ)", "प्रथम n पदों का योग (Sₙ)", "व्यावहारिक प्रश्न"],
    formulas: [
      "सार्व अंतर: d = a₂ - a₁ = aₙ - aₙ₋₁",
      "nवाँ पद: aₙ = a + (n - 1)d",
      "प्रथम n पदों का योग: Sₙ = (n/2)[2a + (n - 1)d]",
      "यदि अंतिम पद l ज्ञात हो: Sₙ = (n/2)[a + l]"
    ]
  },
  {
    id: 6,
    num: 6,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "त्रिभुज",
    titleEn: "Triangles",
    topics: ["समरूप आकृतियाँ", "आधारभूत आनुपातिकता प्रमेय (थेल्स)", "समरूपता कसौटियाँ (AAA, SSS, SAS)"],
    formulas: [
      "थेल्स प्रमेय (BPT): त्रिभुज की एक भुजा के समांतर खींची गई रेखा अन्य दो भुजाओं को समान अनुपात में विभाजित करती है (AD/DB = AE/EC)",
      "थेल्स प्रमेय का विलोम: यदि कोई रेखा दो भुजाओं को समान अनुपात में बांटे तो वह तीसरी भुजा के समांतर होगी।",
      "समरूपता कसौटियाँ: AAA/AA (कोण-कोण), SSS (भुजा-भुजा-भुजा), SAS (भुजा-कोण-भुजा)"
    ]
  },
  {
    id: 7,
    num: 7,
    unit: "coord",
    unitName: "निर्देशांक ज्यामिति",
    title: "निर्देशांक ज्यामिति",
    titleEn: "Coordinate Geometry",
    topics: ["दूरी सूत्र", "मूल बिंदु से दूरी", "विभाजन सूत्र (Section Formula)", "मध्य बिंदु सूत्र"],
    formulas: [
      "दूरी सूत्र: AB = √[(x₂ - x₁)² + (y₂ - y₁)²]",
      "मूल बिंदु (0, 0) से दूरी: d = √(x² + y²)",
      "विभाजन सूत्र (m₁:m₂ अनुपात): x = (m₁x₂ + m₂x₁)/(m₁+m₂), y = (m₁y₂ + m₂y₁)/(m₁+m₂)",
      "मध्य बिंदु के निर्देशांक: ((x₁ + x₂)/2, (y₁ + y₂)/2)"
    ]
  },
  {
    id: 8,
    num: 8,
    unit: "trig",
    unitName: "त्रिकोणमिति",
    title: "त्रिकोणमिति का परिचय",
    titleEn: "Introduction to Trigonometry",
    topics: ["त्रिकोणमितीय अनुपात (sin, cos, tan...)", "विशिष्ट कोण मान सारणी", "मूलभूत सर्वसमिकाएँ"],
    formulas: [
      "sin θ = लंब/कर्ण | cos θ = आधार/कर्ण | tan θ = लंब/आधार",
      "cosec θ = 1/sin θ | sec θ = 1/cos θ | cot θ = 1/tan θ = cos θ/sin θ",
      "प्रमुख सर्वसमिका 1: sin²θ + cos²θ = 1",
      "प्रमुख सर्वसमिका 2: 1 + tan²θ = sec²θ",
      "प्रमुख सर्वसमिका 3: 1 + cot²θ = cosec²θ"
    ]
  },
  {
    id: 9,
    num: 9,
    unit: "trig",
    unitName: "त्रिकोणमिति",
    title: "त्रिकोणमिति के कुछ अनुप्रयोग",
    titleEn: "Some Applications of Trigonometry",
    topics: ["दृष्टि रेखा", "उन्नयन कोण (Elevation)", "अवनमन कोण (Depression)", "ऊंचाई व दूरी प्रश्न"],
    formulas: [
      "उन्नयन कोण: जब वस्तु क्षैतिज रेखा से ऊपर हो (सिर उठाकर देखना)",
      "अवनमन कोण: जब वस्तु क्षैतिज रेखा से नीचे हो (सिर झुकाकर देखना)",
      "ऊंचाई और दूरी में अधिकांशतः tan θ = लंब/आधार का उपयोग होता है।"
    ]
  },
  {
    id: 10,
    num: 10,
    unit: "geometry",
    unitName: "ज्यामिति",
    title: "वृत्त",
    titleEn: "Circles",
    topics: ["वृत्त की स्पर्श रेखा", "स्पर्श बिंदु पर त्रिज्या लंब (प्रमेय 10.1)", "बाह्य बिंदु से स्पर्श रेखाएँ (प्रमेय 10.2)"],
    formulas: [
      "प्रमेय 10.1: वृत्त के किसी बिंदु पर स्पर्श रेखा स्पर्श बिंदु से जाने वाली त्रिज्या पर लंब होती है (OP ⊥ AB)",
      "प्रमेय 10.2: बाह्य बिंदु से वृत्त पर खींची गई स्पर्श रेखाओं की लंबाइयां बराबर होती हैं (PQ = PR)",
      "एक वृत्त की अपरिमित स्पर्श रेखाएं हो सकती हैं; किसी बाह्य बिंदु से केवल 2 स्पर्श रेखाएं खींची जा सकती हैं।"
    ]
  },
  {
    id: 11,
    num: 11,
    unit: "mensuration",
    unitName: "क्षेत्रमिति",
    title: "वृत्तों से संबंधित क्षेत्रफल",
    titleEn: "Areas Related to Circles",
    topics: ["त्रिज्यखंड का क्षेत्रफल", "चाप की लंबाई", "वृत्तखंड का क्षेत्रफल", "छायांकित भाग का क्षेत्रफल"],
    formulas: [
      "वृत्त का क्षेत्रफल = πr² | परिधि = 2πr",
      "त्रिज्यखंड का क्षेत्रफल = (θ/360°) × πr²",
      "चाप की लंबाई (l) = (θ/360°) × 2πr",
      "लघु वृत्तखंड का क्षेत्रफल = त्रिज्यखंड का क्षेत्रफल - संगत त्रिभुज का क्षेत्रफल"
    ]
  },
  {
    id: 12,
    num: 12,
    unit: "mensuration",
    unitName: "क्षेत्रमिति",
    title: "पृष्ठीय क्षेत्रफल और आयतन",
    titleEn: "Surface Areas and Volumes",
    topics: ["संयोजित ठोसों का क्षेत्रफल", "ठोसों का आयतन", "घन, घनाभ, बेलन, शंकु, गोला, अर्धगोला"],
    formulas: [
      "बेलन: वक्र पृष्ठीय = 2πrh | कुल = 2πr(r+h) | आयतन = πr²h",
      "शंकु: तिर्यक ऊंचाई l = √(r²+h²) | वक्र = πrl | कुल = πr(l+r) | आयतन = (1/3)πr²h",
      "गोला: पृष्ठीय क्षेत्रफल = 4πr² | आयतन = (4/3)πr³",
      "अर्धगोला: वक्र = 2πr² | कुल = 3πr² | आयतन = (2/3)πr³"
    ]
  },
  {
    id: 13,
    num: 13,
    unit: "stats",
    unitName: "सांख्यिकी एवं प्रायिकता",
    title: "सांख्यिकी",
    titleEn: "Statistics",
    topics: ["माध्य (प्रत्यक्ष व कल्पित माध्य विधि)", "बहुलक (Mode)", "माध्यक (Median)", "तीनों में आनुभविक संबंध"],
    formulas: [
      "प्रत्यक्ष माध्य: x̄ = Σ(fᵢxᵢ) / Σfᵢ",
      "कल्पित माध्य: x̄ = a + [Σ(fᵢdᵢ) / Σfᵢ] जहाँ dᵢ = xᵢ - a",
      "बहुलक = l + [(f₁ - f₀) / (2f₁ - f₀ - f₂)] × h",
      "माध्यक = l + [((n/2) - cf) / f] × h",
      "आनुभविक संबंध: 3 माध्यक = बहुलक + 2 माध्य (3 Median = Mode + 2 Mean)"
    ]
  },
  {
    id: 14,
    num: 14,
    unit: "stats",
    unitName: "सांख्यिकी एवं प्रायिकता",
    title: "प्रायिकता",
    titleEn: "Probability",
    topics: ["सैद्धांतिक प्रायिकता", "सम-संभावी परिणाम", "निश्चित व असंभव घटना", "पूरक घटना"],
    formulas: [
      "प्रायिकता: P(E) = (घटना E के अनुकूल परिणामों की संख्या) / (प्रयोग के सभी संभव परिणामों की संख्या)",
      "किसी भी घटना की प्रायिकता: 0 ≤ P(E) ≤ 1",
      "निश्चित घटना की प्रायिकता = 1 | असंभव घटना की प्रायिकता = 0",
      "पूरक घटना: P(E) + P(not E) = 1 ⇒ P(Ē) = 1 - P(E)"
    ]
  }
];

let currentMathUnit = 'all';

document.addEventListener('DOMContentLoaded', () => {
  renderMathChapters(mathChapters);

  const searchInput = document.getElementById('mathSearchBar');
  if (searchInput) {
    searchInput.addEventListener('input', filterAndRenderMath);
  }

  const unitButtons = document.querySelectorAll('.unit-tab-btn');
  unitButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      unitButtons.forEach(b => b.classList.remove('active'));
      const target = e.currentTarget || e.target;
      target.classList.add('active');
      currentMathUnit = target.getAttribute('data-unit') || 'all';
      filterAndRenderMath();
    });
  });
});

function filterAndRenderMath() {
  const searchTerm = (document.getElementById('mathSearchBar')?.value || '').toLowerCase().trim();

  const filtered = mathChapters.filter(chap => {
    const matchesUnit = (currentMathUnit === 'all' || chap.unit === currentMathUnit);
    const matchesSearch = 
      chap.title.toLowerCase().includes(searchTerm) ||
      chap.titleEn.toLowerCase().includes(searchTerm) ||
      chap.unitName.toLowerCase().includes(searchTerm) ||
      chap.topics.some(t => t.toLowerCase().includes(searchTerm));
    return matchesUnit && matchesSearch;
  });

  renderMathChapters(filtered);
}

function renderMathChapters(data) {
  const grid = document.getElementById('math-chapter-grid');
  if (!grid) return;

  grid.innerHTML = '';

  if (data.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1/-1; text-align:center; padding:3.5rem; color: var(--text-secondary); background: var(--card-bg); border-radius: 16px; border: 1px dashed var(--card-border);">
        <h3 style="color: var(--accent-gold); margin-bottom: 0.5rem; font-size: 1.3rem;">कोई अध्याय या सूत्र नहीं मिला।</h3>
        <p>कृपया अन्य शब्द से खोजें या 'सभी अध्याय' फ़िल्टर चुनें।</p>
      </div>
    `;
    return;
  }

  data.forEach((chapter) => {
    const card = document.createElement('div');
    card.className = 'chapter-card';
    card.style.position = 'relative';

    const topicsHtml = chapter.topics.map(t => `<span class="math-topic-pill">📌 ${t}</span>`).join('');

    card.innerHTML = `
      <span class="subject-badge badge-${chapter.unit}">${chapter.unitName}</span>
      <div class="chapter-num">${String(chapter.num).padStart(2, '0')}</div>
      <h3 class="chapter-title" style="margin-bottom: 2px;">${chapter.title}</h3>
      <div class="chapter-subtitle-en">${chapter.titleEn}</div>
      
      <div class="math-topics-list">
        ${topicsHtml}
      </div>

      <div class="chapter-actions" style="display:flex; flex-direction:column; gap:8px; margin-top: 15px;">
        <button class="btn-formula" onclick="showFormulaModal(${chapter.id})">
          📐 मुख्य सूत्र व प्रमेय संग्रह (Formula Sheet)
        </button>
        <button class="btn-primary" onclick="showNotesModal(${chapter.id})">
          📖 संपूर्ण अध्याय नोट्स (Comprehensive Notes)
        </button>
        <button class="btn-math-solutions" onclick="window.open('qa_master_math' + ${chapter.id} + '.html', '_blank')">
          ✍️ अभ्यास प्रश्न व बोर्ड समाधान (Master Q&A ➔)
        </button>
      </div>
    `;
    grid.appendChild(card);
  });
}

// Modal logic for Formulas, Notes, and Solutions
function showFormulaModal(id) {
  const chap = mathChapters.find(c => c.id === id);
  if (!chap) return;

  const modalOverlay = document.createElement('div');
  modalOverlay.id = 'math-modal';
  modalOverlay.style.cssText = `
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(11, 15, 25, 0.88); backdrop-filter: blur(8px);
    z-index: 9999; display: flex; align-items: center; justify-content: center;
    padding: 20px; box-sizing: border-box;
  `;

  const formulaItems = chap.formulas.map(f => `
    <div style="background: rgba(255, 255, 255, 0.05); border-left: 4px solid var(--accent-gold); padding: 12px 16px; margin-bottom: 12px; border-radius: 8px; font-size: 1rem; color: #f8fafc; line-height: 1.6;">
      ${f}
    </div>
  `).join('');

  modalOverlay.innerHTML = `
    <div style="background: #111827; border: 2px solid #818cf8; border-radius: 20px; max-width: 650px; width: 100%; max-height: 85vh; overflow-y: auto; padding: 28px; box-shadow: 0 20px 50px rgba(0,0,0,0.7); position: relative;">
      <button onclick="document.getElementById('math-modal').remove()" style="position: absolute; top: 16px; right: 18px; background: rgba(255,255,255,0.1); border: none; color: #ffffff; font-size: 1.4rem; cursor: pointer; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">✕</button>
      
      <div style="display: inline-block; background: rgba(56, 189, 248, 0.2); color: #7dd3fc; padding: 4px 12px; border-radius: 6px; font-size: 0.85rem; font-weight: 700; margin-bottom: 10px;">
        अध्याय ${chap.num} • ${chap.unitName}
      </div>
      <h2 style="color: #ffffff; font-size: 1.6rem; margin-bottom: 4px;">${chap.title}</h2>
      <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 20px;">${chap.titleEn} — प्रमुख सूत्र व अवधारणाएँ</p>
      
      <div style="margin-bottom: 24px;">
        ${formulaItems}
      </div>

      <div style="display:flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <button onclick="window.open('qa_master_math' + ${id} + '.html', '_blank')" style="background: #0284c7; color: #fff; border: 1px solid #38bdf8; padding: 10px 18px; border-radius: 10px; font-weight: 700; cursor: pointer;">📖 संपूर्ण प्रश्न-उत्तर हल खोलें ➔</button>
        <button onclick="document.getElementById('math-modal').remove()" style="background: #4f46e5; color: #fff; border: none; padding: 10px 24px; border-radius: 10px; font-weight: 700; cursor: pointer; margin-left: auto;">
          ठीक है, बंद करें (Close)
        </button>
      </div>
    </div>
  `;

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) modalOverlay.remove();
  });

  document.body.appendChild(modalOverlay);
}

function showNotesModal(id) {
  const chap = mathChapters.find(c => c.id === id);
  if (!chap) return;

  const modalOverlay = document.createElement('div');
  modalOverlay.id = 'math-modal';
  modalOverlay.style.cssText = `
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(11, 15, 25, 0.88); backdrop-filter: blur(8px);
    z-index: 9999; display: flex; align-items: center; justify-content: center;
    padding: 20px; box-sizing: border-box;
  `;

  const topicsList = chap.topics.map(t => `<li style="margin-bottom: 8px; color: #e2e8f0;">${t}</li>`).join('');

  modalOverlay.innerHTML = `
    <div style="background: #111827; border: 2px solid #38bdf8; border-radius: 20px; max-width: 650px; width: 100%; max-height: 85vh; overflow-y: auto; padding: 28px; box-shadow: 0 20px 50px rgba(0,0,0,0.7); position: relative;">
      <button onclick="document.getElementById('math-modal').remove()" style="position: absolute; top: 16px; right: 18px; background: rgba(255,255,255,0.1); border: none; color: #ffffff; font-size: 1.4rem; cursor: pointer; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">✕</button>
      
      <div style="display: inline-block; background: rgba(56, 189, 248, 0.2); color: #7dd3fc; padding: 4px 12px; border-radius: 6px; font-size: 0.85rem; font-weight: 700; margin-bottom: 10px;">
        📖 संपूर्ण अध्याय नोट्स
      </div>
      <h2 style="color: #ffffff; font-size: 1.6rem; margin-bottom: 4px;">${chap.title} (${chap.titleEn})</h2>
      <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 18px;">NCERT कक्षा 10 गणित — अध्याय पाठ्यक्रम एवं मुख्य बिंदु</p>

      <div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
        <h4 style="color: var(--accent-gold); margin-bottom: 12px;">📌 इस अध्याय के मुख्य अध्ययन विषय (Key Syllabus Topics):</h4>
        <ul style="padding-left: 20px; line-height: 1.8;">
          ${topicsList}
        </ul>
      </div>

      <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 16px; margin-bottom: 20px; color: #a7f3d0; font-size: 0.92rem;">
        💡 <strong>बोर्ड परीक्षा टिप:</strong> इस अध्याय के सभी प्रमेय और अभ्यास प्रश्नों को चरणबद्ध (step-by-step) लिखकर हल करने से पूरे अंक प्राप्त होते हैं।
      </div>

      <div style="display:flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <button onclick="window.open('qa_master_math' + ${id} + '.html', '_blank')" style="background: #059669; color: #fff; border: 1px solid #34d399; padding: 10px 18px; border-radius: 10px; font-weight: 700; cursor: pointer;">✍️ अध्याय ${chap.num} के संपूर्ण प्रश्नोत्तर हल देखें ➔</button>
        <button onclick="document.getElementById('math-modal').remove()" style="background: #0284c7; color: #fff; border: none; padding: 10px 24px; border-radius: 10px; font-weight: 700; cursor: pointer; margin-left: auto;">
          बंद करें (Close)
        </button>
      </div>
    </div>
  `;

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) modalOverlay.remove();
  });

  document.body.appendChild(modalOverlay);
}

function showSolutionsModal(id) {
  const chap = mathChapters.find(c => c.id === id);
  if (!chap) return;

  const modalOverlay = document.createElement('div');
  modalOverlay.id = 'math-modal';
  modalOverlay.style.cssText = `
    position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
    background: rgba(11, 15, 25, 0.88); backdrop-filter: blur(8px);
    z-index: 9999; display: flex; align-items: center; justify-content: center;
    padding: 20px; box-sizing: border-box;
  `;

  modalOverlay.innerHTML = `
    <div style="background: #111827; border: 2px solid #10b981; border-radius: 20px; max-width: 650px; width: 100%; max-height: 85vh; overflow-y: auto; padding: 28px; box-shadow: 0 20px 50px rgba(0,0,0,0.7); position: relative;">
      <button onclick="document.getElementById('math-modal').remove()" style="position: absolute; top: 16px; right: 18px; background: rgba(255,255,255,0.1); border: none; color: #ffffff; font-size: 1.4rem; cursor: pointer; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">✕</button>
      
      <div style="display: inline-block; background: rgba(16, 185, 129, 0.2); color: #6ee7b7; padding: 4px 12px; border-radius: 6px; font-size: 0.85rem; font-weight: 700; margin-bottom: 10px;">
        ✍️ एनसीईआरटी प्रश्नोत्तर व अभ्यास हल
      </div>
      <h2 style="color: #ffffff; font-size: 1.6rem; margin-bottom: 4px;">${chap.title} (${chap.titleEn})</h2>
      <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 18px;">बोर्ड परीक्षा समाधान गाइड एवं अभ्यास सेट</p>

      <div style="background: rgba(30, 41, 59, 0.6); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
        <h4 style="color: #6ee7b7; margin-bottom: 10px;">✅ अभ्यास प्रश्नमाला सूची:</h4>
        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.7;">
          इस अध्याय के सभी प्रश्नावली अभ्यास, उदाहरण और महत्वपूर्ण अतिरिक्त प्रश्नों के विस्तृत चरण-दर-चरण हल तैयार किए गए हैं।
        </p>
      </div>

      <div style="display:flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <button onclick="window.open('qa_master_math' + ${id} + '.html', '_blank')" style="background: linear-gradient(135deg, #10b981, #059669); color: #fff; border: 1px solid #6ee7b7; padding: 10px 18px; border-radius: 10px; font-weight: 800; cursor: pointer;">🚀 संपूर्ण हल पृष्ठ खोलें ➔</button>
        <button onclick="document.getElementById('math-modal').remove()" style="background: #059669; color: #fff; border: none; padding: 10px 24px; border-radius: 10px; font-weight: 700; cursor: pointer; margin-left: auto;">
          बंद करें (Close)
        </button>
      </div>
    </div>
  `;

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) modalOverlay.remove();
  });

  document.body.appendChild(modalOverlay);
}
