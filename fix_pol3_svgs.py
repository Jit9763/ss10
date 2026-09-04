import os

svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18080c"/>
      <stop offset="50%" stop-color="#2a0f1b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="titleGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f472b6"/>
      <stop offset="50%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad1)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#f472b6" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow1)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#f472b6" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad1)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">👩‍💼 श्रम का लैंगic विभाजन बनाम महिला सशक्तिकरण (Gender &amp; Power)</text>
  </g>

  <!-- Left: Traditional Division -->
  <g transform="translate(35, 125)" filter="url(#shadow1)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#ef4444" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#dc2626"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">1. श्रम का पारंपरिक लैंगिक विभाजन</text>
    
    <text x="20" y="100" fill="#fca5a5" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• निजी बनाम सार्वजनिक का विभाजन:</text>
    <text x="20" y="140" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">घर के अंदर का सारा काम (खाना, सफाई) महिलाओं के जिम्मे।</text>

    <text x="20" y="205" fill="#fca5a5" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• अवैतनिक श्रम (Unpaid Labor):</text>
    <text x="20" y="245" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">महिलाओं के घरेलू श्रम का कोई आर्थिक मूल्य नहीं आंका जाता।</text>

    <rect x="20" y="320" width="460" height="140" rx="14" fill="#0f172a" stroke="#ef4444" stroke-width="2"/>
    <text x="250" y="355" fill="#f87171" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">💥 सामाजिक परिणाम:</text>
    <text x="250" y="395" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold" text-anchor="middle">राजनीति और सार्वजनिक जीवन में महिलाओं की कम भूमिका।</text>
  </g>

  <!-- Right: Feminist Movement & Empowerment -->
  <g transform="translate(565, 125)" filter="url(#shadow1)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#f472b6" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#db2777"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">2. नारीवादी आंदोलन एवं राजनीतिक सशक्तिकरण</text>
    
    <text x="20" y="100" fill="#fbcfe8" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• नारीवादी आंदोलन (Feminist Movement):</text>
    <text x="20" y="140" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">महिला-पुरुष के समान अधिकारों व अवसरों हेतु आंदोलन।</text>

    <text x="20" y="205" fill="#fbcfe8" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• राजनीतिक आरक्षण व कानून:</text>
    <text x="20" y="245" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">पंचायतों में 33% आरक्षण व नारी शक्ति वंदन अधिनियम।</text>

    <rect x="20" y="320" width="460" height="140" rx="14" fill="#0f172a" stroke="#f472b6" stroke-width="2"/>
    <text x="250" y="355" fill="#f472b6" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">🎯 मुख्य उपलब्धि:</text>
    <text x="250" y="395" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold" text-anchor="middle">सार्वजनिक क्षेत्र व निर्णय प्रक्रिया में महिलाओं की हिस्सेदारी।</text>
  </g>
</svg>"""

svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="titleGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad2)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow2)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#38bdf8" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad2)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">🕊️ धर्मनिरपेक्ष राज्य के 4 संवैधानिक सिद्धांत (Secular State Principles)</text>
  </g>

  <!-- 4 Grid Cards -->
  <g transform="translate(35, 125)" filter="url(#shadow2)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#0284c7"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">1. राजकीय धर्म का अभाव</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• भारतीय राज्य का कोई आधिकारिक धर्म नहीं है।</text>
    <text x="15" y="130" fill="#7dd3fc" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• संविधान किसी भी धर्म को विशेष दर्जा नहीं देता।</text>
  </g>

  <g transform="translate(565, 125)" filter="url(#shadow2)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#34d399" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#059669"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">2. धार्मिक स्वतंत्रता (Article 25)</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• सभी नागरिकों को किसी भी धर्म को मानने की आजादी।</text>
    <text x="15" y="130" fill="#6ee7b7" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• किसी धर्म का आचरण या न मानने का पूरा अधिकार।</text>
  </g>

  <g transform="translate(35, 380)" filter="url(#shadow2)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#facc15" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#ca8a04"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">3. भेदभाव का निषेध (Article 15)</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• धर्म के आधार पर किसी नागरिक से भेदभाव पर रोक।</text>
    <text x="15" y="130" fill="#fde047" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• सार्वजनिक स्थानों पर पूर्ण समानता और निष्पक्षता।</text>
  </g>

  <g transform="translate(565, 380)" filter="url(#shadow2)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#c084fc" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#9333ea"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">4. राज्य का हस्तक्षेप (State Intervention)</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• छुआछूत जैसी कुरीतियों को मिटाने हेतु हस्तक्षेप।</text>
    <text x="15" y="130" fill="#e9d5ff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• धार्मिक समुदायों में समानता सुनिश्चित करना।</text>
  </g>
</svg>"""

svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180808"/>
      <stop offset="50%" stop-color="#2d1212"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="titleGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="50%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#facc15"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad3)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow3)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#ef4444" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad3)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">⚠️ सांप्रदायिकता के 4 प्रमुख रूप (Forms of Communalism)</text>
  </g>

  <!-- 4 Grid Cards -->
  <g transform="translate(35, 125)" filter="url(#shadow3)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#d97706"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">1. दैनिक जीवन में धार्मिक पूर्वाग्रह</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• धार्मिक रूढ़िवादिता और दूसरों को नीचा समझना।</text>
    <text x="15" y="130" fill="#fde047" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• अपने धर्म को ही सर्वश्रेष्ठ मानने का अहंकार।</text>
  </g>

  <g transform="translate(565, 125)" filter="url(#shadow3)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#fb923c" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#ea580c"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">2. राजनीतिक गोलबंदी (Mobilization)</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• धार्मिक प्रतीकों, धर्मगुरुओं व भावनाओं का उपयोग।</text>
    <text x="15" y="130" fill="#fed7aa" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• चुनाव में वोटों के लिए धार्मिक ध्रुवीकरण।</text>
  </g>

  <g transform="translate(35, 380)" filter="url(#shadow3)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#ef4444" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#dc2626"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">3. बहुसंख्यकवाद व पृथकतावाद</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• बहुसंख्यकों का वर्चस्व स्थापित करने का प्रयास।</text>
    <text x="15" y="130" fill="#fca5a5" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• अल्पसंख्यकों द्वारा अलग राज्य की मांग करना।</text>
  </g>

  <g transform="translate(565, 380)" filter="url(#shadow3)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#b91c1c" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#991b1b"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">4. सांप्रदायिक हिंसा व दंगे</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• हिंसा, दंगे और नरसंहार का भयानक रूप लेना।</text>
    <text x="15" y="130" fill="#f87171" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• विभाजन के समय और बाद के सांप्रदायिक दंगे।</text>
  </g>
