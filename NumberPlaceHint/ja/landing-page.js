// A single, fixed logical step. The full playable puzzle lives in learn/play.html.
(() => {
    'use strict';
    const carousel = document.querySelector('[data-carousel]');
    if (carousel) {
        const track = carousel.querySelector('.screenshots-track');
        const dots = carousel.querySelector('[data-carousel-dots]');
        const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
        let positions = [];
        const current = () => positions.reduce((best, position, index) =>
            Math.abs(position - track.scrollLeft) < Math.abs(positions[best] - track.scrollLeft) ? index : best, 0);
        const update = () => {
            const selected = current();
            Array.from(dots.children).forEach((button, index) => {
                button.setAttribute('aria-current', String(index === selected));
            });
        };
        const move = index => track.scrollTo({
            left: positions[Math.max(0, Math.min(index, positions.length - 1))],
            behavior: reducedMotion.matches ? 'instant' : 'smooth'
        });
        const resize = () => {
            const card = track.querySelector('[data-carousel-item]');
            const gap = parseFloat(getComputedStyle(track).gap) || 0;
            const stride = card.getBoundingClientRect().width + gap;
            const maximum = Math.max(0, track.scrollWidth - track.clientWidth);
            positions = [0];
            for (let left = stride; left < maximum - 2; left += stride) positions.push(left);
            if (maximum > 2) positions.push(maximum);
            dots.replaceChildren(...positions.map((position, index) => {
                const button = document.createElement('button');
                button.type = 'button';
                button.setAttribute('aria-label', `${index + 1} / ${positions.length}`);
                button.setAttribute('aria-controls', track.id);
                button.addEventListener('click', () => move(index));
                return button;
            }));
            dots.hidden = positions.length < 2;
            update();
        };
        track.addEventListener('scroll', update, { passive: true });
        track.addEventListener('keydown', event => {
            if (event.target !== track || !['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
            event.preventDefault();
            move(current() + (event.key === 'ArrowRight' ? 1 : -1));
        });
        new ResizeObserver(resize).observe(track);
        resize();
    }

    const preview = document.querySelector('[data-hint-preview]');
    if (!preview) return;
    const action = preview.querySelector('[data-preview-action]');
    const reset = preview.querySelector('[data-preview-reset]');
    const cell = preview.querySelector('[data-preview-cell]');
    const kicker = preview.querySelector('[data-preview-kicker]');
    const reason = preview.querySelector('[data-preview-reason]');
    const messages = JSON.parse(document.getElementById('lp-messages').textContent);
    const arrow = document.documentElement.dir === 'rtl' ? '←' : '→';

    function track(name) {
        if (typeof window.gtag === 'function') {
            window.gtag('event', name, { article_id: 'app_lp', technique_id: 'naked-single' });
        }
    }

    action.hidden = false;
    reset.hidden = false;
    action.addEventListener('click', () => {
        if (preview.dataset.state === 'initial') {
            preview.dataset.state = 'hint';
            cell.textContent = '5';
            cell.setAttribute('aria-label', messages.candidateLabel);
            kicker.textContent = messages.hintKicker;
            reason.textContent = messages.hintReason;
            action.textContent = messages.place + ' ' + arrow;
            track('sudoku_lp_hint_view');
        } else if (preview.dataset.state === 'hint') {
            preview.dataset.state = 'applied';
            cell.setAttribute('aria-label', messages.placedLabel);
            kicker.textContent = messages.appliedKicker;
            reason.textContent = messages.appliedReason;
            action.textContent = messages.complete;
            action.disabled = true;
            track('sudoku_lp_step_complete');
        }
    });

    reset.addEventListener('click', () => {
        preview.dataset.state = 'initial';
        cell.textContent = '?';
        cell.setAttribute('aria-label', messages.resetLabel);
        kicker.textContent = messages.initialKicker;
        reason.textContent = messages.initialReason;
        action.textContent = messages.hint + ' ' + arrow;
        action.disabled = false;
    });
})();
