import numpy as np
from scipy.io import wavfile
import os

sr = 44100
bpm = 92
beat_sec = 60.0 / bpm
total_beats = 32  # 4 measures of 8 beats
total_duration = total_beats * beat_sec  # ~20.87 seconds
num_samples = int(sr * total_duration)
t_full = np.linspace(0, total_duration, num_samples, False)

left = np.zeros(num_samples, dtype=np.float32)
right = np.zeros(num_samples, dtype=np.float32)

# ==========================================
# 1. TANPURA / TAMBURA DRONE (Sa - Pa - Sa')
# Root: D3 (146.83 Hz), Pa: A3 (220 Hz), Sa': D4 (293.66 Hz)
# ==========================================
def add_tanpura():
    global left, right
    drone = np.zeros(num_samples, dtype=np.float32)
    # Fundamental and rich harmonics with slight chorus
    harmonics = [(146.83, 0.25), (220.0, 0.20), (293.66, 0.18), (440.0, 0.08), (587.33, 0.05)]
    for freq, amp in harmonics:
        # slow subtle modulation
        mod = 1.0 + 0.08 * np.sin(2 * np.pi * 0.3 * t_full + freq)
        drone += amp * mod * np.sin(2 * np.pi * freq * t_full)
        drone += (amp * 0.5) * np.sin(2 * np.pi * (freq * 1.003) * t_full) # chorus
    
    # Smooth fade in and fade out for loop
    fade_len = int(sr * 1.0)
    fade_in = np.linspace(0, 1, fade_len)
    fade_out = np.linspace(1, 0, fade_len)
    drone[:fade_len] *= fade_in
    drone[-fade_len:] *= fade_out
    
    left += drone * 0.35
    right += drone * 0.35

add_tanpura()

# ==========================================
# 2. THABALA & THAVIL PERCUSSION SYNTHESIS
# ==========================================
# Bayan (Bass - "Ghe", "Dheem"): pitch dive 110Hz -> 65Hz
def hit_bayan(start_time, amp=0.7, decay=0.35):
    global left, right
    idx = int(start_time * sr)
    dur_samp = int(decay * sr)
    if idx >= num_samples: return
    dur_samp = min(dur_samp, num_samples - idx)
    t = np.linspace(0, dur_samp / sr, dur_samp, False)
    
    # Pitch bend downwards
    freq = 65.0 + 55.0 * np.exp(-t * 18.0)
    phase = 2 * np.pi * np.cumsum(freq) / sr
    env = np.exp(-t / (decay * 0.38))
    signal = np.sin(phase) * env * amp
    # Bass warm distortion
    signal = np.tanh(signal * 1.5)
    
    left[idx:idx+dur_samp] += signal * 0.65
    right[idx:idx+dur_samp] += signal * 0.45

# Dayan (Treble - "Ta", "Tin", "Na"): ring at 293.66 Hz + overtone
def hit_dayan(start_time, amp=0.5, decay=0.22, pitch=293.66):
    global left, right
    idx = int(start_time * sr)
    dur_samp = int(decay * sr)
    if idx >= num_samples: return
    dur_samp = min(dur_samp, num_samples - idx)
    t = np.linspace(0, dur_samp / sr, dur_samp, False)
    
    env = np.exp(-t / (decay * 0.28))
    sig = np.sin(2 * np.pi * pitch * t) * 0.7
    sig += np.sin(2 * np.pi * pitch * 2.76 * t) * 0.25  # Inharmonic ring of tabla syahi
    sig += np.sin(2 * np.pi * pitch * 4.1 * t) * 0.12
    # Rim tap transient
    trans = np.random.normal(0, 0.4, dur_samp) * np.exp(-t / 0.015)
    sig = (sig + trans) * env * amp
    
    left[idx:idx+dur_samp] += sig * 0.45
    right[idx:idx+dur_samp] += sig * 0.70

# Thavil / Stick Crack ("Katt"): sharp wedding snap
def hit_thavil(start_time, amp=0.45):
    global left, right
    decay = 0.06
    idx = int(start_time * sr)
    dur_samp = int(decay * sr)
    if idx >= num_samples: return
    dur_samp = min(dur_samp, num_samples - idx)
    t = np.linspace(0, dur_samp / sr, dur_samp, False)
    
    noise = np.random.normal(0, 1.0, dur_samp)
    # Bandpass around 2200 Hz
    snap = noise * np.sin(2 * np.pi * 2200 * t) * np.exp(-t / 0.018) * amp
    left[idx:idx+dur_samp] += snap * 0.5
    right[idx:idx+dur_samp] += snap * 0.5

