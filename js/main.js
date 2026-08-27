/**
 * Class 10 NCERT Social Science Interactive Portal Logic
 */

const chapters = [
  // History (इतिहास)
  { id: "hist1", num: 1, subject: "history", subjectName: "इतिहास", title: "यूरोप में राष्ट्रवाद का उदय" },
  { id: "hist2", num: 2, subject: "history", subjectName: "इतिहास", title: "भारत में राष्ट्रवाद" },
  { id: "hist3", num: 3, subject: "history", subjectName: "इतिहास", title: "भूमंडलीकृत विश्व का बनना" },
  { id: "hist4", num: 4, subject: "history", subjectName: "इतिहास", title: "औद्योगिकरण का युग" },
  { id: "hist5", num: 5, subject: "history", subjectName: "इतिहास", title: "मुद्रण संस्कृति और आधुनिक दुनिया" },

  // Geography (भूगोल)
  { id: "geo1", num: 1, subject: "geography", subjectName: "भूगोल", title: "संसाधन एवं विकास" },
  { id: "geo2", num: 2, subject: "geography", subjectName: "भूगोल", title: "वन एवं वन्यजीव संसाधन" },
  { id: "geo3", num: 3, subject: "geography", subjectName: "भूगोल", title: "जल संसाधन" },
  { id: "geo4", num: 4, subject: "geography", subjectName: "भूगोल", title: "कृषि" },
  { id: "geo5", num: 5, subject: "geography", subjectName: "भूगोल", title: "खनिज तथा ऊर्जा संसाधन" },
  { id: "geo6", num: 6, subject: "geography", subjectName: "भूगोल", title: "विनिर्माण उद्योग" },
  { id: "geo7", num: 7, subject: "geography", subjectName: "भूगोल", title: "राष्ट्रीय अर्थव्यवस्था की जीवन रेखाएं" },

  // Civics (लोकतांत्रिक राजनीति)
  { id: "civ1", num: 1, subject: "civics", subjectName: "राजनीति विज्ञान", title: "सत्ता की साझेदारी" },
  { id: "civ2", num: 2, subject: "civics", subjectName: "राजनीति विज्ञान", title: "संघवाद" },
  { id: "civ3", num: 3, subject: "civics", subjectName: "राजनीति विज्ञान", title: "जाति, धर्म और लैंगिक मसले" },
  { id: "civ4", num: 4, subject: "civics", subjectName: "राजनीति विज्ञान", title: "राजनीतिक दल" },
  { id: "civ5", num: 5, subject: "civics", subjectName: "राजनीति विज्ञान", title: "लोकतंत्र के परिणाम" },

  // Economics (अर्थशास्त्र)
  { id: "eco1", num: 1, subject: "economics", subjectName: "अर्थशास्त्र", title: "विकास" },
  { id: "eco2", num: 2, subject: "economics", subjectName: "अर्थशास्त्र", title: "भारतीय अर्थव्यवस्था के क्षेत्रक" },
  { id: "eco3", num: 3, subject: "economics", subjectName: "अर्थशास्त्र", title: "मुद्रा और साख" },
  { id: "eco4", num: 4, subject: "economics", subjectName: "अर्थशास्त्र", title: "वैश्वीकरण और भारतीय अर्थव्यवस्था" },
  { id: "eco5", num: 5, subject: "economics", subjectName: "अर्थशास्त्र", title: "उपभोक्ता अधिकार" }
];

let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', () => {
  renderChapters(chapters);

  const searchBar = document.getElementById('searchBar');
  if (searchBar) {
    searchBar.addEventListener('input', filterAndRender);
  }

  const tabButtons = document.querySelectorAll('.tab-btn');
  tabButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      tabButtons.forEach(b => b.classList.remove('active'));
      e.target.classList.add('active');
      currentFilter = e.target.getAttribute('data-subject');
      filterAndRender();
    });
  });
});

function filterAndRender() {
  const searchTerm = (document.getElementById('searchBar')?.value || '').toLowerCase();
  
  const filtered = chapters.filter(chap => {
    const matchesSubject = (currentFilter === 'all' || chap.subject === currentFilter);
    const matchesSearch = chap.title.toLowerCase().includes(searchTerm) || 
                          chap.subjectName.toLowerCase().includes(searchTerm);
    return matchesSubject && matchesSearch;
  });

  renderChapters(filtered);
}

function renderChapters(data) {
  const grid = document.getElementById('chapter-grid');
  if (!grid) return;

  grid.innerHTML = '';

  if (data.length === 0) {
    grid.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:3rem; color: var(--text-secondary);">
      <h3>कोई अध्याय नहीं मिला।</h3>
      <p>कृपया अपनी खोज शब्द बदलें।</p>
    </div>`;
    return;
  }

  data.forEach((chapter, index) => {
    const card = document.createElement('div');
    card.className = 'chapter-card';
    
    let badgeClass = `badge-${chapter.subject}`;
    
    card.innerHTML = `
      <span class="subject-badge ${badgeClass}">${chapter.subjectName}</span>
      <div class="chapter-num">${String(chapter.num).padStart(2, '0')}</div>
      <h3 class="chapter-title">${chapter.title}</h3>
      <div class="chapter-actions">
        <button class="btn-primary" onclick="window.open('notes_html_view.html?id=${chapter.id}', '_blank')">🌍 संपूर्ण नोट्स देखें (Premium HTML)</button>
        <button class="btn-secondary-notes" onclick="window.open('notes_copy_view.html?id=${chapter.id}', '_blank')">📝 छात्र नोट्स (Copy View)</button>
        <button class="btn-secondary-qa" onclick="window.open((chapter.id.startsWith('hist') || chapter.id === 'geo7') ? 'qa_master_' + chapter.id + '.html' : 'qa_view.html?id=' + chapter.id, '_blank')">❓ प्रश्न-उत्तर (Master Q&A)</button>
      </div>
    `;
    grid.appendChild(card);
  });
}
