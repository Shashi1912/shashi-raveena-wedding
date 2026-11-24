import urllib.request
import re
import json

channel_id = 'UCSwFHMCpTMuu1L42gpZ4jlg'
url = f'https://www.youtube.com/channel/{channel_id}/shorts'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

with open('alanaati_channel_shorts.html', 'w', encoding='utf-8') as f:
    f.write(html)

m = re.search(r'var ytInitialData\s*=\s*({.*?});</script>', html)
if m:
    data = json.loads(m.group(1))
    with open('channel_shorts_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Saved channel_shorts_data.json!")
    
    # parse all video titles and videoIds
    found = []
    def extract_shorts(obj):
        if isinstance(obj, dict):
            if 'videoId' in obj:
                v_id = obj['videoId']
                # headline or title
                headline = ""
                if 'headline' in obj and 'simpleText' in obj['headline']:
                    headline = obj['headline']['simpleText']
                elif 'title' in obj:
                    t = obj['title']
                    if 'simpleText' in t:
                        headline = t['simpleText']
                    elif 'runs' in t:
                        headline = "".join(r.get('text', '') for r in t['runs'])
                found.append((v_id, headline))
            for k, v in obj.items():
                extract_shorts(v)
        elif isinstance(obj, list):
            for item in obj:
                extract_shorts(item)
    extract_shorts(data)
    # Deduplicate while preserving order
    seen = set()
    for vid, title in found:
        if vid not in seen:
            seen.add(vid)
            print(f"Short: https://www.youtube.com/shorts/{vid} | Title: {title}")
else:
    print("Could not find ytInitialData")
