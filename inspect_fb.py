import re
import json

with open('alanaatii_fb.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File length:", len(text))

# Search for shortcode or post ids or text
shortcodes = set(re.findall(r'\"code\":\"([^\"]+)\"', text))
print("Found codes:", len(shortcodes), list(shortcodes)[:10])

# Search for edge_owner_to_timeline_media or xdt_api__v1__feed
matches = re.findall(r'\"([^\"]*postcard[^\"]*)\"', text, re.I)
print("Matches with postcard:", len(matches), matches[:5])

matches_card = re.findall(r'\"([^\"]*vintage[^\"]*)\"', text, re.I)
print("Matches with vintage:", len(matches_card), matches_card[:5])

# Find any post captions or text
captions = re.findall(r'\"text\":\"([^\"]{20,200})\"', text)
print("Found captions:", len(captions))
for c in captions[:10]:
    print("-", c.encode('utf-8', 'ignore').decode('unicode_escape', 'ignore'))

# Let's search for json scripts
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
for i, s in enumerate(scripts):
    if 'edge_owner_to_timeline_media' in s or 'xdt_api' in s or 'items' in s:
        print(f"Script {i} has timeline media or items! len: {len(s)}")
