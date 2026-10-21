from pathlib import Path
import json, html, re
import argparse
from number_place_experience_content import hub, demo_markup, write_experience_pages, write_browser_bundles
parser=argparse.ArgumentParser(description='Generate NumberPlaceHint learning pages and four curated practice samples.')
parser.add_argument('--site-root',type=Path,default=Path(__file__).resolve().parents[1])
parser.add_argument('--app-root',type=Path,required=True,help='Read-only source of the app guide practice data')
args=parser.parse_args()
ROOT=args.site_root.resolve()
APP=args.app_root.resolve()
OUT=ROOT/'NumberPlaceHint/ja/learn'; OUT.mkdir(parents=True,exist_ok=True)
BASE='https://takekapp.com/NumberPlaceHint/ja/learn/'
articles=[
('candidate-notes','候補メモの使い方','まずはここから','空きマスに入る可能性を整理する', 'ナンプレの候補メモの書き方・消し方と、見直すタイミングを図で説明します。候補と確定数字をどう区別するかも解説します。', '''
<p>候補メモは、空きマスに「まだ入る可能性がある数字」を小さく書いておく方法です。同じ行・列・3×3ブロックにある確定済みの数字を調べ、残った数字を書きます。</p>
<h2 id="condition">候補は3つの範囲から絞る</h2><p>空きマスを1つ選び、同じ行、同じ列、同じ3×3ブロックを確認します。そのどこかに確定済みの数字があれば、その数字は候補になりません。残った数字をすべて書くのが基本です。</p><p>たとえば、3つの範囲にある数字を合わせると1・2・4・5・6・8・9が見つかるなら、そのマスの候補は3と7です。候補が2つでも、どちらかはまだ決まりません。</p>
<h2 id="example">図解：行だけで候補を決めない</h2>{{diagram}}<p>この行で足りないのは3・7・9です。この行を見ただけでは、どの空きマスにどの数字が入るかは決まりません。それぞれの列とブロックを調べると、さらに候補を減らせます。</p>
<h2 id="steps">候補を更新する手順</h2><ol><li>空きマスの行・列・ブロックを調べ、使われていない数字をメモします。</li><li>数字が1つ確定したら、そのマスの候補メモを消します。</li><li>確定した数字を、同じ行・列・ブロックにある他の空きマスのメモから消します。</li><li>候補が1つになったマスや、ある数字の入る場所が1か所しかない範囲を探します。</li></ol>
<h2 id="mistakes">よくある間違い</h2><p><strong>メモの数字は、まだ答えとして決まっていません。</strong> 隣のマスに小さな3が書いてあっても、それだけで自分のマスから3を消すことはできません。同じ行・列・ブロックに数字が確定したときや、手筋で候補を外せるとわかったときに、該当する候補を消します。</p><p>また、書き忘れがあると「候補が1つ」という誤った判断につながります。行き詰まったときは、メモが最新かを確認しましょう。</p>
<h2 id="next">次に覚えること</h2><p>候補が1つのマスを確定するのが「裸のシングル」です。一方、ある行・列・ブロックで、特定の数字が入る場所を1か所に絞れるのが「隠れたシングル」です。候補メモを整えると、この2つを探しやすくなります。</p>'''),
('naked-single','裸のシングル','基本の手筋','候補が1つのマスを見つける','ナンプレの裸のシングルの見つけ方を図で説明します。候補が1つならなぜ確定できるのか、隠れたシングルとの違い、Webで試せる練習2問を紹介します。','''
<p>裸のシングルは、ある空きマスに入る候補が1つだけになったとき、その数字を確定する手筋です。まずは候補が1つだけのマスを探します。</p>
<h2 id="condition">数字を確定できる条件</h2><p>同じ行・列・ブロックにある数字を調べたり、ほかの手筋で候補を消したりした結果、候補が1つになっていれば使えます。他の8種類の数字が入らないため、残った数字を入れるしかありません。</p><p>メモに1つしか書いていないというだけでは不十分です。候補の書き忘れがないことを確かめてから確定しましょう。</p>
<h2 id="example">図解：最後に残った候補を入れる</h2>{{diagram}}<p>この行には1・2・4・5・6・7・8・9があるため、空きマスは3と確定できます。実際の盤面では、行だけでなく列やブロックの数字を組み合わせて、候補が1つになる場合もあります。</p>
<h2 id="steps">見つけ方</h2><ol><li>候補メモが1つの空きマスを探します。</li><li>同じ行・列・ブロックの数字や、それまでに消した候補を見直し、メモに書き忘れがないか確認します。</li><li>残った数字を確定し、関係するマスのメモを更新します。</li></ol>
<h2 id="mistakes">隠れたシングルとの違い</h2><p>裸のシングルは<strong>1つのマスの候補が1つ</strong>です。隠れたシングルは<strong>1つの範囲で、ある数字の候補位置が1か所</strong>です。隠れたシングルでは、そのマスに複数の候補が残っていても数字を確定できます。</p><p>数字を確定した直後は、周辺に新しいシングルが生まれやすいので、更新したメモをもう一度見てみましょう。</p>
<h2 id="next">盤面で試してみる</h2><p>次の練習では、裸のシングルで確定できるマスを選び、その数字を回答します。問題を最後まで解く必要はありません。この手筋による一手だけを探してください。</p>'''),
('hidden-single','隠れたシングル','基本の手筋','その数字を置ける場所が1か所だけ','ナンプレの隠れたシングルを、候補の位置を示しながら解説します。行・列・ブロックのどこを見るのか、裸のシングルとの違い、見落としやすい点を説明します。','''
<p>隠れたシングルは、ある行・列・ブロックで、特定の数字を置けるマスが1か所しかないときに使います。マスの候補が複数でも、数字の置き場所が1か所なら確定できます。</p>
<h2 id="condition">数字を確定できる条件</h2><p>調べている行・列・ブロックにその数字がまだ入っておらず、候補として残るマスが1つだけなら使えます。各行・各列・各ブロックには1〜9が1つずつ必要なので、そのマスに入れるしかありません。</p><p>同じ範囲の空きマスをすべて確認しましょう。いくつかのマスだけを見て「ここにしかない」と判断すると、別の候補位置を見落とします。</p>
<h2 id="example">図解：候補の数ではなく、位置を数える</h2>{{diagram}}<p>この行で候補の7があるのは、5列目の1マスだけです。そのマスには2と9も候補として残っていますが、7を置ける場所がほかにないので7と確定できます。</p>
<h2 id="steps">見つけ方</h2><ol><li>1つの行・列・ブロックを選び、まだ入っていない数字を確認します。</li><li>そのうち1つの数字に注目し、候補として残るマスを数えます。</li><li>位置が1か所だけなら、そのマスに数字を入れます。</li><li>同じ範囲の別の数字や、別の範囲でも繰り返します。</li></ol>
<h2 id="mistakes">候補が多いマスも見落とさない</h2><p>候補が2・7・9のマスを見て「3つもあるから決まらない」と考えると、隠れたシングルを見逃します。そのマスの候補の数だけでなく、7を置けるマスが行の中にいくつあるかを調べます。</p><p>逆に、その行に7の候補が2か所あるなら、この手筋ではどちらとも決まりません。その場合は、ほかの数字や、別の行・列・ブロックを調べましょう。</p>
<h2 id="next">裸のシングルと交互に探す</h2><p>候補が1つのマスが見つからないときは、行・列・ブロックごとに、各数字を置けるマスを数えてみましょう。数字を入れたらメモを更新し、両方のシングルを探し直しましょう。</p>'''),
('naked-pairs','裸のペア','候補を減らす手筋','2マスに限られた2つの数字を使う','ナンプレの裸のペアを図で説明します。成立する条件、消せる候補の範囲、隠れたペアとの違いを説明し、Webの練習2問で候補削除を試せます。','''
<p>裸のペアは、同じ行、同じ列、または同じブロックに、候補が同じ2種類だけのマスが2つあるときに使います。その2種類の数字を、同じ範囲のほかのマスから削除できます。</p>
<h2 id="condition">候補を消せる条件</h2><p>たとえば候補が{2,7}だけのマスが、同じ行に2つある場合です。片方が2ならもう片方は7、片方が7ならもう片方は2になります。どちらの場合も、2と7はこの2マスに入ります。したがって、同じ行のほかのマスに2や7は入りません。</p><p>この時点では、ペアのどちらに2が入るかまでは決まりません。裸のペアは数字を確定する手筋ではなく、候補を減らす手筋です。</p>
<h2 id="example">図解：ペア以外のマスから消す</h2>{{diagram}}<p>2列目と5列目の{2,7}がペアです。8列目の{2,5,7}から2と7を消せます。残った5を確定するのは、その次の「裸のシングル」による一手です。</p>
<h2 id="steps">見つけ方</h2><ol><li>候補が2種類だけのマスを探します。</li><li>同じ行・列・ブロックに、同じ2種類だけを持つ別のマスがあるか調べます。</li><li>共有する範囲の、ペア以外のマスからその2種類を消します。</li><li>候補削除によって新しいシングルが生まれたか確認します。</li></ol>
<h2 id="mistakes">候補が共通しているだけでは不十分</h2><p>{2,7}と{2,7,9}の2マスでは、裸のペアは成立しません。後者に9が入る可能性があるため、2と7が2マスを占めるとは限らないからです。</p><p>また、同じ行だけを共有するペアから、無関係な列の候補を消すことはできません。2マスが同じブロックも共有している場合は、そのブロックのほかのマスからも消せます。</p><p>「隠れたペア」は、2つの数字の候補位置が同じ2マスに限られる手筋です。裸のペアとは確認する条件が異なります。</p>
<h2 id="next">消せる候補を選ぶ練習</h2><p>練習では、ペアの2マスを答えるのではなく、そこから直接消せる候補をすべて選びます。ペアの候補自体は消さないように注意してください。</p>'''),
('locked-candidates','Locked Candidates','候補を減らす手筋','ブロックと行・列の重なりを見る','ナンプレのLocked Candidates（ロックされた候補）を図で説明します。PointingとClaimingの違い、候補を消せる範囲、成立しない例を解説します。','''
<p>Locked Candidatesは、ある数字の候補位置が「ブロックと行・列の重なる部分」に限られることを使い、候補を削除する手筋です。見る方向によってPointingとClaimingの2種類があります。</p>
<h2 id="condition">Pointing：ブロックから行・列を見る</h2><p>あるブロックの中で、特定の数字の候補がすべて同じ行にあるとします。その数字はブロック内に必要なので、その行のブロック内に入ります。したがって、同じ行のブロック外から、その数字を消せます。候補が同じ列にそろう場合も同様です。</p>
<h2 id="example">図解：同じ行のブロック外から消す</h2>{{diagram}}<p>これは左上ブロックにある5の候補位置を、行ごとに示した図です。左上ブロックの5の候補が1行目の1・3列目だけなら、1行目の4〜9列目から候補の5を消せます。</p><p>左上ブロックの2・3行目にも5の候補があるなら、このPointingは成立しません。「1行目に候補が並んでいる」だけでなく、ブロック内の候補位置がすべてそこに限られる必要があります。</p>
<h2 id="steps">Claiming：行・列からブロックを見る</h2><p>逆に、ある行で特定の数字の候補がすべて同じブロック内にあるなら、その数字はその行のブロック内に入ります。したがって、そのブロックの別の行から同じ数字の候補を消せます。列から見る場合は、別の列から消します。</p><ol><li>数字を1つ選び、ブロック内の候補位置を見ます。</li><li>1本の行か列に限られていれば、Pointingによる削除を探します。</li><li>次に行・列を見て、候補位置が1ブロックに限られていれば、Claimingによる削除を探します。</li></ol>
<h2 id="mistakes">削除する側を取り違えない</h2><p>Pointingは「ブロック内に限られる候補位置」を根拠に、行・列のブロック外から消します。Claimingは「行・列内に限られる候補位置」を根拠に、ブロックのその行・列以外から消します。</p><p>根拠になった候補は消しません。また、この手筋だけでは、重なり部分のどのマスに数字が入るかは決まりません。</p>
<h2 id="next">基本の手筋と組み合わせる</h2><p>候補を消したら、裸のシングルや隠れたシングルができていないか見直しましょう。候補を減らす手筋と数字を確定する手筋を交互に使うことで、盤面を進められます。</p>''')]

