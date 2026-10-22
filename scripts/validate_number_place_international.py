"""Read-only checks for every localized learning page and LP integration."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,re,xml.etree.ElementTree as ET
from number_place_translations import PACKS
from build_number_place_international import LANGS,TAGS,SLUGS,url
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.h1=0;self.attrs={};self.alternates={};self.canonical=None;self.metas={};self.option=0;self.text=[];self.selection=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.attrs=a
  if tag=='h1':self.h1+=1
  if 'id' in a:self.ids.append(a['id'])
  if tag=='link' and a.get('rel')=='alternate':self.alternates[a['hreflang']]=a['href']
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a['href']
  if tag=='meta':self.metas[a.get('name',a.get('property',''))]=a.get('content','')
  for name in ['href','src']:
   if name in a:self.links.append(a[name])
  if tag=='option':self.option+=1
  if tag=='select' and 'data-learning-language' in a:self.selection=True
 def handle_endtag(self,tag):
  if tag=='option':self.option-=1
 def handle_data(self,data):
  if not self.option:self.text.append(data)
def parse(path):
 p=Page();p.feed(path.read_text());return p
site=ET.parse(ROOT/'sitemap.xml');ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[x.text for x in site.findall('.//s:loc',ns)];assert len(urls)==len(set(urls))
count=0
for code in LANGS:
 for slug in SLUGS:
  file=ROOT/f'NumberPlaceHint/{code}/learn'/('index.html' if slug=='index' else slug+'.html')
  p=parse(file);assert p.h1==1,(file,'H1')
  assert len(p.ids)==len(set(p.ids)),(file,'duplicate ids')
  assert p.attrs['lang']==TAGS[code],file
  assert p.attrs.get('dir','ltr')==('rtl' if code=='ar' else 'ltr'),file
  assert p.canonical==url(code,slug),file
  assert p.metas.get('description') and p.metas.get('og:image'),file
  assert set(p.alternates)==set(TAGS.values())|{'x-default'},file
  for c,tag in TAGS.items():assert p.alternates[tag]==url(c,slug),(file,c)
  assert p.alternates['x-default']==url('en',slug),file
  assert p.selection,file
  assert url(code,slug) in urls,file
  for href in p.links:
   u=urlparse(href)
   if u.scheme or u.netloc:continue
   target=file if not u.path else ROOT/unquote(u.path.lstrip('/')) if u.path.startswith('/') else file.parent/unquote(u.path)
   if target.is_dir():target=target/'index.html'
   assert target.exists(),(file,href)
   if u.fragment:assert u.fragment in parse(target).ids,(file,href)
  if code!='ja':
   assert not re.search(r'[ぁ-ゖァ-ヺ]',''.join(p.text)),(file,'untranslated Japanese')
   assert not re.search(r'\{(?:candidate|row|col|value|count|total)\}',''.join(p.text)),(file,'unresolved placeholder')
  count+=1
 lp=ROOT/f'NumberPlaceHint/{code}/landing_page_{code}.html';s=lp.read_text()
 assert s.count('id="learning"')==1,(code,'LP entry')
 assert 'href="learn/"' in s,(code,'LP link')
 if 'data-lp-redesign' in s:
  assert '../ja/landing-page.js' in s and 'id="lp-messages"' in s and 'data-hint-preview' in s,(code,'LP hint preview')
 else:assert 'experience-browser.js' in s,(code,'LP demo')
 for name in ['experience-browser.js','learning-browser.js']:
  source=(lp.parent/'learn'/name).read_text();assert 'await fetch(' not in source,(code,name)
assert len(PACKS)==21
print(f'PASS: {count} pages / {len(LANGS)} languages; reciprocal hreflang, canonical URLs, metadata, links, anchors, RTL, localized copy, LP entries, and sitemap.')
