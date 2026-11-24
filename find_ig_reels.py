import re
import json

with open('alanaatii_fb.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for /reel/ or /p/
reels = set(re.findall(r'instagram\.com/(?:reel|p)/([A-Za-z0-9_-]+)', text))
print("Reels found with domain:", reels)

# Let's search for any shortcode pattern "shortcode":"..." or "code":"..."
codes = set(re.findall(r'\"(?:shortcode|code)\":\"([A-Za-z0-9_-]{10,13})\"', text))
print("Shortcodes found:", codes)

# Let's search for video urls (.mp4)
mp4s = set(re.findall(r'https?://[^\s\"\'<>]+\.mp4[^\s\"\'<>]*', text))
print("MP4s found:", len(mp4s))
for m in list(mp4s)[:5]:
    print("MP4:", m[:100])

# Let's search for captions or descriptions
texts = re.findall(r'\"text\":\"(.*?)\"', text)
print(f"Total texts found: {len(texts)}")
for t in texts[:20]:
    if any(k in t.lower() for k in ['postcard', 'wedding', 'card', 'letter', 'pelli']):
        print("MATCH TEXT:", t.encode('utf-8', 'ignore').decode('unicode_escape', 'ignore'))
