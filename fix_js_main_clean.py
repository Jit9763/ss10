with open('js/main.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

target = r"onclick=\"window.open(\'qa_master_\' + chapter.id + \'.html\', \'_blank\')\""
clean = r"onclick=\"window.open('qa_master_' + chapter.id + '.html', '_blank')\""

js_code = js_code.replace(target, clean)

with open('js/main.js', 'w', encoding='utf-8') as out_f:
    out_f.write(js_code)

print("SUCCESS! Cleaned js/main.js button line!")
