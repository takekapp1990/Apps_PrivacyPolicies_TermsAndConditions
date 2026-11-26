#!/usr/bin/env python3
"""Build localized LPs from current English markup and update language navigation.

Japanese/English body copy is edited in its own HTML. Missing translation text fails
explicitly when the English template changes. App-side files are never written.
"""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re
import struct
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
LOCALES = json.loads((ROOT / 'locales.json').read_text())
TRANSLATIONS = json.loads((ROOT / 'translations.json').read_text())
BY_CODE = {loc['code']: loc for loc in LOCALES}
TAGS = [loc['tag'] for loc in LOCALES]


def page_url(loc):
    return f"https://takekapp.com/MyDreams100/{loc['code']}/landing_page_{loc['code']}.html"


def language_menu(loc):
    links = ''.join(f'<a href="../{other["code"]}/landing_page_{other["code"]}.html" lang="{other["tag"]}" hreflang="{other["tag"]}"' + (' aria-current="page"' if other['code'] == loc['code'] else '') + f'>{escape(other["label"])}</a>' for other in LOCALES)
    return f'<details class="language-switcher"><summary aria-label="{loc["language"]}">{loc["short"]}<span aria-hidden="true">⌄</span></summary><nav aria-label="{loc["language"]}">{links}</nav></details>'


def wire_common(html, loc):
    html = re.sub(r'  <link rel="alternate" hreflang="[^\"]+" href="[^\"]+">\n', '', html)
    alternates = ''.join(f'  <link rel="alternate" hreflang="{other["tag"]}" href="{page_url(other)}">\n' for other in LOCALES)
    alternates += f'  <link rel="alternate" hreflang="x-default" href="{page_url(BY_CODE["en"])}">\n'
    html = re.sub(r'(  <link rel="canonical"[^>]+>\n)', lambda m: m[0]+alternates, html)
    html = re.sub(r'  <meta property="og:locale:alternate"[^>]+>\n', '', html)
    og = ''.join(f'  <meta property="og:locale:alternate" content="{other["og"]}">\n' for other in LOCALES if other['code'] != loc['code'])
    html = re.sub(r'(  <meta property="og:locale"[^>]+>\n)', lambda m: m[0]+og, html)
    share_image = f'https://takekapp.com/MyDreams100/images/ogp/{loc["code"]}.jpg'
    html = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]+("[^>]*>)',
                  lambda m: m[1] + share_image + m[2], html)
    html = re.sub(r'<details class="language-switcher">.*?</details>|<a class="language"[^>]*>.*?</a>', lambda _: language_menu(loc), html, flags=re.S)
    def schema(m):
        data = json.loads(m[1]); data['inLanguage'] = TAGS
        return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False)+'</script>'
    html = re.sub(r'<script type="application/ld\+json">(.*?)</script>', schema, html, flags=re.S)
    if loc['code'] in TRANSLATIONS:
        notice = TRANSLATIONS[loc['code']]['screen_language_notice']
        html = html.replace('<figcaption>', '<figcaption>'+escape(notice)+'<br>', 1)
    if loc['code'] not in ('ja', 'zh'):
        html = re.sub(r'(<p class="lead">.*?<br>)\s*', r'\1 ', html)
    version = hashlib.sha256((ROOT / 'landing.css').read_bytes()).hexdigest()[:12]
    return re.sub(r'landing.css\?v=[a-f0-9]+', 'landing.css?v='+version, html)


