import os
import shutil

src_dir = r"D:\Shashi\Card\Version_1_Mandapam_Gatefold"
dest_dir = r"D:\Shashi\Card\Version_2_Interactive_Wings"

os.makedirs(dest_dir, exist_ok=True)

assets = [
    "feet_artwork_feathered.png",
    "venue_qr.svg",
    "venue_qr.png",
    "ganesha_clean.png",
    "sikku_kolam_clean.png",
    "GreatVibes-Regular.ttf",
]

for a in assets:
    s = os.path.join(src_dir, a)
    d = os.path.join(dest_dir, a)
    if os.path.exists(s):
        shutil.copy2(s, d)

print("Version 2 directory initialized with all assets!")
