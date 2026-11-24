import json
import re

with open('yt_videos.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'var ytInitialData\s*=\s*({.*?});</script>', text)
if m:
    data = json.loads(m.group(1))
    print("Found ytInitialData!")
    # dump titles and videoIds
    # recursive search for videoId and title
    def find_videos(obj):
        if isinstance(obj, dict):
            if 'videoId' in obj:
                title = obj.get('title', {})
                if isinstance(title, dict):
                    runs = title.get('runs', [])
                    if runs:
                        print(f"Video: {obj['videoId']} - {runs[0].get('text')}")
                    elif 'simpleText' in title:
                        print(f"Video: {obj['videoId']} - {title.get('simpleText')}")
            for k, v in obj.items():
                find_videos(v)
        elif isinstance(obj, list):
            for item in obj:
                find_videos(item)
    find_videos(data)
else:
    print("ytInitialData not found")
