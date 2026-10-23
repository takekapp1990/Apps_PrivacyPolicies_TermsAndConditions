"""Build the approved NumberPlaceHint LP in all 22 languages.

Japanese HTML is the editable layout. Japanese source strings and translated LP
copy are explicit catalogs; app names and common controls reuse existing sources.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse, html, json, re, shutil
from number_place_translations import PACKS as LEARNING
from number_place_lp_translations import PACKS, KEYS

ROOT=Path(__file__).resolve().parents[1]
LANGS=['ja','en','ar','da','de','es','fr','hi','id','it','ko','nl','pl','pt','ru','sv','th','tr','uk','vi','zh_CN','zh_TW']
TAGS={c:{'zh_CN':'zh-Hans','zh_TW':'zh-Hant'}.get(c,c) for c in LANGS}
STORE={c:{'en':'en-US','de':'de-DE','es':'es-ES','fr':'fr-FR','pt':'pt-BR','zh_CN':'zh-Hans','zh_TW':'zh-Hant'}.get(c,c) for c in LANGS}
SOURCE=json.loads((ROOT/'scripts/number_place_lp_ja.json').read_text())
PUZZLE='530070000600195000098000060800060003400803001700020006060000280000419005000080079'
esc=lambda s:html.escape(str(s),quote=True)


def common(code,app):
    m=LEARNING[code]; brand=app['appName']
    cell=m['cell'].format(row=5,col=5)
    copy=PACKS[code].copy()
    for i,k in {0:'skip',3:'contents',4:'aboutApp',5:'guide',6:'language',56:'notes',57:'check',70:'guide',73:'learn',75:'playTrial',77:'enjoy',82:'hint',83:'hint',84:'hintFallback',85:'hint',86:'reset',104:'guide',105:'related',106:'guide',109:'operator'}.items():copy[str(i)]=m[k]
    copy.update({'1':brand+' · '+m['aboutApp'],'2':brand,'12':'App Store / Google Play','13':'App Store','14':'Google Play','44':brand,'58':app['gameActionHighlight'],'59':app['gameModeProvisional'],'88':m['placeReason'].format(cell=cell,value=5)})
    for to,fr in [(17,16),(18,19),(20,21),(22,23),(24,25),(26,27),(48,21),(51,19),(54,23),(110,16)]:copy[str(to)]=copy[str(fr)]
    suffix=' (English)' if code!='en' else ''
    copy.update({'107':m['privacy']+suffix,'108':m['terms']+suffix})
    copy={k:v.replace('{brand}',brand) for k,v in copy.items()}
    assert set(copy)==set(SOURCE),(code,'Missing text',set(SOURCE)-set(copy))
    messages={'initialKicker':copy['83'],'initialReason':copy['84'],'hint':copy['85'],'reset':copy['86'],
      'candidateLabel':cell+', '+m['candidateLabel'].format(digits='5'), 'hintKicker':copy['19'],
      'hintReason':m['placeReason'].format(cell=cell,value=5),'place':m['step'],'placedLabel':cell+', 5, '+m['entered'],
      'appliedKicker':'5 · '+m['entered'],'appliedReason':copy['76'],'complete':'5 ✓',
      'resetLabel':cell+', '+m['empty']}
    return copy,m,messages


def ja_messages():
 return {'initialKicker':'どこから考える？','initialReason':'青枠のマスと同じ行・列・ブロックには、どの数字があるでしょう。','hint':'ヒントを見る','reset':'もう一度','candidateLabel':'5行5列、候補は5。まだ入力していません','hintKicker':'残る候補は、5だけ。','hintReason':'同じ行・列・ブロックには、1・2・3・4・6・7・8・9があります。このマスに入るのは、残った「5」です。','place':'5を入れてみる','placedLabel':'5行5列、5を入力しました','appliedKicker':'「5」が決まりました。','appliedReason':'こうして数字をひとつずつ絞り込んでいきます。続きを解きたいときは、体験版で1問遊んでみてください。','complete':'一手できました','resetLabel':'5行5列、空きマス、ヒントの対象'}


def grid(m):
 cells=[]
 for i,v in enumerate(PUZZLE):
  r,c=divmod(i,9);related=r==4 or c==4 or (r//3==1 and c//3==1)
  classes='preview-cell'+(' is-given' if v!='0' else '')+(' is-related' if related else '')+(' is-target' if i==40 else '')
  label=m['cell'].format(row=r+1,col=c+1)+', '+(v if v!='0' else m['empty'])
  cells.append(f'<span class="{classes}" aria-label="{esc(label)}"'+(' data-preview-cell' if i==40 else '')+'>'+('?' if i==40 else v if v!='0' else '')+'</span>')
 return '<div class="preview-grid" role="group" aria-label="'+esc(m['gameBoard'])+'">'+''.join(cells)+'</div>'


class Translator(HTMLParser):
 def __init__(self,code,copy,m,images):
  super().__init__(convert_charrefs=False);self.code=code;self.copy=copy;self.m=m;self.images=images;self.out=[]
  self.lookup={v:copy[k] for k,v in SOURCE.items()}
 def text(self,value):
  if value in self.lookup:return self.lookup[value]
  assert not re.search('[\u3040-\u30ff]',value),(self.code,'Untranslated Japanese',value)
  return value
 def attr(self,match):
  key,value=match.group(1),html.unescape(match.group(2))
  if key in ['alt','aria-label','title']:value=self.text(value)
  elif key in ['src','href']:
   value=value.replace('landing_page_ja.html',f'landing_page_{self.code}.html')
   if value=='privacy_policy_ja.html':value='../en/privacy_policy_en.html'
   if value=='terms_and_conditions_ja.html':value='../en/terms_and_conditions_en.html'
   if value.startswith('https://apps.apple.com/'):
    country={'en':'us','ar':'sa','da':'dk','hi':'in','ko':'kr','sv':'se','uk':'ua','zh_CN':'cn','zh_TW':'tw'}.get(self.code,self.code)
    value=f'https://apps.apple.com/{country}/app/id6758233715'
   if '/images/lp/ja/' in value:value=value.replace('/images/lp/ja/','/images/lp/'+self.code+'/')
   if value=='../images/screen_shots/ja/resized_slide_004.png':value=self.images[3]
   if '/badgeiOSAppStore/' in value:value='../../commonImages/badgeiOSAppStore/Download_on_the_App_Store_Badge_US-UK_RGB_blk_092917.svg'
   if '/badgeAndroid/' in value:value='../../commonImages/badgeAndroid/GetItOnGooglePlay_Badge_Web_color_English.png'
  return key+'="'+esc(value)+'"'
 def start(self):
  tag=re.sub(r'(alt|aria-label|title|href|src)="([^"]*)"',self.attr,self.get_starttag_text())
  if self.lasttag=='img' and '/badgeiOSAppStore/' in tag:tag=re.sub(r'width="\d+"','width="120"',tag)
  self.out.append(tag)
 def handle_starttag(self,t,a):self.start()
 def handle_startendtag(self,t,a):self.start()
 def handle_endtag(self,t):self.out.append('</'+t+'>')
 def handle_data(self,s):
  stripped=s.strip()
  if not stripped:self.out.append(s);return
  if stripped=='WEB DEMO':translated=self.m['example']
  else:translated=self.text(stripped)
  self.out.append(s.replace(stripped,esc(translated),1))
 def handle_entityref(self,n):self.out.append('&'+n+';')
 def handle_charref(self,n):self.out.append('&#'+n+';')
 def handle_comment(self,s):self.out.append('<!--'+s+'-->')


def head(code,title,description,image,brand):
 canonical=f'https://takekapp.com/NumberPlaceHint/{code}/landing_page_{code}.html'
 alternates=''.join(f'<link rel="alternate" hreflang="{TAGS[c]}" href="https://takekapp.com/NumberPlaceHint/{c}/landing_page_{c}.html">' for c in LANGS)
 schema={'@context':'https://schema.org','@type':'MobileApplication','name':brand,'url':canonical,'description':description,'applicationCategory':'EducationalApplication','operatingSystem':'Android, iOS','offers':{'@type':'Offer','price':'0','priceCurrency':'JPY'},'publisher':{'@type':'Organization','name':'TakeKApp','url':'https://takekapp.com/'}}
 return f'''<!DOCTYPE html>
<html lang="{TAGS[code]}" dir="{'rtl' if code=='ar' else 'ltr'}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title><link rel="icon" href="../favicon.ico"><meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">{alternates}<link rel="alternate" hreflang="x-default" href="https://takekapp.com/NumberPlaceHint/en/landing_page_en.html">
<meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:image" content="{esc(image)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{esc(image)}"><meta name="twitter:site" content="@takekapp">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0VCS46ZTHC"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-0VCS46ZTHC');</script>
<script defer src="/js/app_store_analytics.js"></script><link rel="stylesheet" href="../language_switcher.css">{('<link rel="stylesheet" href="../fonts/fonts.css">' if code=='ja' else '')}<link rel="stylesheet" href="../ja/landing-page.css?v=20261023-badges"><script defer src="../ja/landing-page.js?v=20261023"></script></head>
'''


def build(app_root):
 assert set(PACKS)==set(LANGS)-{'ja'}
 source=(ROOT/'NumberPlaceHint/ja/landing_page_ja.html').read_text()
 body=source[source.index('<body'):]
 body=re.sub(r'<script type="application/json" id="lp-messages">.*?</script>\s*','',body,flags=re.S)
 body=re.sub(r'<body[^>]*>','<body data-lp-redesign>',body,count=1)
 body=body.replace('src="../language_switcher.js"','src="../language_switcher.js?v=20261023"')
 base_grid=re.search(r'<div class="preview-grid".*?</div>',body,re.S).group(0)
 template=body.replace(base_grid,'__LP_GRID__')
 for code in LANGS:
  page=ROOT/f'NumberPlaceHint/{code}/landing_page_{code}.html';old=page.read_text()
  title=html.unescape(re.search(r'<title>(.*?)</title>',old,re.S).group(1))
  image=re.search(r'<meta property="og:image" content="([^"]+)"',old).group(1)
  app=json.loads((app_root/f'lib/l10n/app_{code}.arb').read_text())
  if code=='ja':
   rendered=body;messages=ja_messages();description=SOURCE['10']+' '+SOURCE['11']
  else:
   copy,m,messages=common(code,app)
   previous_images=re.findall(r'<img[^>]*src="([^\"]*screen_shots/[^\"]+)"',old)
   if len(previous_images)<4:
    # Already generated pages keep their localized theme as the fifth image.
    theme=re.search(r'src="([^\"]*screen_shots/[^\"]+)"',old).group(1)
    previous_images=['','','',theme]
   trans=Translator(code,copy,m,previous_images);trans.feed(template)
   rendered=''.join(trans.out).replace('__LP_GRID__',grid(m))
   description=copy['10']+' '+copy['11']
   target=ROOT/f'NumberPlaceHint/images/lp/{code}';target.mkdir(exist_ok=True)
   for number,name in [('01','hint-explanation'),('02','image-scan'),('03','technique-practice'),('06','gameplay')]:
    shutil.copyfile(app_root/f'ios/fastlane/screenshots/{STORE[code]}/{number}_IPHONE_67.png',target/(name+'.png'))
  rendered=rendered.replace('</body>','<script type="application/json" id="lp-messages">'+json.dumps(messages,ensure_ascii=False).replace('<','\\u003c')+'</script>\n</body>')
  page.write_text(head(code,title,description,image,app['appName'])+rendered)
 print('Built 22 localized landing pages, with 5 localized screenshots each.')


if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--app-root',type=Path,required=True)
 build(parser.parse_args().app_root)
