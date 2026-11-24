import urllib.request
import re
import json

url = 'https://www.youtube.com/shorts/qPS0yLEwG3U'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        title = re.findall(r'<title>(.*?)</title>', html, re.I)
        print("Title:", title)
        desc = re.findall(r'<meta [^>]*name=[\"\']description[\"\'][^>]*content=[\"\'](.*?)[\"\']', html, re.I)
        print("Description:", desc)
        # find channel url / name
        channel = re.findall(r'\"channelId\":\"([^\"]+)\"|\"ownerChannelName\":\"([^\"]+)\"', html)
        print("Channel info:", [c for c in channel if any(c)])
        
        # let's find more shorts / video links
        shorts = set(re.findall(r'/shorts/([A-Za-z0-9_-]{11})', html))
        print("Other shorts:", list(shorts)[:10])
except Exception as e:
    print("Error:", e)
