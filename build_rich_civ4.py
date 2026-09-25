import os

# Read current copy_master_civ4.html
with open(os.path.join(os.path.dirname(__file__), "copy_master_civ4.html"), "r", encoding="utf-8") as f:
    html_content = f.read()

out_path = os.path.join(os.path.dirname(__file__), "copy_master_civ4.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {out_path} ({len(html_content)} chars)")
