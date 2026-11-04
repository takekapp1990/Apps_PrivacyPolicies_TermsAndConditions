from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
folder=root/'_ogp';folder.mkdir(exist_ok=True)
css='''
html{scroll-behavior:auto!important}body{width:1200px;height:800px;overflow:hidden;margin:0}
.skip,.header nav,.header .language-picker,.header .header-cta,.hero .actions,.hero figcaption,.hero .carousel-controls,main>section:not(.hero),main>.overview,.footer{display:none!important}
.header.wrap{width:880px;min-height:96px;height:96px;border:0;display:flex!important;flex-wrap:nowrap!important;padding:28px 0 0!important;margin:0 auto;gap:0!important}
.header .brand{font-size:20px!important;max-width:100%!important}.header .brand img{width:36px}
.hero.wrap{width:880px;height:704px;display:grid;grid-template-columns:1.1fr 1fr;align-items:center;gap:24px;padding:0 0 28px!important;margin:0 auto}
.hero .hero-copy{min-width:0;max-width:none}.hero .category{font-size:12px;line-height:1.7;letter-spacing:0}
.hero h1,html[lang=en] .hero h1,html:not([lang=ja]):not([lang=en]) .hero h1{font-size:48px!important;line-height:1.35!important;margin:22px 0!important;letter-spacing:-.035em}
.hero .audience,html[lang=en] .hero .audience,html:not([lang=ja]):not([lang=en]) .hero .audience{font-size:18px!important;line-height:1.8}
.hero .store-links{margin-top:25px;gap:14px}.hero .store-badge img{height:40px}
.hero .hero-visual{padding:0;max-width:none;width:100%}.hero .hero-visual .phone{width:245px;box-shadow:12px 18px 30px #52371b28}
.hero .hero-backdrop{inset:25px 12px 8px 12px}
html[lang=ja] .hero h1{font-size:62px!important}
html:lang(ar) .hero h1,html:lang(hi) .hero h1,html:lang(th) .hero h1{letter-spacing:normal!important;line-height:1.5!important}
'''
for locale in json.loads((root/'content/locales.json').read_text()):
 lang=locale['tag'];s=(root/lang/'index.html').read_text()
 s=re.sub(r'<script src="[^"]+" defer></script>','',s)
 s=s.replace('</head>',f'<style>{css}</style></head>')
 (folder/(lang+'.html')).write_text(s)
print('Prepared capture pages from the actual 20 LP KV sections.')
