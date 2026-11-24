import re
import os

with open("D:/Shashi/Card/Version_2_Interactive_Wings/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Title and Add OpenGraph Metadata
old_title_meta = """  <title>Shashi & Raveena — Version 2: Multi-Wing Mandapam Gatefold Invitation</title>"""
new_title_meta = """  <title>Shashi & Raveena — Royal Telugu Wedding Invitation</title>
  <meta name="description" content="With the divine blessings of Sri Venkateswara Swamy, Sri Angajala & Sri Kotipalli families cordially invite you to celebrate the wedding of Shashi & Raveena on 13th December 2026 at Thanmaya Farmstay Resort.">
  <meta property="og:title" content="Shashi & Raveena — Royal Telugu Wedding Invitation">
  <meta property="og:description" content="13th Dec 2026 • Thanmaya Farmstay Resort • Tap to experience the interactive Mandapam wedding card.">
  <meta property="og:image" content="preview_v2_closed.png">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">"""

html = html.replace(old_title_meta, new_title_meta)

# 1B. Center Page in Viewport
old_body_css = """    body {
      background: radial-gradient(circle at 50% 20%, #1c0e04 0%, #0a0401 100%);
      color: #3b2010;
      font-family: 'Cormorant Garamond', serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 25px 20px 80px;
      gap: 22px;
      perspective: 1400px;
      -webkit-font-smoothing: antialiased;
    }"""

new_body_css = """    body {
      background: radial-gradient(circle at 50% 20%, #1c0e04 0%, #0a0401 100%);
      color: #3b2010;
      font-family: 'Cormorant Garamond', serif;
      min-height: 100vh;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px 15px;
      margin: 0;
      perspective: 1400px;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }"""

html = html.replace(old_body_css, new_body_css)

# 2. Add V3 CSS for Floating Music Badge, Close Button, Tap Hint, and Calendar Button
v3_styles = """
    /* ========================================================
       VERSION 3: PURE DOOR-TOUCH MINIMALIST LUXURY STYLES
       ======================================================== */
    
    /* FLOATING MUSIC BADGE (TOP-RIGHT) */
    .music-floating-badge {
      position: fixed;
      top: 18px;
      right: 20px;
      z-index: 9999;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: rgba(35, 14, 7, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      padding: 7px 15px;
      border-radius: 30px;
      border: 1.5px solid rgba(212, 175, 55, 0.7);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6), 0 0 16px rgba(212, 175, 55, 0.25);
      color: #ffd700;
      font-family: 'Cinzel', serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      cursor: pointer;
      transition: all 0.25s ease;
      user-select: none;
    }
    .music-floating-badge:hover {
      background: rgba(50, 20, 10, 0.95);
      border-color: #ffd700;
      box-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
      transform: translateY(-1px);
    }
    .music-floating-badge.muted {
      opacity: 0.6;
      border-color: rgba(212, 175, 55, 0.35);
      color: #c9b07a;
    }

    /* FLOATING CLOSE INVITATION BUTTON (APPEARS WHEN OPEN) */
    .close-floating-btn {
      position: fixed;
      top: 18px;
      left: 20px;
      z-index: 9999;
      display: none;
      align-items: center;
      gap: 6px;
      background: rgba(25, 9, 4, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      padding: 7px 15px;
      border-radius: 30px;
      border: 1.2px solid rgba(212, 175, 55, 0.55);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
      color: #f7e6c4;
      font-family: 'Cinzel', serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      cursor: pointer;
      transition: all 0.25s ease;
      user-select: none;
    }
    .close-floating-btn:hover {
      background: rgba(139, 37, 24, 0.95);
      border-color: #ffd700;
      color: #ffffff;
      transform: translateY(-1px);
    }
    .mandapam-stage.opened-groom ~ .close-floating-btn,
    .mandapam-stage.opened-bride ~ .close-floating-btn,
    .mandapam-stage.opened-both ~ .close-floating-btn {
      display: inline-flex;
    }

    /* TAP TO OPEN PULSING HINT */
    .door-tap-hint {
      position: absolute;
      bottom: -32px;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;
      font-family: 'Montserrat', sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      color: #ffd700;
      background: rgba(18, 6, 2, 0.88);
      border: 1px solid rgba(212, 175, 55, 0.5);
      padding: 4px 12px;
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
      animation: pulseHintAnim 2s infinite ease-in-out;
      pointer-events: none;
      transition: opacity 0.4s ease;
      z-index: 50;
    }
    @keyframes pulseHintAnim {
      0%, 100% { opacity: 0.85; transform: translateX(-50%) scale(1); }
      50% { opacity: 1; transform: translateX(-50%) scale(1.05); box-shadow: 0 0 16px rgba(212, 175, 55, 0.6); }
    }
    .mandapam-stage.opened-groom .door-tap-hint,
    .mandapam-stage.opened-bride .door-tap-hint,
    .mandapam-stage.opened-both .door-tap-hint {
      display: none !important;
    }

    /* CALENDAR TOAST NOTIFICATION */
    .calendar-toast {
      position: fixed;
      top: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(-70px);
      z-index: 10000;
      background: rgba(35, 14, 7, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid #d4af37;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7), 0 0 20px rgba(212, 175, 55, 0.35);
      color: #ffd700;
      font-family: 'Cinzel', serif;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.8px;
      padding: 10px 24px;
      border-radius: 30px;
      transition: transform 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.4s ease;
      opacity: 0;
      pointer-events: none;
      white-space: nowrap;
    }
    .calendar-toast.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    /* CALENDAR DATE BLOCK CLICKABLE */
    .calendar-date-card {
      cursor: pointer;
      transition: all 0.25s ease;
      padding: 4px 8px;
      border-radius: 8px;
    }
    .calendar-date-card:hover {
      background: rgba(212, 175, 55, 0.15);
      transform: translateY(-1px);
    }

    /* VIEWPORT CENTERING AND RESPONSIVE SCALING */
    .mandapam-stage {
      margin: auto !important;
      transition: transform 0.35s ease;
      transform-origin: center center;
    }
    @media (max-width: 1040px) {
      .mandapam-stage { transform: scale(0.88); }
    }
    @media (max-width: 860px) {
      .mandapam-stage { transform: scale(0.74); }
    }
    @media (max-width: 680px) {
      .mandapam-stage { transform: scale(0.58); }
    }
    @media (max-width: 480px) {
      .mandapam-stage { transform: scale(0.44); }
    }
"""

html = html.replace("  </style>", v3_styles + "\n  </style>")

# 3. Replace the Nav Bar & Title Tag in body with V3 floating badges and calendar toast
old_nav_and_tag = re.search(r'<!-- PRO FLOATING CONTROLLER -->.*?<!-- THE MANDAPAM 3D GATEFOLD STAGE -->', html, re.DOTALL)
if old_nav_and_tag:
    v3_nav_replacement = """<!-- V3 FLOATING MINIMALIST CONTROLS -->
  <button class="music-floating-badge playing" id="btnMusic" onclick="toggleWeddingMusic()" title="Click to mute or play wedding music">
    <span id="musicIcon">🎺🥁</span>
    <span id="musicBtnLabel">బాజంత్రీలు: ON</span>
    <span class="music-waves" id="musicWaves">
      <span class="m-bar"></span>
      <span class="m-bar"></span>
      <span class="m-bar"></span>
      <span class="m-bar"></span>
    </span>
  </button>

  <button class="close-floating-btn" id="btnCloseFloating" onclick="closeAllDoors()" title="Click to close doors">
    ✕ Close Invitation
  </button>

  <div class="calendar-toast" id="calendarToast">
    📅 Wedding Added to Calendar (13-Dec-2026 • 09:50 AM)
  </div>

  <!-- THE MANDAPAM 3D GATEFOLD STAGE -->"""
    html = html.replace(old_nav_and_tag.group(0), v3_nav_replacement)
    print("Replaced old nav bar and title tag with V3 floating badges and toast.")

# 4. Add the Door Tap Hint under center wax seal
old_seal = """    <!-- Center Auspicious Union Seal (Click to Open Both) -->
    <div class="center-union-seal" onclick="openBothDoors()" title="Click to open full wedding invitation">
      <div class="seal-inner">
        <div class="seal-sanskrit">॥ श्रीः ॥</div>
        <div class="seal-text">SHASHI<br>&amp;<br>RAVEENA</div>
        <div class="seal-sub">13-DEC-2026</div>
      </div>
    </div>"""

new_seal = """    <!-- Center Auspicious Union Seal (Click to Open Both) -->
    <div class="center-union-seal" onclick="openBothDoors()" title="Click to open full wedding invitation">
      <div class="seal-inner">
        <div class="seal-sanskrit">॥ श्रीः ॥</div>
        <div class="seal-text">SHASHI<br>&amp;<br>RAVEENA</div>
        <div class="seal-sub">13-DEC-2026</div>
      </div>
      <div class="door-tap-hint" id="doorTapHint">✨ Tap doors or seal to open ✨</div>
    </div>"""

html = html.replace(old_seal, new_seal)
print("Added door-tap-hint under center wax seal.")

# 5. Make Auspicious Date block clickable for calendar without adding a specific button
old_date_card = """            <div>
              <span class="event-lbl">Auspicious Date</span>
              <div class="event-val">Sun, 13 Dec 2026</div>
              <div class="event-sub">In presence of family &amp; elders</div>
            </div>"""

new_date_card = """            <div class="calendar-date-card" onclick="addDirectlyToCalendar(true)" title="Tap to sync/view in Calendar">
              <span class="event-lbl">Auspicious Date</span>
              <div class="event-val">Sun, 13 Dec 2026</div>
              <div class="event-sub">In presence of family &amp; elders • Tap to sync</div>
            </div>"""

if old_date_card in html:
    html = html.replace(old_date_card, new_date_card)
    print("Made Auspicious Date block directly synced with calendar!")
else:
    print("WARNING: old_date_card not found in html")

# 6B. Direct calendar sync on entering the main window (openBothDoors)
old_open_both = """    // Open BOTH Doors (The Grand Union) -> Plays FULL, authentic Ketti Melam (గట్టిమేళం)!
    function openBothDoors() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-both';
      resetActiveButtons();
      btnUnion.classList.add('active');
      playSectionSound(audioUnion, 'గట్టిమేళం (Full Mela)', '👑🥁');
    }"""

new_open_both = """    const CALENDAR_URL = 'https://calendar.google.com/calendar/render?action=TEMPLATE&text=Shashi+%26+Raveena+Wedding&dates=20261213T042000Z/20261213T093000Z&details=Auspicious+Sumuhurtham+at+09:50+AM.+Thanmaya+Farmstay+Resort,+Warangal+Highway.&location=Thanmaya+Farmstay+Resort,+Rajavaram,+Telangana+506144';
    let hasAddedToCalendar = false;

    function addDirectlyToCalendar(force = false) {
      if (!hasAddedToCalendar || force) {
        hasAddedToCalendar = true;
        try {
          window.open(CALENDAR_URL, '_blank');
        } catch (e) {
          console.log('Calendar auto-sync waiting for user interaction');
        }
        const toast = document.getElementById('calendarToast');
        if (toast) {
          toast.classList.add('show');
          setTimeout(() => toast.classList.remove('show'), 5000);
        }
      }
    }

    // Open BOTH Doors (The Grand Union) -> Plays FULL, authentic Ketti Melam (గట్టిమేళం)!
    function openBothDoors() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-both';
      resetActiveButtons();
      playSectionSound(audioUnion, 'గట్టిమేళం (Full Mela)', '👑🥁');
      addDirectlyToCalendar();
    }"""

if old_open_both in html:
    html = html.replace(old_open_both, new_open_both)
    print("Injected direct calendar sync in openBothDoors!")
else:
    print("WARNING: old_open_both not found in html!")

# 6. Adjust JavaScript to avoid referencing missing nav buttons
html = html.replace("const btnGroom = document.getElementById('btnGroom');", "// removed btnGroom")
html = html.replace("const btnBride = document.getElementById('btnBride');", "// removed btnBride")
html = html.replace("const btnUnion = document.getElementById('btnUnion');", "// removed btnUnion")
html = html.replace("const btnClose = document.getElementById('btnClose');", "// removed btnClose")
html = html.replace("btnGroom.classList.add('active');", "// no button active class")
html = html.replace("btnBride.classList.add('active');", "// no button active class")
html = html.replace("btnUnion.classList.add('active');", "// no button active class")
html = html.replace("btnClose.classList.add('active');", "// no button active class")

# In resetActiveButtons:
html = html.replace("""    function resetActiveButtons() {
      btnGroom.classList.remove('active');
      btnBride.classList.remove('active');
      btnUnion.classList.remove('active');
      btnClose.classList.remove('active');
    }""", """    function resetActiveButtons() {
      // V3 has direct door-touch interaction
    }""")

# In handleFirstUserTap:
html = html.replace("""    function handleFirstUserTap() {
      if (!hasInteracted) {
        hasInteracted = true;
      }
    }""", """    function handleFirstUserTap() {
      if (!hasInteracted) {
        hasInteracted = true;
        const hint = document.getElementById('doorTapHint');
        if (hint) hint.style.display = 'none';
      }
    }""")

# 7. Write to Version_3_Door_Touch/index.html and Shashi_Raveena_Wedding_Invitation_v3.html
v3_index_path = "D:/Shashi/Card/Version_3_Door_Touch/index.html"
v3_named_path = "D:/Shashi/Card/Version_3_Door_Touch/Shashi_Raveena_Wedding_Invitation_v3.html"

with open(v3_index_path, "w", encoding="utf-8") as f:
    f.write(html)
with open(v3_named_path, "w", encoding="utf-8") as f:
    f.write(html)

# 8. Set up 3-second trimmed Full Mela audio
import shutil
src_mela = "D:/Shashi/Card/Version_3_Door_Touch/kettimelam_from_3s.mp3"
dst_mela = "D:/Shashi/Card/Version_3_Door_Touch/kettimelam_exact_mela.mp3"
if os.path.exists(src_mela):
    shutil.copyfile(src_mela, dst_mela)
    print("Copied 3-second trimmed audio as default kettimelam_exact_mela.mp3")

print("Version 3 HTML generated successfully!")
