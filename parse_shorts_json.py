import json

with open('channel_shorts_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find reelItemRenderer or richItemRenderer
shorts_info = []

def walk(obj):
    if isinstance(obj, dict):
        if 'reelItemRenderer' in obj:
            r = obj['reelItemRenderer']
            vid = r.get('videoId')
            headline = r.get('headline', {}).get('simpleText', '')
            shorts_info.append((vid, headline))
        for k, v in obj.items():
            walk(v)
    elif isinstance(obj, list):
        for i in obj:
            walk(i)

walk(data)
print(f"Extracted {len(shorts_info)} shorts:")
for vid, title in shorts_info:
    print(f"https://www.youtube.com/shorts/{vid} -> {title}")