def unit(cells,caption):
 return '<figure class="unit-figure"><div class="unit" aria-label="'+caption+'">'+''.join('<div class="unit-cell '+('pattern' if isinstance(c,tuple) else '')+'">'+(c[0] if isinstance(c,tuple) else c)+'</div>' for c in cells)+'</div><figcaption>'+caption+'</figcaption></figure>'
diagrams={
 'candidate-notes':unit(['1','2','□','4','5','6','□','8','□'],'1つの行を抜き出した例です。空きマスの候補は、それぞれの列・ブロックも見て調べます。'),
 'naked-single':unit(['1','2',('3',),'4','5','6','7','8','9'],'1つの行を抜き出した例です。強調したマスはもともと空欄で、候補は3だけです。'),
 'hidden-single':unit(['1','<small>2 4</small>','3','<small>2 4 9</small>',('<small>2 <b>7</b> 9</small>',),'5','6','8','<small>2 9</small>'],'1つの行にある候補を示しています。7の候補位置は強調した5列目だけです。'),
 'naked-pairs':unit(['1',('<small>2 7</small>',),'3','4',('<small>2 7</small>',),'6','8','<small><s>2</s> 5 <s>7</s></small>','9'],'1つの行にある候補を示しています。枠を付けた2マスがペアです。8列目の取り消し線は削除できる候補です。'),
 'locked-candidates': '<figure class="unit-figure"><table class="pointing"><caption>左上ブロックで、5の候補がある位置を示しています。</caption><tbody><tr><th scope="row">1行目</th><td class="pattern">5候補</td><td>—</td><td class="pattern">5候補</td></tr><tr><th scope="row">2行目</th><td>—</td><td>—</td><td>—</td></tr><tr><th scope="row">3行目</th><td>—</td><td>—</td><td>—</td></tr></tbody></table><figcaption>—は「5の候補がない」位置です。1行目のブロック外では5の候補を削除できます。</figcaption></figure>'}