</svg>"""

svg4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
    <linearGradient id="titleGrad4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad4)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#facc15" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow4)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#facc15" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad4)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">⚖️ जातिगत असमानता एवं आधुनिक बदलाव (Caste &amp; Modern Changes)</text>
  </g>

  <!-- Left: Traditional Caste System -->
  <g transform="translate(35, 125)" filter="url(#shadow4)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#facc15" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#ca8a04"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">1. पारंपरिक जाति व्यवस्था का रूप</text>
    
    <text x="20" y="100" fill="#fde047" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• जन्म आधारित कार्य एवं छुआछूत:</text>
    <text x="20" y="140" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">पेशे का वंशानुगत निर्धारण व ऊंच-नीच का सामाजिक भेदभाव।</text>

    <text x="20" y="205" fill="#fde047" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• अपनी ही जाति में विवाह का नियम:</text>
    <text x="20" y="245" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">शादी-विवाह और भोजन अपनी ही जाति तक सीमित रहना।</text>

    <rect x="20" y="320" width="460" height="140" rx="14" fill="#0f172a" stroke="#facc15" stroke-width="2"/>
    <text x="250" y="355" fill="#fde047" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">💔 सामाजिक बुराई:</text>
    <text x="250" y="395" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold" text-anchor="middle">अछूत मानी जाने वाली जातियों का उत्पीड़न व वंचना।</text>
  </g>

  <!-- Right: Factors of Modern Change -->
  <g transform="translate(565, 125)" filter="url(#shadow4)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#34d399" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#059669"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">2. आधुनिक बदलाव लाने वाले 5 कारक</text>
    
    <text x="20" y="100" fill="#6ee7b7" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• आर्थिक विकास व शहरीकरण (Urbanization):</text>
    <text x="20" y="140" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">शहरों में बसों व होटलों में जाति पूछकर काम नहीं होता।</text>

    <text x="20" y="205" fill="#6ee7b7" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">• साक्षरता, संविधान व कानूनी रोक:</text>
    <text x="20" y="245" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">अनुच्छेद 17 द्वारा अस्पृश्यता का अंत व शिक्षा का प्रसार।</text>

    <rect x="20" y="320" width="460" height="140" rx="14" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="250" y="355" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">🎯 आधुनिक स्थिति:</text>
    <text x="250" y="395" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold" text-anchor="middle">पुराने जातिगत बंधन टूट रहे हैं, फिर भी विषमता मौजूद।</text>
  </g>
</svg>"""

svg5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="50%" stop-color="#111c38"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="titleGrad5" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
    <filter id="shadow5" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad5)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#34d399" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow5)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#34d399" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad5)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">🗳️ राजनीति में जाति बनाम जाति में राजनीति (Caste &amp; Politics)</text>
  </g>

  <g transform="translate(35, 120)" filter="url(#shadow5)">
    <rect width="1010" height="495" rx="18" fill="#1e293b" stroke="#34d399" stroke-width="2.5"/>
    
    <text x="25" y="55" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">1. राजनीति में जाति (Caste in Politics):</text>
    <text x="380" y="55" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">उम्मीदवार चुनते समय निर्वाचन क्षेत्र के जातिगत समीकरण का ध्यान रखना।</text>

    <text x="25" y="125" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">2. जातिगत गोलबंदी व वोट बैंक:</text>
    <text x="380" y="125" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">जातिगत भावनाओं को उकसाकर चुनाव में राजनीतिक समर्थन जुटाना।</text>

    <text x="25" y="195" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">3. केवल जाति ही निर्णायक नहीं:</text>
    <text x="380" y="195" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">कोई भी सांसदीय क्षेत्र केवल 1 ही जाति के बहुमत वाला नहीं होता।</text>

    <text x="25" y="265" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">4. जाति में राजनीति (Politics in Caste):</text>
    <text x="380" y="265" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">हर जाति खुद को बड़ा बनाने हेतु उप-जातियों को साथ लाने का प्रयास करती है।</text>

    <text x="25" y="335" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">5. सकारात्मक पहलू:</text>
    <text x="380" y="335" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">वंचित व पिछड़ी जातियों को सत्ता में साझेदारी व आवाज़ उठाने का अवसर।</text>

    <rect x="25" y="390" width="960" height="75" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="505" y="435" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">💡 केवल जाति नहीं, बल्कि विकास, शिक्षा व सरकार का काम ही अंतिम फैसला तय करता है!</text>
  </g>
</svg>"""

base_path = r'c:\Users\jiten\Desktop\class11\ss10\images\pol3'
svgs = [
    ('chart_pol3_1_gender_division_vs_empowerment.svg', svg1),
    ('chart_pol3_2_secular_state_principles.svg', svg2),
    ('chart_pol3_3_four_forms_of_communalism.svg', svg3),
    ('chart_pol3_4_caste_inequalities_and_modern_change.svg', svg4),
    ('chart_pol3_5_caste_and_politics_matrix.svg', svg5)
]

for name, content in svgs:
    fp = os.path.join(base_path, name)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated POL3 SVG:', name)
