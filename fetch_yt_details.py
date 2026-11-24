import urllib.request
import re
import json

targets = ['qPS0yLEwG3U', 'DMmbbweYGKY', 'aosKebQY4uw', 'w49tXp-S2zk', 'm-Br8HPka0o', 'FG4edQ5P4UM']

for vid in targets:
    url = f'https://www.youtube.com/watch?v={vid}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract title and description
            m_title = re.findall(r'<meta property=\"og:title\" content=\"(.*?)\"', html)
            m_desc = re.findall(r'<meta property=\"og:description\" content=\"(.*?)\"', html)
            m_tags = re.findall(r'<meta property=\"og:video:tag\" content=\"(.*?)\"', html)
            
            # Look for captions or subtitles url
            captions_match = re.search(r'\"captionTracks\":(\[.*?\])', html)
            captions_info = "Yes" if captions_match else "No"
            
            print(f"\n================ Video: {vid} ================")
            print("Title:", m_title[0] if m_title else "")
            print("Description:", m_desc[0] if m_desc else "")
            print("Tags:", m_tags)
            print("Has Captions:", captions_info)
            
            # Save html for deep dive
            with open(f'yt_{vid}.html', 'w', encoding='utf-8') as f:
                f.write(html)
    except Exception as e:
        print(f"Error {vid}:", e)
