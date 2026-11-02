"""Check LP links, metadata, localized page structure, and share assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / 'FlagMemoryAwaAwaPon'
spec = importlib.util.spec_from_file_location('flag_lp_build', ROOT / 'scripts/build_flag_memory_landing.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]; self.links=[]; self.images=[]; self.alternates={}; self.store_links=[]; self.canonical=None; self.h1=0; self.lang=None; self.schema=[]; self.in_json=False; self.buffer=[]; self.text=[]
    def handle_starttag(self, tag, attributes):
        a=dict(attributes)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='a' and a.get('href'):
            self.links.append(a['href'])
            if urlsplit(a['href']).netloc in ['apps.apple.com','play.google.com']:self.store_links.append(a)
        if tag=='img':self.images.append(a);assert 'alt' in a,'Missing img alt'
        if tag=='link':
            if a.get('rel')=='alternate':self.alternates[a.get('hreflang')]=a.get('href')
            if a.get('rel')=='canonical':self.canonical=a.get('href')
            if a.get('rel')=='stylesheet':self.links.append(a['href'])
        if tag=='script':
            if a.get('src'):self.links.append(a['src'])
            self.in_json=a.get('type')=='application/ld+json';self.buffer=[]
    def handle_endtag(self,tag):
        if tag=='script' and self.in_json:
            self.schema.append(json.loads(''.join(self.buffer)));self.in_json=False
    def handle_data(self,data):
        self.text.append(data)
        if self.in_json:self.buffer.append(data)

def local_url(value, page):
    u=urlsplit(value)
    if u.scheme and u.scheme not in ['http','https']:return None,u.fragment
    if u.netloc and u.netloc!='takekapp.com':return None,u.fragment
    if not u.path:return page,u.fragment
    p=ROOT/unquote(u.path.lstrip('/')) if u.path.startswith('/') or u.netloc else page.parent/unquote(u.path)
    p=p.resolve()
    if p.is_dir():p=p/'index.html'
    return p,u.fragment

def main():
    files=list(APP.glob('*/*.html'))
    for file in files:
        page=Page();page.feed(file.read_text())
        assert page.h1==1,(file,'h1 count',page.h1)
        assert len(page.ids)==len(set(page.ids)),(file,'duplicate ids')
        assert page.lang==file.parent.name,(file,'lang mismatch')
        assert page.canonical==f'https://takekapp.com/{file.relative_to(ROOT).as_posix()}',(file,'canonical')
        for link in page.links+[i['src'] for i in page.images]:
            target,fragment=local_url(link,file)
            if target is None:continue
            assert target.exists(),(file,link,'missing file')
            if fragment:
                t=page if target==file.resolve() else Page()
                if target!=file.resolve():t.feed(target.read_text())
                assert fragment in t.ids,(file,link,'missing fragment')
        if file.name.startswith('landing_page_'):
            assert set(page.alternates)==set(builder.LANGUAGES)|{'x-default'},(file,'hreflang')
            assert len(page.schema)==2,(file,'schema')
            assert page.schema[0]['inLanguage']==list(builder.LANGUAGES)
            assert len(page.schema[1]['mainEntity'])==6
            assert len([x for x in page.links if 'apps.apple.com' in x])==2
            apple_links=[x for x in page.links if urlsplit(x).netloc=='apps.apple.com']
            expected_apple=builder.app_store_url(page.lang)
            assert apple_links==[expected_apple]*2,(file,'localized App Store links',apple_links)
            assert len([x for x in page.links if 'play.google.com' in x])==2
            for position in ['hero','download']:
                links=[a for a in page.store_links if a.get('data-analytics-position')==position]
                assert {urlsplit(a['href']).netloc for a in links}=={'apps.apple.com','play.google.com'},(file,position,'store links')
            assert (APP/f'images/lp/og/{page.lang}.png').exists()
    assert 'Lerne Weltflaggen' not in (APP/'es/landing_page_es.html').read_text()
    ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
    sitemap=ET.parse(ROOT/'sitemap.xml')
    urls={e.text for e in sitemap.findall('.//s:loc',ns)}
    for file in files:assert f'https://takekapp.com/{file.relative_to(ROOT).as_posix()}' in urls
    print(f'PASS: {len(files)} HTML pages, 10 LP locales, localized App Store links, metadata, internal links/fragments, assets, sitemap, schema and Spanish copy')

if __name__=='__main__':main()
