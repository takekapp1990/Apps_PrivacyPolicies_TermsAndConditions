"""Build ten static LPs. Copy lives in flag_memory_lp_copy; no runtime framework."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'FlagMemoryAwaAwaPon'
COPY = Path(__file__).parent / 'flag_memory_lp_copy'
LANGUAGES = {'ja': '日本語', 'en': 'English', 'es': 'Español', 'de': 'Deutsch', 'ko': '한국어', 'th': 'ไทย', 'id': 'Bahasa Indonesia', 'fr': 'Français', 'pt-BR': 'Português (Brasil)', 'zh-Hant': '繁體中文（台灣）'}
BASE = 'https://takekapp.com/FlagMemoryAwaAwaPon'
ASSET = '../images/lp'

def e(value):
    return escape(str(value), quote=True)

def lines(value):
    return '<br>'.join(e(part) for part in value.split('\n'))

def url(lang):
    return f'{BASE}/{lang}/landing_page_{lang}.html'

def icon(index):
    paths = [
        '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M4 12h16M12 4v16"/>',
        '<path d="M4 6h5v5H4zM15 13h5v5h-5zM9 8h6v8"/>',
        '<path d="M4 19V4l8 2v10l-8-2M12 6l8-2v10l-8 2"/>',
        '<circle cx="12" cy="12" r="8"/><path d="M12 7v5l3 2"/>',
        '<circle cx="10" cy="10" r="6"/><path d="m15 15 5 5M8 10h4M10 8v4"/>',
        '<path d="m3 9 9-6 9 6M5 10h14M5 20h14M7 10v10M12 10v10M17 10v10"/>',
        '<path d="M4 20V9h5v11M10 20V4h5v16M16 20v-7h4v7"/>',
        '<path d="m3 5 6-2 6 2 6-2v16l-6 2-6-2-6 2zM9 3v16M15 5v16"/>',
    ]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[index]}</svg>'

def language_menu(lang, d):
    links = ''.join(f'<li><a href="../{key}/landing_page_{key}.html" lang="{key}" hreflang="{key}"'+(' aria-current="page"' if key == lang else '')+f'>{e(label)}</a></li>' for key, label in LANGUAGES.items())
    return f'<details class="language-menu"><summary aria-label="{e(d["languageLabel"]+": "+LANGUAGES[lang])}"><span aria-hidden="true">◎</span>{e(LANGUAGES[lang])}</summary><ul>{links}</ul></details>'

def stores(lang, d, position):
    ja = lang == 'ja'
    apple = 'Download_on_the_App_Store_Badge_JP_RGB_blk_100317.svg' if ja else 'Download_on_the_App_Store_Badge_US-UK_RGB_blk_092917.svg'
    google = 'GetItOnGooglePlay_Badge_Web_color_Japanese.png' if ja else 'GetItOnGooglePlay_Badge_Web_color_English.png'
    loading = 'eager' if position == 'hero' else 'lazy'
    apple_width = 109 if ja else 120
    return f'''<div class="store-links"><a class="store-badge" data-analytics-position="{position}" href="https://apps.apple.com/app/id6757128485" aria-label="{e(d['appStore'])}"><img src="../../commonImages/badgeiOSAppStore/{apple}" alt="{e(d['appStore'])}" width="{apple_width}" height="40" decoding="async" loading="{loading}"></a><a class="store-badge google" data-analytics-position="{position}" href="https://play.google.com/store/apps/details?id=com.NationalFlagsAwaPop.takekapp1990.prod&amp;hl={lang}" aria-label="{e(d['googlePlay'])}"><img src="../../commonImages/badgeAndroid/{google}" alt="{e(d['googlePlay'])}" width="270" height="80" decoding="async" loading="{loading}"></a></div>'''

def screen(lang, d, number, cls='', eager=False):
    return f'<div class="phone {cls}"><img src="{ASSET}/{lang}/screen-{number:02}.webp" alt="{e(d["screenshotAlt"][number-1])}" width="820" height="1777" decoding="async"'+(' fetchpriority="high"' if eager else ' loading="lazy"')+'></div>'

def build(lang):
    d = json.loads((COPY / f'{lang}.json').read_text())
    canonical = url(lang)
    h = ''.join(f'<span>{e(t)}</span>' for t in d['heroTitle'])
    alternate = '\n'.join(f'<link rel="alternate" hreflang="{key}" href="{url(key)}">' for key in LANGUAGES)
    schema = {'@context': 'https://schema.org', '@type': 'MobileApplication', 'name': d['name'], 'url': canonical, 'description': d['description'], 'operatingSystem': 'iOS, Android', 'applicationCategory': 'EducationalApplication', 'inLanguage': list(LANGUAGES), 'image': f'{BASE}/images/lp/app-icon.webp', 'screenshot': [f'{BASE}/images/lp/{lang}/screen-{n:02}.webp' for n in [1, 2, 3, 6]], 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'JPY', 'description': d['storeNote']}, 'publisher': {'@type': 'Organization', 'name': 'TakeKApp', 'url': 'https://takekapp.com/'}}
    faq_schema = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in d['faqs']]}
    facts = ''.join(f'<div class="fact"><strong>{number}</strong><span>{e(label)}</span></div>' for number, label in zip([206, 8, 10], d['facts']))
    tabs = ''.join(f'''<button class="step-tab" type="button" role="tab" aria-selected="{str(n==0).lower()}" aria-controls="learning-screen" id="learning-tab-{n}" tabindex="{0 if n==0 else -1}" data-step="{n}" data-image="{ASSET}/{lang}/screen-{slot:02}.webp" data-alt="{e(d['screenshotAlt'][slot-1])}"><span class="step-number">0{n+1}</span><span><span class="step-title">{e(step['title'])}</span><span class="step-body">{e(step['body'])}</span></span></button>''' for n, (step, slot) in enumerate(zip(d['steps'], [1, 2, 5])))
    games = ''.join(f'<article class="game"><div class="game-number"><span>0{n+1}</span>{icon(n)}</div><h3>{e(title)}</h3><p>{e(body)}</p></article>' for n, (title, body) in enumerate(d['games']))
    world = ''.join(f'<div class="world-item"><h3>{e(title)}</h3><p>{e(body)}</p></div>' for title, body in d['worldItems'])
    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in d['faqs'])
    pills = ''.join(f'<a href="../{key}/landing_page_{key}.html" lang="{key}" hreflang="{key}">{e(label)}</a>' for key, label in LANGUAGES.items())
    policy_lang = 'ja' if lang == 'ja' else 'en'
    policy_suffix = '' if lang in ['ja', 'en'] else ' (English)'
    doc = f'''<!doctype html>
<html lang="{lang}" dir="ltr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d['title'])}</title><meta name="description" content="{e(d['description'])}"><meta name="theme-color" content="#f7f6ef">
<link rel="canonical" href="{canonical}">{alternate}<link rel="alternate" hreflang="x-default" href="{url('en')}">
<link rel="icon" type="image/webp" href="{ASSET}/app-icon.webp"><link rel="apple-touch-icon" href="{ASSET}/app-icon.webp">
<meta property="og:type" content="website"><meta property="og:site_name" content="{e(d['name'])}"><meta property="og:title" content="{e(d['title'])}"><meta property="og:description" content="{e(d['description'])}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}/images/lp/og/{lang}.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{e(d['name'])}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{BASE}/images/lp/og/{lang}.png"><meta name="twitter:title" content="{e(d['title'])}"><meta name="twitter:description" content="{e(d['description'])}"><meta name="apple-itunes-app" content="app-id=6757128485">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False).replace('</', '<\\/')}</script>
<script type="application/ld+json">{json.dumps(faq_schema, ensure_ascii=False).replace('</', '<\\/')}</script>
<link rel="stylesheet" href="../landing.css?v=20261102b"><script defer src="../landing.js?v=20261102b"></script>
<script>if(location.hostname==='takekapp.com'){{window.dataLayer=window.dataLayer||[];window.gtag=function(){{dataLayer.push(arguments)}};gtag('js',new Date());gtag('config','G-0VCS46ZTHC');var analytics=document.createElement('script');analytics.async=true;analytics.src='https://www.googletagmanager.com/gtag/js?id=G-0VCS46ZTHC';document.head.append(analytics);}}</script><script defer src="/js/app_store_analytics.js"></script>
</head><body>
<a class="skip" href="#main">{e(d['skip'])}</a>
<header class="site-header"><div class="shell header-inner"><a class="brand" href="landing_page_{lang}.html"><img src="{ASSET}/app-icon.webp" alt="" width="41" height="41"><span>{e(d['name'])}</span></a><nav class="header-nav" aria-label="{e(d['menuLabel'])}"><a href="#learn">{e(d['navLearn'])}</a><a href="#games">{e(d['navGames'])}</a><a href="#plans">{e(d['navPlans'])}</a></nav><div class="header-actions">{language_menu(lang,d)}<a class="button button-small" href="#download">{e(d['download'])}<span aria-hidden="true">↗</span></a></div></div></header>
<main id="main">
<section class="hero shell" aria-labelledby="hero-title"><div class="hero-copy reveal"><p class="hero-kicker">{e(d['heroEyebrow'])}</p><h1 id="hero-title">{h}</h1><p class="hero-lead">{lines(d['heroLead'])}</p><div class="hero-download">{stores(lang,d,'hero')}<p class="store-note">{e(d['storeNote'])}</p></div><a class="text-link hero-secondary" href="#learn">{e(d['heroSecondary'])}<span aria-hidden="true">↓</span></a></div><div class="hero-art reveal"><div class="orbit" aria-hidden="true"><div class="orbit-grid"></div></div>{screen(lang,d,1,'hero-phone-main',True)}{screen(lang,d,3,'hero-phone-secondary',True)}<div class="flag-postcard" aria-hidden="true"><img src="{ASSET}/flags/jp.svg" alt="" width="90" height="60"></div><div class="hero-seal">{e(d['heroSticker'])}</div><p class="art-caption">{e(d['heroCaption'])}</p></div></section>
<div class="shell facts">{facts}</div>
<section class="section shell" id="learn" aria-labelledby="learn-title"><div class="section-intro"><div><h2 id="learn-title">{lines(d['learnTitle'])}</h2></div><p class="lead">{e(d['learnLead'])}</p></div><div class="learning-layout"><div><div class="learning-display" id="learning-screen" role="tabpanel" aria-labelledby="learning-tab-0"><div class="phone"><img data-learning-image src="{ASSET}/{lang}/screen-01.webp" alt="{e(d['screenshotAlt'][0])}" width="820" height="1777" loading="lazy" decoding="async"></div></div><p class="record-note" data-record-note hidden>{e(d['recordNote'])}</p></div><div class="step-tabs" role="tablist" aria-label="{e(d['screenLabel'])}" aria-orientation="vertical">{tabs}</div></div></section>
<section class="section compare-section" aria-labelledby="compare-title"><div class="shell compare-layout"><div class="compare-copy"><h2 id="compare-title">{lines(d['compareTitle'])}</h2><p class="lead">{e(d['compareLead'])}</p></div><div class="sample" data-demo data-correct="{e(d['demoCorrect'])}" data-wrong="{e(d['demoWrong'])}" data-explanation="{e(d['demoExplanation'])}"><h3>{e(d['demoQuestion'])}</h3><div class="flag-options"><button class="flag-option" type="button" data-choice aria-pressed="false" aria-label="{e(d['demoChoices'][0])}"><img src="{ASSET}/flags/fr.svg" alt="" width="90" height="60"><span aria-hidden="true">A</span></button><button class="flag-option" type="button" data-choice aria-pressed="false" aria-label="{e(d['demoChoices'][1])}"><img src="{ASSET}/flags/it.svg" alt="" width="90" height="60"><span aria-hidden="true">B</span></button></div><div class="demo-answer" data-demo-answer aria-live="polite" aria-atomic="true" aria-label="{e(d['demoStatusLabel'])}">{e(d['demoInitial'])}</div><button class="demo-reveal" data-reveal type="button">{e(d['demoReveal'])}</button><button class="demo-reset" data-reset type="button" hidden>{e(d['demoReset'])}</button><p class="sample-note">{e(d['demoLabel'])}</p></div></div></section>
<section class="section shell" id="games" aria-labelledby="games-title"><div class="section-intro games-heading"><div><h2 id="games-title">{lines(d['gamesTitle'])}</h2></div><p class="lead">{e(d['gamesLead'])}</p></div><div class="game-grid">{games}</div></section>
<section class="section world-section" aria-labelledby="world-title"><div class="shell world-layout"><div class="world-gallery">{screen(lang,d,4)}{screen(lang,d,6)}</div><div class="world-copy"><h2 id="world-title">{lines(d['worldTitle'])}</h2>{world}<p class="small-note">{e(d['worldNote'])}</p></div></div></section>
<section class="section shell" id="plans" aria-labelledby="plans-title"><div class="plans-heading"><h2 id="plans-title">{lines(d['plansTitle'])}</h2></div><div class="plans"><article class="plan"><p class="plan-badge">{e(d['freeBadge'])}</p><h3>{e(d['freeTitle'])}</h3><ul>{''.join(f'<li>{e(t)}</li>' for t in d['freeItems'])}</ul><p class="plan-note">{e(d['freeNote'])}</p></article><article class="plan plan-plus"><p class="plan-badge">{e(d['plusBadge'])}</p><h3>{e(d['plusTitle'])}</h3><ul>{''.join(f'<li>{e(t)}</li>' for t in d['plusItems'])}</ul><p class="period">{e(d['planPeriod'])}</p><p class="trial">{e(d['trialNote'])}</p></article></div><p class="price-note">{e(d['priceNote'])}</p></section>
<section class="languages-section"><div class="shell languages-inner"><h2>{e(d['languagesTitle'])}</h2><div><p>{e(d['languagesBody'])}</p><div class="language-pills">{pills}</div></div></div></section>
<section class="section faq-section" id="faq" aria-labelledby="faq-title"><div class="shell faq-layout"><h2 id="faq-title">{e(d['faqTitle'])}</h2><div class="faq-list">{faq}</div></div></section>
<section class="closing" id="download" aria-labelledby="download-title"><div class="shell"><h2 id="download-title">{lines(d['closingTitle'])}</h2><p>{e(d['closingLead'])}</p>{stores(lang,d,'download')}<p class="store-note">{e(d['storeNote'])}</p></div></section>
</main><footer class="site-footer shell"><div class="footer-top"><a class="brand" href="landing_page_{lang}.html"><img src="{ASSET}/app-icon.webp" alt="" width="41" height="41"><span>{e(d['name'])}</span></a><nav class="footer-links" aria-label="{e(d['privacy']+' / '+d['terms'])}"><a href="../{policy_lang}/privacy_policy_{policy_lang}.html">{e(d['privacy']+policy_suffix)}</a><a href="../{policy_lang}/terms_and_conditions_{policy_lang}.html">{e(d['terms']+policy_suffix)}</a><a href="mailto:takekapp1990@gmail.com">{e(d['contact'])}</a><a href="/">{e(d['allApps'])} ↗</a></nav></div><div class="footer-bottom"><p>{e(d['footerNote'])}</p><span>© 2026 TakeKApp</span></div></footer>
</body></html>'''
    target = APP / lang / f'landing_page_{lang}.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding='utf-8')
    return target

if __name__ == '__main__':
    for lang in LANGUAGES:
        print(build(lang).relative_to(ROOT))
