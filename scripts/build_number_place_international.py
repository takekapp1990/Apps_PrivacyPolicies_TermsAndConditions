"""Build all 22 learning locales, using app ARB explanations and web copy catalogs."""
from pathlib import Path
import html,json,re,sys,xml.etree.ElementTree as ET
from number_place_translations import PACKS,LABEL_KEYS,TEXT_KEYS,MESSAGE_KEYS
from number_place_experience_content import DEMO,PUZZLE,grid
from number_place_runtime_i18n import compile_bundles
LANGS={'ja':'日本語','en':'English','ar':'العربية','da':'Dansk','de':'Deutsch','es':'Español','fr':'Français','hi':'हिन्दी','id':'Bahasa Indonesia','it':'Italiano','ko':'한국어','nl':'Nederlands','pl':'Polski','pt':'Português','ru':'Русский','sv':'Svenska','th':'ไทย','tr':'Türkçe','uk':'Українська','vi':'Tiếng Việt','zh_CN':'简体中文','zh_TW':'繁體中文'}
TAGS={k:({'zh_CN':'zh-Hans','zh_TW':'zh-Hant'}.get(k,k)) for k in LANGS}
SLUGS=['index','enjoy','brain-training','play','candidate-notes','naked-single','hidden-single','naked-pairs','locked-candidates']
BASE='https://takekapp.com/NumberPlaceHint/'
def esc(value):return html.escape(str(value),quote=True)
def para(value):return '<p>'+esc(value)+'</p>'
def url(code,slug):return BASE+code+'/learn/'+('' if slug=='index' else slug+'.html')
def alternates(slug):return ''.join(f'<link rel="alternate" hreflang="{tag}" href="{url(code,slug)}">' for code,tag in TAGS.items())+f'<link rel="alternate" hreflang="x-default" href="{url("en",slug)}">'
def picker(code,slug,m):
 filename='' if slug=='index' else slug+'.html'
 return '<label class="learning-language">'+esc(m['language'])+' <select data-learning-language aria-label="'+esc(m['language'])+'">'+''.join(f'<option lang="{TAGS[c]}" value="../../{c}/learn/{filename}"'+(' selected' if c==code else '')+'>'+esc(name)+'</option>' for c,name in LANGS.items())+'</select></label>'
def demo(m,id='home-demo'):
 controls=''.join(f'<button type="button" class="xp-button {"" if action=="play" else "xp-secondary"}" data-action="{action}">{esc(m[key])}</button>' for action,key in [('play','play'),('step','step'),('reset','reset')])
 options='<label>'+esc(m['style'])+' <select data-setting="style">'+''.join(f'<option value="{v}">{esc(m[k])}</option>' for v,k in [('standard','standard'),('sparkle','sparkle'),('neon','neon'),('zen','zen')])+'</select></label>'
 options+='<label>'+esc(m['speed'])+' <select data-setting="speed">'+''.join(f'<option value="{v}"'+(' selected' if v==850 else '')+'>'+esc(m[k])+'</option>' for v,k in [(1400,'slow'),(850,'normal'),(350,'fast')])+'</select></label>'
 options+='<label><input type="checkbox" data-setting="effects" checked>'+esc(m['effects'])+'</label>'
 return f'<div class="sudoku-experience xp-demo" id="{id}" data-demo data-style="standard"><p class="xp-caption">{esc(m["demoCaption"])}</p><div class="xp-controls">{controls}</div><div class="xp-stage"><div class="experience-grid" role="group" aria-label="{esc(m["gameBoard"])}">{grid(DEMO)}</div><div class="xp-effects" aria-hidden="true"></div></div><p class="xp-status" role="status">{esc(m["demoFoot"])}</p><div class="xp-options">{options}</div><p class="xp-small">{esc(m["demoFoot"])}</p></div>'
def cta(m,apple):
 return f'<section class="app-cta" id="continue"><h2>{esc(m["appHeading"])}</h2>{para(m["appText"])}<p class="fine">{esc(m["premium"])}</p><div class="store-links"><a class="button" data-analytics-position="learning_footer" href="{esc(apple)}">App Store ↗</a><a class="button secondary" data-analytics-position="learning_footer" href="https://play.google.com/store/apps/details?id=com.NumberPlaceHint.takekapp1990.prod">Google Play ↗</a></div><a class="text-link" href="../landing_page_'+m['code']+'.html">'+esc(m['aboutApp'])+' →</a></section>'
