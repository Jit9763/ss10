import os

svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="titleGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <filter id="shadow1" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad1)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow1)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#38bdf8" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad1)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">📢 राजनीतिक दल के 3 घटक व मुख्य कार्य (Components &amp; Functions)</text>
  </g>

  <!-- 3 Components Box -->
  <g transform="translate(35, 125)" filter="url(#shadow1)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#0284c7"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">1. राजनीतिक दल के 3 हिस्से (Components)</text>
    
    <text x="25" y="110" fill="#7dd3fc" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900">1. नेता (Leaders):</text>
    <text x="25" y="145" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17">चुनाव लड़ते हैं और सरकार में पद संभालते हैं।</text>

    <text x="25" y="210" fill="#7dd3fc" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900">2. सक्रिय सदस्य (Active Members):</text>
    <text x="25" y="245" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17">पार्टी के कार्यक्रमों और रैलियों को संचालित करते हैं।</text>

    <text x="25" y="310" fill="#7dd3fc" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900">3. अनुयायी या समर्थक (Followers):</text>
    <text x="25" y="345" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17">चुनाव में पार्टी की नीतियों पर भरोसा करके वोट देते हैं।</text>
  </g>

  <!-- Functions Box -->
  <g transform="translate(565, 125)" filter="url(#shadow1)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#34d399" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#059669"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">2. राजनीतिक दलों के 6 मुख्य कार्य (Functions)</text>
    
    <text x="25" y="100" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold">• चुनाव लड़ना व उम्मीदवार खड़े करना।</text>
    <text x="25" y="140" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold">• नीतियां व कार्यक्रम जनता के सामने रखना।</text>
    <text x="25" y="180" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold">• देश के लिए कानून बनाने में निर्णायक भूमिका।</text>
    <text x="25" y="220" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold">• सरकार बनाना और चलाना।</text>
    <text x="25" y="260" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold">• विपक्ष की भूमिका निभाना (अंकुश लगाना)।</text>
    <text x="25" y="300" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold">• जनमत का निर्माण करना व योजनाएं पहुंचाना।</text>

    <rect x="20" y="340" width="460" height="120" rx="14" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="250" y="375" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">🎯 लोकतंत्र का आधार:</text>
    <text x="250" y="415" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">राजनीतिक दलों के बिना आधुनिक लोकतंत्र असंभव है।</text>
  </g>
</svg>"""

svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070d1e"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="titleGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
    <filter id="shadow2" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad2)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#facc15" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow2)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#facc15" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad2)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">🌐 दलीय व्यवस्था के 3 प्रमुख मॉडल (3 Party System Models)</text>
  </g>

  <!-- 3 Columns -->
  <!-- One-party -->
  <g transform="translate(35, 125)" filter="url(#shadow2)">
    <rect width="330" height="490" rx="16" fill="#1e293b" stroke="#ef4444" stroke-width="2.5"/>
    <rect x="0" y="0" width="330" height="50" rx="16" fill="#dc2626"/>
    <text x="165" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">1. एकदलीय व्यवस्था (One Party)</text>

    <text x="15" y="90" fill="#fca5a5" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15" font-weight="bold">• केवल 1 दल को ही शासन का अधिकार।</text>
    <text x="15" y="130" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15">• अलोकतांत्रिक विकल्प माना जाता है।</text>
    <text x="15" y="170" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15">• स्वतंत्र चुनाव प्रतिस्पर्धा का अभाव।</text>

    <rect x="15" y="300" width="300" height="170" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <text x="165" y="340" fill="#f87171" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">🇨🇳 उदाहरण देश:</text>
    <text x="165" y="385" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">चीन (कम्युनिस्ट पार्टी)</text>
  </g>

  <!-- Two-party -->
  <g transform="translate(385, 125)" filter="url(#shadow2)">
    <rect width="330" height="490" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
    <rect x="0" y="0" width="330" height="50" rx="16" fill="#0284c7"/>
    <text x="165" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">2. द्विदलीय व्यवस्था (Two Party)</text>

    <text x="15" y="90" fill="#7dd3fc" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15" font-weight="bold">• मुख्य रूप से 2 दलों में ही सत्ता फेरबदल।</text>
    <text x="15" y="130" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15">• सरकार में स्पष्ट बहुमत व स्थिरता।</text>
    <text x="15" y="170" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15">• छोटे दलों को बहुत कम सीटें मिलती हैं।</text>

    <rect x="15" y="300" width="300" height="170" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="340" fill="#38bdf8" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">🇺🇸 🇬🇧 उदाहरण देश:</text>
    <text x="165" y="385" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">अमेरिका व ब्रिटेन</text>
  </g>

  <!-- Multi-party -->
  <g transform="translate(735, 125)" filter="url(#shadow2)">
    <rect width="330" height="490" rx="16" fill="#1e293b" stroke="#34d399" stroke-width="2.5"/>
    <rect x="0" y="0" width="330" height="50" rx="16" fill="#059669"/>
    <text x="165" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">3. बहुदलीय व्यवस्था (Multi Party)</text>

    <text x="15" y="90" fill="#6ee7b7" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15" font-weight="bold">• कई दल सत्ता की दौड़ में भाग लेते हैं।</text>
    <text x="15" y="130" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15">• गठबंधन सरकार (Coalition) बनती है।</text>
    <text x="15" y="170" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="15">• सामाजिक व क्षेत्रीय विविधता को जगह।</text>

    <rect x="15" y="300" width="300" height="170" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="165" y="340" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">🇮🇳 उदाहरण देश:</text>
    <text x="165" y="385" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">भारत 🇮🇳 (NDA / INDIA)</text>
  </g>
</svg>"""

svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#312e81"/>
    </linearGradient>
    <linearGradient id="titleGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#facc15"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <filter id="shadow3" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad3)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#facc15" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow3)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#facc15" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad3)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">🏛️ राष्ट्रीय बनाम राज्यस्तरीय (क्षेत्रीय) दल की पात्रता शर्तें</text>
  </g>

  <!-- Left: State Party Criteria -->
  <g transform="translate(35, 125)" filter="url(#shadow3)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#0284c7"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">1. राज्यस्तरीय दल (State/Regional Party)</text>
    
    <text x="20" y="100" fill="#7dd3fc" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">चुनाव आयोग की निर्धारित शर्तें:</text>
    <text x="20" y="145" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">• राज्य विधानसभा चुनाव में पड़े कुल वोटों का <b>कम से कम 6% वोट</b>।</text>
    <text x="20" y="210" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">• राज्य विधानसभा में <b>कम से कम 2 सीटें</b> जीतना अनिवार्य।</text>

    <rect x="20" y="320" width="460" height="140" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="250" y="355" fill="#38bdf8" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">🎯 प्रमुख उदाहरण दल:</text>
    <text x="250" y="395" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">सपा, राजद, तृणमूल कांग्रेस, डीएमके, आप आदि।</text>
  </g>

  <!-- Right: National Party Criteria -->
  <g transform="translate(565, 125)" filter="url(#shadow3)">
    <rect width="500" height="490" rx="18" fill="#1e293b" stroke="#34d399" stroke-width="3"/>
    <rect x="0" y="0" width="500" height="60" rx="18" fill="#059669"/>
    <text x="250" y="40" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="20" font-weight="900" text-anchor="middle">2. राष्ट्रीय दल (National Party)</text>
    
    <text x="20" y="100" fill="#6ee7b7" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">चुनाव आयोग की निर्धारित शर्तें:</text>
    <text x="20" y="145" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">• लोकसभा या 4 राज्यों के चुनाव में <b>6% वोट</b> हासिल करना।</text>
    <text x="20" y="210" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">• लोकसभा चुनाव में <b>कम से कम 4 सीटें</b> जीतना अनिवार्य।</text>

    <rect x="20" y="320" width="460" height="140" rx="14" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="250" y="355" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">🎯 मान्यता प्राप्त राष्ट्रीय दल:</text>
    <text x="250" y="395" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="17" font-weight="bold" text-anchor="middle">BJP, INC (कांग्रेस), CPI(M), AAP, BSP आदि।</text>
  </g>
