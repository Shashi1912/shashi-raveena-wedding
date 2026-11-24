import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}
for u in ['https://www.instagram.com/instagram/', 'https://www.instagram.com/alanaatii/', 'https://www.instagram.com/alanaati/']:
    req = urllib.request.Request(u, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            m = re.findall(r'\"pageID\":\"([^\"]+)\"', text)
            print(u, "-> Status:", resp.status, "pageID:", m)
    except Exception as e:
        print(u, "-> Error:", e)
