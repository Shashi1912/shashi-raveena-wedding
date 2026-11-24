import subprocess
import os
import json
import re

# 1. Download Groom track
url = "https://www.youtube.com/shorts/0QsHcbd1CQ8"
audio_dir = "D:/Shashi/Card/V5_Audio"
raw_groom = os.path.join(audio_dir, "groom_0QsHcbd1CQ8.mp3")

print(f"1. Downloading Groom short: {url}")
cmd_dl = [
    "yt-dlp", "-x", "--audio-format", "mp3", "--audio-quality", "0",
    "-o", os.path.join(audio_dir, "groom_0QsHcbd1CQ8.%(ext)s"),
    url
]
p_dl = subprocess.run(cmd_dl, capture_output=True, text=True)
if p_dl.returncode == 0:
    print(f"Downloaded groom raw audio: {os.path.getsize(raw_groom)} bytes")
else:
    print("Download error:", p_dl.stderr[:300])

# Get metadata
cmd_info = ["yt-dlp", "--dump-json", url]
p_info = subprocess.run(cmd_info, capture_output=True, text=True)
try:
    info = json.loads(p_info.stdout)
    print("Groom track title:", info.get("title"))
    print("Groom track duration:", info.get("duration"))
except Exception as e:
    print("Metadata parse error:", e)

# 2. Process into 8D audio
filter_chain = "apulsator=mode=sine:hz=0.12:amount=0.82,extrastereo=m=1.2,aecho=0.8:0.85:30:0.25,loudnorm=I=-14:TP=-1.0:LRA=11"
groom_8d_path = os.path.join(audio_dir, "groom_8d.mp3")
v5_groom_8d = "D:/Shashi/Card/Version_5_Spatial_8D/groom_8d.mp3"

cmd_8d = [
    "ffmpeg", "-i", raw_groom,
    "-af", filter_chain,
    "-b:a", "192k",
    groom_8d_path, "-y"
]
print("2. Converting Groom audio to 8D format...")
p_8d = subprocess.run(cmd_8d, capture_output=True, text=True)
if p_8d.returncode == 0:
    import shutil
    shutil.copyfile(groom_8d_path, v5_groom_8d)
    print(f"Success: groom_8d.mp3 generated and copied to V5 ({os.path.getsize(v5_groom_8d)} bytes)")
else:
    print("8D conversion error:", p_8d.stderr[-300:])

# 3. Update Calendar name across ALL versions
print("\n3. Updating Calendar name in all versions (removing 'Royal Wedding')...")
search_dirs = [
    "D:/Shashi/Card",
    "D:/Shashi/Card/Version_2_Interactive_Wings",
    "D:/Shashi/Card/Version_3_Door_Touch",
    "D:/Shashi/Card/Version_5_Spatial_8D"
]

target_files = []
for d in search_dirs:
    for f in os.listdir(d):
        if f.endswith(".html") or f.endswith(".py"):
            target_files.append(os.path.join(d, f))

# Also include build scripts
target_files.extend([
    "D:/Shashi/Card/build_v3.py",
    "D:/Shashi/Card/build_v5.py"
])
target_files = sorted(list(set(target_files)))

replacements = [
    ("Shashi+%26+Raveena+Wedding", "Shashi+%26+Raveena+Wedding"),
    ("Shashi%20%26%20Raveena%20Wedding", "Shashi%20%26%20Raveena%20Wedding"),
    ("Shashi & Raveena Wedding", "Shashi & Raveena Wedding"),
    ("Shashi &amp; Raveena Wedding", "Shashi &amp; Raveena Wedding")
]

modified_count = 0
for fpath in target_files:
    if not os.path.isfile(fpath):
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    new_content = content
    for old_s, new_s in replacements:
        new_content = new_content.replace(old_s, new_s)
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Updated calendar title in: {os.path.relpath(fpath, 'D:/Shashi/Card')}")
        modified_count += 1

print(f"\nTotal files updated: {modified_count}")
