import os
import shutil
import re

v5_dir = "D:/Shashi/Card/Version_5_Spatial_8D"
os.makedirs(v5_dir, exist_ok=True)

# 1. Copy base visual assets from Version_3_Door_Touch
v3_dir = "D:/Shashi/Card/Version_3_Door_Touch"
base_assets = [
    "GreatVibes-Regular.ttf",
    "bride_doodle.png",
    "groom_doodle.png",
    "feet_artwork_feathered.png",
    "ganesha_clean.png",
    "sikku_kolam_clean.png",
    "venue_qr.svg",
    "venue_qr.png",
    "sfx_door_open.mp3",
    "sfx_union.mp3",
    "preview_v2_closed.png"
]

for a in base_assets:
    src = os.path.join(v3_dir, a)
    dst = os.path.join(v5_dir, a)
    if os.path.exists(src):
        shutil.copyfile(src, dst)

# 2. Copy 8D Audio tracks from V5_Audio
v5_audio_dir = "D:/Shashi/Card/V5_Audio"
audio_tracks = [
    "entry_8d.mp3",
    "bride_8d.mp3",
    "main_8d.mp3",
    "groom_8d.mp3"
]

for a in audio_tracks:
    src = os.path.join(v5_audio_dir, a)
    dst = os.path.join(v5_dir, a)
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print(f"Copied {a}: {os.path.getsize(dst)} bytes")
    else:
        print(f"Missing audio: {a}")

