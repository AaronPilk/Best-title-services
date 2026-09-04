/* Best Title Services — interactions */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Nav scroll state --- */
  var nav = document.querySelector('.nav');
  function onScroll() {
    if (!nav) return;
    if (window.scrollY > 12) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* --- Mobile menu --- */
  var burger = document.querySelector('.nav__burger');
  var menu = document.querySelector('.mobile-menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      nav.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.remove('open');
        nav.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* --- Scroll reveal --- */
  var revealEls = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* --- Accordion --- */
  document.querySelectorAll('.acc__q').forEach(function (q) {
    q.addEventListener('click', function () {
      var acc = q.closest('.acc');
      var body = acc.querySelector('.acc__a');
      var open = acc.classList.toggle('open');
      body.style.maxHeight = open ? body.scrollHeight + 'px' : '0px';
    });
  });
  window.addEventListener('resize', function () {
    document.querySelectorAll('.acc.open .acc__a').forEach(function (b) {
      b.style.maxHeight = b.scrollHeight + 'px';
    });
  });

  /* --- Hero: pointer parallax on floating glass cards --- */
  var hero = document.querySelector('.hero');
  if (hero && !reduce && window.matchMedia('(hover: hover)').matches) {
    var cards = hero.querySelectorAll('[data-parallax]');
    if (cards.length) {
      hero.addEventListener('mousemove', function (ev) {
        var r = hero.getBoundingClientRect();
        var x = (ev.clientX - r.left) / r.width - 0.5;
        var y = (ev.clientY - r.top) / r.height - 0.5;
        cards.forEach(function (c) {
          var d = parseFloat(c.getAttribute('data-parallax')) || 10;
          c.style.transform = 'translate3d(' + (x * d).toFixed(2) + 'px,' + (y * d).toFixed(2) + 'px,0)';
        });
      });
      hero.addEventListener('mouseleave', function () {
        cards.forEach(function (c) { c.style.transform = ''; });
      });
    }
  }

  /* --- Hero: gentle scroll parallax on the background photo --- */
  var heroImg = document.querySelector('.hero--home .hero__bg img');
  if (heroImg && !reduce) {
    var ticking = false;
    var park = function () {
      var y = window.scrollY;
      if (y < window.innerHeight * 1.2) {
        heroImg.style.transform = 'translate3d(0,' + (y * 0.16).toFixed(1) + 'px,0) scale(1.06)';
      }
      ticking = false;
    };
    heroImg.style.transform = 'scale(1.06)';
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(park); ticking = true; }
    }, { passive: true });
  }

  /* --- Current year --- */
  document.querySelectorAll('#year').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
