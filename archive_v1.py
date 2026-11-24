import os
import shutil

src_dir = r"D:\Shashi\Card\Unique_Wedding_Invitations"
dest_dir = r"D:\Shashi\Card\Version_1_Mandapam_Gatefold"

os.makedirs(dest_dir, exist_ok=True)

files_to_copy = [
    ("concept3_mandapam_gatefold.html", "index.html"),
    ("concept3_mandapam_gatefold.html", "mandapam_gatefold_v1.html"),
    ("preview_concept3_mandapam_gatefold.png", "preview_concept3_mandapam_gatefold.png"),
    ("preview_concept3_opened.png", "preview_concept3_opened.png"),
    ("feet_artwork_feathered.png", "feet_artwork_feathered.png"),
    ("venue_qr.svg", "venue_qr.svg"),
    ("venue_qr.png", "venue_qr.png"),
    ("ganesha_clean.png", "ganesha_clean.png"),
    ("sikku_kolam_clean.png", "sikku_kolam_clean.png"),
    ("GreatVibes-Regular.ttf", "GreatVibes-Regular.ttf"),
]

for src_name, dest_name in files_to_copy:
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)

# Create a locked backup inside Unique_Wedding_Invitations as well
shutil.copy2(
    os.path.join(src_dir, "concept3_mandapam_gatefold.html"),
    os.path.join(src_dir, "version1_mandapam_gatefold_LOCKED.html")
)

# Create README.txt in Version_1 folder
readme_content = """===============================================================
SHASHI & RAVEENA - WEDDING INVITATION (VERSION 1 - LOCKED)
===============================================================
STATUS: FROZEN / DO NOT MODIFY
DATE CREATED: 24th November 2026

Design: Concept 3 - Interactive Royal Mandapam Double Gatefold Doors
- Auspicious Date: Sunday, 13th December 2026
- Sumuhurtham: 09:50 AM (Dhanur Lagna • Saptapadi)
- Grand Reception: Following the Marriage (Wedding Lunch & Celebrations)
- Venue: Thanmaya Farmstay & Resort, Near Chinna Pendyala, 
  Rajaram (Rajavaram), Warangal-Hyderabad Highway, Telangana (PIN: 506144)
- Google Maps Navigation: Direct GPS route via scannable/clickable QR badge

Contents of this locked folder:
1. index.html & mandapam_gatefold_v1.html (Master Interactive Web Invitation)
2. preview_concept3_mandapam_gatefold.png (Closed Teak Doors Preview)
3. preview_concept3_opened.png (Inner Sanctum Opened Preview)
4. Vector Assets: venue_qr.svg, venue_qr.png, feet_artwork_feathered.png,
   ganesha_clean.png, sikku_kolam_clean.png, GreatVibes-Regular.ttf
===============================================================
"""

with open(os.path.join(dest_dir, "README_VERSION_1.txt"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Version 1 successfully archived and locked!")
