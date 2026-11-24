import os
import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_path = r"D:\Shashi\Card\Version_2_Interactive_Wings\index.html"
v2_dir = r"D:\Shashi\Card\Version_2_Interactive_Wings"

with open(html_path, "r", encoding="utf-8") as f:
    base_html = f.read()

styles_to_render = [
    ("setPortraitStyle('lineart');", "preview_style_1_gold_lineart.png"),
    ("setPortraitStyle('doodle');", "preview_style_2_cute_doodle.png"),
    ("setPortraitStyle('heritage');", "preview_style_3_royal_heritage.png"),
    ("setPortraitStyle('emblem');", "preview_style_4_sacred_emblems.png"),
    ("setPortraitStyle('lineart'); openGroomWing();", "preview_groom_wing_lineart.png"),
    ("setPortraitStyle('lineart'); openBrideWing();", "preview_bride_wing_lineart.png"),
]

for script_call, out_file in styles_to_render:
    temp_file = os.path.join(v2_dir, "temp_style_capture.html")
    injected_html = base_html.replace("</body>", f"<script>{script_call}</script></body>")
    with open(temp_file, "w", encoding="utf-8") as tf:
        tf.write(injected_html)
        
    out_path = os.path.join(v2_dir, out_file)
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1180,950",
        f"--screenshot={out_path}",
        temp_file
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print(f"Captured: {out_file}")

print("All style previews rendered successfully!")
