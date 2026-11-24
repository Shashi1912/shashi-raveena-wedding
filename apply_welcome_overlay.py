import re
import os

v5_path = "D:/Shashi/Card/Version_5_Spatial_8D/index.html"
with open(v5_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Overlay CSS
overlay_css = """
    /* AUSPICIOUS ROYAL WELCOME OVERLAY */
    .welcome-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      background: radial-gradient(circle at 50% 30%, #2a1106 0%, #0a0301 100%);
      z-index: 99999;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      transition: opacity 0.6s ease, visibility 0.6s ease;
      padding: 20px;
    }
    .welcome-overlay.hidden {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }
    .welcome-modal {
      text-align: center;
      background: rgba(35, 14, 7, 0.9);
      border: 2px solid #d4af37;
      border-radius: 20px;
      padding: 40px 30px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba(212, 175, 55, 0.35);
      max-width: 480px;
      width: 90%;
      animation: modalGlow 3s infinite ease-in-out;
    }
    @keyframes modalGlow {
      0%, 100% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95), 0 0 30px rgba(212, 175, 55, 0.3); }
      50% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95), 0 0 55px rgba(255, 215, 0, 0.6); }
    }
    .welcome-sanskrit {
      font-family: 'Cinzel', serif;
      font-size: 13px;
      letter-spacing: 2px;
      color: #ffd700;
      margin-bottom: 12px;
    }
    .welcome-couple {
      font-family: 'Great Vibes Local', 'Great Vibes', cursive;
      font-size: 46px;
      color: #fce8a6;
      line-height: 1.1;
      text-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
      margin-bottom: 8px;
    }
    .welcome-sub {
      font-family: 'Cinzel', serif;
      font-size: 11px;
      letter-spacing: 1.5px;
      color: #d4af37;
      text-transform: uppercase;
      margin-bottom: 24px;
    }
    .welcome-btn {
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
      background: linear-gradient(135deg, #8b2518, #5a140b);
      border: 1.5px solid #ffd700;
      padding: 12px 28px;
      border-radius: 30px;
      color: #ffffff;
      font-family: 'Cinzel', serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
      animation: pulseBtn 2s infinite ease-in-out;
    }
    @keyframes pulseBtn {
      0%, 100% { transform: scale(1); box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5); }
      50% { transform: scale(1.04); box-shadow: 0 0 25px rgba(255, 215, 0, 0.7); }
    }
    .welcome-headphone-note {
      font-family: 'Montserrat', sans-serif;
      font-size: 9.5px;
      letter-spacing: 0.8px;
      color: #ffd700;
      font-weight: 500;
    }
"""

html = html.replace("  </style>", overlay_css + "\n  </style>")

# 2. Add Welcome Overlay HTML at the top of <body>
overlay_html = """  <!-- AUSPICIOUS ROYAL WELCOME OVERLAY (Unlocks 8D Audio on every phone/browser) -->
  <div class="welcome-overlay" id="welcomeOverlay" onclick="dismissWelcomeAndPlay()">
    <div class="welcome-modal">
      <div class="welcome-sanskrit">॥ శ్రీ వేంకటేశ్వర ప్రసన్న ॥</div>
      <div class="welcome-couple">Shashi &amp; Raveena</div>
      <div class="welcome-sub">Wedding Invitation • 13-Dec-2026</div>
      <div class="welcome-btn">
        <span>✨ Tap to Open Invitation ✨</span>
        <span class="welcome-headphone-note">🎧 8D Spatial Audio Experience</span>
      </div>
    </div>
  </div>
"""

html = html.replace("<body>\n", "<body>\n\n" + overlay_html + "\n")

# 3. Update Audio Autoplay & Overlay dismiss JS
old_js = """    function startEntryAudio() {
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

new_js = """    function dismissWelcomeAndPlay() {
      const overlay = document.getElementById('welcomeOverlay');
      if (overlay) overlay.classList.add('hidden');
      handleFirstUserTap();
      playSectionSound(audioEntry, '✨ కళ్యాణ ప్రవేశం (8D)', '🎧🎺');
    }

    function startEntryAudio() {
      if (!hasInteracted && isMusicEnabled) {
        dismissWelcomeAndPlay();
      }
    }

    // Attempt autoplay immediately on link load
    window.addEventListener('DOMContentLoaded', () => {
      audioEntry.play().then(() => {
        // Autoplay allowed by browser!
        hasInteracted = true;
        const overlay = document.getElementById('welcomeOverlay');
        if (overlay) overlay.classList.add('hidden');
        btnMusic.classList.remove('muted');
        btnMusic.classList.add('playing');
        musicBtnLabel.textContent = '✨ కళ్యాణ ప్రవేశం (8D)';
      }).catch(() => {
        // Autoplay blocked by browser policy -> Welcome overlay is active for natural 1-tap open!
        console.log('Autoplay waiting for natural tap to open');
      });
    });

    // On desktop: mousemove or wheel or keydown triggers entry audio and dissolves overlay
    ['mousemove', 'wheel', 'keydown'].forEach(evt => {
      window.addEventListener(evt, () => {
        if (!hasInteracted) {
          dismissWelcomeAndPlay();
        }
      }, { once: true });
    });"""

html = html.replace(old_js, new_js)

# Write to Version_5_Spatial_8D/index.html and Shashi_Raveena_Wedding_Invitation_v5.html
with open(v5_path, "w", encoding="utf-8") as f:
    f.write(html)

named_v5 = "D:/Shashi/Card/Version_5_Spatial_8D/Shashi_Raveena_Wedding_Invitation_v5.html"
with open(named_v5, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied Welcome Overlay & Immediate Audio Unlock to Version 5!")
