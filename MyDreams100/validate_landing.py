#!/usr/bin/env python3
"""Check local assets, navigation, SEO and store links for all localized landing pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--app-source", type=Path, help="Read-only app checkout, to verify original captures too")
args = parser.parse_args()

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []
        self.scripts = []
        self.in_json = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        self.in_json = tag == 'script' and attrs.get('type') == 'application/ld+json'

    def handle_data(self, data):
        if self.in_json:
            self.scripts.append(json.loads(data))

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_json = False


results = []
locales = json.loads((ROOT / 'MyDreams100/locales.json').read_text())
for locale in locales:
    lang = locale['code']
    path = ROOT / 'MyDreams100' / lang / f'landing_page_{lang}.html'
    text = path.read_text()
    page = Page()
    page.feed(text)
    elements = page.elements
    ids = [attrs['id'] for _, attrs in elements if 'id' in attrs]
    assert len(ids) == len(set(ids)), f'{lang}: duplicate anchor IDs'
    assert sum(tag == 'h1' for tag, _ in elements) == 1, f'{lang}: expected one h1'
    assert 'support' in ids, f'{lang}: missing support anchor'
    images = [attrs for tag, attrs in elements if tag == 'img']
    assert images and all('alt' in img and 'width' in img and 'height' in img for img in images)
    for tag, attrs in elements:
        for prop in ['href', 'src']:
            value = attrs.get(prop, '')
            if not value:
                continue
            target = urlparse(value)
            if target.scheme or target.netloc:
                continue
            if target.path:
                local = (ROOT / unquote(target.path.lstrip('/'))) if value.startswith('/') else (path.parent / unquote(target.path))
                assert local.is_file(), f'{lang}: missing {value}'
            elif target.fragment:
                assert target.fragment in ids, f'{lang}: missing anchor {value}'
        if 'srcset' in attrs:
            assert attrs.get('sizes'), f'{lang}: responsive image missing sizes'
            for entry in attrs['srcset'].split(','):
                image_path, width = entry.strip().split()
                assert width in {'390w', '780w'}, f'{lang}: unexpected responsive width'
                assert (path.parent / image_path).is_file(), f'{lang}: missing srcset image {image_path}'
    canonical = [a['href'] for tag, a in elements if tag == 'link' and a.get('rel') == 'canonical']
    assert canonical == [f'https://takekapp.com/MyDreams100/{lang}/landing_page_{lang}.html']
    alternates = {a.get('hreflang') for tag, a in elements if tag == 'link' and a.get('rel') == 'alternate'}
    assert alternates == {loc['tag'] for loc in locales} | {'x-default'}
    assert next(a['lang'] for tag, a in elements if tag == 'html') == locale['tag']
    alternate_urls = {a['hreflang']: a['href'] for tag, a in elements if tag == 'link' and a.get('rel') == 'alternate'}
    for loc in locales:
        assert alternate_urls[loc['tag']] == f"https://takekapp.com/MyDreams100/{loc['code']}/landing_page_{loc['code']}.html"
    language_links = [a for tag, a in elements if tag == 'a' and a.get('hreflang')]
    assert {a['hreflang'] for a in language_links} == {loc['tag'] for loc in locales}
    assert sum(a.get('aria-current') == 'page' for a in language_links) == 1
    links = [a.get('href', '') for tag, a in elements if tag == 'a']
    assert sum('apps.apple.com/' in v for v in links) == 2
    assert sum('play.google.com/store/apps/details?id=com.mydreams100.takekapp1990.prod' in v for v in links) == 2
    assert 'mailto:takekapp1990+mydreams100@gmail.com' in links
    assert sum('id6751042472' in v for v in links) == 2
    assert any('privacy_policy_' in v for v in links) and any('terms_and_conditions_' in v for v in links)
    assert '/js/app_store_analytics.js' in text and 'G-0VCS46ZTHC' in text
    assert len(page.scripts) == 1 and page.scripts[0]['@type'] == 'MobileApplication'
    assert page.scripts[0]['url'] == canonical[0]
    assert page.scripts[0]['inLanguage'] == [loc['tag'] for loc in locales]
    css_version = hashlib.sha256((ROOT / 'MyDreams100' / 'landing.css').read_bytes()).hexdigest()[:12]
    assert f'../landing.css?v={css_version}' in text, f'{lang}: stale CSS cache key'
    assert all(a.get('data-analytics-position') in {'hero', 'download'} for tag, a in elements if tag == 'a' and ('apps.apple.com/' in a.get('href', '') or 'play.google.com/' in a.get('href', '')))
    assert 'TODO' not in text and 'Lorem ipsum' not in text
    screens = [img for img in images if '/screens/' in img['src']]
    assert len(screens) == 5 and all(img['src'].endswith('.jpg') and 'srcset' in img for img in screens)
    results.append({'locale': lang, 'images': len(images), 'store_links': 4, 'anchors': len(ids), 'seo_and_assets': 'passed'})

css = (ROOT / 'MyDreams100' / 'landing.css').read_text()
assert css.count('{') == css.count('}')
assert 'prefers-reduced-motion' in css and ':focus-visible' in css
assert 'overflow-x:clip' in css, 'Hero decoration must not create horizontal page overflow'
manifest = json.loads((ROOT / 'MyDreams100/asset-provenance.json').read_text())
for asset in manifest['assets']:
    local = ROOT / 'MyDreams100/images' / asset['asset']
    assert hashlib.sha256(local.read_bytes()).hexdigest() == asset['sha256'], f"asset checksum mismatch: {local}"
for font in manifest.get('fonts', []):
    local = ROOT / 'MyDreams100' / font['asset']
    assert hashlib.sha256(local.read_bytes()).hexdigest() == font['sha256']
    assert (ROOT / 'MyDreams100' / font['license']).is_file()
screens = [a for a in manifest['assets'] if a['asset'].startswith('screens/')]
assert len(screens) == 20
for asset in screens:
    actual = ROOT / 'MyDreams100/images' / asset['asset']
    assert hashlib.sha256(actual.read_bytes()).hexdigest() == asset['sha256']
    if args.app_source:
        original = args.app_source / asset['source']
        assert hashlib.sha256(original.read_bytes()).hexdigest() == asset['source_sha256']
    assert asset['width'] in [390, 780] and asset['conversion']['crop'] is False
assert not list((ROOT / 'MyDreams100/images/screens').glob('*.png'))
print(json.dumps({'checks': results, 'responsive_derivatives_verified': len(screens),
                  'original_capture_hashes_verified': 10 if args.app_source else 0,
                  'optimization': manifest['optimization'],
                  'browser_visual_review': 'See MyDreams100/verification.json for separate browser QA', 'published': False}, ensure_ascii=False, indent=2))
