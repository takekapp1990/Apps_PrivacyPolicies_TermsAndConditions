(() => {
  const quiz = document.querySelector('[data-quiz]');
  if (quiz) {
    const words = [['海月', 'くらげ'], ['土筆', 'つくし'], ['河豚', 'ふぐ']];
    let index = 0;
    let revealed = false;
    const reveal = quiz.querySelector('[data-reveal]');
    const reading = quiz.querySelector('[data-reading]');
    const updateReading = () => {
      reading.textContent = revealed ? words[index][1] : '';
      reveal.textContent = revealed ? '読みを隠す' : '読みを見る';
      reveal.setAttribute('aria-expanded', String(revealed));
    };
    reveal.addEventListener('click', () => {
      revealed = !revealed;
      updateReading();
    });
    quiz.querySelector('[data-next]').addEventListener('click', () => {
      index = (index + 1) % words.length;
      quiz.querySelector('[data-word]').textContent = words[index][0];
      revealed = false;
      updateReading();
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
