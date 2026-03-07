// TapAlbum Language Switcher Logic
const LANGUAGE_ORDER = [
    { code: 'ja', name: '🇯🇵 日本語' },
    { code: 'en', name: '🇺🇸 English' },
    { code: 'zh_Hans', name: '🇨🇳 中文（简体）' },
    { code: 'zh_Hant', name: '🇹🇼 中文（繁體）' },
    { code: 'ko', name: '🇰🇷 한국어' },
    { code: 'vi', name: '🇻🇳 Tiếng Việt' },
    { code: 'th', name: '🇹🇭 ไทย' },
    { code: 'hi', name: '🇮🇳 हिन्दी' },
    { code: 'id', name: '🇮🇩 Bahasa Indonesia' },
    { code: 'es', name: '🇪🇸 Español' },
    { code: 'fr', name: '🇫🇷 Français' },
    { code: 'de', name: '🇩🇪 Deutsch' },
    { code: 'it', name: '🇮🇹 Italiano' },
    { code: 'pt', name: '🇵🇹 Português' },
    { code: 'nl', name: '🇳🇱 Nederlands' },
    { code: 'ru', name: '🇷🇺 Русский' },
    { code: 'uk', name: '🇺🇦 Українська' },
    { code: 'pl', name: '🇵🇱 Polski' },
    { code: 'da', name: '🇩🇰 Dansk' },
    { code: 'no', name: '🇳🇴 Norsk' },
    { code: 'tr', name: '🇹🇷 Türkçe' },
    { code: 'ar', name: '🇸🇦 العربية' },
    { code: 'bn', name: '🇧🇩 বাংলা' },
    { code: 'sw', name: '🇹🇿 Kiswahili' }
];

document.addEventListener('DOMContentLoaded', () => {
    const switcher = document.getElementById('languageSwitcher');
    if (!switcher) return;

    const currentLangCode = switcher.getAttribute('data-current-lang') || 'en';
    const toggleBtn = document.getElementById('lsToggle');
    const menu = document.getElementById('lsMenu');

    // Find current language object
    const currentLangObj = LANGUAGE_ORDER.find(l => l.code === currentLangCode) || LANGUAGE_ORDER.find(l => l.code === 'en');
    
    // Set button text preserving the original emoji and language text format
    toggleBtn.textContent = currentLangObj.name;

    // Build the dropdown menu
    LANGUAGE_ORDER.forEach(lang => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        
        a.className = 'ls-item' + (lang.code === currentLangCode ? ' active' : '');
        a.textContent = lang.name;
        a.href = `../${lang.code}/landing_page_${lang.code}.html`;
        
        // Use normal link behavior, no preventDefault needed unless doing custom transitions
        
        li.appendChild(a);
        menu.appendChild(li);
    });

    // Toggle menu visibility
    toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isShowing = menu.classList.contains('show');
        
        if (isShowing) {
            menu.classList.remove('show');
            toggleBtn.setAttribute('aria-expanded', 'false');
        } else {
            menu.classList.add('show');
            toggleBtn.setAttribute('aria-expanded', 'true');
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!switcher.contains(e.target)) {
            menu.classList.remove('show');
            toggleBtn.setAttribute('aria-expanded', 'false');
        }
    });
});
