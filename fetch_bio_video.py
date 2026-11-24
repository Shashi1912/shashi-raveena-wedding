import urllib.request
import re
import json

url = 'https://www.youtube.com/watch?v=erSGP8xhOXk'
oembed = f'https://www.youtube.com/oembed?url={url}&format=json'

try:
    req = urllib.request.Request(oembed, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("OEmbed Data:", data)
except Exception as e:
    print("OEmbed Error:", e)

# Fetch video page
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        title = re.findall(r'<title>(.*?)</title>', html)
        print("Title:", title)
        desc = re.findall(r'<meta property=\"og:description\" content=\"(.*?)\"', html)
        print("OG Description:", desc)
        with open('bio_video.html', 'w', encoding='utf-8') as f:
            f.write(html)
except Exception as e:
    print("Page error:", e)