</svg>"""

svg4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 650" width="1100" height="650">
  <defs>
    <linearGradient id="bgGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180808"/>
      <stop offset="50%" stop-color="#2d1212"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="titleGrad4" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f87171"/>
      <stop offset="50%" stop-color="#fb923c"/>
      <stop offset="100%" stop-color="#facc15"/>
    </linearGradient>
    <filter id="shadow4" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="1100" height="650" rx="24" fill="url(#bgGrad4)" stroke="#334155" stroke-width="2.5"/>
  <rect x="12" y="12" width="1076" height="626" rx="20" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-opacity="0.4"/>

  <!-- Title -->
  <g filter="url(#shadow4)">
    <rect x="40" y="24" width="1020" height="74" rx="16" fill="#090d16" stroke="#ef4444" stroke-width="3"/>
    <text x="550" y="72" fill="url(#titleGrad4)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">⚠️ राजनीतिक दलों के सामने 4 प्रमुख चुनौतियां (4 Challenges)</text>
  </g>

  <!-- 4 Grid Cards -->
  <g transform="translate(35, 125)" filter="url(#shadow4)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#d97706"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">1. आंतरिक लोकतंत्र की कमी</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• नियमित सांगठनिक चुनावों का अभाव।</text>
    <text x="15" y="130" fill="#fde047" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• शीर्ष 1-2 नेताओं के पास ही शक्ति का केंद्र होना।</text>
  </g>

  <g transform="translate(565, 125)" filter="url(#shadow4)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#fb923c" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#ea580c"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">2. वंशवाद की चुनौती (Dynasty)</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• शीर्ष पदों पर केवल 1 परिवार का नियंत्रण।</text>
    <text x="15" y="130" fill="#fed7aa" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• आम व योग्य कार्यकर्ताओं की उपेक्षा।</text>
  </g>

  <g transform="translate(35, 380)" filter="url(#shadow4)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#ef4444" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#dc2626"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">3. धन और बाहुबल का प्रभाव</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• धनवानों व अपराधियों को चुनाव टिकट देना।</text>
    <text x="15" y="130" fill="#fca5a5" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• चंदा देने वाली कंपनियों का नीतियों पर प्रभाव।</text>
  </g>

  <g transform="translate(565, 380)" filter="url(#shadow4)">
    <rect width="500" height="235" rx="16" fill="#1e293b" stroke="#b91c1c" stroke-width="2.5"/>
    <rect x="0" y="0" width="500" height="50" rx="16" fill="#991b1b"/>
    <text x="250" y="34" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">4. सार्थक विकल्प की कमी</text>
    <text x="15" y="90" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• विभिन्न दलों की नीतियों में वैचारिक एकरूपता।</text>
    <text x="15" y="130" fill="#f87171" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16" font-weight="bold">• मतदाताओं के पास असली नीतियों का अभाव।</text>
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
    <text x="550" y="72" fill="url(#titleGrad5)" font-family="'Tiro Devanagari Hindi', 'Segoe UI', sans-serif" font-size="26" font-weight="900" text-anchor="middle">🛠️ राजनीतिक दलों में सुधार के 5 प्रमुख उपाय (Reforms in Political Parties)</text>
  </g>

  <g transform="translate(35, 120)" filter="url(#shadow5)">
    <rect width="1010" height="495" rx="18" fill="#1e293b" stroke="#34d399" stroke-width="2.5"/>
    
    <text x="25" y="55" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">1. दल-बदल विरोधी कानून:</text>
    <text x="380" y="55" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">जीतने के बाद दल बदलने वाले विधायकों/सांसदों की सदस्यता रद्द।</text>

    <text x="25" y="125" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">2. संपत्ति व मुकदमों का हलफनामा:</text>
    <text x="380" y="125" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">उम्मीदवारों को अपनी संपत्ति व मुकदमों का Affidavit देना अनिवार्य।</text>

    <text x="25" y="195" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">3. सांगठनिक चुनाव व टैक्स रिटर्न:</text>
    <text x="380" y="195" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">दलों में नियमित आंतरिक चुनाव व आय-कर आईटीआर भरना अनिवार्य।</text>

    <text x="25" y="265" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">4. आंतरिक लोकतंत्र हेतु कानून:</text>
    <text x="380" y="265" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">सदस्यों का रजिस्टर रखना व विवादों हेतु स्वतंत्र तंत्र बनाना।</text>

    <text x="25" y="335" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="18" font-weight="900">5. चुनाव का सरकारी खर्च (State Funding):</text>
    <text x="380" y="335" fill="#ffffff" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="16">पेट्रोल, कागज, फोन हेतु सरकार द्वारा वित्तीय सहायता देना।</text>

    <rect x="25" y="390" width="960" height="75" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="505" y="435" fill="#34d399" font-family="'Tiro Devanagari Hindi', sans-serif" font-size="19" font-weight="900" text-anchor="middle">💡 जनता का दबाव व आंदोलन ही राजनीतिक दलों में वास्तविक सुधार ला सकता है!</text>
  </g>
</svg>"""

base_path = r'c:\Users\jiten\Desktop\class11\ss10\images\pol4'
svgs = [
    ('chart_pol4_1_party_components_and_functions.svg', svg1),
    ('chart_pol4_2_three_party_system_models.svg', svg2),
    ('chart_pol4_3_national_vs_regional_party_criteria.svg', svg3),
    ('chart_pol4_4_four_challenges_to_political_parties.svg', svg4),
    ('chart_pol4_5_five_electoral_reforms_in_parties.svg', svg5)
]

for name, content in svgs:
    fp = os.path.join(base_path, name)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated SVG:', name)
