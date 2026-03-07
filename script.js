/* ===========================================================
   RUSHIKESH PUNEKAR — PORTFOLIO SCRIPT
   =========================================================== */

(function () {
  'use strict';

  // ---- DOM ----
  const html = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const navBurger = document.getElementById('navBurger');
  const mobileMenu = document.getElementById('mobileMenu');
  const musicToggle = document.getElementById('musicToggle');
  const bgMusic = document.getElementById('bgMusic');
  const viewPreviewBtn = document.getElementById('viewPreviewBtn');
  const previewModal = document.getElementById('previewModal');
  const modalClose = document.getElementById('modalClose');
  const nav = document.getElementById('nav');

  // ===========================================================
  // PROJECTS TRACK TIMELINE ANIMATION
  // ===========================================================
  const trackTimeline = document.querySelector('.track-timeline');
  const trackProgress = document.getElementById('trackProgress');

  if (trackTimeline && trackProgress) {
    window.addEventListener('scroll', () => {
      // Calculate how far we've scrolled into the track timeline
      const rect = trackTimeline.getBoundingClientRect();
      const windowHeight = window.innerHeight;

      // We want the line to start growing when the top of the track enters the bottom half of the screen
      // and finish when the bottom of the track is near the middle of the screen
      const totalPath = rect.height;
      const scrolled = windowHeight / 1.5 - rect.top;

      let percentage = (scrolled / totalPath) * 100;

      // Clamp between 0 and 100
      percentage = Math.max(0, Math.min(100, percentage));

      trackProgress.style.height = percentage + '%';
    });
  }

  // ===========================================================
  // THEME SYSTEM
  // ===========================================================
  function getStoredTheme() { return localStorage.getItem('rp-theme') || 'dark'; }

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('rp-theme', theme);
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#0a0a0f' : '#f4f5fa');
  }

  setTheme(getStoredTheme());

  themeToggle.addEventListener('click', () => {
    setTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  });

  // ===========================================================
  // MOBILE NAV
  // ===========================================================
  navBurger.addEventListener('click', () => {
    navBurger.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  });

  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navBurger.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  // ===========================================================
  // HOTSPOT INTERACTIONS
  // ===========================================================
  document.querySelectorAll('.hotspot').forEach(spot => {
    spot.addEventListener('click', () => {
      const target = spot.getAttribute('data-target');
      if (target) {
        const el = document.querySelector(target);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // ===========================================================
  // BACKGROUND MUSIC
  // ===========================================================
  const MUSIC_VOLUME = 0.15;
  let musicPlaying = false;

  // Attempt autoplay
  function tryAutoplay() {
    bgMusic.volume = MUSIC_VOLUME;
    bgMusic.play().then(() => {
      musicPlaying = true;
      musicToggle.classList.add('playing');
    }).catch(() => {
      // Autoplay blocked — user interaction needed
      musicPlaying = false;
    });
  }

  // Try autoplay on first user interaction as fallback
  function onFirstInteraction() {
    if (!musicPlaying) {
      tryAutoplay();
    }
    document.removeEventListener('click', onFirstInteraction);
    document.removeEventListener('touchstart', onFirstInteraction);
  }

  document.addEventListener('click', onFirstInteraction, { once: true });
  document.addEventListener('touchstart', onFirstInteraction, { once: true });

  // Try immediate autoplay
  window.addEventListener('load', () => {
    tryAutoplay();
  });

  musicToggle.addEventListener('click', (e) => {
    e.stopPropagation(); // Don't trigger first interaction handler
    if (musicPlaying) {
      bgMusic.pause();
      musicPlaying = false;
      musicToggle.classList.remove('playing');
    } else {
      bgMusic.volume = MUSIC_VOLUME;
      bgMusic.play().then(() => {
        musicPlaying = true;
        musicToggle.classList.add('playing');
      }).catch(() => { });
    }
  });

  // Pause when tab hidden
  document.addEventListener('visibilitychange', () => {
    if (!musicPlaying) return;
    if (document.hidden) bgMusic.pause();
    else bgMusic.play().catch(() => { });
  });

  // ===========================================================
  // PREVIEW MODAL
  // ===========================================================
  if (viewPreviewBtn) {
    viewPreviewBtn.addEventListener('click', () => {
      previewModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });
  }

  function closeModal() {
    previewModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (previewModal) {
    const overlay = previewModal.querySelector('.modal__overlay');
    if (overlay) overlay.addEventListener('click', closeModal);
  }

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && previewModal.classList.contains('active')) closeModal();
  });

  // ===========================================================
  // SCROLL REVEAL
  // ===========================================================
  const reveals = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    const revealObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    reveals.forEach(el => revealObs.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('visible'));
  }

  // ===========================================================
  // DASHBOARD DIAL ANIMATION
  // ===========================================================
  const dialProgressBars = document.querySelectorAll('.dial-progress');
  const circumference = 251.2;

  function animateDial(dial) {
    const rawPct = dial.getAttribute('data-pct');
    const targetPct = parseInt(rawPct, 10);
    const targetOffset = circumference - (circumference * (targetPct / 100));

    // Set offset variable for CSS transition
    dial.style.setProperty('--target-offset', targetOffset);
    dial.classList.add('animate');

    // Number counter animation
    const contentWrap = dial.closest('.dial-svg-wrap').querySelector('.dial-pct');
    let current = 0;
    const duration = 1500; // ms
    const stepTime = Math.abs(Math.floor(duration / targetPct));

    const timer = setInterval(() => {
      current += 1;
      contentWrap.textContent = current + '%';
      if (current >= targetPct) {
        clearInterval(timer);
      }
    }, stepTime);
  }

  if ('IntersectionObserver' in window) {
    const dialObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateDial(entry.target);
          dialObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    dialProgressBars.forEach(dial => dialObs.observe(dial));
  } else {
    dialProgressBars.forEach(dial => animateDial(dial));
  }

  // ===========================================================
  // NAV SCROLL SHADOW
  // ===========================================================
  window.addEventListener('scroll', () => {
    if (window.scrollY > 60) {
      nav.style.boxShadow = '0 4px 30px rgba(0,0,0,.18)';
    } else {
      nav.style.boxShadow = 'none';
    }
  }, { passive: true });

  // ===========================================================
  // BACKGROUND VIDEO SCROLL LOGIC
  // ===========================================================
  const bgVideo = document.getElementById('bgVideo');
  const sectionsToPlayVideo = document.querySelectorAll('#about, #skills, #projects, #contact');

  if ('IntersectionObserver' in window && bgVideo) {
    let visibleSections = new Set();

    const videoObs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          visibleSections.add(entry.target.id);
        } else {
          visibleSections.delete(entry.target.id);
        }
      });

      if (visibleSections.size > 0) {
        bgVideo.classList.add('visible');
        if (bgVideo.paused) bgVideo.play().catch(() => { });
      } else {
        bgVideo.classList.remove('visible');
        if (!bgVideo.paused) bgVideo.pause();
      }
    }, { threshold: 0.1 });

    sectionsToPlayVideo.forEach(sec => videoObs.observe(sec));
  }

})();
