/* Shared locale matching for the entry page and explicit language selection. */
(() => {
  'use strict';
  const supported = ['ja', 'en', 'zh-Hans', 'zh-Hant', 'ko', 'es', 'pt-BR', 'fr', 'de', 'it', 'nl', 'ru', 'uk', 'pl', 'tr', 'ar', 'hi', 'id', 'vi', 'th'];
  const storageKey = 'nemucue.language';
  const match = (value) => {
    const tag = String(value || '').replaceAll('_', '-').toLowerCase();
    if (!/^[a-z]{2,3}(?:-[a-z0-9]{2,8})*$/.test(tag)) return null;
    const parts = tag.split('-');
    if (parts[0] === 'zh') {
      if (parts.includes('hant')) return 'zh-Hant';
      if (parts.includes('hans')) return 'zh-Hans';
      return parts.some((part) => ['tw', 'hk', 'mo'].includes(part)) ? 'zh-Hant' : 'zh-Hans';
    }
    if (parts[0] === 'pt') return 'pt-BR';
    return supported.find((locale) => locale.toLowerCase() === parts[0]) || null;
  };
  const choose = (languages, saved) => {
    if (supported.includes(saved)) return saved;
    for (const language of languages || []) {
      const locale = match(language);
      if (locale) return locale;
    }
    return 'en';
  };
  const remember = (locale) => {
    if (!supported.includes(locale)) return;
    try { localStorage.setItem(storageKey, locale); } catch (_) { /* File URLs/private browsing may block storage. */ }
  };
  window.NemuCueLocale = Object.freeze({ match, choose, remember });
  if (document.documentElement.hasAttribute('data-language-entry')) {
    let saved;
    try { saved = localStorage.getItem(storageKey); } catch (_) { /* Use browser preferences. */ }
    const locale = choose(navigator.languages?.length ? navigator.languages : [navigator.language], saved);
    window.location.replace(`./${locale}/index.html${window.location.search}${window.location.hash}`);
  }
  document.addEventListener('click', (event) => {
    const link = event.target.closest?.('a[data-language]');
    if (link) remember(link.dataset.language);
  });
})();
