import re

with open('ig_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Title:", re.findall(r'<title>(.*?)</title>', text, re.IGNORECASE))
print("First 2000 chars:")
print(text[:2000])

# Look for embedded JSON or scripts
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print(f"Total scripts: {len(scripts)}")
for i, s in enumerate(scripts):
    if 'alanaatii' in s.lower() or 'biography' in s.lower() or 'graphql' in s.lower():
        print(f"Script {i} matches! Length: {len(s)}")
        # print snippet
        idx = s.lower().find('alanaatii')
        print("Snippet around alanaatii:")
        print(s[max(0, idx-100):min(len(s), idx+200)])
