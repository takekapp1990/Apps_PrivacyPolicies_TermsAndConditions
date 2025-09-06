// SharedDice Language Switcher Module
// 共通の言語切り替え機能を提供

const LANGUAGE_ORDER = [
    { code: 'ja', name: '🇯🇵 日本語' },
    { code: 'en', name: '🇺🇸 English' },
    { code: 'zh_CN', name: '🇨🇳 中文（简体）' },
    { code: 'zh_TW', name: '🇹🇼 中文（繁體）' },
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
    { code: 'cs', name: '🇨🇿 Čeština' },
    { code: 'hu', name: '🇭🇺 Magyar' },
    { code: 'fi', name: '🇫🇮 Suomi' },
    { code: 'sv', name: '🇸🇪 Svenska' },
    { code: 'no', name: '🇳🇴 Norsk' },
    { code: 'da', name: '🇩🇰 Dansk' },
    { code: 'el', name: '🇬🇷 Ελληνικά' },
    { code: 'tr', name: '🇹🇷 Türkçe' },
    { code: 'ar', name: '🇸🇦 العربية' }
];

const LANGUAGE_URLS = {
    'ja': '../ja/landing_page_ja.html',
    'en': '../en/landing_page_en.html',
    'zh_CN': '../zh_CN/landing_page_zh_CN.html',
    'zh_TW': '../zh_TW/landing_page_zh_TW.html',
    'ko': '../ko/landing_page_ko.html',
    'vi': '../vi/landing_page_vi.html',
    'th': '../th/landing_page_th.html',
    'hi': '../hi/landing_page_hi.html',
    'id': '../id/landing_page_id.html',
    'es': '../es/landing_page_es.html',
    'fr': '../fr/landing_page_fr.html',
    'de': '../de/landing_page_de.html',
    'it': '../it/landing_page_it.html',
    'pt': '../pt/landing_page_pt.html',
    'nl': '../nl/landing_page_nl.html',
    'ru': '../ru/landing_page_ru.html',
    'uk': '../uk/landing_page_uk.html',
    'pl': '../pl/landing_page_pl.html',
    'cs': '../cs/landing_page_cs.html',
    'hu': '../hu/landing_page_hu.html',
    'fi': '../fi/landing_page_fi.html',
    'sv': '../sv/landing_page_sv.html',
    'no': '../no/landing_page_no.html',
    'da': '../da/landing_page_da.html',
    'el': '../el/landing_page_el.html',
    'tr': '../tr/landing_page_tr.html',
    'ar': '../ar/landing_page_ar.html'
};

// ドロップダウンメニューを生成
function generateLanguageDropdown(currentLang) {
    let html = '<ul class="dropdown-menu" aria-labelledby="languageDropdown">';
    
    LANGUAGE_ORDER.forEach(lang => {
        const activeClass = lang.code === currentLang ? 'active' : '';
        html += `<li><a class="dropdown-item ${activeClass}" href="#" onclick="switchLanguage('${lang.code}')">${lang.name}</a></li>`;
    });
    
    html += '</ul>';
    return html;
}

// 現在の言語を取得（data属性から）
function getCurrentLanguage() {
    const languageSwitcher = document.querySelector('.language-switcher');
    return languageSwitcher ? languageSwitcher.getAttribute('data-current-lang') : 'ja';
}

// 言語切り替え機能
function switchLanguage(lang) {
    const dropdownToggle = document.getElementById('languageDropdown');
    const selectedItem = event.target;
    
    // 要素の存在チェック
    if (!dropdownToggle || !selectedItem) {
        console.error('Required DOM elements not found');
        return;
    }
    
    // アクティブ状態を更新
    document.querySelectorAll('.dropdown-item').forEach(item => {
        if (item && item.classList) {
            item.classList.remove('active');
        }
    });
    
    if (selectedItem.classList) {
        selectedItem.classList.add('active');
    }
    
    // ドロップダウンの表示テキストを更新
    dropdownToggle.innerHTML = selectedItem.innerHTML;
    
    // 言語に応じたページにリダイレクト
    if (LANGUAGE_URLS[lang]) {
        window.location.href = LANGUAGE_URLS[lang];
    }
}

// ページ読み込み時にドロップダウンメニューを生成
document.addEventListener('DOMContentLoaded', function() {
    const currentLang = getCurrentLanguage();
    const dropdownContainer = document.querySelector('.language-switcher .dropdown');
    
    if (dropdownContainer) {
        // 既存のドロップダウンメニューを置き換え
        const existingMenu = dropdownContainer.querySelector('.dropdown-menu');
        if (existingMenu) {
            existingMenu.outerHTML = generateLanguageDropdown(currentLang);
        } else {
            // 既存のメニューがない場合は新しく追加
            dropdownContainer.innerHTML += generateLanguageDropdown(currentLang);
        }
    } else {
        console.error('Language switcher dropdown container not found');
    }
});