import urllib.request
import json

video_ids = [
    'w49tXp-S2zk', 'm-Br8HPka0o', 'DMmbbweYGKY', 'mMNO_wnZBCw',
    'lPE6tZgvr2I', 'ZJZjaG8Rbps', 'FG4edQ5P4UM', 'qPS0yLEwG3U',
    'DVGzS1wFFOY', 'EfQvegxzNwQ', 'Xyq5xxqI-CA', 'lGSEGjtLHkM',
    '-nm5Pop8usc', '9O8Vc2o7Rf4', 'BLb_2i9pVe4', 'sT3COUk0cv4',
    'aosKebQY4uw', 'qA4dyG3vCpM'
]

results = []
for vid in video_ids:
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    try:
        req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title', '')
            author = data.get('author_name', '')
            results.append({'id': vid, 'title': title, 'author': author})
            print(f"[{vid}] {title} (by {author})")
    except Exception as e:
        print(f"[{vid}] Error: {e}")

with open('shorts_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