# Golden Temple Bell / Talam (Cymbals)
def hit_talam(start_time, amp=0.3):
    global left, right
    decay = 0.9
    idx = int(start_time * sr)
    dur_samp = int(decay * sr)
    if idx >= num_samples: return
    dur_samp = min(dur_samp, num_samples - idx)
    t = np.linspace(0, dur_samp / sr, dur_samp, False)
    
    env = np.exp(-t / 0.3)
    # Metallic shimmer
    sig = (np.sin(2 * np.pi * 1860 * t) * 0.4 +
           np.sin(2 * np.pi * 2780 * t) * 0.35 +
           np.sin(2 * np.pi * 4120 * t) * 0.2 +
           np.sin(2 * np.pi * 5490 * t) * 0.15) * env * amp
    left[idx:idx+dur_samp] += sig * 0.6
    right[idx:idx+dur_samp] += sig * 0.6

# Play the Rhythmic Cycle (Kalyana Bajentriyulu Nadai)
# Pattern over 8 beats, repeated 4 times
for cycle in range(4):
    c_start = cycle * 8 * beat_sec
    # Beat 0: Sam (The Grand Auspicious Dha + Bell)
    hit_bayan(c_start + 0 * beat_sec, amp=0.85, decay=0.45)
    hit_dayan(c_start + 0 * beat_sec, amp=0.6, pitch=293.66)
    hit_talam(c_start + 0 * beat_sec, amp=0.35)
    
    # Beat 1: Dheem (Bayan)
    hit_bayan(c_start + 1 * beat_sec, amp=0.6, decay=0.3)
    
    # Beat 1.5: Thavil stick
    hit_thavil(c_start + 1.5 * beat_sec, amp=0.35)
    
    # Beat 2: Ta (Dayan rim)
    hit_dayan(c_start + 2 * beat_sec, amp=0.55, pitch=330.0)
    
    # Beat 3: Dha (Bayan + Dayan)
    hit_bayan(c_start + 3 * beat_sec, amp=0.7, decay=0.35)
    hit_dayan(c_start + 3 * beat_sec, amp=0.5, pitch=293.66)
    
    # Beat 4: Talam + Dheem
    hit_talam(c_start + 4 * beat_sec, amp=0.25)
    hit_bayan(c_start + 4 * beat_sec, amp=0.65, decay=0.35)
    
    # Beat 5: Ge - Na roll
    hit_bayan(c_start + 5 * beat_sec, amp=0.45, decay=0.2)
    hit_dayan(c_start + 5.5 * beat_sec, amp=0.4, pitch=293.66)
    
    # Beat 6: Thavil snap
    hit_thavil(c_start + 6 * beat_sec, amp=0.4)
    hit_dayan(c_start + 6.5 * beat_sec, amp=0.45, pitch=330.0)
    
    # Beat 7: Fast Fill (Tha-ki-ta rolling to next cycle)
    hit_dayan(c_start + 7.0 * beat_sec, amp=0.4, pitch=293.66)
    hit_thavil(c_start + 7.33 * beat_sec, amp=0.35)
    hit_bayan(c_start + 7.66 * beat_sec, amp=0.55, decay=0.2)

# ==========================================
# 3. NADASWARAM / SHEHNAI AUSPICIOUS WEDDING MELODY
# (Raga Mohanam / Gambheera Nattai - classic marriage notes)
# D4=293.66, E4=329.63, F#4=369.99, A4=440.0, B4=493.88, D5=587.33
# ==========================================
def play_nadaswaram_note(t_start, dur, freq1, freq2=None, amp=0.38):
    global left, right
    idx = int(t_start * sr)
    dur_samp = int(dur * sr)
    if idx >= num_samples: return
    dur_samp = min(dur_samp, num_samples - idx)
    t = np.linspace(0, dur_samp / sr, dur_samp, False)
    
    if freq2 is None:
        freq2 = freq1
    
    # Gamaka: smooth frequency glide between notes
    freq_glide = np.linspace(freq1, freq2, dur_samp)
    # Vibrato (5.5 Hz Indian reed vibrato)
    vibrato = 1.0 + 0.018 * np.sin(2 * np.pi * 5.5 * t)
    phase = 2 * np.pi * np.cumsum(freq_glide * vibrato) / sr
    
    # Double reed harmonic profile (sawtooth + odd/even harmonics)
    sig = np.sin(phase) * 0.7
    sig += np.sin(phase * 2) * 0.45
    sig += np.sin(phase * 3) * 0.35
    sig += np.sin(phase * 4) * 0.25
    sig += np.sin(phase * 5) * 0.18
    sig += np.sin(phase * 6) * 0.12
    # Nasal reed saturation
    sig = np.tanh(sig * 1.8)
    
    # Note Envelope: soft attack, sustained body, expressive release
    att = int(min(0.04 * sr, dur_samp * 0.15))
    rel = int(min(0.08 * sr, dur_samp * 0.25))
    env = np.ones(dur_samp, dtype=np.float32)
    if att > 0: env[:att] = np.linspace(0, 1, att)
    if rel > 0: env[-rel:] = np.linspace(1, 0, rel)
    
    sig = sig * env * amp
    # Center-right presence for nadaswaram
    left[idx:idx+dur_samp] += sig * 0.45
    right[idx:idx+dur_samp] += sig * 0.55

