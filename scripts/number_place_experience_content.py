"""Editorial content and the single public trial puzzle for the learning site."""
import json
PUZZLE='530070000600195000098000060800060003400803001700020006060000280000419005000080079'
SOLUTION='534678912672195348198342567859761423426853791713924856961537284287419635345286179'
# Start from the original puzzle: 30 givens and 51 blanks.
DEMO=PUZZLE

def grid(text):
 return ''.join(f'<span class="xp-cell {"xp-given" if v!="0" else ""}">{v if v!="0" else ""}</span>' for v in text)

def demo_markup(id):
 return f'''<div class="sudoku-experience xp-demo" id="{id}" data-demo data-style="standard"><p class="xp-caption">こんな感じで数字を埋めていこう</p><div class="xp-controls"><button type="button" class="xp-button" data-action="play">デモを再生</button><button type="button" class="xp-button xp-secondary" data-action="step">一手進める</button><button type="button" class="xp-button xp-secondary" data-action="reset">最初に戻す</button></div><div class="xp-stage"><div class="experience-grid" role="group" aria-label="自動で解くデモの盤面、9行9列">{grid(DEMO)}</div><div class="xp-effects" aria-hidden="true"></div></div><p class="xp-status" role="status">画面に表示されると、音なしで自動再生します。</p><div class="xp-options"><label>演出 <select data-setting="style"><option value="standard">スタンダード</option><option value="sparkle">スパークル</option><option value="neon">ネオン</option><option value="zen">禅</option></select></label><label>速さ <select data-setting="speed"><option value="1400">ゆっくり</option><option value="850" selected>ふつう</option><option value="350">速く</option></select></label><label><input type="checkbox" data-setting="effects" checked>演出を表示</label></div><p class="xp-small">数字を入れるときやマスがそろったときの演出を、4種類から選べます。デモは音なしで再生します。</p><noscript><p>デモの再生にはJavaScriptが必要です。</p></noscript></div>'''

def hub(cards,cta):
 return f'''<section class="experience-hero"><div><p class="eyebrow">ナンプレの楽しみ方と解き方</p><h1>ナンプレを遊んで、<br><em>解き方も学べます。</em></h1><p class="lead">行・列・ブロックを見比べて、数字が入る場所を探します。まずは解いていく様子を見て、1問遊んでみてください。</p><div class="hero-actions"><a class="button" href="play.html">ナンプレを1問遊ぶ →</a><a href="enjoy.html">どんなところが面白い？</a></div></div>{demo_markup('home-demo')}</section>
<nav class="path-nav" aria-label="目的から選ぶ"><a href="enjoy.html"><b>楽しみ方を知る</b><span>ルールと、解くときの面白さを紹介します。</span></a><a href="play.html"><b>1問遊んでみる</b><span>候補メモやヒントを使って最後まで解けます。</span></a><a href="#guides"><b>手筋を覚える</b><span>図解と短い練習で解き方を学べます。</span></a></nav>
<section class="reading-note"><h2>ナンプレってどんなパズル？</h2><p>ナンプレは、9×9のマスに1〜9の数字を入れるパズルです。縦の列・横の行・太線で囲まれた3×3のブロックに、それぞれ同じ数字が重ならないように埋めていきます。</p><p>最初から入っている数字を手がかりに、空いているマスの数字を考えます。</p><a href="enjoy.html">ルールと楽しみ方を読む →</a></section>
<section class="brain-intro"><h2>頭を使う遊びとして楽しめます</h2><p>候補を見比べ、条件を整理して考えるナンプレは、脳トレとしても親しまれています。認知機能との関連を調べた研究はありますが、遊べば能力が上がると断定はできません。研究でわかっていることと、解くときに使う考え方を紹介します。</p><a href="brain-training.html">ナンプレと脳トレについて読む →</a></section>
<section id="guides"><div class="section-heading"><h2>解き方を知りたいときは</h2><p>候補メモを初めて使う方は、最初の記事から読んでみてください。裸のシングルと裸のペアには各2問の手筋練習もあります。</p></div><div class="guide-list">{cards}</div></section>
<section class="practice-invite"><div><h2>手筋だけを練習することもできます</h2><p>問題を最初から解かずに、数字を1つ入れたり、消せる候補を選んだりする練習です。</p></div><a class="button" href="naked-single.html#practice">裸のシングルの練習へ →</a></section>{cta()}'''

