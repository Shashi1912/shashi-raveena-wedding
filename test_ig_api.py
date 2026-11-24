import urllib.request
import json

url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=alanaatii'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-IG-App-ID': '936619743392459',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.instagram.com/alanaatii/',
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Success! Got data keys:", data.keys())
        with open('alanaatii_api.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
except Exception as e:
    print("Error:", e)
