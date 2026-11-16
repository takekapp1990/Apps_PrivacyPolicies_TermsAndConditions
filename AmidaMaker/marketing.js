(() => {
  'use strict';
  document.querySelectorAll('[data-language]').forEach((select) => {
    select.addEventListener('change', () => {
      const target = select.value;
      if (target.startsWith('../') && !target.includes('://')) window.location.assign(target);
    });
  });
  document.querySelectorAll('[data-tabs]').forEach((group) => {
    const tabs = [...group.querySelectorAll('[role="tab"]')];
    const activate = (selected, focus = false) => {
      tabs.forEach((tab) => {
        const active = tab === selected;
        tab.setAttribute('aria-selected', String(active));
        tab.tabIndex = active ? 0 : -1;
        const panel = document.getElementById(tab.getAttribute('aria-controls'));
        panel.hidden = !active;
      });
      if (focus) selected.focus();
    };
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => activate(tab));
      tab.addEventListener('keydown', (event) => {
        let next;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === 'Home') next = 0;
        else if (event.key === 'End') next = tabs.length - 1;
        if (next !== undefined) { event.preventDefault(); activate(tabs[next], true); }
      });
    });
  });
  document.querySelectorAll('[data-method]').forEach((link) => {
    link.addEventListener('click', () => {
      document.getElementById(`method-tab-${link.dataset.method}`)?.click();
    });
  });
  document.querySelectorAll('[data-gallery]').forEach((gallery) => {
    const track = gallery.querySelector('[data-gallery-track]');
    const cards = [...track.children];
    const previous = gallery.querySelector('[data-gallery-prev]');
    const next = gallery.querySelector('[data-gallery-next]');
    const currentLabel = gallery.querySelector('[data-gallery-current]');
    const position = (index) => cards[index].offsetLeft - cards[0].offsetLeft;
    const current = () => cards.reduce((best, _, index) =>
      Math.abs(position(index) - track.scrollLeft) < Math.abs(position(best) - track.scrollLeft) ? index : best, 0);
    const update = () => {
      const index = current();
      currentLabel.textContent = String(index + 1);
      previous.disabled = index === 0;
      next.disabled = index === cards.length - 1;
    };
    const move = (index) => {
      const target = Math.max(0, Math.min(cards.length - 1, index));
      track.scrollTo({left: position(target), behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
    };
    previous.addEventListener('click', () => move(current() - 1));
    next.addEventListener('click', () => move(current() + 1));
    track.addEventListener('scroll', update, {passive: true});
    window.addEventListener('resize', update);
    track.addEventListener('keydown', (event) => {
      if (!['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      move(event.key === 'Home' ? 0 : event.key === 'End' ? cards.length - 1 : current() + (event.key === 'ArrowRight' ? 1 : -1));
    });
    update();
  });
  const viewer = document.getElementById('image-viewer');
  if (!viewer) return;
  const image = viewer.querySelector('img');
  let opener;
  document.querySelectorAll('[data-enlarge]').forEach((button) => {
    button.addEventListener('click', () => {
      opener = button;
      image.src = button.dataset.enlarge;
      image.alt = button.dataset.alt || button.querySelector('img')?.alt || '';
      viewer.showModal();
      viewer.scrollTop = 0;
    });
  });
  viewer.querySelector('.viewer-close').addEventListener('click', () => viewer.close());
  viewer.addEventListener('click', (event) => {
    if (event.target !== viewer) return;
    const rect = viewer.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) viewer.close();
  });
  viewer.addEventListener('close', () => opener?.focus());
})();
