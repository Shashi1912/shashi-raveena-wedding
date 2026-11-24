import json

with open('channel_shorts_data.json', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'\"([a-zA-Z0-9_-]{11})\":\{\"title\"|\"videoId\":\"([a-zA-Z0-9_-]{11})\"', text)
vids = [m[0] or m[1] for m in matches if (m[0] or m[1])]
unique_vids = []
for v in vids:
    if v not in unique_vids:
        unique_vids.append(v)

print("Unique video IDs:", unique_vids)

# Let's inspect the renderer around one of the videoIds
for v in unique_vids[:5]:
    pos = text.find(v)
    start = max(0, pos - 200)
    end = min(len(text), pos + 500)
    print(f"\n--- Context for {v} ---")
    print(text[start:end])
