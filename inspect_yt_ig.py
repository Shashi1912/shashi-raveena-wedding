import urllib.request
import re
import json

# Fetch YouTube channel videos / shorts
url = 'https://www.youtube.com/@alanaati/videos'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        yt_html = resp.read().decode('utf-8', errors='ignore')
        with open('yt_videos.html', 'w', encoding='utf-8') as f:
            f.write(yt_html)
        print("Fetched yt videos, length:", len(yt_html))
        # find video titles
        titles = re.findall(r'\"title\":\{\"runs\":\[\{\"text\":\"([^\"]+)\"\}\]', yt_html)
        print("Video titles:", titles[:10])
except Exception as e:
    print("YT Videos error:", e)

url_shorts = 'https://www.youtube.com/@alanaati/shorts'
req = urllib.request.Request(url_shorts, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        yt_shorts = resp.read().decode('utf-8', errors='ignore')
        with open('yt_shorts.html', 'w', encoding='utf-8') as f:
            f.write(yt_shorts)
        titles = re.findall(r'\"headline\":\{\"simpleText\":\"([^\"]+)\"\}|\"title\":\{\"runs\":\[\{\"text\":\"([^\"]+)\"\}\]', yt_shorts)
        print("Shorts titles:", titles[:10])
except Exception as e:
    print("YT Shorts error:", e)

# Also check bio links in alanaatii_fb.html
with open('alanaatii_fb.html', 'r', encoding='utf-8') as f:
    fb_text = f.read()

# bio links
external_urls = re.findall(r'\"external_url\":\"([^\"]+)\"', fb_text)
print("External URLs in Instagram bio:", external_urls)
biography = re.findall(r'\"biography\":\"([^\"]+)\"', fb_text)
print("Biography in IG:", biography)

