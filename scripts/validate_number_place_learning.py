"""Read-only structural checks for the NumberPlaceHint learning pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
LEARN=ROOT/'NumberPlaceHint/ja/learn'
class Parser(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.ids=[]; self.h1=0; self.meta={}; self.scripts=[]; self.current_json=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  for k in ['src','href']:
   if k in a:self.links.append(a[k])
  if tag=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if tag=='script' and a.get('type')=='application/ld+json':self.current_json=''
 def handle_data(self,d):
  if self.current_json is not None:self.current_json+=d
 def handle_endtag(self,tag):
  if tag=='script' and self.current_json is not None:self.scripts.append(json.loads(self.current_json));self.current_json=None
pages=sorted(LEARN.glob('*.html'));assert len(pages)==9
for page in pages:
 source=page.read_text();p=Parser();p.feed(source)
 assert p.h1==1,(page,'Exactly one H1')
 assert len(p.ids)==len(set(p.ids)),(page,'Duplicate ID')
 assert p.meta.get('description') and p.meta.get('og:image'),page
 assert p.scripts and p.scripts[0]['@type']=='BreadcrumbList'
 expected='https://takekapp.com/NumberPlaceHint/ja/learn/'+('' if page.name=='index.html' else page.name)
 assert f'rel="canonical" href="{expected}"' in source,page
 for href in p.links:
  u=urlparse(href)
  if u.scheme or u.netloc:continue
  target=page if not u.path else (ROOT/unquote(u.path.lstrip('/'))) if u.path.startswith('/') else page.parent/unquote(u.path)
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(page.name,href,'Broken local link')
  if u.fragment:
   t=Parser();t.feed(target.read_text());assert u.fragment in t.ids,(page.name,href,'Missing fragment')
 assert 'adsbygoogle' not in source
site=ET.parse(ROOT/'sitemap.xml'); ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[x.text for x in site.findall('.//s:loc',ns)]
assert len(urls)==len(set(urls))
for p in pages:assert 'https://takekapp.com/NumberPlaceHint/ja/learn/'+('' if p.name=='index.html' else p.name) in urls
lp=(ROOT/'NumberPlaceHint/ja/landing_page_ja.html').read_text();assert lp.count('id="learning"')==1
assert 'href="learn/"' in lp
print('PASS: 9 HTML pages, local links and fragments, metadata, breadcrumbs, sitemap, LP entry, and no ads.')
