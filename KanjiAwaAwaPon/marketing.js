(() => {
  const challenge = document.querySelector('[data-challenge]');
  if (challenge) {
    const questions = [
      { word: '海月', answer: 'くらげ', options: ['くらげ', 'なまこ', 'ひとで', 'いそぎんちゃく'] },
      { word: '土筆', answer: 'つくし', options: ['どふで', 'つくし', 'すぎな', 'たんぽぽ'] },
      { word: '河豚', answer: 'ふぐ', options: ['かっぱ', 'いるか', 'ふぐ', 'かわうそ'] },
    ];
    let index = 0;
    let answered = false;
    const word = challenge.querySelector('[data-challenge-word]');
    const options = challenge.querySelector('[data-challenge-options]');
    const buttons = [...options.querySelectorAll('button')];
    const feedback = challenge.querySelector('[data-challenge-feedback]');
    const position = challenge.querySelector('[data-question-position]');
    const render = () => {
      const question = questions[index];
      word.textContent = question.word;
      position.textContent = `${index + 1} / ${questions.length}`;
      options.setAttribute('aria-label', `${question.word}の読みを選ぶ`);
      buttons.forEach((button, i) => {
        button.textContent = question.options[i];
        button.dataset.choice = question.options[i];
        button.disabled = false;
        button.classList.remove('is-correct', 'is-wrong');
      });
      challenge.classList.remove('is-solved');
      feedback.textContent = 'どれだと思う？ 選んでみよう。';
      delete feedback.dataset.result;
      answered = false;
    };
    buttons.forEach((button) => button.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const question = questions[index];
      const correct = button.dataset.choice === question.answer;
      buttons.forEach((candidate) => {
        candidate.disabled = true;
        if (candidate.dataset.choice === question.answer) candidate.classList.add('is-correct');
      });
      if (!correct) button.classList.add('is-wrong');
      feedback.textContent = correct ? `正解！ ${question.word}は「${question.answer}」` : `おしい！ 正解は「${question.answer}」`;
      feedback.dataset.result = correct ? 'correct' : 'wrong';
      challenge.classList.add('is-solved');
    }));
    challenge.querySelector('[data-challenge-next]').addEventListener('click', () => {
      index = (index + 1) % questions.length;
      render();
    });
  }

  const showcase = document.querySelector('[data-game-showcase]');
  if (showcase) {
    const tabs = [...showcase.querySelectorAll('[data-game-tab]')];
    const panels = [...showcase.querySelectorAll('[role="tabpanel"]')];
    const activate = (tab) => {
      tabs.forEach((item) => {
        const selected = item === tab;
        item.setAttribute('aria-selected', String(selected));
        item.tabIndex = selected ? 0 : -1;
      });
      panels.forEach((panel) => { panel.hidden = panel.id !== tab.getAttribute('aria-controls'); });
    };
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => activate(tab));
      tab.addEventListener('keydown', (event) => {
        let target;
        if (event.key === 'ArrowRight' || event.key === 'ArrowDown') target = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') target = (index + tabs.length - 1) % tabs.length;
        if (event.key === 'Home') target = 0;
        if (event.key === 'End') target = tabs.length - 1;
        if (target === undefined) return;
        event.preventDefault();
        activate(tabs[target]);
        tabs[target].focus();
      });
    });
  }

  const gallery = document.querySelector('[data-gallery]');
  if (gallery) {
    const previous = document.querySelector('[data-gallery-prev]');
    const next = document.querySelector('[data-gallery-next]');
    const position = document.querySelector('[data-gallery-position]');
    const cards = Array.from(gallery.children);
    const step = () => cards.length > 1 ? cards[1].offsetLeft - cards[0].offsetLeft : 0;
    const update = () => {
      const maximum = gallery.scrollWidth - gallery.clientWidth;
      previous.disabled = gallery.scrollLeft <= 2;
      next.disabled = gallery.scrollLeft >= maximum - 2;
      const current = Math.min(cards.length - 1, Math.round(gallery.scrollLeft / (step() || 1)));
      position.textContent = `${current + 1} / ${cards.length}`;
    };
    const move = (direction) => gallery.scrollBy({
      left: direction * step(),
      behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth',
    });
    previous.addEventListener('click', () => move(-1));
    next.addEventListener('click', () => move(1));
    gallery.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    update();
  }
})();
