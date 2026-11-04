// Match the language dropdown behavior used by the other TakeKApp landing pages.
document.querySelectorAll('.language-picker').forEach((picker) => {
  document.addEventListener('pointerdown', (event) => {
    if (!picker.contains(event.target)) picker.open = false;
  });
  picker.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || !picker.open) return;
    picker.open = false;
    picker.querySelector('summary').focus();
  });
  picker.addEventListener('focusout', (event) => {
    if (!picker.contains(event.relatedTarget)) picker.open = false;
  });
});

document.querySelectorAll('[data-hero-carousel]').forEach((carousel) => {
  const slides = [...carousel.querySelectorAll('[data-carousel-slide]')];
  const dots = [...carousel.querySelectorAll('[data-carousel-dot]')];
  if (slides.length < 2 || slides.length !== dots.length) return;
  const viewport = carousel.querySelector('[data-carousel-viewport]');
  const caption = carousel.querySelector('[data-carousel-caption]');
  const rotation = carousel.querySelector('[data-carousel-rotation]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let index = 0;
  let timer;
  let userPaused = reducedMotion.matches;
  let inView = false;
  let hovered = false;
  let touchStart;

  const stop = () => {
    window.clearTimeout(timer);
    timer = undefined;
  };
  const updateRotation = () => {
    rotation.hidden = reducedMotion.matches;
    const label = userPaused ? rotation.dataset.playLabel : rotation.dataset.pauseLabel;
    rotation.setAttribute('aria-label', label);
    rotation.title = label;
    rotation.firstElementChild.textContent = userPaused ? '▶' : 'Ⅱ';
    caption.setAttribute('aria-live', userPaused ? 'polite' : 'off');
  };
  const show = (next) => {
    index = (next + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      const active = i === index;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', String(!active));
      dots[i].setAttribute('aria-pressed', String(active));
    });
    caption.textContent = slides[index].dataset.caption;
  };
  const start = () => {
    stop();
    if (userPaused || reducedMotion.matches || document.hidden || !inView || hovered || carousel.contains(document.activeElement)) return;
    timer = window.setTimeout(() => {
      timer = undefined;
      show(index + 1);
      start();
    }, 4000);
  };
  const select = (next) => {
    userPaused = true;
    stop();
    updateRotation();
    show(next);
  };
  dots.forEach((dot, i) => dot.addEventListener('click', () => select(i)));
  carousel.querySelector('[data-carousel-prev]').addEventListener('click', () => select(index - 1));
  carousel.querySelector('[data-carousel-next]').addEventListener('click', () => select(index + 1));
  rotation.addEventListener('click', () => {
    userPaused = !userPaused;
    updateRotation();
    start();
  });
  carousel.addEventListener('mouseenter', () => { hovered = true; stop(); });
  carousel.addEventListener('mouseleave', () => { hovered = false; start(); });
  carousel.addEventListener('focusin', stop);
  carousel.addEventListener('focusout', (event) => {
    if (!carousel.contains(event.relatedTarget)) {
      // Wait for the browser to update activeElement after focusout.
      window.setTimeout(start, 0);
    }
  });
  carousel.addEventListener('keydown', (event) => {
    if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
    event.preventDefault();
    select(index + (event.key === 'ArrowRight' ? 1 : -1));
    dots[index].focus();
  });
  viewport.addEventListener('pointerdown', (event) => {
    if (event.pointerType !== 'touch' || !event.isPrimary) return;
    stop();
    touchStart = { x: event.clientX, y: event.clientY };
  });
  viewport.addEventListener('pointerup', (event) => {
    if (!touchStart) return;
    const dx = event.clientX - touchStart.x;
    const dy = event.clientY - touchStart.y;
    touchStart = undefined;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.3) select(index + (dx < 0 ? 1 : -1));
    else start();
  });
  viewport.addEventListener('pointercancel', () => { touchStart = undefined; start(); });
  document.addEventListener('visibilitychange', start);
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) userPaused = true;
    updateRotation();
    start();
  });
  new IntersectionObserver(([entry]) => {
    inView = entry.isIntersecting;
    start();
  }, { threshold: 0.15 }).observe(carousel);
  carousel.querySelector('.carousel-controls').hidden = false;
  updateRotation();
  show(0);
});
