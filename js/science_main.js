/**
 * NCERT Class 10 Science (विज्ञान) Interactive Portal Logic
 * Covers All 13 Chapters (Rationalised Syllabus) with Hindi Medium Focus
 */

const scienceChapters = [
  {
    id: 1,
    num: 1,
    unit: "chemistry",
    unitName: "रसायन विज्ञान",
    title: "रासायनिक अभिक्रियाएं एवं समीकरण",
    titleEn: "Chemical Reactions and Equations",
    topics: ["समीकरण संतुलन (हिट एंड ट्रायल)", "संयोजन व वियोजन अभिक्रियाएँ", "विस्थापन व द्विविस्थापन", "रेडॉक्स (उपचयन-अपचयन)", "संक्षारण व विकृतगंधिता"],
    keyPoints: [
      "द्रव्यमान संरक्षण का नियम: किसी भी रासायनिक अभिक्रिया में द्रव्यमान का न तो निर्माण होता है और न ही विनाश।",
      "समीकरण संतुलन: अभिकारकों और उत्पादों के प्रत्येक तत्व के परमाणुओं की संख्या समान होनी चाहिए।",
      "संक्षारण से बचाव: यशदलेपन (गैल्वेनीकरण), पेंटिंग, ग्रीस लगाना या मिश्रधातु बनाना।"
    ]
  },
  {
    id: 2,
    num: 2,
    unit: "chemistry",
    unitName: "रसायन विज्ञान",
    title: "अम्ल, क्षारक एवं लवण",
    titleEn: "Acids, Bases and Salts",
    topics: ["pH पैमाना एवं दैनिक जीवन में महत्व", "सूचक (प्राकृतिक व संश्लेषित)", "उदासीनीकरण अभिक्रिया", "प्लास्टर ऑफ पेरिस, विरंजक चूर्ण व बेकिंग सोडा"],
    keyPoints: [
      "pH मान: अम्लीय विलयन pH < 7, उदासीन pH = 7, क्षारकीय pH > 7।",
      "अम्ल + धातु → लवण + हाइड्रोजन गैस (पॉप ध्वनि परीक्षण)।",
      "जिप्सम को 373 K पर गर्म करने पर प्लास्टर ऑफ पेरिस (CaSO4·½H2O) बनता है।"
    ]
  },
  {
    id: 3,
    num: 3,
    unit: "chemistry",
    unitName: "रसायन विज्ञान",
    title: "धातु एवं अधातु",
    titleEn: "Metals and Non-metals",
    topics: ["सक्रियता श्रेणी", "आयनिक यौगिकों के गुणधर्म", "धातु निष्कर्षण (भर्जन व निस्तापन)", "मिश्रधातु व एनोडीकरण"],
    keyPoints: [
      "सक्रियता श्रेणी: K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au",
      "आयनिक यौगिकों के गलनांक व क्वथनांक उच्च होते हैं तथा जलीय विलयन में विद्युत चालन करते हैं।",
      "सिनाबार (HgS) पारे का प्रमुख अयस्क है।"
    ]
  },
  {
    id: 4,
    num: 4,
    unit: "chemistry",
    unitName: "रसायन विज्ञान",
    title: "कार्बन एवं उसके यौगिक",
    titleEn: "Carbon and its Compounds",
    topics: ["सहसंयोजी आबंध", "समजातीय श्रेणी व IUPAC नामकरण", "दहन, ऑक्सीकरण व संकलन अभिक्रियाएँ", "साबुन एवं अपमार्जक की मिसेल संरचना"],
    keyPoints: [
      "कार्बन की चतुःसंयोजकता एवं शृंखलन गुण के कारण इसके असंख्य यौगिक बनते हैं।",
      "एल्केन (CnH2n+2), एल्कीन (CnH2n), एल्काइन (CnH2n-2)।",
      "साबुन का जलरागी सिरा आयनिक तथा जलविरागी सिरा हाइड्रोकार्बन शृंखला होती है।"
    ]
  },
  {
    id: 5,
    num: 5,
    unit: "biology",
    unitName: "जीव विज्ञान",
    title: "जैव प्रक्रम",
    titleEn: "Life Processes",
    topics: ["प्रकाश संश्लेषण एवं रंध्र कार्यप्रणाली", "मानव पाचन तंत्र", "श्वसन (वायवीय व अवायवीय)", "मानव हृदय एवं दोहरा परिसंचरण", "नेफ्रॉन द्वारा वृक्क में उत्सर्जन"],
    keyPoints: [
      "प्रकाश संश्लेषण: 6CO2 + 12H2O + प्रकाश → C6H12O6 + 6O2 + 6H2O",
      "वायवीय श्वसन माइटोकॉन्ड्रिया में तथा अवायवीय श्वसन कोशिकाद्रव्य में होता है।",
      "मानव हृदय में चार कोष्ठ होते हैं जो ऑक्सीजनित व विऑक्सीजनित रुधिर को अलग रखते हैं।"
    ]
  },
  {
    id: 6,
    num: 6,
    unit: "biology",
    unitName: "जीव विज्ञान",
    title: "नियंत्रण एवं समन्वय",
    titleEn: "Control and Coordination",
    topics: ["तंत्रिका कोशिका (न्यूरॉन) एवं सिनैप्स", "प्रतिवर्ती चाप", "मानव मस्तिष्क के भाग", "पादप हार्मोन (ऑक्सिन, जिबरेलिन, साइटोकाइनिन, एब्सिसिक)"],
    keyPoints: [
      "विद्युत आवेग न्यूरॉन के द्रुमिका से कोशिकाकाय, फिर तंत्रिकाक्ष (एक्सॉन) तक जाता है।",
      "प्रतिवर्ती क्रियाएं मेरुदंड (Spinal Cord) द्वारा नियंत्रित होती हैं।",
      "एब्सिसिक अम्ल पादपों में वृद्धि को रोकता है तथा पत्तियों के मुरझाने हेतु उत्तरदायी है।"
    ]
  },
  {
    id: 7,
    num: 7,
    unit: "biology",
    unitName: "जीव विज्ञान",
    title: "जीव जनन कैसे करते हैं?",
    titleEn: "How do Organisms Reproduce?",
    topics: ["अलैंगिक जनन (विखंडन, मुकुलन, पुनर्जनन, कायिक प्रवर्धन)", "पुष्प की अनुदैर्ध्य काट व परागण", "मानव नर व मादा जनन तंत्र", "ऋतुस्राव एवं गर्भनिरोधक विधियाँ"],
    keyPoints: [
      "अमीबा में द्विखंडन तथा हाइड्रा में मुकुलन एवं पुनरुद्भवन होता है।",
      "परागकणों का परागकोश से वर्तिकाग्र पर स्थानांतरण परागण कहलाता है।",
      "मानव में निषेचन अंडवाहिका (फैलोपियन ट्यूब) में संपन्न होता है।"
    ]
  },
  {
    id: 8,
    num: 8,
    unit: "biology",
    unitName: "जीव विज्ञान",
    title: "आनुवंशिकता",
    titleEn: "Heredity",
    topics: ["मेंडल के आनुवंशिकता के नियम", "एकसंकर व द्विसंकर क्रॉस (9:3:3:1)", "मानव में लिंग निर्धारण (XX व XY)"],
    keyPoints: [
      "मेंडल ने मटर (Pisum sativum) के 7 विपर्यासी लक्षणों पर कार्य किया।",
      "F2 पीढ़ी में एकसंकर लक्षणप्ररूप अनुपात 3:1 तथा जीनप्ररूप अनुपात 1:2:1 होता है।",
      "मानव शिशु का लिंग पिता से प्राप्त शुक्राणु (X अथवा Y) पर निर्भर करता है।"
    ]
  },
  {
    id: 9,
    num: 9,
    unit: "physics",
    unitName: "भौतिक विज्ञान",
    title: "प्रकाश - परावर्तन तथा अपवर्तन",
    titleEn: "Light - Reflection and Refraction",
    topics: ["दर्पण सूत्र व आवर्धन", "गोलीय दर्पणों द्वारा किरण आरेख", "स्नेल का अपवर्तन नियम", "लेंस सूत्र व लेंस की क्षमता (P = 1/f)"],
    keyPoints: [
      "दर्पण सूत्र: 1/v + 1/u = 1/f; लेंस सूत्र: 1/v - 1/u = 1/f",
      "स्नेल का नियम: sin i / sin r = स्थिरांक (अपवर्तनांक n)",
      "लेंस की क्षमता P = 1/f (मीटर में); इसका SI मात्रक डाइऑप्टर (D) है।"
    ]
  },
  {
    id: 10,
    num: 10,
    unit: "physics",
    unitName: "भौतिक विज्ञान",
    title: "मानव नेत्र तथा रंगबिरंगा संसार",
    titleEn: "The Human Eye and the Colourful World",
    topics: ["नेत्र समंजन क्षमता", "दृष्टि दोष (निकट, दूर व जरा-दृष्टि दोष)", "प्रिज्म से प्रकाश का विक्षेपण व इंद्रधनुष", "तारों का टिमटिमाना व अग्रिम सूर्योदय"],
    keyPoints: [
      "निकट दृष्टि दोष (Myopia) का निवारण अवतल लेंस द्वारा किया जाता है।",
      "दीर्घ दृष्टि दोष (Hypermetropia) का निवारण उत्तल लेंस द्वारा किया जाता है।",
      "वायुमंडलीय अपवर्तन के कारण सूर्य वास्तव में उदय होने से 2 मिनट पूर्व दिखाई देता है।"
    ]
  },
  {
    id: 11,
    num: 11,
    unit: "physics",
    unitName: "भौतिक विज्ञान",
    title: "विद्युत",
    titleEn: "Electricity",
    topics: ["ओम का नियम (V = IR)", "प्रतिरोधकता एवं कारक", "श्रेणीक्रम व समांतर क्रम संयोजन", "विद्युत धारा का तापीय प्रभाव (जूल का नियम H = I²Rt)", "विद्युत शक्ति (P = VI = I²R = V²/R)"],
    keyPoints: [
      "ओम का नियम: नियत ताप पर V ∝ I ⇒ V = IR",
      "श्रेणीक्रम में Req = R1 + R2 + R3; समांतर क्रम में 1/Req = 1/R1 + 1/R2 + 1/R3",
      "विद्युत ऊर्जा का व्यापारिक मात्रक 1 kWh (किलोवाट घंटा) = 3.6 × 10⁶ जूल (1 यूनिट) होता है।"
    ]
  },
  {
    id: 12,
    num: 12,
    unit: "physics",
    unitName: "भौतिक विज्ञान",
    title: "विद्युत धारा के चुंबकीय प्रभाव",
    titleEn: "Magnetic Effects of Electric Current",
    topics: ["चुंबकीय क्षेत्र रेखाओं के गुण", "दक्षिण-हस्त अंगुष्ठ नियम", "परिनालिका में चुंबकीय क्षेत्र", "फ्लेमिंग का वामहस्त नियम", "घरेलू विद्युत परिपथ (भू-संपर्क तार, फ्यूज व लघुपथन)"],
    keyPoints: [
      "चुंबकीय क्षेत्र रेखाएँ उत्तरी ध्रुव से निकलकर दक्षिणी ध्रुव पर विलीन होती हैं तथा कभी प्रतिच्छेद नहीं करतीं।",
      "फ्लेमिंग का वामहस्त नियम: अँगूठा बल, तर्जनी चुंबकीय क्षेत्र और मध्यमा विद्युत धारा दर्शाती है।",
      "भू-संपर्क तार (हरा) धात्विक आवरण से विद्युत क्षरण होने पर उपभोक्ता को तीव्र झटके से बचाता है।"
    ]
  },
  {
    id: 13,
    num: 13,
    unit: "biology",
    unitName: "जीव विज्ञान",
    title: "हमारा पर्यावरण",
    titleEn: "Our Environment",
    topics: ["पारितंत्र के घटक (जैव व अजैव)", "आहार शृंखला व पोषी स्तर (10% ऊर्जा नियम)", "जैव आवर्धन (Biological Magnification)", "ओजोन परत का अपक्षय (CFCs) एवं कचरा प्रबंधन"],
    keyPoints: [
      "10% नियम (लिंडमैन): प्रत्येक पोषी स्तर पर केवल 10% ऊर्जा ही अगले स्तर को स्थानांतरित होती है।",
      "जैव आवर्धन: हानिकारक रसायनों (जैसे DDT) की सांद्रता आहार शृंखला में शीर्ष उपभोक्ता तक बढ़ती जाती है।",
      "ओजोन (O3) सूर्य की पराबैंगनी (UV) किरणों से पृथ्वी की रक्षा करती है।"
    ]
  }
];

