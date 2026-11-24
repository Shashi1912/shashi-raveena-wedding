import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
url = 'https://www.instagram.com/alanaatii/'
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        with open('ig_page.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Wrote ig_page.html, length:", len(content))
except Exception as e:
    print("Error:", e)
