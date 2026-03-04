/* ===========================================================
   FERRARI-THEMED PORTFOLIO — SCRIPT
   =========================================================== */

(function () {
  'use strict';

  // ---- DOM Refs ----
  const html = document.documentElement;
  const themeToggle = document.getElementById('themeToggle');
  const navBurger = document.getElementById('navBurger');
  const mobileMenu = document.getElementById('mobileMenu');
  const musicToggle = document.getElementById('musicToggle');
  const bgMusic = document.getElementById('bgMusic');
  const viewPreviewBtn = document.getElementById('viewPreviewBtn');
  const previewModal = document.getElementById('previewModal');
  const modalClose = document.getElementById('modalClose');
  const splineBg = document.getElementById('splineBg');

  // ---- Constants ----
  const SPLINE_URL = 'https://my.spline.design/f12025szferraribolid-uh450ROqJbX0axdlwqf4fDnq/';

  // ===========================================================
  // THEME SYSTEM
  // ===========================================================
  function getStoredTheme() {
    return localStorage.getItem('rp-theme') || 'dark';
  }

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('rp-theme', theme);
    // Update meta theme-color
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#0F0F0F' : '#F9F8F4');
  }

  // Initialize theme (no flash)
  setTheme(getStoredTheme());

  themeToggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    setTheme(current === 'dark' ? 'light' : 'dark');
  });

  // ===========================================================
  // MOBILE NAVIGATION
  // ===========================================================
  navBurger.addEventListener('click', () => {
    navBurger.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  });

  // Close mobile menu on link click
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navBurger.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  // ===========================================================
  // SPLINE 3D BACKGROUND (Lazy Load)
  // ===========================================================
  function loadSpline() {
    // Skip on mobile with prefers-reduced-motion
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const iframe = document.createElement('iframe');
    iframe.src = SPLINE_URL;
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('loading', 'lazy');
    iframe.setAttribute('title', '3D Ferrari Background');
    iframe.setAttribute('allow', 'autoplay');
    splineBg.appendChild(iframe);
  }

  // Load Spline after page is interactive
  if ('requestIdleCallback' in window) {
    requestIdleCallback(loadSpline, { timeout: 3000 });
  } else {
    setTimeout(loadSpline, 1500);
  }

  // ===========================================================
  // BACKGROUND MUSIC SYSTEM
  // ===========================================================
  const MAX_VOLUME = 0.45;
  const FADE_STEP = 0.005;
  const FADE_INTERVAL = 30;

  let isPlaying = false;
  let fadeTimer = null;
  let musicLoaded = false;

  function loadMusic() {
    if (!musicLoaded) {
      bgMusic.load();
      musicLoaded = true;
    }
  }

  function fadeIn() {
    clearInterval(fadeTimer);
    bgMusic.volume = 0;
    bgMusic.play().then(() => {
      fadeTimer = setInterval(() => {
        if (bgMusic.volume < MAX_VOLUME - FADE_STEP) {
          bgMusic.volume = Math.min(bgMusic.volume + FADE_STEP, MAX_VOLUME);
        } else {
          bgMusic.volume = MAX_VOLUME;
          clearInterval(fadeTimer);
        }
      }, FADE_INTERVAL);
    }).catch(() => {
      // Autoplay blocked — silently fail
    });
  }

  function fadeOut() {
    clearInterval(fadeTimer);
    fadeTimer = setInterval(() => {
      if (bgMusic.volume > FADE_STEP) {
        bgMusic.volume = Math.max(bgMusic.volume - FADE_STEP, 0);
      } else {
        bgMusic.volume = 0;
        bgMusic.pause();
        clearInterval(fadeTimer);
      }
    }, FADE_INTERVAL);
  }

  musicToggle.addEventListener('click', () => {
    loadMusic();
    if (isPlaying) {
      fadeOut();
      isPlaying = false;
      musicToggle.classList.remove('playing');
      localStorage.setItem('rp-music', 'paused');
    } else {
      fadeIn();
      isPlaying = true;
      musicToggle.classList.add('playing');
      localStorage.setItem('rp-music', 'playing');
    }
  });

  // Pause music when tab is not visible
  document.addEventListener('visibilitychange', () => {
    if (!isPlaying) return;
    if (document.hidden) {
      bgMusic.pause();
    } else {
      bgMusic.play().catch(() => { });
    }
  });

  // ===========================================================
  // IMAGE PREVIEW MODAL
  // ===========================================================
  viewPreviewBtn.addEventListener('click', () => {
    previewModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  });

  function closeModal() {
    previewModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  modalClose.addEventListener('click', closeModal);
  previewModal.querySelector('.modal__overlay').addEventListener('click', closeModal);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && previewModal.classList.contains('active')) {
      closeModal();
    }
  });

  // ===========================================================
  // SCROLL REVEAL (IntersectionObserver)
  // ===========================================================
  const reveals = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    reveals.forEach((el) => observer.observe(el));
  } else {
    // Fallback: show everything
    reveals.forEach((el) => el.classList.add('visible'));
  }

  // ===========================================================
  // NAV SCROLL SHADOW
  // ===========================================================
  const nav = document.getElementById('nav');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (scrollY > 80) {
      nav.style.boxShadow = '0 4px 30px rgba(0,0,0,0.15)';
    } else {
      nav.style.boxShadow = 'none';
    }
    lastScroll = scrollY;
  }, { passive: true });

})();