function renderScienceGrid(chaptersToRender) {
  const grid = document.getElementById('science-grid');
  if (!grid) return;
  grid.innerHTML = '';

  chaptersToRender.forEach(ch => {
    let unitBadgeColor = '#059669';
    let unitBg = '#ecfdf5';
    if (ch.unit === 'chemistry') {
      unitBadgeColor = '#d97706';
      unitBg = '#fffbeb';
    } else if (ch.unit === 'physics') {
      unitBadgeColor = '#2563eb';
      unitBg = '#eff6ff';
    }

    const card = document.createElement('div');
    card.className = 'chapter-card';
    card.style.borderTop = `5px solid ${unitBadgeColor}`;
    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
        <span style="background: ${unitBg}; color: ${unitBadgeColor}; padding: 4px 10px; border-radius: 6px; font-size: 13px; font-weight: 700; border: 1px solid ${unitBadgeColor}33;">
          ${ch.unitName}
        </span>
        <span style="font-weight: 800; color: #64748b; font-size: 14px;">अध्याय ${ch.num}</span>
      </div>
      <h3 style="font-size: 18px; font-weight: 800; color: #0f172a; margin-bottom: 6px; line-height: 1.3;">
        ${ch.title}
      </h3>
      <div style="font-size: 12px; color: #64748b; margin-bottom: 14px; font-style: italic;">
        ${ch.titleEn}
      </div>
      <div style="margin-bottom: 15px;">
        <div style="font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 6px;">प्रमुख अवधारणाएँ एवं प्रयोग:</div>
        <div style="display: flex; flex-wrap: wrap; gap: 5px;">
          ${ch.topics.map(t => `<span style="background: #f1f5f9; color: #334155; padding: 2px 7px; border-radius: 4px; font-size: 11px;">${t}</span>`).join('')}
        </div>
      </div>
      <div style="background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 6px; padding: 10px; margin-bottom: 15px;">
        <div style="font-size: 11px; font-weight: 700; color: #0284c7; margin-bottom: 4px;">🔬 मुख्य परीक्षा बिंदु:</div>
        <div style="font-size: 11px; color: #475569; line-height: 1.4;">${ch.keyPoints[0]}</div>
      </div>
      <a href="qa_master_sci${ch.num}.html" style="display: block; text-align: center; background: #0284c7; color: #ffffff; padding: 10px 14px; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 14px; transition: background 0.2s;" onmouseover="this.style.background='#0369a1'" onmouseout="this.style.background='#0284c7'">
        📖 संपूर्ण नोट्स व प्रयोग सिमुलेटर खोलें ➔
      </a>
    `;
    grid.appendChild(card);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  renderScienceGrid(scienceChapters);

  // Search
  const searchBar = document.getElementById('searchBar');
  if (searchBar) {
    searchBar.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const filtered = scienceChapters.filter(ch => 
        ch.title.toLowerCase().includes(q) ||
        ch.titleEn.toLowerCase().includes(q) ||
        ch.topics.some(t => t.toLowerCase().includes(q))
      );
      renderScienceGrid(filtered);
    });
  }

  // Tabs
  const tabBtns = document.querySelectorAll('.tab-btn[data-unit]');
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const unit = btn.getAttribute('data-unit');
      if (unit === 'all') {
        renderScienceGrid(scienceChapters);
      } else {
        renderScienceGrid(scienceChapters.filter(c => c.unit === unit));
      }
    });
  });
});
