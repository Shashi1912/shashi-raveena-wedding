import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"D:\Shashi\Card\Version_2_Interactive_Wings\index.html"
v2_dir = r"D:\Shashi\Card\Version_2_Interactive_Wings"

with open(html_path, "r", encoding="utf-8") as f:
    base_html = f.read()

states = [
    ("mandapam-stage", "preview_v2_closed.png"),
    ("mandapam-stage opened-groom", "preview_v2_groom_wing.png"),
    ("mandapam-stage opened-bride", "preview_v2_bride_wing.png"),
    ("mandapam-stage opened-both", "preview_v2_both_open.png"),
]

for class_name, out_file in states:
    modified = base_html.replace('class="mandapam-stage" id="mandapamStage"', f'class="{class_name}" id="mandapamStage"')
    temp_file = os.path.join(v2_dir, "temp_capture.html")
    with open(temp_file, "w", encoding="utf-8") as tf:
        tf.write(modified)
    
    out_path = os.path.join(v2_dir, out_file)
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1150,920",
        f"--screenshot={out_path}",
        temp_file
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print(f"Captured: {out_file}")

print("All 4 interactive states captured successfully for Version 2!")