def cta():
 return '''<section class="app-cta" id="continue"><h2>アプリでもっと楽しく遊ぼう！</h2><p>「ナンプレのヒント」では、手筋ごとに問題を選んで練習できます。複数の手筋を組み合わせた練習や、進み具合の保存にも対応しています。紙の問題を解きたいときは、カメラで読み取ってヒントを確認できます。</p><p class="fine">無料で試せます。一部の練習・ヒント機能はプレミアム向けです。</p><div class="store-links"><a class="button" data-analytics-position="learning_footer" href="https://apps.apple.com/jp/app/id6758233715">App Storeで見る<span aria-hidden="true"> ↗</span></a><a class="button secondary" data-analytics-position="learning_footer" href="https://play.google.com/store/apps/details?id=com.NumberPlaceHint.takekapp1990.prod">Google Playで見る<span aria-hidden="true"> ↗</span></a></div><a class="text-link" href="../landing_page_ja.html">アプリの機能・使い方を見る →</a></section>'''

def page(slug,title,desc,body):
 index=slug=='index'; canonical=BASE if index else BASE+slug+'.html'
 crumbs=[('アプリ紹介','../landing_page_ja.html'),('ナンプレガイド','./')]
 if not index:crumbs.append((title,None))
 schema={'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':t,'item':'https://takekapp.com/NumberPlaceHint/ja/'+u[3:] if u and u.startswith('../') else (BASE if u else canonical)} for i,(t,u) in enumerate(crumbs)]}
 return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | ナンプレのヒント</title>
<meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canonical}"><link rel="icon" href="../../favicon.ico">
<meta property="og:type" content="{'website' if index else 'article'}"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://takekapp.com/NumberPlaceHint/images/ogp_images/ja/ogp_main.png"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="learning.css"><link rel="stylesheet" href="experience.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0VCS46ZTHC"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-0VCS46ZTHC');</script><script defer src="../../../js/app_store_analytics.js"></script><script defer src="learning-browser.js"></script><script defer src="experience-browser.js"></script></head>
<body data-article="{slug}"><a class="skip" href="#main">本文へスキップ</a><header class="masthead"><a class="brand" href="./"><img src="../../images/app_icon/number_place_hint_app_icon_10241024_ios.png" alt="" width="36" height="36">ナンプレのヒント<span>楽しみ方・解き方</span></a><nav aria-label="メイン"><a href="play.html">1問遊ぶ</a><a href="./#guides" {'aria-current="page"' if index else ''}>手筋を学ぶ</a><a href="../landing_page_ja.html">アプリ紹介 ↗</a></nav></header>
<main id="main"><nav class="breadcrumbs" aria-label="パンくず">{''.join(('<a href="'+u+'">'+html.escape(t)+'</a>' if u and not(index and u=='./') else '<span aria-current="page">'+html.escape(t)+'</span>')+(' <span aria-hidden="true">/</span> ' if i<len(crumbs)-1 else '') for i,(t,u) in enumerate(crumbs))}</nav>{body}</main>
<footer class="footer"><a href="./">ナンプレガイド</a><a href="../privacy_policy_ja.html">プライバシーポリシー</a><a href="../terms_and_conditions_ja.html">利用規約</a><a href="/about.html">運営者について</a><a href="/">TakeKApp</a><p>© TakeKApp</p></footer></body></html>'''

cards=''.join(f'<a class="guide-card" href="{slug}.html"><span class="card-number">0{i+1}</span><div><p class="eyebrow">{level}</p><h3>{name}</h3><p>{sub}</p></div><span aria-hidden="true">↗</span></a>' for i,(slug,name,level,sub,*_) in enumerate(articles))
index_body=hub(cards,cta)
(OUT/'index.html').write_text(page('index','ナンプレを楽しむ・遊ぶ・解き方を学ぶ','ナンプレの楽しみ方を、自動で解くデモや無料の体験問題で紹介します。候補メモや手筋の図解、脳トレとの関係を紹介する記事も読めます。',index_body))
for slug,name,level,sub,desc,content in articles:
 content=content.replace('{{diagram}}',diagrams[slug])
 toc=''.join(f'<a href="#{id}">{title}</a>' for id,title in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',content))
 practice=''
 if slug in ['naked-single','naked-pairs']:
  practice=f'''<section id="practice" class="practice" data-technique="{slug}" aria-labelledby="practice-title"><p class="eyebrow">練習問題（全2問）</p><h2 id="practice-title">{name}を練習する</h2><p>{'候補が1つのマスを選び、入る数字を回答してください。' if slug=='naked-single' else '裸のペアを探し、そこから直接消せる候補をすべて選んでください。'}</p><p>各マスの小さな数字は、この局面までに絞り込まれた候補です。</p><div class="practice-mount"><p>練習盤面を読み込んでいます…</p></div><noscript><p>操作できる練習にはJavaScriptが必要です。上の図解と解説はそのまま読めます。</p></noscript></section>'''
 related=''.join(f'<a href="{s}.html">{n} →</a>' for s,n,*_ in articles if s!=slug)
 body=f'''<header class="article-header"><p class="eyebrow">{level}</p><h1>{name}</h1><p class="lead">{sub}</p><p class="byline">制作：TakeKApp · 更新日：<time datetime="2026-10-21">2026年10月21日</time></p></header><div class="article-layout"><aside class="toc"><p>このページの内容</p><nav aria-label="目次">{toc}{'<a href="#practice">練習問題に挑戦</a>' if practice else ''}</nav></aside><article class="article-body">{content}{practice}<section class="related"><h2>ほかの手筋・候補メモの解説</h2>{related}</section></article></div>{cta()}'''
 (OUT/(slug+'.html')).write_text(page(slug,'ナンプレの'+name+'｜'+sub,desc,body))
write_experience_pages(OUT,page,cta)
# Export exactly two samples per technique; never ship the full app question bank.
data={}
for source,slug in [('naked_single','naked-single'),('naked_pairs','naked-pairs')]:
 puzzles=json.loads((APP/('assets/technique_practice/'+source+'.json')).read_text())['puzzles']
 if slug=='naked-pairs':puzzles=sorted(puzzles,key=lambda p:len(p['acceptedSolutions'][0]['eliminations']))
 data[slug]=[{k:p[k] for k in ['id','answerType','givens','values','notes','acceptedSolutions']} for p in puzzles[:2]]
(OUT/'practice-data.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
write_browser_bundles(OUT)
print('Generated 9 pages, 4 practice samples and 1 trial puzzle:',OUT)

# Build the same learning experience for every deployed language.
from build_number_place_international import build as build_international
build_international(ROOT,APP)