class Localize(HTMLParser):
    def __init__(self, loc, translation):
        super().__init__(convert_charrefs=True)
        self.loc = loc
        self.translation = translation
        self.out = []
        self.script_type = None
        self.in_script = False

    def handle_decl(self, decl): self.out.append('<!'+decl+'>')
    def handle_comment(self, comment): self.out.append('<!--'+comment+'-->')

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html': attrs['lang'] = self.loc['tag']
        if tag == 'script':
            self.in_script = True; self.script_type = attrs.get('type')
        title = self.translation['text']['My Dreams 100 — A bucket list that feels like you']
        if tag == 'meta':
            key = attrs.get('name', attrs.get('property'))
            if key in ('description', 'og:description', 'twitter:description'): attrs['content'] = self.translation['description']
            if key in ('og:title', 'twitter:title'): attrs['content'] = title
            if key == 'og:locale': attrs['content'] = self.loc['og']
            if key == 'og:url': attrs['content'] = page_url(self.loc)
            if key in ('og:image:alt', 'twitter:image:alt'): attrs['content'] = self.loc['name']
        if tag == 'link' and attrs.get('rel') == 'canonical': attrs['href'] = page_url(self.loc)
        for name in ('alt', 'aria-label'):
            value = attrs.get(name)
            if value:
                attrs[name] = self.translation['attributes'].get(value, self.translation['text'].get(value))
                assert attrs[name], f"Missing {self.loc['code']} attribute translation: {value}"
        if tag == 'a':
            href = attrs.get('href','')
            if 'apps.apple.com/' in href: attrs['href'] = f'https://apps.apple.com/{self.loc["country"]}/app/id6751042472'
            if 'play.google.com/' in href: attrs['href'] = href+'&hl='+self.loc['play']
            if href in ('terms_and_conditions_en.html','privacy_policy_en.html'): attrs['href'] = '../en/'+href
        if tag == 'img' and '/badges/' in attrs.get('src',''):
            store = 'apple' if 'apple-' in attrs['src'] else 'google'
            asset = ROOT / 'images/badges' / f'{store}-{self.loc["code"]}.{ "svg" if store=="apple" else "png"}'
            assert asset.is_file(), asset
            attrs['src'] = '../'+str(asset.relative_to(ROOT))
            if store == 'apple':
                svg = ET.parse(asset).getroot(); attrs['width'] = svg.attrib['width']; attrs['height'] = svg.attrib['height']
            else:
                width,height = struct.unpack('>II',asset.read_bytes()[16:24]);attrs.update(width=str(width),height=str(height),class_='badge-padded')
                attrs['class'] = attrs.pop('class_')
        self.out.append('<'+tag+''.join(' '+k+('="'+escape(v,quote=True)+'"' if v is not None else '') for k,v in attrs.items())+'>')

    def handle_endtag(self, tag):
        self.out.append('</'+tag+'>')
        if tag == 'script': self.in_script = False; self.script_type = None

    def handle_data(self, text):
        if self.in_script:
            if self.script_type == 'application/ld+json':
                data = json.loads(text);data.update(name=self.loc['name'],url=page_url(self.loc),description=self.translation['description'],inLanguage=TAGS);data['offers']['priceCurrency']=self.loc['currency'];text=json.dumps(data,ensure_ascii=False)
            self.out.append(text);return
        key = text.strip()
        if key:
            assert key in self.translation['text'], f"Missing {self.loc['code']} text translation: {key}"
            text = text.replace(key,self.translation['text'][key],1)
        self.out.append(escape(text,quote=False))


# Normalize the language picker before using the English body as the template.
source = (ROOT / 'en/landing_page_en.html').read_text()
source = re.sub(r'<details class="language-switcher">.*?</details>', '<a class="language" href="../ja/landing_page_ja.html" lang="ja" hreflang="ja">日本語</a>', source, flags=re.S)
for code,translation in TRANSLATIONS.items():
    loc = BY_CODE[code];renderer=Localize(loc,translation);renderer.feed(source)
    html = wire_common(''.join(renderer.out),loc)
    path = ROOT / code / f'landing_page_{code}.html';path.parent.mkdir(exist_ok=True);path.write_text(html)
for code in ('ja','en'):
    path = ROOT / code / f'landing_page_{code}.html';path.write_text(wire_common(path.read_text(),BY_CODE[code]))
print(f'Built {len(TRANSLATIONS)} localized pages; updated navigation and alternate URLs for all {len(LOCALES)} locales.')
