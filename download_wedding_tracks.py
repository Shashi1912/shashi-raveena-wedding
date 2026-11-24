import yt_dlp
import os

urls = {
    "track1": "https://www.youtube.com/watch?v=iJ7p4BnyUmQ",
    "track2": "https://www.youtube.com/watch?v=5g9IRefyASo"
}

out_dir = r"D:\Shashi\Card\Version_2_Interactive_Wings"

for key, url in urls.items():
    print(f"Fetching info for {key}: {url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(out_dir, f'%(title)s__{key}.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"Downloaded: {info.get('title')}")
