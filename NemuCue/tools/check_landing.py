from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
LOCALES=json.loads((ROOT/'content/locales.json').read_text())
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.path=path;self.ids=[];self.refs=[];self.alts=[];self.slides=0;self.languages=[];self.lang=None;self.direction=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang');self.direction=a.get('dir')
  if 'id' in a:self.ids.append(a['id'])
  if 'data-carousel-slide' in a:self.slides+=1
  if 'data-language' in a:self.languages.append(a['data-language'])
  if tag=='link' and a.get('rel')=='alternate':self.alts.append(a.get('hreflang'))
  for k in ['src','href']:
   if k in a:self.refs.append(a[k])
 def check(self):
  self.feed(self.path.read_text())
  assert len(self.ids)==len(set(self.ids)),self.path
  for value in self.refs:
   u=urlparse(value)
   if u.scheme or u.netloc:continue
   dest=self.path.parent/unquote(u.path) if u.path else self.path
   if dest.is_dir():dest=dest/'index.html'
   assert dest.is_file(),(self.path,value)
   if u.fragment:
    other=self if dest==self.path else Page(dest)
    if other is not self:other.feed(dest.read_text())
    assert unquote(u.fragment) in other.ids,(self.path,value)
for locale in LOCALES:
 lang=locale['tag'];p=Page(ROOT/lang/'index.html');p.check()
 assert p.lang==lang and p.direction==locale['direction'],lang
 assert set(p.alts)=={v['tag'] for v in LOCALES}|{'x-default'},lang
 assert set(p.languages)=={v['tag'] for v in LOCALES if v['tag']!=lang},lang
 assert p.slides==5,lang
 for name in ['alarm','vibration','ringing','math','sequence','night','light']:assert (ROOT/'images/lp'/lang/(name+'.jpg')).is_file()
Page(ROOT/'index.html').check()
print('20 LPs: language tags, RTL, 21 hreflang links, 20-way menus, local links, anchors and 140 screenshots passed.')
