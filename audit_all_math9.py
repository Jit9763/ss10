import glob, re

files = sorted(glob.glob('qa_master_math9_*.html'))

all_passed = True
print(f"Auditing {len(files)} chapters: {files}")

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Check form feeds
    ff_count = text.count('\x0c')
    if ff_count > 0:
        print(f"❌ {fn}: Contains {ff_count} FormFeed (\\x0c) characters!")
        all_passed = False

    # 2. Check Hindi in MathJax
    disp_maths = re.findall(r'\$\$([\s\S]*?)\$\$', text)
    inline_maths = re.findall(r'(?<!\$)\$([^\$\n]+)\$(?!\$)', text)
    hindi_in_math = []
    for m in disp_maths + inline_maths:
        dev = [c for c in m if 0x0900 <= ord(c) <= 0x097F]
        if dev:
            hindi_in_math.append(m.strip())
    if hindi_in_math:
        print(f"❌ {fn}: Contains {len(hindi_in_math)} Hindi strings inside MathJax!")
        for h in hindi_in_math[:5]:
            print("   ->", repr(h))
        all_passed = False

    # 3. Check chained equals in display math
    chained_disp = []
    for d in disp_maths:
        for line in d.split(r'\\'):
            if line.count('=') >= 2:
                chained_disp.append(line.strip())
    if chained_disp:
        print(f"❌ {fn}: Contains {len(chained_disp)} chained display math lines!")
        for cd in chained_disp[:5]:
            print("   ->", cd)
        all_passed = False

    # 4. Check for literal \mathbf
    if r'\mathbf' in text:
        print(f"⚠️ {fn}: Contains \\mathbf")

    # 5. Check meta words
    meta_words = ['(One by One Steps)', '(Vertical Steps)', 'एक के नीचे एक चरण']
    for mw in meta_words:
        if mw in text:
            print(f"⚠️ {fn}: Contains meta commentary '{mw}'")

    if all_passed:
        print(f"✅ {fn}: 100% PASSED all audit checks!")

if all_passed:
    print("\n🎉 ALL AUDITED CHAPTERS ARE 100% CLEAN AND COMPLIANT!")
