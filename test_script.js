
    const stage = document.getElementById('mandapamStage');
    // removed btnGroom
    // removed btnBride
    // removed btnUnion
    // removed btnClose
    const btnMusic = document.getElementById('btnMusic');
    const musicBtnLabel = document.getElementById('musicBtnLabel');
    const musicIcon = document.getElementById('musicIcon');

    // ==========================================
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

    function dismissWelcomeAndPlay() {
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
    });

    function resetActiveButtons() {
      // V3 has direct door-touch interaction
    }

    // Open ONLY Groom's Side -> Plays 8D Sundhari Kanaal Violin
    function openGroomWing() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-groom';
      resetActiveButtons();
      playSectionSound(audioGroom, '🤵 వరుని వైభోగం (Violin 8D)', '🤵🎻');
    }

    // Open ONLY Bride's Side -> Plays 8D Kannathil Muthamittal Violin
    function openBrideWing() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-bride';
      resetActiveButtons();
      playSectionSound(audioBride, '👰 వధువు వైభోగం (Violin 8D)', '👰🎻');
    }

    const CALENDAR_URL = 'https://calendar.google.com/calendar/render?action=TEMPLATE&text=Shashi+%26+Raveena+Wedding&dates=20261213T042000Z/20261213T093000Z&details=Auspicious+Sumuhurtham+at+09:50+AM.+Thanmaya+Farmstay+Resort,+Warangal+Highway.&location=Thanmaya+Farmstay+Resort,+Rajavaram,+Telangana+506144';
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

    // Open BOTH Doors (The Grand Union) -> Plays 8D Main Celebratory Wedding Song!
    function openBothDoors() {
      handleFirstUserTap();
      stage.className = 'mandapam-stage opened-both';
      resetActiveButtons();
      playSectionSound(audioMain, '👑 కల్యాణ మహోత్సవం (8D)', '👑🎉');
      addDirectlyToCalendar();
    }

    // Close All Doors -> Resumes Entry 8D Song
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
    }

    // Click handler for Left Door
    function handleLeftDoorClick() {
      if (stage.classList.contains('opened-groom')) {
        closeAllDoors();
      } else {
        openGroomWing();
      }
    }

    // Click handler for Right Door
    function handleRightDoorClick() {
      if (stage.classList.contains('opened-bride')) {
        closeAllDoors();
      } else {
        openBrideWing();
      }
    }
  