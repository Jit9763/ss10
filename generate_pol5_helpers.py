import os
import sys
import subprocess
from PIL import Image, ImageGrab

# Directory setup
WORKSPACE_DIR = r"c:\Users\jiten\Desktop\class11\ss10"
POL5_IMG_DIR = os.path.join(WORKSPACE_DIR, "images", "pol5")
os.makedirs(POL5_IMG_DIR, exist_ok=True)

# Prompts dictionary for Chapter 5 (Pol 5)
PROMPTS = {
    1: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'समानता व गरिमा (Equality & Dignity)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing diverse citizens standing together equally.
Right card top title: 'बेहतर निर्णय व सुधार (Better Decisions & Improvement)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing thoughtful consultation meeting room.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    2: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'उच्च अपेक्षाएं (High Expectations)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing citizens expecting fast economic growth and perfect governance.
Right card top title: 'वास्तविक परिणाम (Actual Outcomes)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing gradual progress, debates, and compromise in democracy.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    3: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'उत्तरदायी सरकार (Accountable Government)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing government official explaining public policies to citizens.
Right card top title: 'जवाबदेही व नियम (Responsibility & Rules)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing constitution book and open procedures.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    4: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'पारदर्शिता (Transparency)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing clear open window to government decisions and public documents.
Right card top title: 'सूचना का अधिकार (Right to Information RTI 2005)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing citizen receiving official information document.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    5: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'जन-आवश्यकताओं की पूर्ति (Meeting Public Needs)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing healthcare, education, and water supply services.
Right card top title: 'जनमत का सम्मान (Respecting Public Opinion)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing leaders listening to public feedback in townhall.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    6: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'वैध सरकार (Legitimate Government)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing democratic election process where people elect their representatives.
Right card top title: 'संविधान का शासन (Rule of Law & Constitution)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing constitutional book and judicial balance scales.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    7: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'आर्थिक विकास (Economic Growth)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing growth chart comparison between dictatorship and democracy.
Right card top title: 'समावेशी विकास (Inclusive Growth)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing economic benefits reaching all sections of society.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    8: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'आर्थिक असमानता (Economic Inequality)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing wealth distribution gap chart.
Right card top title: 'समावेशी नीतियां (Inclusive Policies)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing government welfare support for low income families.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    9: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'गरीब मतदाता (Poor Voters as Voting Power)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing large population of ordinary citizens holding ballot power.
Right card top title: 'जनकल्याणकारी योजनाएं (Welfare Schemes)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing food security ration distribution and rural employment programs.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    10: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'प्रगतिशील कर प्रणाली (Progressive Taxation)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing tax collection scale redistributing resources.
Right card top title: 'अवसरों की समानता (Equal Opportunities)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing equal access to education and jobs for all.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    11: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'सामाजिक विविधताएं (Social Diversity)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing peaceful resolution of differences between diverse cultural groups.
Right card top title: 'बहुसांस्कृतिक सह-अस्तित्व (Multicultural Coexistence)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing harmony among different linguistic and religious communities.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    12: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'सर्वसमावेशी लोकतंत्र (Inclusive Democracy)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing decision making that respects minority views, not just majority rule.
Right card top title: 'हर नागरिक को अवसर (Equal Right to Form Majority)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing changing political majorities based on open elections.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    13: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'महिलाओं की गरिमा (Dignity of Women)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing women participating equally in workforce and parliament.
Right card top title: 'कानूनी व सामाजिक समानता (Legal & Social Equality)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing equal legal rights protection emblem for women.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    14: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'वंचित जातियों का सशक्तीकरण (Empowerment of Marginalized Castes)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing dignity and end of discrimination (Article 17).
Right card top title: 'आरक्षण व प्रतिनिधित्व (Reservation & Representation)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing representation in local governance and education.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    15: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'मौलिक स्वतंत्रताएँ (Fundamental Freedoms)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing freedom of speech, expression, and peaceful assembly.
Right card top title: 'न्यायिक संरक्षण (Judicial Protection)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing Supreme Court emblem protecting fundamental rights.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    16: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'स्वतंत्र मीडिया (Independent Media)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing unbiased journalist reporting and public discourse.
Right card top title: 'जन-बहस व जागरूकता (Public Debate & Awareness)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing informed citizens discussing national issues.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    17: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'भ्रष्टाचार पर नियंत्रण (Control on Corruption)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing transparent anti-corruption audit institution.
Right card top title: 'ई-गवर्नेंस (E-Governance & DBT)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing direct benefit transfer digital services to citizens.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    18: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'स्थानीय स्वशासन (Local Self-Government)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing direct citizen participation in Gram Sabha village meeting.
Right card top title: 'पंचायती राज (Panchayati Raj Leadership)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing elected village woman Sarpanch leading local council.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    19: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'शिकायतें: सफलता का प्रमाण (Complaints: Proof of Success)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing active citizens raising issues to improve democracy.
Right card top title: 'सजग नागरिक (Vigilant & Conscious Citizens)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing citizens voting actively and holding leaders accountable.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags.""",

    20: """A 16:9 minimalist clean 2D vector educational textbook illustration card on a pure solid white background, high resolution classroom teaching visual.
Left card top title: 'सशक्त लोकतांत्रिक राष्ट्र (Strong Democratic Nation)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing constitutional supremacy, sovereignty, and rule of law.
Right card top title: 'विश्व का विशालतम लोकतंत्र (World Largest Democracy)' placed ONCE at top. NO numbers, NO duplicate title at bottom. Showing vibrant multi-ethnic population celebrating democracy.
Pure Hindi Devanagari text labels inside diagram. Bright primary colors, flat design, crisp vector graphics, zero living politicians, zero real party flags."""
}

def copy_prompt(img_num):
    """Copy prompt for img_num to Windows clipboard."""
    if img_num not in PROMPTS:
        print(f"Error: Prompt {img_num} not found.")
        return False
    prompt_str = PROMPTS[img_num]
    p = subprocess.Popen('clip', stdin=subprocess.PIPE, shell=True)
    p.communicate(input=prompt_str.encode('utf-16le'))
    print(f"Successfully copied Prompt {img_num} to clipboard.")
    return True

def save_clipboard_image(img_num):
    """Grab copied image from clipboard and save directly as pol5_real_X.webp."""
    out_path = os.path.join(POL5_IMG_DIR, f"pol5_real_{img_num}.webp")
    img = ImageGrab.grabclipboard()
    if img is None:
        print("Error: No image found in clipboard!")
        return False
    
    if isinstance(img, list): # file paths copied
        img = Image.open(img[0])
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    img.save(out_path, format="WEBP", quality=95)
    print(f"SUCCESS: Saved full clipboard image to {out_path} (Size: {img.size})")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "copy" and len(sys.argv) > 2:
            copy_prompt(int(sys.argv[2]))
        elif cmd == "save_clip" and len(sys.argv) > 2:
            save_clipboard_image(int(sys.argv[2]))
        else:
            print("Usage: python generate_pol5_helpers.py copy <num> | save_clip <num>")
    else:
        print("Pol5 Generator Helpers initialized.")
