import urllib.request
import re

urls = [
    'https://alanaatii.com',
    'https://www.youtube.com/@alanaatii',
    'https://www.youtube.com/@alanaati',
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            title = re.findall(r'<title>(.*?)</title>', content, re.I)
            print(f"URL: {url} -> Status: {resp.status}, Title: {title}")
            # look for wedding or postcard
            wedding = len(re.findall(r'wedding', content, re.I))
            postcard = len(re.findall(r'postcard', content, re.I))
            vintage = len(re.findall(r'vintage', content, re.I))
            print(f"  wedding: {wedding}, postcard: {postcard}, vintage: {vintage}")
            if 'alanaatii.com' in url:
                with open('alanaatii_com.html', 'w', encoding='utf-8') as f:
                    f.write(content)
    except Exception as e:
        print(f"URL: {url} -> Error: {e}")
