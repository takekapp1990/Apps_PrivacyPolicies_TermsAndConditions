(() => {
  'use strict';
  const tabs = [...document.querySelectorAll('[data-step]')];
  const image = document.querySelector('[data-learning-image]');
  const note = document.querySelector('[data-record-note]');
  function selectStep(tab, focus = false) {
    tabs.forEach(item => { const active = item === tab; item.setAttribute('aria-selected', String(active)); item.tabIndex = active ? 0 : -1; });
    if (image) { image.src = tab.dataset.image; image.alt = tab.dataset.alt; image.closest('[role=tabpanel]').setAttribute('aria-labelledby', tab.id); }
    if (note) note.hidden = tab.dataset.step !== '2';
    if (focus) tab.focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectStep(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (['ArrowDown', 'ArrowRight'].includes(event.key)) next = (index + 1) % tabs.length;
      if (['ArrowUp', 'ArrowLeft'].includes(event.key)) next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next !== undefined) { event.preventDefault(); selectStep(tabs[next], true); }
    });
  });
  const sample = document.querySelector('[data-demo]');
  if (sample) {
    const choices = [...sample.querySelectorAll('[data-choice]')];
    const status = sample.querySelector('[data-demo-answer]');
    const reveal = sample.querySelector('[data-reveal]');
    const reset = sample.querySelector('[data-reset]');
    const initial = status.textContent;
    function answer(index) {
      choices.forEach((choice, n) => { choice.setAttribute('aria-pressed', String(n === index)); choice.dataset.wrong = String(n === index && n !== 0); });
      status.replaceChildren();
      const heading = document.createElement('strong');
      heading.textContent = index === 1 ? sample.dataset.wrong : sample.dataset.correct;
      const explanation = document.createElement('p');
      explanation.textContent = sample.dataset.explanation;
      status.append(heading, explanation);
      reset.hidden = false; reveal.hidden = true;
    }
    choices.forEach((choice, index) => choice.addEventListener('click', () => answer(index)));
    reveal.addEventListener('click', () => answer(0));
    reset.addEventListener('click', () => { choices.forEach(choice => { choice.setAttribute('aria-pressed', 'false'); delete choice.dataset.wrong; }); status.textContent = initial; reset.hidden = true; reveal.hidden = false; choices[0].focus(); });
  }
  const menu = document.querySelector('.language-menu');
  if (menu) {
    document.addEventListener('click', event => { if (!menu.contains(event.target)) menu.open = false; });
    document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.open) { menu.open = false; menu.querySelector('summary').focus(); } });
  }
})();
