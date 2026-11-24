import subprocess
import os

audio_dir = "D:/Shashi/Card/V5_Audio"

# 8D Filter definition:
# 1. apulsator: smoothly pans audio across left and right channels in a 360-degree orbit (hz=0.125 = ~8 sec orbit)
# 2. extrastereo: expands the stereo field width for spatial depth
# 3. aecho: acoustic hall reverberation for 3D space illusion
# 4. volume normalization to ensure clear, studio-grade listening
filter_chain = "apulsator=mode=sine:hz=0.12:amount=0.82,extrastereo=m=1.2,aecho=0.8:0.85:30:0.25,loudnorm=I=-14:TP=-1.0:LRA=11"

tracks = {
    "entry_8d.mp3": "entry_short.mp3",
    "bride_8d.mp3": "bride_short.mp3",
    "main_8d.mp3": "main_short.mp3"
}

for out_name, in_name in tracks.items():
    in_path = os.path.join(audio_dir, in_name)
    out_path = os.path.join(audio_dir, out_name)

    # For main_short, since it's 6 seconds, let's create a seamless 18-second 3x loop so the 8D panning can complete a full 360-degree rotation!
    if in_name == "main_short.mp3":
        cmd = [
            "ffmpeg", "-stream_loop", "2", "-i", in_path,
            "-af", filter_chain,
            "-b:a", "192k",
            out_path, "-y"
        ]
    else:
        cmd = [
            "ffmpeg", "-i", in_path,
            "-af", filter_chain,
            "-b:a", "192k",
            out_path, "-y"
        ]

    print(f"Processing {out_name}...")
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode == 0:
        size = os.path.getsize(out_path)
        print(f"  Success: {out_name} ({size} bytes)")
    else:
        print(f"  Error on {out_name}: {p.stderr[-300:]}")

print("\n8D Audio conversion completed!")
