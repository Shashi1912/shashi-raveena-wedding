import re
import json

with open('ig_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check title, description, og tags
print("=== Meta tags ===")
for m in re.findall(r'<meta [^>]+>', text):
    if any(k in m.lower() for k in ['title', 'description', 'og:', 'twitter:']):
        print(m)

# Find any json objects or strings containing 'video' or 'postcard' or 'wedding' or 'shortcode' or 'edge_owner_to_timeline_media'
print("\n=== Search keywords ===")
for kw in ['postcard', 'vintage', 'wedding', 'invitation', 'card']:
    matches = [m.start() for m in re.finditer(kw, text, re.IGNORECASE)]
    print(f"Keyword '{kw}': {len(matches)} occurrences")

# Find reel/post URLs or shortcodes
print("\n=== Posts / Reels ===")
shortcodes = set(re.findall(r'/(?:p|reel)/([A-Za-z0-9_-]+)/', text))
print("Found shortcodes:", list(shortcodes)[:20])

