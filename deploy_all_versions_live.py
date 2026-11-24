import subprocess
import os
import shutil

print("=== 1. PROCESSING NEW BRIDE TRACK (Snehithane Violin) ===")
raw_bride = "D:/Shashi/Card/V5_Audio/bride_5AuhX5l8Zz8.mp3"
bride_8d = "D:/Shashi/Card/V5_Audio/bride_8d.mp3"
filter_chain = "apulsator=mode=sine:hz=0.12:amount=0.82,extrastereo=m=1.2,aecho=0.8:0.85:30:0.25,loudnorm=I=-14:TP=-1.0:LRA=11"

cmd_8d = [
    "ffmpeg", "-i", raw_bride,
    "-af", filter_chain,
    "-b:a", "192k",
    bride_8d, "-y"
]
p = subprocess.run(cmd_8d, capture_output=True, text=True)
if p.returncode == 0:
    print(f"Generated bride_8d.mp3 successfully: {os.path.getsize(bride_8d)} bytes")
else:
    print("FFmpeg error:", p.stderr[-300:])

# Also generate a crisp non-8D master for earlier versions
cmd_norm = [
    "ffmpeg", "-i", raw_bride,
    "-af", "loudnorm=I=-14:TP=-1.0",
    "-b:a", "192k",
    "D:/Shashi/Card/V5_Audio/bride_snehithane_norm.mp3", "-y"
]
subprocess.run(cmd_norm, check=True)

# Copy bride_8d.mp3 to Version_5_Spatial_8D and root
shutil.copyfile(bride_8d, "D:/Shashi/Card/Version_5_Spatial_8D/bride_8d.mp3")
shutil.copyfile(bride_8d, "D:/Shashi/Card/bride_8d.mp3")
shutil.copyfile("D:/Shashi/Card/V5_Audio/bride_snehithane_norm.mp3", "D:/Shashi/Card/Version_3_Door_Touch/sound_bride_side.mp3")
shutil.copyfile("D:/Shashi/Card/V5_Audio/bride_snehithane_norm.mp3", "D:/Shashi/Card/sound_bride_side.mp3")
print("Copied bride audio to Version_5, Version_3, and root.")

# Update V5 label to Snehithane 8D
v5_index = "D:/Shashi/Card/Version_5_Spatial_8D/index.html"
with open(v5_index, "r", encoding="utf-8") as f:
    v5_html = f.read()

v5_html = v5_html.replace(
    "playSectionSound(audioBride, '👰 వధువు వైభోగం (Violin 8D)', '👰🎻');",
    "playSectionSound(audioBride, '👰 వధువు వైభోగం (స్నేహితనే 8D)', '👰🎻');"
)
with open(v5_index, "w", encoding="utf-8") as f:
    f.write(v5_html)

shutil.copyfile(v5_index, "D:/Shashi/Card/Version_5_Spatial_8D/Shashi_Raveena_Wedding_Invitation_v5.html")
print("Updated V5 HTML with Snehithane label.")

print("\n=== 2. PREPARING ALL VERSIONS FOR LIVE DEPLOYMENT ===")
# Root index.html = Version 5 (The latest flagship)
shutil.copyfile(v5_index, "D:/Shashi/Card/index.html")
shutil.copyfile(v5_index, "D:/Shashi/Card/v5.html")
print("Created root index.html (Version 5 flagship) and v5.html")

# v3.html = Version 3
v3_index = "D:/Shashi/Card/Version_3_Door_Touch/index.html"
shutil.copyfile(v3_index, "D:/Shashi/Card/v3.html")
print("Created root v3.html (Version 3 Door Touch)")

# v2.html = Version 2
v2_index = "D:/Shashi/Card/Version_2_Interactive_Wings/index.html"
shutil.copyfile(v2_index, "D:/Shashi/Card/v2.html")
print("Created root v2.html (Version 2 Interactive Wings)")

# v1.html = Version 1
v1_index = "D:/Shashi/Card/Version_1_Mandapam_Gatefold/index.html"
shutil.copyfile(v1_index, "D:/Shashi/Card/v1.html")
print("Created root v1.html (Version 1 Original Mandapam)")

# Copy all audio files needed for all versions to root
root_audios = [
    "entry_8d.mp3",
    "bride_8d.mp3",
    "groom_8d.mp3",
    "main_8d.mp3",
    "sound_groom_side.mp3",
    "sound_bride_side.mp3",
    "kettimelam_exact_mela.mp3"
]
for ra in root_audios:
    for folder in ["D:/Shashi/Card/Version_5_Spatial_8D", "D:/Shashi/Card/V5_Audio", "D:/Shashi/Card/Version_3_Door_Touch"]:
        src = os.path.join(folder, ra)
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join("D:/Shashi/Card", ra))
            break
print("Synchronized all audio assets to root directory.")

print("\n=== 3. GIT STATUS & DEPLOYMENT TO GITHUB PAGES ===")
def run_git(cmd):
    p = subprocess.run(cmd, cwd="D:/Shashi/Card", shell=True, capture_output=True, text=True)
    if p.stdout.strip():
        print(p.stdout.strip())
    if p.stderr.strip() and "warning:" not in p.stderr.lower():
        print("STDERR:", p.stderr.strip())
    return p.returncode

run_git("git add .")
run_git('git commit -m "Deploy all versions (V1, V2, V3, V5) with Snehithane 8D bride track & welcome screen"')
ret = run_git("git push origin main")
if ret == 0:
    print("\nSUCCESS: All versions pushed live to GitHub Pages!")
else:
    print("Push failed with code:", ret)

print("""
Live URLs:
  Main Flagship (V5): https://shashi1912.github.io/shashi-raveena-wedding/
  Version 5:         https://shashi1912.github.io/shashi-raveena-wedding/v5.html
  Version 3:         https://shashi1912.github.io/shashi-raveena-wedding/v3.html
  Version 2:         https://shashi1912.github.io/shashi-raveena-wedding/v2.html
  Version 1:         https://shashi1912.github.io/shashi-raveena-wedding/v1.html
""")