ENJOY='''<p>ナンプレは、各行・各列・各3×3ブロックに1〜9を1つずつ入れるパズルです。足し算や掛け算は使いません。数字の位置を調べ、置ける場所を絞っていきます。</p>
<h2 id="rules">まずは、同じ数字が重ならないことを確かめます</h2><p>空きマスと同じ行に5があれば、そのマスに5は入りません。列や3×3ブロックも同じように確認します。入らない数字を除いていき、残った数字が1つになったら確定できます。</p><p>デモは、数字が30個入った最初の盤面から、空きマス51個を順番に埋めていきます。注目するマスと、そこに数字が入る理由を見てみてください。</p>{{demo}}
<h2 id="chain">数字が1つ入ると、次の手がかりが見つかります</h2><p>候補が2と7だったマスも、同じ行の別のマスに2が入れば、7と決まります。その7が、さらに別のマスの候補を減らすこともあります。1つの数字をきっかけに、止まっていた盤面が続けて埋まる場面があります。</p>
<h2 id="progress">覚えた手筋を、自分で見つけられるようになります</h2><p>最初は見落としていた「候補が1つのマス」や「同じ2候補を持つペア」も、解き方を知ると探す目印になります。前はヒントが必要だったところを、自分で進められるのも続ける楽しみです。</p><p><a href="naked-single.html">候補が1つのマスを探す「裸のシングル」を読む →</a></p>
<h2 id="pace">行き詰まったら、別の場所を調べてみましょう</h2><p>同じ場所を見続けても進まないときは、空きマスが少ない行や列に移ってみてください。候補メモを更新し忘れていないか確かめる方法もあります。時間を競わず、途中で休みながら解いても構いません。</p><p>体験版では候補表示とヒントを使えます。解説を読んだあとに遊んでも、まず遊んでから手筋を調べても大丈夫です。</p><a class="button" href="play.html">ナンプレを1問遊ぶ →</a>'''
BRAIN='''<p>ナンプレを解くときは、数字を見比べ、入る場所を絞り、矛盾がないか確かめます。こうした考える遊びを日常に取り入れたい方には、ナンプレも選択肢になります。ここでは「解くときに何を考えるか」と「研究から言えること」を分けて紹介します。</p>
<h2 id="thinking">解くときは、位置や条件を見比べます</h2><p>同じ行・列・ブロックにどの数字があるかを調べ、空きマスに入らない数字を除きます。複数の候補が残るときは、数字ごとに置ける場所を数えたり、ほかのマスとの関係を調べたりします。</p><p>覚えることが多いと感じたら、候補メモを使って構いません。すべてを頭の中に覚えておく必要はなく、書いた候補を見ながら理由を考えられます。</p>
<h2 id="research">数字パズルと認知機能の関連を調べた研究があります</h2><p>2019年の研究では、50〜93歳の19,078人について、数字パズルを解く頻度の自己申告と認知課題の成績を比較しました。頻度と、注意・推論・記憶などの課題成績との関連が報告されています。<a href="https://pubmed.ncbi.nlm.nih.gov/30746778/">Brookerらの研究（2019年、PubMed）</a></p><p>ただし、これはナンプレを一定期間続けてもらい、その効果を比較した実験ではありません。もともとパズルが得意な人がよく遊んでいる可能性などもあり、「ナンプレをしたから成績が上がった」とは結論できません。数字パズル全般の調査で、このアプリの効果を調べたものでもありません。</p>
<h2 id="limits">能力の向上や認知症予防が保証されるわけではありません</h2><p>研究チームの大学発表でも、パズルを解くことが後年の認知症リスクを下げるとは言えないと説明しています。ナンプレの成績が伸びることと、日常生活全般の記憶力や判断力が向上することも、同じではありません。<a href="https://news-archive.exeter.ac.uk/2019/may/title_716265_en.html">エクセター大学による研究の紹介</a></p>
<h2 id="habit">面白いと思える難しさで遊んでみてください</h2><p>まずは候補を絞れるマスを探し、わからないところはヒントや解説を使ってみてください。解けるようになったら、別の手筋にも取り組めます。健康上の効果を目標に回数を決めるより、考える過程を楽しめるかどうかを、体験版で確かめてみてください。</p><a class="button" href="play.html">ヒント付きの体験版を遊ぶ →</a>'''

