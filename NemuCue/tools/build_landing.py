from pathlib import Path
from html import escape as esc
import json, re

ROOT = Path(__file__).resolve().parents[1]
COPY = json.loads((ROOT / 'content/landing-copy.json').read_text())
LOCALES = json.loads((ROOT / 'content/locales.json').read_text())

def phone(lang, name, alt, eager=False):
    return f'<div class="phone"><img src="../images/lp/{lang}/{name}.jpg" alt="{esc(alt)}" width="640" height="1388" loading="{"eager" if eager else "lazy"}" {"fetchpriority=high" if eager else ""}></div>'

for locale in LOCALES:
    lang = locale['tag']
    c = COPY[lang]
    ctl = c['uiControls']
    (ROOT/lang).mkdir(exist_ok=True)
    language_menu = ''.join(f"<span lang='{item['tag']}' dir='auto' aria-current='true'>✓ {esc(item['name'])}</span>" if item['tag'] == lang else f"<a href='../{item['tag']}/index.html' lang='{item['tag']}' dir='auto' hreflang='{item['tag']}' data-language='{item['tag']}'>{esc(item['name'])}</a>" for item in LOCALES)
    alternates = ''.join(f"<link rel='alternate' hreflang='{item['tag']}' href='https://takekapp.com/NemuCue/{item['tag']}/index.html'>" for item in LOCALES) + '<link rel="alternate" hreflang="x-default" href="https://takekapp.com/NemuCue/">'
    apple_badge = 'Download_on_the_App_Store_Badge_JP_RGB_blk_100317.svg' if lang == 'ja' else 'Download_on_the_App_Store_Badge_US-UK_RGB_blk_092917.svg'
    play_badge = 'GetItOnGooglePlay_Badge_Web_color_Japanese.png' if lang == 'ja' else 'GetItOnGooglePlay_Badge_Web_color_English.png'
    apple_alt = 'App Storeからダウンロード' if lang == 'ja' else 'Download on the App Store'
    play_alt = 'Google Playで手に入れよう' if lang == 'ja' else 'Get it on Google Play'
    badges = f'''<div class="store-links"><a href="https://apps.apple.com/{'jp' if lang == 'ja' else 'us'}/app/id6827425453" class="store-badge"><img src="../../commonImages/badgeiOSAppStore/{apple_badge}" alt="{apple_alt}" width="{'109' if lang == 'ja' else '120'}" height="40"></a><a href="https://play.google.com/store/apps/details?id=com.takekapp1990.nemucue&amp;hl={lang}" class="store-badge"><img src="../../commonImages/badgeAndroid/{play_badge}" alt="{play_alt}" width="270" height="80"></a></div>'''
    nav = ''.join(f'<a href="#{target}">{label}</a>' for target,label in zip(['features','how','pricing','faq'],c['nav']))
    overview = ''.join(f'<a href="#{target}"><span>0{i+1}</span>{label}<b aria-hidden="true">↗</b></a>' for i,(target,label) in enumerate(zip(['features','reminders','stop'],c['overview'])))
    waves = ''.join(f'<div class="rhythm-row"><span>{label}</span><div class="pulses pulses-{i}" aria-hidden="true">'+''.join('<i></i>' for _ in range(12))+'</div></div>' for i,label in enumerate(c['rhythms']))
    steps = ''.join(f'<li><span>0{i+1}</span><div><h3>{title}</h3><p>{body}</p></div></li>' for i,(title,body) in enumerate(c['how']))
    rows = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{d}</td></tr>' for a,b,d in c['priceRows'])
    faq = ''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q,a in c['faq'])
    foot = ''.join(f'<a href="../{c["legalLang"]}/{target}.html" hreflang="{c["legalLang"]}">{label}</a>' for target,label in zip(['privacy','terms','support'],c['footer']))
    carousel_items = [('alarm', c['heroCaption']), ('ringing', c['ringingCaption']), ('vibration', c['vLabel']), ('math', c['math']), ('night', c['nightCaption'])]
    carousel_slides = ''.join(f'<div class="hero-slide{" is-active" if i == 0 else ""}" data-carousel-slide data-caption="{esc(label)}" role="group" aria-roledescription="{ctl[7]}" aria-label="{i+1} / {len(carousel_items)}" aria-hidden="{str(i != 0).lower()}"><img src="../images/lp/{lang}/{name}.jpg" alt="{esc(label)}" width="640" height="1388" decoding="async" {"fetchpriority=high" if i == 0 else ""}></div>' for i,(name,label) in enumerate(carousel_items))
    carousel_dots = ''.join(f'<button type="button" class="carousel-dot" data-carousel-dot aria-label="{esc(ctl[6])}: {esc(label)}" aria-pressed="{str(i == 0).lower()}"><span aria-hidden="true"></span></button>' for i,(_,label) in enumerate(carousel_items))
    page = f'''<!doctype html>
<html lang="{lang}" dir="{locale['direction']}">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, follow"><meta name="theme-color" content="#f7f2e9">
  <title>{esc(c['title'])}</title><meta name="description" content="{esc(c['description'])}">
  <link rel="canonical" href="https://takekapp.com/NemuCue/{lang}/index.html">
  {alternates}
  <meta property="og:type" content="website"><meta property="og:title" content="{esc(c['title'])}"><meta property="og:description" content="{esc(c['description'])}"><meta property="og:url" content="https://takekapp.com/NemuCue/{lang}/index.html"><meta property="og:image" content="https://takekapp.com/NemuCue/images/app_icon.png">
  <link rel="icon" href="../images/app_icon.png"><link rel="stylesheet" href="../landing.css"><script src="../language-router.js" defer></script><script src="../landing.js" defer></script>
</head>
<body id="top">
<a class="skip" href="#main">{c['skip']}</a>
<header class="header wrap">
  <a class="brand" href="./"><img src="../images/app_icon.png" width="40" height="40" alt=""><span>{esc(c['name'])}</span></a>
  <nav aria-label="{ctl[8]}">{nav}</nav>
  <details class="language-picker">
    <summary aria-label="{esc(ctl[0])}: {esc(locale['name'])}">{esc(locale['name'])}</summary>
    <div class="language-menu">{language_menu}</div>
  </details>
  <a class="header-cta" href="#download">{c['download']} <span aria-hidden="true">↗</span></a>
</header>
<main id="main">
  <section class="hero wrap" aria-labelledby="hero-title">
    <div class="hero-copy">
      <p class="category"><span aria-hidden="true"></span>{c['category']}</p>
      <h1 id="hero-title">{c['headline']}</h1>
      <p class="audience">{c['audience']}</p>
      {badges}
      <div class="actions"><a class="text-link" href="#features">{c['heroCta']} <span aria-hidden="true">↓</span></a></div>
    </div>
    <figure class="hero-visual" data-hero-carousel role="region" aria-roledescription="{ctl[7]}" aria-label="{ctl[1]}">
      <div class="hero-backdrop" aria-hidden="true"></div>
      <div class="phone carousel-phone"><div class="carousel-slides" data-carousel-viewport>{carousel_slides}</div></div>
      <figcaption><span data-carousel-caption aria-live="off" aria-atomic="true">{c['heroCaption']}</span></figcaption>
      <div class="carousel-controls" hidden>
        <button type="button" class="carousel-arrow" data-carousel-prev aria-label="{ctl[2]}">←</button>
        <div class="carousel-dots" role="group" aria-label="{ctl[6]}">{carousel_dots}</div>
        <button type="button" class="carousel-arrow" data-carousel-next aria-label="{ctl[3]}">→</button>
        <button type="button" class="carousel-rotation" data-carousel-rotation data-pause-label="{ctl[4]}" data-play-label="{ctl[5]}" aria-label="{ctl[4]}"><span aria-hidden="true">Ⅱ</span></button>
      </div>
    </figure>
  </section>
  <div class="overview wrap">{overview}</div>

  <section class="feature-section wrap" id="features">
    <div class="feature-copy"><p class="section-label"><span>01</span>{c['vLabel']}</p><h2>{c['vTitle']}</h2><p class="feature-benefit">{c['vBenefit']}</p><p>{c['vBody']}</p>
      <div class="rhythms" role="img" aria-label="{c['rhythm']}">{waves}</div><p class="small-note">{c['rhythm']}</p><p class="feature-foot">{c['vFoot']}</p>
    </div>
    <figure class="feature-image vibration-image">{phone(lang,'vibration',c['vLabel'])}</figure>
  </section>

  <section class="repeat-band" id="reminders"><div class="wrap repeat-grid">
    <div class="feature-copy"><p class="section-label"><span>02</span>{c['repeatLabel']}</p><h2>{c['repeatTitle']}</h2><p>{c['repeatBody']}</p><p class="feature-foot">{c['repeatFoot']}</p></div>
    <div class="repeat-diagram"><p class="diagram-title">{c['repeatDiagram']}</p><div class="repeat-start"><span aria-hidden="true">＋</span>{c['repeatSteps'][0]}</div>
      <div class="reminder-line" aria-hidden="true"></div><div class="reminder-nodes">{''.join(f'<div><span class="ring-symbol" aria-hidden="true">≋</span><strong>{s}</strong></div>' for s in [c['repeatCount'],c['repeatCount2'],c['repeatCount3']])}</div>
      <p class="repeat-end"><span aria-hidden="true">✓</span>{c['repeatSteps'][2]}</p><p class="small-note">{c['repeatDiagramNote']}</p>
    </div>
  </div></section>

  <section class="feature-section stop-section wrap" id="stop">
    <div class="feature-copy"><p class="section-label"><span>03</span>{c['stopLabel']}</p><h2>{c['stopTitle']}</h2><p>{c['stopBody']}</p><p class="feature-foot">{c['stopFoot']}</p></div>
    <div class="stop-images"><figure>{phone(lang,'math',c['math'])}<figcaption>{c['math']}</figcaption></figure><figure>{phone(lang,'sequence',c['sequence'])}<figcaption>{c['sequence']}</figcaption></figure></div>
  </section>

  <section class="night-band" id="how"><div class="wrap">
    <div class="night-grid"><div class="night-copy"><p class="section-label">{c['nightLabel']}</p><h2>{c['nightTitle']}</h2><p>{c['nightBody']}</p><ol class="steps">{steps}</ol></div><figure class="night-image">{phone(lang,'night',c['nightTitle'].replace('<br>',' '))}</figure></div>
    <aside class="iphone-note" id="iphone"><h3>{c['iosTitle']}</h3><p>{c['iosBody']}</p></aside>
    <aside class="schedule-note"><h3>{c['scheduleTitle']}</h3><p>{c['scheduleBody']}</p></aside>
  </div></section>

  <section class="feature-section relax-section wrap" id="sounds-light" aria-labelledby="relax-title">
    <div class="feature-copy"><p class="section-label">{c['relaxLabel']}</p><h2 id="relax-title">{c['relaxTitle']}</h2><p>{c['relaxBody']}</p>
      <div class="relax-details">
        <article><h3>{c['soundTitle']}</h3><p>{c['soundBody']}</p></article>
        <article><h3>{c['lightTitle']}</h3><p>{c['lightBody']}</p><ul class="light-colors">{''.join(f'<li><span class="light-color-{i}" aria-hidden="true"></span>{label}</li>' for i,label in enumerate(c['lightColors']))}</ul></article>
      </div><p class="feature-foot">{c['relaxFoot']}</p>
    </div>
    <figure class="feature-image light-image">{phone(lang,'light',c['relaxAlt'])}</figure>
  </section>

  <section class="pricing wrap" id="pricing"><div class="section-heading"><p class="section-label">{c['priceLabel']}</p><h2>{c['priceTitle']}</h2><p>{c['priceBody']}</p></div>
    <table><caption class="sr-only">{c['priceLabel']}</caption><thead><tr>{''.join(f'<th scope="col">{h}</th>' for h in c['priceHead'])}</tr></thead><tbody>{rows}</tbody></table><p class="price-foot">{c['priceFoot']}</p>
  </section>

  <section class="faq wrap" id="faq"><div class="section-heading"><p class="section-label">{c['nav'][3]}</p><h2>{c['faqTitle']}</h2></div><div class="faq-list">{faq}</div><a class="text-link" href="../{c['legalLang']}/support.html" hreflang="{c['legalLang']}">{c['support']} <span aria-hidden="true">↗</span></a></section>

  <section class="download-band" id="download"><div class="wrap download-content"><img src="../images/app_icon.png" width="64" height="64" alt=""><p class="section-label">{c['download']}</p><h2>{esc(c['downloadTitle'])}</h2><p>{c['downloadBody']}</p>
    {badges}<p class="download-note">{c['freeNote']}</p><p class="requirements">{c['requirements']}</p>
  </div></section>
</main>
<footer class="footer wrap"><a class="brand" href="#top">{esc(c['name'])}</a><div>{foot}</div><small>© 2026 TakeKApp</small><a class="back-top" href="#top" aria-label="{c['top']}">↑</a></footer>
</body></html>
'''
    if lang not in ['ja', 'zh-Hans', 'zh-Hant']:
        page = page.replace('<br>', '<br> ')
    page = re.sub(r'<p class="(?:feature-foot|small-note)"></p>', '', page)
    (ROOT/lang/'index.html').write_text(page)
print(f'Built {len(LOCALES)} localized landing pages.')
