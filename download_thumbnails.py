import urllib.request
import os

targets = ['qPS0yLEwG3U', 'DMmbbweYGKY', 'aosKebQY4uw', 'w49tXp-S2zk', 'm-Br8HPka0o', 'FG4edQ5P4UM', '9O8Vc2o7Rf4', 'qA4dyG3vCpM']

os.makedirs('thumbnails', exist_ok=True)

for vid in targets:
    for quality in ['maxresdefault.jpg', 'hqdefault.jpg']:
        url = f'https://i.ytimg.com/vi/{vid}/{quality}'
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                data = resp.read()
                # YouTube returns a 1092-byte placeholder if maxres doesn't exist
                if len(data) > 2000:
                    filename = f'thumbnails/{vid}.jpg'
                    with open(filename, 'wb') as f:
                        f.write(data)
                    print(f"Downloaded {filename} ({quality}, {len(data)} bytes)")
                    break
        except Exception as e:
            pass