# 3. Read V3 index.html as base
with open(os.path.join(v3_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Update title & tags
html = html.replace(
    "<title>Shashi & Raveena — Royal Telugu Wedding Invitation</title>",
    "<title>Shashi & Raveena — Version 5: 3D/8D Spatial Audio Wedding Invitation</title>"
)

# Add 8D Headphone Badge to UI
headphone_badge_css = """
    /* 8D AUDIO HEADPHONE RECOMMENDED CHIP */
    .headphone-cue-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(20, 8, 4, 0.82);
      border: 1px solid rgba(212, 175, 55, 0.5);
      border-radius: 20px;
      padding: 5px 14px;
      color: #ffd700;
      font-family: 'Montserrat', sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
      animation: cuePulse 2.5s infinite ease-in-out;
    }
    @keyframes cuePulse {
      0%, 100% { opacity: 0.85; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.03); box-shadow: 0 0 15px rgba(212, 175, 55, 0.5); }
    }
"""

html = html.replace("  </style>", headphone_badge_css + "\n  </style>")

# Insert Headphone Chip above the mandapam stage
chip_html = """  <!-- 8D AUDIO EXPERIENCE RECOMMENDATION -->
  <div class="headphone-cue-badge">
    🎧 8D Spatial Audio • Headphones Recommended for 360° Sound
  </div>
  
  <!-- THE MANDAPAM 3D GATEFOLD STAGE -->"""

html = html.replace("<!-- THE MANDAPAM 3D GATEFOLD STAGE -->", chip_html)

# Update Floating Music Button Label to reflect 8D
html = html.replace('<span id="musicBtnLabel">బాజంత్రీలు: ON</span>', '<span id="musicBtnLabel">8D బాజంత్రీలు: ON</span>')

# Update Audio Engine to use Entry, Groom, Bride, and Main 8D tracks
old_audio_engine = re.search(r'// ==========================================.*?// Auto-trigger music on first user click', html, re.DOTALL)

new_audio_engine = """// ==========================================
    // VERSION 5: 3D / 8D SPATIAL AUDIO ENGINE
    // - Entry: Auspicious 8D Shenhai & Nadaswaram on open
    // - Groom's Wing: Energetic 8D Nadaswaram & Thavil
    // - Bride's Wing: 8D Kannathil Muthamittal Violin Melody
    // - Main Union: Grand 8D Celebratory Wedding Music
    // ==========================================
    let isMusicEnabled = true;
    let currentAudio = null;

    const audioEntry = new Audio('entry_8d.mp3');
    audioEntry.loop = true;
    audioEntry.volume = 0.65;

    const audioGroom = new Audio('groom_8d.mp3');
    audioGroom.volume = 0.68;

    const audioBride = new Audio('bride_8d.mp3');
    audioBride.volume = 0.68;

    const audioMain = new Audio('main_8d.mp3');
    audioMain.loop = true;
    audioMain.volume = 0.72;

    function stopAllAudio(fade = false) {
      const audios = [audioEntry, audioGroom, audioBride, audioMain];
      audios.forEach(a => {
        if (!a.paused) {
          if (fade) {
            let vol = a.volume;
            const timer = setInterval(() => {
              vol -= 0.15;
              if (vol <= 0.05) {
                clearInterval(timer);
                a.pause();
                a.currentTime = 0;
                a.volume = 0.65;
              } else {
                a.volume = vol;
              }
            }, 50);
          } else {
            a.pause();
            a.currentTime = 0;
          }
        }
      });
      currentAudio = null;
    }

    function playSectionSound(audioObj, labelText, iconText = '🎧') {
      if (!isMusicEnabled) return;
      stopAllAudio(false);
      currentAudio = audioObj;
      audioObj.currentTime = 0;
      audioObj.volume = 0.68;
      audioObj.play().then(() => {
        btnMusic.classList.remove('muted');
        btnMusic.classList.add('playing');
        musicBtnLabel.textContent = labelText;
        if (musicIcon) musicIcon.textContent = iconText;
      }).catch(e => {
        console.log('Audio autoplay waiting for user interaction:', e);
      });
    }

    function toggleWeddingMusic() {
      if (isMusicEnabled) {
        isMusicEnabled = false;
        stopAllAudio(false);
        btnMusic.classList.add('muted');
        btnMusic.classList.remove('playing');
        musicBtnLabel.textContent = '8D Audio: OFF';
      } else {
        isMusicEnabled = true;
        if (stage.classList.contains('opened-groom')) {
          playSectionSound(audioGroom, '🤵 వరుని బాజంత్రీలు (8D)', '🤵🎺');
        } else if (stage.classList.contains('opened-bride')) {
          playSectionSound(audioBride, '👰 వధువు వైభోగం (8D)', '👰🎻');
        } else if (stage.classList.contains('opened-both')) {
          playSectionSound(audioMain, '👑 కల్యాణ మహోత్సవం (8D)', '👑🎉');
        } else {
          playSectionSound(audioEntry, '✨ కళ్యాణ ప్రవేశం (8D)', '🎧🎺');
        }
      }
    }

    // Single interaction flag
    let hasInteracted = false;

    function handleFirstUserTap() {
      if (!hasInteracted) {
        hasInteracted = true;
        const hint = document.getElementById('doorTapHint');
        if (hint) hint.style.display = 'none';
      }
    }

    function startEntryAudio() {
      if (!hasInteracted && isMusicEnabled) {
        handleFirstUserTap();
        playSectionSound(audioEntry, '✨ కళ్యాణ ప్రవేశం (8D)', '🎧🎺');
      }
    }

    // Attempt autoplay immediately on link load
    window.addEventListener('DOMContentLoaded', () => {
      audioEntry.play().then(() => {
        handleFirstUserTap();
        btnMusic.classList.remove('muted');
        btnMusic.classList.add('playing');
        musicBtnLabel.textContent = '✨ కళ్యాణ ప్రవేశం (8D)';
      }).catch(() => {
        // If browser blocks autoplay until interaction, bind to first tap
        document.addEventListener('pointerdown', startEntryAudio, { once: true });
      });
    });"""

old_audio_engine = re.search(r'// ==========================================.*?document\.addEventListener\(\'pointerdown\', handleFirstUserTap, \{ once: true \}\);', html, re.DOTALL)

if old_audio_engine:
    html = html.replace(old_audio_engine.group(0), new_audio_engine)
    print("Replaced audio engine with 8D Spatial Audio Suite.")
else:
    print("WARNING: old_audio_engine not matched!")

# Update openGroomWing, openBrideWing, openBothDoors, closeAllDoors
old_groom_fn = """    // Open ONLY Groom's Side -> Plays trimmed energetic Groom Nadaswaram & Thavil
    function openGroomWing() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-groom';
      resetActiveButtons();
      // no button active class
      playSectionSound(audioGroom, 'వరుని బాజంత్రీలు', '🤵🎺');
    }"""

new_groom_fn = """    // Open ONLY Groom's Side -> Plays 8D Groom Nadaswaram & Thavil
    function openGroomWing() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-groom';
      resetActiveButtons();
      playSectionSound(audioGroom, '🤵 వరుని బాజంత్రీలు (8D)', '🤵🎺');
    }"""

html = html.replace(old_groom_fn, new_groom_fn)

old_bride_fn = """    // Open ONLY Bride's Side -> Plays trimmed soulful Seetha Kalyanam
    function openBrideWing() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-bride';
      resetActiveButtons();
      // no button active class
      playSectionSound(audioBride, 'సీతా కల్యాణం', '👰🪷');
    }"""

new_bride_fn = """    // Open ONLY Bride's Side -> Plays 8D Kannathil Muthamittal Violin
    function openBrideWing() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-bride';
      resetActiveButtons();
      playSectionSound(audioBride, '👰 వధువు వైభోగం (Violin 8D)', '👰🎻');
    }"""

html = html.replace(old_bride_fn, new_bride_fn)

old_union_fn = """    // Open BOTH Doors (The Grand Union) -> Plays FULL, authentic Ketti Melam (గట్టిమేళం)!
    function openBothDoors() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-both';
      resetActiveButtons();
      playSectionSound(audioUnion, 'గట్టిమేళం (Full Mela)', '👑🥁');
      addDirectlyToCalendar();
    }"""

new_union_fn = """    // Open BOTH Doors (The Grand Union) -> Plays 8D Main Celebratory Wedding Song!
    function openBothDoors() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-both';
      resetActiveButtons();
      playSectionSound(audioMain, '👑 కల్యాణ మహోత్సవం (8D)', '👑🎉');
      addDirectlyToCalendar();
    }"""

html = html.replace(old_union_fn, new_union_fn)

old_close_fn = """    // Close All Doors -> Smoothly fade out the sound
    function closeAllDoors() {
      stage.className = 'mandapam-stage';
      resetActiveButtons();
      // no button active class
      stopAllAudio(true);
      btnMusic.classList.add('muted');
      btnMusic.classList.remove('playing');
      musicBtnLabel.textContent = 'బాజంత్రీలు: Paused';
    }"""

new_close_fn = """    // Close All Doors -> Resumes Entry 8D Song
    function closeAllDoors() {
      stage.className = 'mandapam-stage';
      resetActiveButtons();
      if (isMusicEnabled) {
        playSectionSound(audioEntry, '✨ కళ్యాణ ప్రవేశం (8D)', '🎧🎺');
      } else {
        stopAllAudio(true);
        btnMusic.classList.add('muted');
        btnMusic.classList.remove('playing');
        musicBtnLabel.textContent = '8D Audio: Paused';
      }
    }"""

html = html.replace(old_close_fn, new_close_fn)

# Write V5 files
v5_index = os.path.join(v5_dir, "index.html")
v5_named = os.path.join(v5_dir, "Shashi_Raveena_Wedding_Invitation_v5.html")

with open(v5_index, "w", encoding="utf-8") as f:
    f.write(html)
with open(v5_named, "w", encoding="utf-8") as f:
    f.write(html)

print("Version 5 HTML generated successfully in Version_5_Spatial_8D!")
