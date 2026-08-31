/**
 * Universal Floating Control Toolbar for all NCERT Class 10 Master Notes
 * Features:
 * - W+ / W- : Adjust Container Width
 * - A+ / A- : Adjust Text Font Size
 * - B+ / B- : Adjust Text Boldness / Stroke Weight
 * - 📋 : Copy Entire Formatted Content for Google Docs
 * - 🖨️ : Print / Save as PDF
 * - 🏠 : Return to Main Hub
 */

(function() {
    // Inject CSS
    const style = document.createElement('style');
    style.innerHTML = `
        .master-action-bar {
            position: relative;
            margin: 0 auto 30px auto;
            display: flex;
            gap: 12px;
            z-index: 100;
            flex-wrap: wrap;
            justify-content: center;
            background: #0f172a;
            padding: 12px 24px;
            border-radius: 20px;
            border: 3px solid #3b82f6;
            box-shadow: 0 8px 25px rgba(0,0,0,0.35);
            width: fit-content;
        }

        .master-action-btn {
            width: 56px;
            height: 56px;
            border-radius: 14px;
            border: 2.5px solid #3b82f6;
            background: #1e293b;
            color: #ffffff;
            font-size: 1.4rem;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            font-family: 'Segoe UI', Arial, sans-serif;
            user-select: none;
        }

        .master-action-btn:hover {
            transform: scale(1.1);
            background: #3b82f6;
            box-shadow: 0 6px 18px rgba(59, 130, 246, 0.6);
        }

        .master-btn-copy {
            background: #f59e0b;
            color: #000000;
            border-color: #d97706;
        }
        .master-btn-copy:hover {
            background: #d97706;
            color: #ffffff;
        }
        .master-btn-copy.success {
            background: #10b981;
            color: #ffffff;
            border-color: #059669;
        }

        .master-floating-home {
            position: fixed;
            bottom: 20px;
            left: 20px;
            z-index: 99999;
            background: #1e293b;
            color: white;
            width: 52px;
            height: 52px;
            border-radius: 50%;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            border: 2.5px solid #fbbf24;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            transition: all 0.3s ease;
        }
        .master-floating-home:hover {
            transform: scale(1.15);
            background: #fbbf24;
            color: #000;
        }

        @media print {
            .master-action-bar, .master-floating-home {
                display: none !important;
            }
        }
    `;
    document.head.appendChild(style);

    // Create Action Bar DOM
    const bar = document.createElement('div');
    bar.className = 'master-action-bar';
    bar.innerHTML = `
        <button class="master-action-btn" onclick="window.__adjustWidth(120)" title="कंटेनर चौड़ाई तेजी से बढ़ाएँ (W+)">W+</button>
        <button class="master-action-btn" onclick="window.__adjustWidth(-120)" title="कंटेनर चौड़ाई तेजी से घटाएँ (W-)">W-</button>
        <button class="master-action-btn" onclick="window.__adjustFontSize(2.5)" title="अक्षर का आकार बढ़ाएँ (A+)">A+</button>
        <button class="master-action-btn" onclick="window.__adjustFontSize(-2.5)" title="अक्षर का आकार घटाएँ (A-)">A-</button>
        <button class="master-action-btn" onclick="window.__adjustFontWeight(100)" title="अक्षर की मोटाई बढ़ाएँ (B+)">B+</button>
        <button class="master-action-btn" onclick="window.__adjustFontWeight(-100)" title="अक्षर की मोटाई घटाएँ (B-)">B-</button>
        <button id="__masterCopyBtn" class="master-action-btn master-btn-copy" onclick="window.__copyEntireContent()" title="Google Docs के लिए कॉपी करें">📋</button>
        <button class="master-action-btn" onclick="window.print()" title="प्रिंट या PDF सेव करें">🖨️</button>
    `;

    // Create Home Button
    const homeBtn = document.createElement('a');
    homeBtn.href = 'index.html';
    homeBtn.className = 'master-floating-home';
    homeBtn.title = 'मुख्य पृष्ठ पर जाएँ (Home)';
    homeBtn.innerHTML = '🏠';

    function attachToolbar() {
        if (document.querySelector('.master-action-bar-attached')) return;
        const target = document.getElementById('contentToCopy') || document.querySelector('.page-container') || document.querySelector('.copy-container') || document.body;
        if (target) {
            bar.classList.add('master-action-bar-attached');
            if (target.firstChild) {
                target.insertBefore(bar, target.firstChild);
            } else {
                target.appendChild(bar);
            }
        }
        if (!document.querySelector('.master-floating-home')) {
            document.body.appendChild(homeBtn);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', attachToolbar);
    } else {
        attachToolbar();
    }

    // Controls Logic
    let currentWidth = 1400;
    let sizeOffset = 0;
    let weightOffset = 0;
    let strokeOffset = 0;

    window.__adjustWidth = function(amount) {
        currentWidth += amount;
        if (currentWidth < 250) currentWidth = 250;
        if (currentWidth > 10000) currentWidth = 10000;
        const target = document.getElementById('contentToCopy') || document.querySelector('.page-container') || document.querySelector('.copy-container') || document.body;
        if (target) {
            target.style.setProperty('max-width', currentWidth + 'px', 'important');
            target.style.setProperty('width', currentWidth + 'px', 'important');
            target.style.setProperty('margin', '0 auto', 'important');
        }
    };

    window.__adjustFontSize = function(amount) {
        sizeOffset += amount;
        if (sizeOffset < -18) sizeOffset = -18;
        if (sizeOffset > 35) sizeOffset = 35;
        const elements = document.querySelectorAll('body, p, li, td, th, div, span, h1, h2, h3, h4, b, strong');
        elements.forEach(el => {
            if (el.closest('.master-action-bar')) return;
            const currentSize = parseFloat(window.getComputedStyle(el).fontSize);
            if (!el.dataset.origFontSize) {
                el.dataset.origFontSize = currentSize;
            }
            const baseSize = parseFloat(el.dataset.origFontSize);
            el.style.setProperty('font-size', (baseSize + sizeOffset) + 'px', 'important');
        });
    };

    window.__adjustFontWeight = function(amount) {
        weightOffset += amount;
        strokeOffset += (amount / 100) * 0.3;
        if (strokeOffset < -2.0) strokeOffset = -2.0;
        if (strokeOffset > 4.0) strokeOffset = 4.0;

        const elements = document.querySelectorAll('p, li, td, th, div, span, h1, h2, h3, h4, b, strong');
        elements.forEach(el => {
            if (el.closest('.master-action-bar')) return;
            if (weightOffset > 0) {
                el.style.setProperty('font-weight', '900', 'important');
                el.style.setProperty('-webkit-text-stroke', (1.1 + strokeOffset) + 'px #000', 'important');
            } else if (weightOffset < 0) {
                el.style.setProperty('font-weight', 'normal', 'important');
                el.style.setProperty('-webkit-text-stroke', '0px', 'important');
            } else {
                el.style.removeProperty('-webkit-text-stroke');
            }
        });
    };

    window.__copyEntireContent = async function() {
        const btn = document.getElementById('__masterCopyBtn');
        const target = document.getElementById('contentToCopy') || document.querySelector('.page-container') || document.querySelector('.copy-container') || document.body;
        
        const clone = target.cloneNode(true);
        // Remove toolbar from copy
        const barInClone = clone.querySelector('.master-action-bar');
        if (barInClone) barInClone.remove();
        const homeInClone = clone.querySelector('.master-floating-home');
        if (homeInClone) homeInClone.remove();

        const images = clone.querySelectorAll('img');
        images.forEach(img => {
            img.setAttribute('src', img.src);
        });

        const content = clone.innerHTML;
        try {
            const blob = new Blob([content], { type: 'text/html' });
            const item = new ClipboardItem({ 'text/html': blob });
            await navigator.clipboard.write([item]);
            btn.innerText = '✅';
            btn.classList.add('success');
            setTimeout(() => {
                btn.innerText = '📋';
                btn.classList.remove('success');
            }, 3000);
        } catch (err) {
            // Fallback
            const txt = clone.innerText;
            await navigator.clipboard.writeText(txt);
            btn.innerText = '✅';
            btn.classList.add('success');
            setTimeout(() => {
                btn.innerText = '📋';
                btn.classList.remove('success');
            }, 3000);
        }
    };

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
        if (['INPUT', 'TEXTAREA'].includes(document.activeElement?.tagName)) return;
        if (e.key === 'w' || e.key === 'W') {
            if (e.shiftKey) window.__adjustWidth(-120);
            else window.__adjustWidth(120);
        } else if (e.key === '+' || e.key === '=') {
            window.__adjustFontSize(2.5);
        } else if (e.key === '-') {
            window.__adjustFontSize(-2.5);
        }
    });
})();