def play_markup():
 return f'''<p>初心者向けの固定問題を1問、最後まで解けます。マスを選び、下の数字ボタンかキーボードで入力してください。入力した数字は、その場で正誤を確認します。</p><div class="sudoku-experience xp-game" data-game data-style="standard"><div class="xp-options"><label><input type="checkbox" data-setting="notes">候補を表示</label><label><input type="checkbox" data-setting="effects" checked>演出を表示</label><label>演出 <select data-setting="style"><option value="standard">スタンダード</option><option value="sparkle">スパークル</option><option value="neon">ネオン</option><option value="zen">禅</option></select></label></div><div class="xp-stage"><div class="experience-grid" role="group" aria-label="体験版のナンプレ盤面、9行9列">{grid(PUZZLE)}</div><div class="xp-effects" aria-hidden="true"></div></div><p class="xp-status" role="status">空きマスを選んでください。</p><div class="xp-keypad" role="group" aria-label="入力する数字">{''.join(f'<button type="button" data-digit="{n}" aria-label="{n}を入力">{n}</button>' for n in range(1,10))}</div><div class="xp-controls"><button type="button" class="xp-button" data-action="hint">次の一手のヒント</button><button type="button" class="xp-button xp-secondary" data-action="erase">数字を消す</button><button type="button" class="xp-button xp-secondary" data-action="undo">一手戻す</button><button type="button" class="xp-button xp-secondary" data-action="reset">最初から遊ぶ</button></div><div class="xp-clear" hidden><h2>すべてのマスが埋まりました</h2><p>この問題はクリアです。ほかの問題を解きたいときは、アプリでも遊べます。</p><a href="#continue">アプリの案内を見る →</a></div><p class="xp-small">矢印キーで空きマス間を移動できます。数字キーで入力し、Delete・Backspaceで消せます。途中の状態は保存されません。</p><noscript><p>数字の入力にはJavaScriptが必要です。</p></noscript></div><section><h2>手筋を練習したいときは</h2><p><a href="naked-single.html#practice">裸のシングル</a>と<a href="naked-pairs.html#practice">裸のペア</a>には、手筋だけを答える例題もあります。</p></section>'''

def write_experience_pages(out,page,cta):
 for slug,title,sub,desc,content in [
 ('enjoy','ナンプレの面白さと楽しみ方','数字の入る場所を探して、盤面を埋めていきます。','ナンプレのルールと楽しみ方を紹介します。数字が入る理由を見ながら解くアニメーションと、1問遊べる体験版もあります。',ENJOY.replace('{{demo}}',demo_markup('enjoy-demo'))),
 ('brain-training','ナンプレは脳トレになる？','解くときに使う考え方と、研究から言えることを紹介します。','ナンプレや数字パズルと認知機能の関連を調べた研究を紹介します。頭を使う遊びとしての楽しみ方と、効果について断定できない点を説明します。',BRAIN),
 ('play','ナンプレを1問遊ぶ','候補表示とヒントを使って、最後まで解けます。','初心者向けのナンプレを無料で1問遊べます。候補表示、次の一手のヒント、入力時・完成時の演出付きで、ブラウザから解けます。',play_markup())]:
  body=f'<header class="article-header"><p class="eyebrow">ナンプレの楽しみ方・解き方</p><h1>{title}</h1><p class="lead">{sub}</p><p class="byline">制作：TakeKApp · 更新日：2026年10月21日</p></header><article class="experience-article article-body">{content}</article>{cta()}'
  (out/(slug+'.html')).write_text(page(slug,title,desc,body))
 (out/'experience-data.mjs').write_text('export const PUZZLE='+json.dumps([int(c) for c in PUZZLE])+';\nexport const SOLUTION='+json.dumps([int(c) for c in SOLUTION])+';\nexport const DEMO='+json.dumps([int(c) for c in DEMO])+';\n')

def write_browser_bundles(out):
 """Emit ordinary scripts so local file previews work without module/fetch restrictions."""
 import re
 def plain(name):
  source=(out/name).read_text()
  source=re.sub(r'^import .*?;\n','',source,flags=re.M)
  return re.sub(r'^export ','',source,flags=re.M)
 experience='\n'.join(plain(name) for name in ['experience-data.mjs','sudoku-engine.mjs','experience.js'])
 (out/'experience-browser.js').write_text('// Generated by scripts/build_number_place_learning.py. Edit the source modules.\n(()=>{\n\"use strict\";\n'+experience+'\n})();\n')
 learning=plain('learning.js')
 old="  const response = await fetch(new URL('./practice-data.json', import.meta.url));\n  if (!response.ok) throw new Error('Practice data unavailable');\n  const data = await response.json();"
 assert old in learning, 'Practice loader changed; update browser bundle generation.'
 learning=learning.replace(old,'  const data = '+(out/'practice-data.json').read_text().strip()+';')
 (out/'learning-browser.js').write_text('// Generated by scripts/build_number_place_learning.py. Edit learning.js and practice-engine.mjs.\n(()=>{\n\"use strict\";\n'+plain('practice-engine.mjs')+'\n'+learning+'\n})();\n')
