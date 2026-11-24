import subprocess
import os

tracks = {
    'bride_short': 'https://www.youtube.com/shorts/vYVJkHl0-MA',
    'main_short': 'https://www.youtube.com/shorts/xr-6OHfrsR8',
    'entry_short': 'https://www.youtube.com/shorts/FS2yGfKu0_M'
}

download_dir = 'D:/Shashi/Card/V5_Audio'
os.makedirs(download_dir, exist_ok=True)

for name, url in tracks.items():
    out_tmpl = os.path.join(download_dir, f'{name}.%(ext)s')
    cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', '--audio-quality', '0', '-o', out_tmpl, url]
    print(f'Downloading {name}: {url}')
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode == 0:
        print(f'Success: {name}')
    else:
        print(f'Error for {name}: {p.stderr[:300]}')

print('\nDownloaded files in V5_Audio:')
for f in os.listdir(download_dir):
    p = os.path.join(download_dir, f)
    print(f'  {f}: {os.path.getsize(p)} bytes')
