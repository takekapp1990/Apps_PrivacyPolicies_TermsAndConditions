"""Compile localized classic-script bundles from the approved Japanese behavior."""
import json,re
JAPANESE=re.compile(r'[ぁ-ゖァ-ヺ一-龯]')

def compile_bundles(source,m,out):
 prefix='(()=>{\n"use strict";\nconst M='+json.dumps(m,ensure_ascii=False)+';\nconst tr=(key,values={})=>M[key].replace(/\\{(\\w+)\\}/g,(_,name)=>String(values[name]??"{"+name+"}"));\nconst cellName=(row,col)=>tr("cell",{row:row+1,col:col+1});\n'
 def plain(name):
  s=(source/name).read_text();s=re.sub(r'^import .*?;\n','',s,flags=re.M);return re.sub(r'^export ','',s,flags=re.M)
 def literal(s,old,key):
  needle="'"+old+"'";assert needle in s,(old,key)
  return s.replace(needle,'tr('+json.dumps(key)+')')
 def exact(s,old,new):
  assert old in s,old
  return s.replace(old,new)
 engine=plain('sudoku-engine.mjs')
 engine=exact(engine,'`${Math.floor(i/9)+1}行${i%9+1}列`','cellName(Math.floor(i/9),i%9)')
 engine=exact(engine,'`${position(i)}は、同じ行・列・ブロックにある数字を除くと、候補が${ns[0]}だけになります。`','tr("placeReason",{cell:position(i),value:ns[0]})')
 engine=exact(engine,'`${u+1}行目`','M.rowUnit.replace("{n}",u+1)')
 engine=exact(engine,'`${u-8}列目`','M.colUnit.replace("{n}",u-8)')
 engine=exact(engine,'`${u-17}番目のブロック`','M.blockUnit.replace("{n}",u-17)')
 engine=exact(engine,'`${label}で${n}を置けるのは${position(positions[0])}だけです。`','M.hiddenGeneric+" "+tr("placeEffect",{cell:position(positions[0]),value:n})')
 xp=plain('experience.js')
 xp=exact(xp,"`${position(i)}、${this.board[i]?this.board[i]+'、'+(this.initial[i]?'問題の数字':'入力した数字'):'空きマス'}`",'`${position(i)}: ${this.board[i]?this.board[i]+" ("+(this.initial[i]?M.given:M.entered)+")":M.empty}`')
 xp=exact(xp,'`、候補${candidates(this.board,i).join(\'・\')}`','"; "+tr("candidateLabel",{digits:candidates(this.board,i).join(", ")})')
 xp=exact(xp,'`${position(i)}を選んでいます。入る数字を選んでください。`','tr("selected",{cell:position(i)})')
 for a,k in [('クリア！','clearLabel'),('そろいました！','groupLabel'),('一時停止','pause'),('デモを再生','play'),('最初の盤面に戻しました。空きマスを順番に解いていきます。','resetDemo'),('自動再生は停止しています。再生ボタンか「一手進める」で見ることができます。','motionPaused'),('空きマスの候補を調べてみましょう。','hintFallback'),('まだ戻せる入力はありません。','undoEmpty'),('一手前の状態に戻しました。','undone'),('最初の問題に戻しました。「一手戻す」で直前の状態に戻せます。','resetGame'),('正解です。すべてのマスが埋まりました！','gameComplete'),('消したい入力済みのマスを選んでください。','erasePrompt')]:xp=literal(xp,a,k)
 for a,b in [
 ('`${step.reason} 次に${step.value}を入れます。`','tr("nextDigit",{reason:step.reason,value:step.value})'),
 ('`${this.total}マスすべてが埋まりました。自動再生中は、少し待つと最初から繰り返します。`','tr("completeDemo",{total:this.total})'),
 ('`${step.reason} ${step.value}を入れました。（${count}/${this.total}マス）`','tr("progress",{reason:step.reason,value:step.value,count,total:this.total})'),
 ('`${position(this.selected)}の${value}は正解と一致しません。ほかの候補を調べてみましょう。`','tr("wrong",{cell:position(this.selected),value})'),
 ('`${position(i)}に${value}を入れました。残り${this.board.filter(v=>!v).length}マスです。`','tr("remaining",{cell:position(i),value,count:this.board.filter(v=>!v).length})'),
 ('`${position(this.selected)}の数字を消しました。`','tr("erased",{cell:position(this.selected)})')]:xp=exact(xp,a,b)
 experience=plain('experience-data.mjs')+'\n'+engine+'\n'+xp
 assert not JAPANESE.search(experience),JAPANESE.search(experience)
 (out/'experience-browser.js').write_text('// Generated localized runtime.\n'+prefix+experience+'\n})();\n')
 practice=plain('practice-engine.mjs')
 for a,b in [
 ('`${s.cell.row + 1}行${s.cell.col + 1}列の候補は${s.value}だけです。ほかの数字は候補から除かれているため、このマスは${s.value}と確定できます。`','tr("placeReason",{cell:cellName(s.cell.row,s.cell.col),value:s.value})'),
 ('`回答：${s.cell.row + 1}行${s.cell.col + 1}列に${s.value}を入れます。`','tr("placeEffect",{cell:cellName(s.cell.row,s.cell.col),value:s.value})'),
 ('`${c.row + 1}行${c.col + 1}列`','cellName(c.row,c.col)'),
 (".join('と')",".join(' / ')") ,
 ('`${u.index + 1}行目`','M.rowUnit.replace("{n}",u.index+1)'),
 ('`${u.index + 1}列目`','M.colUnit.replace("{n}",u.index+1)'),
 ('`${u.index + 1}番目のブロック`','M.blockUnit.replace("{n}",u.index+1)'),
 ('`${e.row + 1}行${e.col + 1}列の${e.candidate}`','tr("elimination",{cell:cellName(e.row,e.col),value:e.candidate})'),
 (".join('、')",".join('; ')") ,
 ('`${coords}は、候補がどちらも${digits}だけです。この2マスには${digits}が1つずつ入るため、${unit}のほかのマスからは、この2つの数字を候補から外せます。`','tr("pairReason",{cells:coords,digits,unit})'),
 ('`削除できる候補：${eliminations}。ペアのどちらにどの数字が入るかは、まだ決まりません。`','tr("pairEffect",{eliminations})')]:practice=exact(practice,a,b)
 p=plain('learning.js')
 loader="  const response = await fetch(new URL('./practice-data.json', import.meta.url));\n  if (!response.ok) throw new Error('Practice data unavailable');\n  const data = await response.json();"
 p=exact(p,loader,'  const data = '+(source/'practice-data.json').read_text().strip()+';')
 p=literal(p,'練習盤面を読み込めませんでした。通信状態をご確認のうえ、ページを再読み込みしてください。','loadingFailure')
 # Text inside the HTML template is interpolated; native strings never become executable code.
 for a,k in [('練習問題を選ぶ','question'),('問題 ','question'),('例題 ','example'),('候補を表示','notes'),('行は上から、列は左から数えます。マスを選び、下の数字ボタンで答えを入力します。矢印キーで移動し、数字キー1〜9でも操作できます。','boardHelp'),('練習用ナンプレ盤面、9行9列','practiceBoard'),('回答する数字','answerDigits'),('回答を確認','check'),('選択を消す','clearSelection'),('やり直す','retry'),('解説を見る','reveal'),('この一手の根拠','solutionTitle'),('青い枠で囲んだマスが、この手筋の根拠です。取り消し線を付けた候補は消せます。','solutionLegend'),('次の例題へ →','nextExample'),('アプリで練習を続ける →','appHeading')]:
  # Only translate occurrences within the initial mount template.
  start=p.index('  mount.innerHTML = `');end=p.index('`;\n',start)
  piece=p[start:end];assert a in piece,a;piece=piece.replace(a,'${M.'+k+'}'+(' ' if a.endswith(' ') else ''));p=p[:start]+piece+p[end:]
 p=exact(p,"`${row + 1}行${col + 1}列、`",'cellName(row,col)+": "')
 p=exact(p,"`${value}、確定済み`",'`${value}, ${M.given}`')
 p=exact(p,"`候補${notes.join('・')}`",'tr("candidateLabel",{digits:notes.join(", ")})')
 p=exact(p,'`、回答${digit}`','`; ${M.check}: ${digit}`')
 p=exact(p,"`${Number(selectedCell.split(',')[0]) + 1}行${Number(selectedCell.split(',')[1]) + 1}列を選んでいます。${p.answerType === 'placeValue' ? '入る数字を1つ選びます。' : '消す候補を選びます。再度押すと解除できます。'} 回答数：${selected.size}`",'tr("selected",{cell:cellName(...selectedCell.split(",").map(Number))})+" "+(p.answerType==="placeValue"?M.placePrompt:M.eliminatePrompt)+" "+tr("answerCount",{count:selected.size})')
 p=exact(p,'`${n}を回答として選択・解除`','tr("digitToggle",{value:n})')
 for a,k in [('解説を表示中です。「やり直す」で、もう一度回答できます。','practiceLocked'),('まず空きマスを選んでください。','chooseCell'),('回答を選択しました。「回答を確認」を押してください。','answerChosen'),('まだ回答がありません。マスを選んでから数字を選んでください。','noAnswer'),('正解です。下の解説で理由を確認できます。','practiceCorrect'),('正解ではありません。選んだマスや数字を見直してください。消す候補を答える問題では、選び忘れや選びすぎがないかも確認しましょう。','practiceWrong'),('解説を表示しました。「やり直す」を押すと、同じ問題にもう一度回答できます。','revealShown'),('候補が1つのマスを探しましょう。','nakedPrompt'),('同じ2候補だけを持つ2マスを探し、消せる候補を選びましょう。','pairPrompt'),('回答の選択をすべて消しました。','clearedSelection')]:p=literal(p,a,k)
 learning=practice+'\n'+p
 assert not JAPANESE.search(learning),JAPANESE.search(learning)
 (out/'learning-browser.js').write_text('// Generated localized runtime.\n'+prefix+learning+'\n})();\n')