def shell(m,slug,title,description,body,apple,image):
 code=m['code'];canonical=url(code,slug);lp=BASE+code+'/landing_page_'+code+'.html'
 schema={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':m['aboutApp'],'item':lp},{'@type':'ListItem','position':2,'name':m['guide'],'item':url(code,'index')}]+([] if slug=='index' else [{'@type':'ListItem','position':3,'name':title,'item':canonical}])}
 legal='en';suffix=' (English)' if code!='en' else ''
 return f'''<!doctype html><html lang="{TAGS[code]}" dir="{'rtl' if code=='ar' else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} | {esc(m['brand'])}</title><meta name="description" content="{esc(description)}"><link rel="canonical" href="{canonical}">{alternates(slug)}<link rel="icon" href="../../favicon.ico"><meta property="og:type" content="{'website' if slug=='index' else 'article'}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{image}"><meta name="twitter:card" content="summary_large_image"><link rel="stylesheet" href="../../ja/learn/learning.css"><link rel="stylesheet" href="../../ja/learn/experience.css"><link rel="stylesheet" href="../../learning-locales/international.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><script async src="https://www.googletagmanager.com/gtag/js?id=G-0VCS46ZTHC"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-0VCS46ZTHC');</script><script defer src="../../../js/app_store_analytics.js"></script><script defer src="../../learning-locales/language-navigation.js"></script><script defer src="learning-browser.js"></script><script defer src="experience-browser.js"></script></head><body data-article="{slug}" data-learning-locale="{code}"><a class="skip" href="#main">{esc(m['skip'])}</a><header class="masthead"><a class="brand" href="./"><img src="../../images/app_icon/number_place_hint_app_icon_10241024_ios.png" alt="" width="36" height="36">{esc(m['brand'])}</a><nav aria-label="{esc(m['guide'])}"><a href="play.html">{esc(m['playTrial'])}</a><a href="./#guides">{esc(m['learn'])}</a><a href="../landing_page_{code}.html">{esc(m['aboutApp'])} ↗</a></nav>{picker(code,slug,m)}</header><main id="main"><nav class="breadcrumbs" aria-label="{esc(m['guide'])}"><a href="../landing_page_{code}.html">{esc(m['aboutApp'])}</a><span aria-hidden="true">/</span><a href="./">{esc(m['guide'])}</a>{'' if slug=='index' else '<span aria-hidden="true">/</span><span aria-current="page">'+esc(title)+'</span>'}</nav>{body}</main><footer class="footer"><a href="./">{esc(m['guide'])}</a><a href="../../en/privacy_policy_en.html">{esc(m['privacy']+suffix)}</a><a href="../../en/terms_and_conditions_en.html">{esc(m['terms']+suffix)}</a><a href="../../../about.html">{esc(m['operator'])}</a><a href="../../../index.html">TakeKApp</a><p>© TakeKApp</p></footer></body></html>'''
def heading(title,sub):return '<header class="article-header"><h1>'+esc(title)+'</h1><p class="lead">'+esc(sub)+'</p><p class="byline">TakeKApp · <time datetime="2026-10-21">2026-10-21</time></p></header>'
def figure(slug,m):
 cells={'candidate-notes':['1','2','□','4','5','6','□','8','□'],'naked-single':['1','2','<b>3</b>','4','5','6','7','8','9'],'hidden-single':['1','<small>2 4</small>','3','<small>2 4 9</small>','<small>2 <b>7</b> 9</small>','5','6','8','<small>2 9</small>'],'naked-pairs':['1','2','<small>3 7</small>','4','<small>3 7</small>','6','8','<small><s>3</s> 5 <s>7</s></small>','9']}
 if slug=='locked-candidates':return '<figure class="unit-figure"><table class="pointing"><caption>'+esc(m['example'])+' · 5</caption><tbody>'+''.join('<tr><th scope="row">'+esc(m['rowUnit'].replace('{n}',str(r+1)))+'</th>'+''.join('<td'+(' class="pattern"' if r==0 and c!=1 else '')+'>'+('5' if r==0 and c!=1 else '—')+'</td>' for c in range(3))+'</tr>' for r in range(3))+'</tbody></table><figcaption>'+esc(m['lockedWarning'])+'</figcaption></figure>'
 marked={'naked-single':[2],'hidden-single':[4],'naked-pairs':[2,4]}.get(slug,[])
 return '<figure class="unit-figure"><div class="unit" dir="ltr">'+''.join('<div class="unit-cell'+(' pattern' if i in marked else '')+'">'+v+'</div>' for i,v in enumerate(cells[slug]))+'</div><figcaption>'+esc(m['example'])+' · '+esc(m[{'candidate-notes':'notesWarning','naked-single':'singleWarning','hidden-single':'hiddenWarning','naked-pairs':'pairWarning'}[slug]])+'</figcaption></figure>'
def game(m):
 opt='<div class="xp-options"><label><input type="checkbox" data-setting="notes">'+esc(m['notes'])+'</label><label><input type="checkbox" data-setting="effects" checked>'+esc(m['effects'])+'</label><label>'+esc(m['style'])+' <select data-setting="style">'+''.join(f'<option value="{v}">{esc(m[v])}</option>' for v in ['standard','sparkle','neon','zen'])+'</select></label></div>'
 return '<div class="sudoku-experience xp-game" data-game data-style="standard">'+opt+'<div class="xp-stage"><div class="experience-grid" role="group" aria-label="'+esc(m['gameBoard'])+'">'+grid(PUZZLE)+'</div><div class="xp-effects" aria-hidden="true"></div></div><p class="xp-status" role="status">'+esc(m['chooseCell'])+'</p><div class="xp-keypad" role="group" aria-label="'+esc(m['answerDigits'])+'">'+''.join(f'<button type="button" data-digit="{n}" aria-label="{n}">{n}</button>' for n in range(1,10))+'</div><div class="xp-controls">'+''.join(f'<button type="button" class="xp-button {"" if action=="hint" else "xp-secondary"}" data-action="{action}">{esc(m[key])}</button>' for action,key in [('hint','hint'),('erase','erase'),('undo','undo'),('reset','reset')])+'</div><div class="xp-clear" hidden><h2>'+esc(m['gameComplete'])+'</h2><a href="#continue">'+esc(m['appHeading'])+' →</a></div><p class="xp-small">'+esc(m['keyboard'])+'</p></div>'
def build(root,app_root):
 source=root/'NumberPlaceHint/ja/learn';shared=root/'NumberPlaceHint/learning-locales';shared.mkdir(exist_ok=True)
 assert set(PACKS)==set(LANGS)-{'ja'},('Missing locales',set(LANGS)-{'ja'}-set(PACKS))
 expected_placeholders=lambda s:set(re.findall(r'\{(\w+)\}',s))
 for code,pack in PACKS.items():
  for key in LABEL_KEYS+TEXT_KEYS+MESSAGE_KEYS:assert expected_placeholders(pack[key])==expected_placeholders(PACKS['en'][key]),(code,key)
 for code in LANGS:
  if code=='ja':continue
  m={**PACKS[code],'code':code}
  app=json.loads((app_root/f'lib/l10n/app_{code}.arb').read_text());exp=json.loads((app_root/f'lib/l10n/src/explanations_{code}.arb').read_text());screens=json.loads((app_root/f'lib/l10n/src/screens_{code}.arb').read_text())
  m.update(brand=app['appName'],hiddenGeneric=exp['techniqueHiddenSinglePage2'],rowUnit=app['completionRow']+' {n}',colUnit=app['completionColumn']+' {n}',blockUnit=app['completionBlock']+' {n}',clearLabel=app['celebrationMessage'],groupLabel=app['celebrationMessage'])
  if code=='zh_TW':m.update(rowUnit='列 {n}',colUnit='欄 {n}',blockUnit='宮 {n}')
  lp=root/f'NumberPlaceHint/{code}/landing_page_{code}.html';lptext=lp.read_text();apple_match=re.search(r'href="(https://apps.apple.com/[^\"]+)"',lptext);apple=html.unescape(apple_match.group(1)) if apple_match else 'https://apps.apple.com/us/app/sudoku-hint/id6758233715'
  image=re.search(r'<meta property="og:image" content="([^\"]+)"',lptext).group(1)
  out=root/f'NumberPlaceHint/{code}/learn';out.mkdir(exist_ok=True)
  topics=[('candidate-notes',screens['sudokuGuideItemCandidateNotesTitle'],screens['sudokuGuideItemCandidateNotesSummary'],[exp['sudokuGuideCandidateNotesPage1'],exp['sudokuGuideCandidateNotesPage2'],exp['sudokuGuideUpdateAfterConfirmPage1']],'notesWarning'),('naked-single',exp['techniqueNakedSingleTitle'],exp['techniqueNakedSinglePage1'],[exp[f'techniqueNakedSinglePage{i}'] for i in range(1,4)],'singleWarning'),('hidden-single',exp['techniqueHiddenSingleTitle'],exp['techniqueHiddenSinglePage1'],[exp[f'techniqueHiddenSinglePage{i}'] for i in range(1,3)],'hiddenWarning'),('naked-pairs',exp['reductionNakedPairsTitle'],exp['reductionNakedPairsPage1'],[exp[f'reductionNakedPairsPage{i}'] for i in range(1,4)],'pairWarning'),('locked-candidates',exp['techniqueLockedCandidatesTitle'],exp['techniqueLockedCandidatesPage1_1'],[exp[f'techniqueLockedCandidatesPage{i}_{j}'] for i in [1,2] for j in [1,2,3]],'lockedWarning')]
  cards=''.join(f'<a class="guide-card" href="{slug}.html"><span class="card-number">0{i+1}</span><div><h3>{esc(title)}</h3>{para(sub)}</div><span aria-hidden="true">↗</span></a>' for i,(slug,title,sub,_,_) in enumerate(topics))
  body='<section class="experience-hero"><div><p class="eyebrow">'+esc(m['guide'])+'</p><h1>'+esc(m['hero'])+'</h1><p class="lead">'+esc(m['intro'])+'</p><div class="hero-actions"><a class="button" href="play.html">'+esc(m['playTrial'])+' →</a><a href="enjoy.html">'+esc(m['enjoy'])+'</a></div></div>'+demo(m)+'</section><nav class="path-nav" aria-label="'+esc(m['guide'])+'">'+''.join('<a href="'+href+'"><b>'+esc(m[key])+'</b></a>' for href,key in [('enjoy.html','enjoy'),('play.html','playTrial'),('#guides','learn')])+'</nav><section class="reading-note"><h2>'+esc(m['rulesHeading'])+'</h2>'+para(m['enjoyIntro'])+'<a href="enjoy.html">'+esc(m['enjoy'])+' →</a></section><section class="brain-intro"><h2>'+esc(m['brain'])+'</h2>'+para(m['brainIntro'])+'<a href="brain-training.html">'+esc(m['brain'])+' →</a></section><section id="guides"><div class="section-heading"><h2>'+esc(m['learn'])+'</h2>'+para(m['practiceIntro'])+'</div><div class="guide-list">'+cards+'</div></section>'+cta(m,apple)
  (out/'index.html').write_text(shell(m,'index',m['hero'],m['intro'],body,apple,image))
  for slug,title,sub,paragraphs,warning in topics:
   content='<h2 id="condition">'+esc(m['how'])+'</h2>'+''.join(para(p) for p in paragraphs)+'<h2 id="example">'+esc(m['example'])+'</h2>'+figure(slug,m)+'<h2 id="mistakes">'+esc(m['mistakes'])+'</h2>'+para(m[warning])
   if slug in ['naked-single','naked-pairs']:
    content+='<section id="practice" class="practice" data-technique="'+slug+'" aria-labelledby="practice-title"><p class="eyebrow">'+esc(m['practice'])+' · 2</p><h2 id="practice-title">'+esc(title)+' · '+esc(m['practice'])+'</h2>'+para(m['nakedPrompt' if slug=='naked-single' else 'pairPrompt'])+'<div class="practice-mount">'+para(m['practiceIntro'])+'</div></section>'
   content+='<section class="related"><h2>'+esc(m['related'])+'</h2>'+''.join('<a href="'+s+'.html">'+esc(t)+' →</a>' for s,t,*_ in topics if s!=slug)+'</section>'
   toc='<aside class="toc"><p>'+esc(m['contents'])+'</p><nav>'+''.join('<a href="#'+id+'">'+esc(m[key])+'</a>' for id,key in [('condition','how'),('example','example'),('mistakes','mistakes')])+('</nav></aside>')
   body=heading(title,sub)+'<div class="article-layout">'+toc+'<article class="article-body">'+content+'</article></div>'+cta(m,apple)
   (out/(slug+'.html')).write_text(shell(m,slug,title,sub,body,apple,image))
  enjoy='<article class="experience-article article-body">'+para(m['enjoyIntro'])+demo(m,'enjoy-demo')+'<h2 id="chain">'+esc(m['chainHeading'])+'</h2>'+para(m['chainText'])+'<h2 id="progress">'+esc(m['progressHeading'])+'</h2>'+para(m['progressText'])+'<a class="button" href="play.html">'+esc(m['playTrial'])+' →</a></article>'
  brain='<article class="experience-article article-body">'+para(m['brainIntro'])+'<h2 id="research">'+esc(m['researchHeading'])+'</h2>'+para(m['researchText'])+'<p><a href="https://pubmed.ncbi.nlm.nih.gov/30746778/">Brooker et al., 2019 · PubMed</a></p><h2 id="limits">'+esc(m['limitsHeading'])+'</h2>'+para(m['limitsText'])+'<p><a href="https://news-archive.exeter.ac.uk/2019/may/title_716265_en.html">University of Exeter · 2019</a></p>'+para(m['habitText'])+'<a class="button" href="play.html">'+esc(m['playTrial'])+' →</a></article>'
  play='<article class="experience-article article-body">'+para(m['playIntro'])+game(m)+para(m['practiceIntro'])+'<a href="naked-single.html#practice">'+esc(topics[1][1])+' →</a></article>'
  for slug,title,desc,content in [('enjoy',m['enjoy'],m['enjoyIntro'],enjoy),('brain-training',m['brain'],m['brainIntro'],brain),('play',m['playTrial'],m['gameFoot'],play)]:
   (out/(slug+'.html')).write_text(shell(m,slug,title,desc,heading(title,desc)+content+cta(m,apple),apple,image))
  compile_bundles(source,m,out)
  # Redesigned LPs are maintained by build_number_place_landing.py.
  if 'data-lp-redesign' not in lptext:
   # Add one bounded section, preserving every existing LP edit outside the marker.
   lptext=re.sub(r'<!-- sudoku-learning:start -->.*?<!-- sudoku-learning:end -->\s*','',lptext,flags=re.S)
   section='<!-- sudoku-learning:start --><section class="container" id="learning"><h2>'+esc(m['guide'])+'</h2>'+para(m['intro'])+demo(m,'lp-demo')+'<p><a class="btn-secondary" href="learn/">'+esc(m['hero'])+' →</a></p></section><!-- sudoku-learning:end -->\n'
   lptext=lptext.replace('</main>',section+'</main>',1)
   deps='<link rel="stylesheet" href="../ja/learn/experience.css"><link rel="stylesheet" href="../learning-locales/international.css"><script defer src="learn/experience-browser.js"></script>'
   if 'src="learn/experience-browser.js"' not in lptext:lptext=lptext.replace('</head>',deps+'</head>',1)
   lp.write_text(lptext)
 # Keep the approved Japanese body, adding only language navigation and alternate URLs.
 jm={'language':'言語を選択'}
 for slug in SLUGS:
  p=source/('index.html' if slug=='index' else slug+'.html');s=p.read_text()
  s=re.sub(r'<link rel="alternate" hreflang="[^\"]+" href="[^\"]+">','',s)
  s=s.replace('</head>',alternates(slug)+'</head>',1)
  s=re.sub(r'<label class="learning-language">.*?</label>','',s)
  s=s.replace('</header>',picker('ja',slug,jm)+'</header>',1)
  if '../../learning-locales/international.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="../../learning-locales/international.css"><script defer src="../../learning-locales/language-navigation.js"></script></head>',1)
  p.write_text(s)
 # Only append missing URLs; do not regenerate unrelated sitemap entries.
 path=root/'sitemap.xml';s=path.read_text();new=''
 for code in LANGS:
  for slug in SLUGS:
   u=url(code,slug)
   if '<loc>'+u+'</loc>' not in s:new+=f'  <url>\n    <loc>{u}</loc>\n    <lastmod>2026-10-21</lastmod>\n  </url>\n'
 path.write_text(s.replace('</urlset>',new+'</urlset>'))
 (shared/'locales.json').write_text(json.dumps({'languages':LANGS,'tags':TAGS,'slugs':SLUGS},ensure_ascii=False,indent=2)+'\n')
 print(f'Generated {len(LANGS)*len(SLUGS)} learning pages in {len(LANGS)} languages.')
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--site-root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--app-root',type=Path,required=True);a=p.parse_args();build(a.site_root,a.app_root)