# Melodic phrases (Mohanam Auspicious Wedding Theme)
D4 = 293.66
E4 = 329.63
F_s4 = 369.99
A4 = 440.00
B4 = 493.88
D5 = 587.33
E5 = 659.25

# Cycle 1: Opening Auspicious Fanfare
play_nadaswaram_note(0 * beat_sec, 1.8 * beat_sec, D4, A4, amp=0.35)
play_nadaswaram_note(2 * beat_sec, 0.9 * beat_sec, A4, B4)
play_nadaswaram_note(3 * beat_sec, 1.0 * beat_sec, B4, D5)
play_nadaswaram_note(4 * beat_sec, 2.0 * beat_sec, D5, D5, amp=0.42)
play_nadaswaram_note(6 * beat_sec, 0.8 * beat_sec, B4, A4)
play_nadaswaram_note(7 * beat_sec, 0.9 * beat_sec, A4, F_s4)

# Cycle 2: Flowing Wedding Gamakas
c2 = 8 * beat_sec
play_nadaswaram_note(c2 + 0 * beat_sec, 1.4 * beat_sec, F_s4, A4)
play_nadaswaram_note(c2 + 1.5 * beat_sec, 0.5 * beat_sec, A4, B4)
play_nadaswaram_note(c2 + 2 * beat_sec, 1.8 * beat_sec, D5, E5, amp=0.44)
play_nadaswaram_note(c2 + 4 * beat_sec, 1.2 * beat_sec, E5, D5)
play_nadaswaram_note(c2 + 5.2 * beat_sec, 0.8 * beat_sec, D5, B4)
play_nadaswaram_note(c2 + 6 * beat_sec, 1.8 * beat_sec, A4, F_s4)

# Cycle 3: Celebratory High Octave Flourish
c3 = 16 * beat_sec
play_nadaswaram_note(c3 + 0 * beat_sec, 1.0 * beat_sec, D5, D5, amp=0.45)
play_nadaswaram_note(c3 + 1 * beat_sec, 1.0 * beat_sec, E5, E5, amp=0.45)
play_nadaswaram_note(c3 + 2 * beat_sec, 1.8 * beat_sec, D5, B4, amp=0.40)
play_nadaswaram_note(c3 + 4 * beat_sec, 1.5 * beat_sec, A4, B4)
play_nadaswaram_note(c3 + 5.5 * beat_sec, 0.5 * beat_sec, B4, D5)
play_nadaswaram_note(c3 + 6 * beat_sec, 1.8 * beat_sec, D5, D5, amp=0.42)

# Cycle 4: Kalyana Theermanam (Auspicious Wedding Cadence)
c4 = 24 * beat_sec
play_nadaswaram_note(c4 + 0 * beat_sec, 0.8 * beat_sec, D5, A4)
play_nadaswaram_note(c4 + 1 * beat_sec, 0.8 * beat_sec, A4, F_s4)
play_nadaswaram_note(c4 + 2 * beat_sec, 0.8 * beat_sec, F_s4, E4)
play_nadaswaram_note(c4 + 3 * beat_sec, 1.2 * beat_sec, E4, D4)
# Triple Cadence (Dha-Ti-Ghin-Thom)
play_nadaswaram_note(c4 + 4.5 * beat_sec, 0.6 * beat_sec, F_s4, A4, amp=0.45)
play_nadaswaram_note(c4 + 5.5 * beat_sec, 0.6 * beat_sec, F_s4, A4, amp=0.45)
play_nadaswaram_note(c4 + 6.5 * beat_sec, 1.4 * beat_sec, A4, D4, amp=0.48)

# Normalize and master
stereo = np.column_stack((left, right))
peak = np.max(np.abs(stereo))
if peak > 0:
    stereo = stereo / peak * 0.92

out_path = r"D:\Shashi\Card\Version_2_Interactive_Wings\wedding_bajentriyulu.wav"
wavfile.write(out_path, sr, (stereo * 32767).astype(np.int16))
print(f"Generated wedding_bajentriyulu.wav: {len(stereo)/sr:.2f} seconds")
