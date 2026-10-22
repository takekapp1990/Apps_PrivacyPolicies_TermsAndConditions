"""Read-only release checks for the 22 NumberPlaceHint landing pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,re
from build_number_place_landing import LANGS,TAGS,PUZZLE
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.links=[];self.h1=0;self.alternates={};self.text=[];self.ignore=0;self.messages=None;self.json_id=None;self.json_text='';self.cells=[];self.in_cell=False;self.cell='';self.images=[];self.tag='';self.direction=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.tag=a.get('lang');self.direction=a.get('dir')
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='img':self.images.append(a['src'])
  for k in ('href','src'):
   if k in a:self.links.append(a[k])
  if tag=='link' and a.get('rel')=='alternate':self.alternates[a['hreflang']]=a['href']
  if tag=='script':
   self.ignore+=1;self.json_id=a.get('id') if a.get('type')=='application/json' else None;self.json_text=''
  if tag=='span' and 'preview-cell' in a.get('class','').split():self.in_cell=True;self.cell=''
 def handle_data(self,d):
  if self.ignore:
   if self.json_id:self.json_text+=d
  else:self.text.append(d)
  if self.in_cell:self.cell+=d
 def handle_endtag(self,tag):
  if tag=='script':
   if self.json_id:self.messages=json.loads(self.json_text)
   self.ignore=max(0,self.ignore-1);self.json_id=None
  if tag=='span' and self.in_cell:self.cells.append(self.cell);self.in_cell=False
for code in LANGS:
 page=ROOT/f'NumberPlaceHint/{code}/landing_page_{code}.html';source=page.read_text();p=Page();p.feed(source)
 assert p.tag==TAGS[code] and p.direction==('rtl' if code=='ar' else 'ltr'),code
 assert p.h1==1 and len(p.ids)==len(set(p.ids)),code
 assert 'data-lp-redesign' in source and 'data-carousel-dots' in source
 assert len(p.alternates)==23,(code,'hreflang')
 assert source.count('data-carousel-item')==5,(code,'Screenshots')
 assert ''.join(v if v.isdigit() else '0' for v in p.cells)==PUZZLE,(code,'Demo board')
 assert p.messages and all(p.messages.values()),(code,'Demo messages')
 if code!='ja':
  assert not re.search('[\u3040-\u30ff]',''.join(p.text)),(code,'Japanese text leaked')
  assert not re.search('[\u3040-\u30ff]',json.dumps(p.messages,ensure_ascii=False)),(code,'Japanese runtime text leaked')
 for href in p.links:
  u=urlparse(href)
  if u.scheme or u.netloc:continue
  target=page if not u.path else ROOT/unquote(u.path.lstrip('/')) if u.path.startswith('/') else page.parent/unquote(u.path)
  if target.is_dir():target=target/'index.html'
  assert target.exists(),(code,href,'Missing dependency')
  if u.fragment:
   dest=Page();dest.feed(target.read_text());assert u.fragment in dest.ids,(code,href,'Broken anchor')
 for c in LANGS:assert p.alternates[TAGS[c]]==f'https://takekapp.com/NumberPlaceHint/{c}/landing_page_{c}.html'
 if code not in ('ja','en'):
  assert 'privacy_policy_en.html' in source and '(English)' in source,(code,'Legal-language disclosure')
css=(ROOT/'NumberPlaceHint/fonts/fonts.css').read_text()
for name in re.findall(r"url\('./([^']+)'\)",css):
 path=ROOT/'NumberPlaceHint/fonts'/name;assert path.exists() and path.read_bytes()[:4]==b'wOF2'
assert (ROOT/'NumberPlaceHint/fonts/OFL.txt').exists()
print('PASS: 22 locales, 110 localized screenshots, links, anchors, hreflang, RTL, messages, demo boards, legal labels and fonts.')
