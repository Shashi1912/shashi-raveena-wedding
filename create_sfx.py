import numpy as np
from scipy.io import wavfile
import subprocess

sr = 44100
v2_dir = r"D:\Shashi\Card\Version_2_Interactive_Wings"

# 1. Door Open Sound (Resonant Temple Bell + Tabla "Dheem-Dha")
dur = 2.2
num_samp = int(sr * dur)
t = np.linspace(0, dur, num_samp, False)

# Temple bell shimmer
bell = (np.sin(2 * np.pi * 1280 * t) * 0.4 +
        np.sin(2 * np.pi * 2560 * t) * 0.3 +
        np.sin(2 * np.pi * 3840 * t) * 0.2) * np.exp(-t / 0.6)

# Tabla Dheem (bass drop)
tabla_t = t[:int(sr * 0.6)]
freq = 70.0 + 50.0 * np.exp(-tabla_t * 15.0)
phase = 2 * np.pi * np.cumsum(freq) / sr
bayan = np.sin(phase) * np.exp(-tabla_t / 0.25) * 0.8
bayan_full = np.zeros(num_samp)
bayan_full[:len(bayan)] = bayan

# Soft wooden door movement
wood_noise = np.random.normal(0, 0.15, int(sr * 0.4)) * np.exp(-np.linspace(0, 2, int(sr * 0.4)))
door_creak = np.zeros(num_samp)
door_creak[:len(wood_noise)] = wood_noise

sfx_open = bell * 0.5 + bayan_full * 0.7 + door_creak * 0.3
sfx_open = sfx_open / np.max(np.abs(sfx_open)) * 0.85
wav_open = f"{v2_dir}\\sfx_door_open.wav"
wavfile.write(wav_open, sr, (sfx_open * 32767).astype(np.int16))
subprocess.run(["ffmpeg", "-y", "-i", wav_open, "-b:a", "192k", f"{v2_dir}\\sfx_door_open.mp3"], check=True)

# 2. Union Grand Crescendo (Triple Wedding Theermanam)
dur_u = 3.2
num_samp_u = int(sr * dur_u)
t_u = np.linspace(0, dur_u, num_samp_u, False)
sfx_u = np.zeros(num_samp_u)

# Hits at 0.0s, 0.4s, 0.8s, 1.2s
hits = [0.0, 0.35, 0.7, 1.1]
for h in hits:
    h_idx = int(h * sr)
    rem = num_samp_u - h_idx
    dur_h = min(int(0.8 * sr), rem)
    th = np.linspace(0, dur_h / sr, dur_h, False)
    
    # Bass
    f_b = 60.0 + 60.0 * np.exp(-th * 16.0)
    sig_b = np.sin(2 * np.pi * np.cumsum(f_b) / sr) * np.exp(-th / 0.28) * 0.8
    # Treble snap
    sig_t = (np.sin(2 * np.pi * 330 * th) + np.sin(2 * np.pi * 920 * th) * 0.4) * np.exp(-th / 0.15) * 0.6
    # Bell
    sig_bell = np.sin(2 * np.pi * 2100 * th) * np.exp(-th / 0.4) * 0.35
    sfx_u[h_idx:h_idx+dur_h] += (sig_b + sig_t + sig_bell) * 0.5

# Grand final resonant bell swell
final_bell = np.sin(2 * np.pi * 880 * t_u) * 0.3 + np.sin(2 * np.pi * 1760 * t_u) * 0.2
sfx_u += final_bell * np.exp(-t_u / 1.2) * 0.4
sfx_u = sfx_u / np.max(np.abs(sfx_u)) * 0.9
wav_u = f"{v2_dir}\\sfx_union.wav"
wavfile.write(wav_u, sr, (sfx_u * 32767).astype(np.int16))
subprocess.run(["ffmpeg", "-y", "-i", wav_u, "-b:a", "192k", f"{v2_dir}\\sfx_union.mp3"], check=True)

print("Sound effects created successfully!")
