import urllib.request
import re

ua = 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)'
req = urllib.request.Request('https://www.instagram.com/alanaatii/', headers={'User-Agent': ua})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

with open('alanaatii_fb.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved alanaatii_fb.html, length:", len(html))

# Look for post links, image links, video links, text
links = set(re.findall(r'https?://[^\s\"\'<>]+', html))
posts = [l for l in links if '/p/' in l or '/reel/' in l]
print("Post/reel links found:", len(posts))
for p in posts[:20]:
    print(p)
