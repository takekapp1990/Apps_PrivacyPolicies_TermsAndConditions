import { PUZZLE, SOLUTION, DEMO } from './experience-data.mjs';
import { candidates, related, nextStep, completedUnits, complete, position } from './sudoku-engine.mjs';

const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
function track(name,details={}) { if(typeof window.gtag==='function')window.gtag('event',name,{article_id:document.body.dataset.article||'app_lp',...details}); }
const palettes={standard:['#ffc107','#ff6d00','#ff4081','#7c4dff','#00bcd4','#69f0ae'],sparkle:['#fff59d','#ffd740','#ff80ab','#e1bee7','#80d8ff'],neon:['#00e5ff','#18ffff','#7c4dff','#e040fb','#76ff03'],zen:['#80cbc4','#a5d6a7','#b39ddb','#90caf9','#ffccbc']};

class Presentation {
  constructor(root,initial){
    this.root=root;this.initial=[...initial];this.board=[...initial];this.selected=null;this.focused=null;
    this.grid=root.querySelector('.experience-grid');this.status=root.querySelector('.xp-status');this.overlay=root.querySelector('.xp-effects');
    this.effects=root.querySelector('[data-setting="effects"]');
    this.effects.checked=!reduced.matches;
    root.querySelector('[data-setting="style"]').addEventListener('change',e=>{root.dataset.style=e.target.value;});
    this.effects.addEventListener('change',()=>{if(!this.effects.checked)this.overlay.replaceChildren();});
    reduced.addEventListener('change',e=>{if(e.matches){this.effects.checked=false;this.overlay.replaceChildren();}});
    this.render();
  }
  say(text){this.status.textContent=text;}
  render(){
    const focused=this.grid.contains(document.activeElement)?document.activeElement.dataset.index:null;
    this.grid.replaceChildren();
    for(let i=0;i<81;i++){
      const editable=!!this.input&&!this.initial[i];
      const cell=document.createElement(editable?'button':'span');
      if(editable)cell.type='button';
      cell.className=`xp-cell ${this.initial[i]?'xp-given':''}`;
      cell.dataset.index=i;
      if(i===this.selected)cell.classList.add('xp-selected');
      else if(this.selected!==null&&related(i,this.selected))cell.classList.add('xp-related');
      if(this.board[i])cell.textContent=this.board[i];
      else if(this.showNotes||this.focused===i){
        const ns=candidates(this.board,i),notes=document.createElement('span');notes.className='xp-notes';notes.setAttribute('aria-hidden','true');
        for(let n=1;n<=9;n++){const digit=document.createElement('span');digit.textContent=ns.includes(n)?n:'';notes.append(digit);}cell.append(notes);
      }
      let desc=`${position(i)}、${this.board[i]?this.board[i]+'、'+(this.initial[i]?'問題の数字':'入力した数字'):'空きマス'}`;
      if(!this.board[i]&&(this.showNotes||this.focused===i))desc+=`、候補${candidates(this.board,i).join('・')}`;
      cell.setAttribute('aria-label',desc);
      if(editable){cell.setAttribute('aria-pressed',String(i===this.selected));cell.addEventListener('click',()=>{this.selected=i;this.focused=null;this.render();this.say(`${position(i)}を選んでいます。入る数字を選んでください。`);});}
      this.grid.append(cell);
    }
    if(focused!==null)this.grid.querySelector(`[data-index="${focused}"]`)?.focus();
    this.root.querySelectorAll('[data-digit]').forEach(b=>{b.disabled=this.selected===null||complete(this.board);});
  }
  burst(index,kind='input',label=''){
    if(!this.effects.checked||reduced.matches)return;
    const duration=kind==='clear'?1800:kind==='unit'?1150:620;
    const colors=palettes[this.root.dataset.style]||palettes.standard;
    const x=kind==='clear'?50:(index%9+.5)/9*100,y=kind==='clear'?50:(Math.floor(index/9)+.5)/9*100;
    const burst=document.createElement('div');burst.className=`xp-burst xp-burst-${kind}`;
    burst.style.setProperty('--x',`${x}%`);burst.style.setProperty('--y',`${y}%`);burst.style.setProperty('--duration',`${duration}ms`);burst.style.setProperty('--ring-color',colors[0]);
    const maxRadius=this.grid.clientWidth*(kind==='clear'?.72:kind==='unit'?.52:.15);
    burst.style.setProperty('--ring-size',`${maxRadius*2}px`);
    const ring=document.createElement('i');ring.className='xp-ring';burst.append(ring);
    const count=kind==='clear'?74:kind==='unit'?46:18;
    for(let j=0;j<count;j++){
      const spark=document.createElement('i');const angle=j/count*Math.PI*2;
      const radius=maxRadius*(0.35+(j%7)*.12);
      spark.className='xp-spark';spark.style.setProperty('--dx',`${Math.cos(angle)*radius}px`);spark.style.setProperty('--dy',`${Math.sin(angle)*radius+(kind==='clear'?35:0)}px`);spark.style.background=colors[j%colors.length];spark.style.setProperty('--turn',`${j*37}deg`);burst.append(spark);
    }
    if(label){const text=document.createElement('span');text.className='xp-effect-label';text.textContent=label;burst.append(text);}
    this.overlay.append(burst);burst.addEventListener('animationend',e=>{if(e.target===ring)burst.remove();});
    // Fallback for browsers where animationend is suppressed after a visibility change.
    setTimeout(()=>burst.remove(),duration+100);
  }
  apply(index,value){
    const before=[...this.board];this.board[index]=value;this.selected=index;this.focused=null;this.render();
    const cell=this.grid.querySelector(`[data-index="${index}"]`);
    if(this.effects.checked&&!reduced.matches)cell.classList.add('xp-pop');
    const finished=completedUnits(before,this.board);
    if(complete(this.board)){
      this.burst(index,'clear','クリア！');
      this.grid.classList.add('xp-board-complete');
      if(this.root.querySelector('.xp-clear'))this.root.querySelector('.xp-clear').hidden=false;
    }else if(finished.length){
      if(this.effects.checked&&!reduced.matches){for(const u of finished)for(const i of u)this.grid.querySelector(`[data-index="${i}"]`).classList.add('xp-unit-complete');}
      this.burst(index,'unit','そろいました！');
    }else this.burst(index);
  }
}

class Demo extends Presentation {
  constructor(root){
    super(root,DEMO);
    this.timer=null;this.running=false;this.pending=null;this.started=false;
    this.visible=false;this.wantsPlay=!reduced.matches;
    this.total=DEMO.filter(value=>!value).length;
    this.playButton=root.querySelector('[data-action="play"]');
    this.stepButton=root.querySelector('[data-action="step"]');
    this.speed=root.querySelector('[data-setting="speed"]');
    this.playButton.addEventListener('click',()=>{
      if(this.running){this.pause();return;}
      if(complete(this.board))this.resetBoard();
      this.wantsPlay=true;this.sync();
    });
    this.stepButton.addEventListener('click',()=>{
      this.pause();if(complete(this.board))return;
      const step=this.pending||nextStep(this.board);if(step)this.commit(step);
    });
    root.querySelector('[data-action="reset"]').addEventListener('click',()=>{
      const resume=this.wantsPlay;this.suspend();this.resetBoard();this.wantsPlay=resume;
      this.say('最初の盤面に戻しました。空きマスを順番に解いていきます。');this.sync();
    });
    this.speed.addEventListener('change',()=>{
      if(this.running){clearTimeout(this.timer);this.schedule(()=>this.advance());}
    });
    document.addEventListener('visibilitychange',()=>this.sync());
    new IntersectionObserver(entries=>{
      this.visible=entries[0].isIntersecting&&entries[0].intersectionRatio>=0.25;this.sync();
    },{threshold:0.25}).observe(this.grid);
    reduced.addEventListener('change',e=>{if(e.matches)this.pause();});
    if(reduced.matches)this.say('自動再生は停止しています。再生ボタンか「一手進める」で見ることができます。');
  }
  resetBoard(){
    this.board=[...DEMO];this.selected=null;this.focused=null;this.pending=null;this.started=false;
    this.overlay.replaceChildren();this.grid.classList.remove('xp-board-complete');
    this.stepButton.disabled=false;this.render();
  }
  schedule(fn,delay=Number(this.speed.value)){this.timer=setTimeout(fn,delay);}
  sync(){
    const shouldPlay=this.wantsPlay&&this.visible&&!document.hidden;
    if(shouldPlay&&!this.running){
      this.running=true;this.playButton.textContent='一時停止';
      if(!this.started){track('sudoku_demo_start');this.started=true;}
      this.advance();
    }else if(!shouldPlay&&this.running)this.suspend();
  }
  suspend(){clearTimeout(this.timer);this.running=false;this.playButton.textContent='デモを再生';}
  pause(){this.wantsPlay=false;this.suspend();}
  advance(){
    if(!this.running)return;
    if(complete(this.board)){
      this.schedule(()=>{this.resetBoard();this.advance();},4000);return;
    }
    if(this.pending){
      this.commit(this.pending);
      if(this.running)this.schedule(()=>this.advance(),complete(this.board)?0:Number(this.speed.value));
      return;
    }
    const step=nextStep(this.board);
    if(!step){this.pause();return;}
    // Most steps go straight to the placed digit. Show candidates only every eighth step.
    const filled=this.board.filter((value,i)=>!DEMO[i]&&value).length;
    if((filled+1)%8===0){
      this.pending=step;this.selected=step.index;this.focused=step.index;this.render();
      this.say(`${step.reason} 次に${step.value}を入れます。`);
    }else this.commit(step);
    this.schedule(()=>this.advance(),complete(this.board)?0:Number(this.speed.value));
  }
  commit(step){
    this.pending=null;this.apply(step.index,step.value);
    const count=this.board.filter((value,i)=>!DEMO[i]&&value).length;
    const done=complete(this.board);
    this.say(done?`${this.total}マスすべてが埋まりました。自動再生中は、少し待つと最初から繰り返します。`:`${step.reason} ${step.value}を入れました。（${count}/${this.total}マス）`);
    if(done){this.stepButton.disabled=true;track('sudoku_demo_complete');}
  }
}

class Game extends Presentation {
  constructor(root){
    super(root,PUZZLE);this.input=true;this.history=[];this.started=false;
    root.querySelector('[data-setting="notes"]').addEventListener('change',e=>{this.showNotes=e.target.checked;this.render();});
    root.querySelectorAll('[data-digit]').forEach(button=>button.addEventListener('click',()=>this.enter(Number(button.dataset.digit))));
    root.querySelector('[data-action="hint"]').addEventListener('click',()=>{
      if(complete(this.board))return;this.start();const step=nextStep(this.board);if(!step){this.say('空きマスの候補を調べてみましょう。');return;}
      this.selected=step.index;this.focused=step.index;this.render();this.say(step.reason);track('sudoku_trial_hint',{technique_id:step.type});
    });
    root.querySelector('[data-action="erase"]').addEventListener('click',()=>this.erase());
    root.querySelector('[data-action="undo"]').addEventListener('click',()=>{
      if(!this.history.length){this.say('まだ戻せる入力はありません。');return;}
      this.board=this.history.pop();this.hideClear();this.render();this.say('一手前の状態に戻しました。');
    });
    root.querySelector('[data-action="reset"]').addEventListener('click',()=>{this.history.push([...this.board]);this.board=[...PUZZLE];this.selected=null;this.focused=null;this.hideClear();this.render();this.say('最初の問題に戻しました。「一手戻す」で直前の状態に戻せます。');});
    this.grid.addEventListener('keydown',e=>{
      const origin=e.target.closest('[data-index]');if(!origin)return;
      const i=Number(origin.dataset.index);this.selected=i;
      const ds={ArrowUp:-9,ArrowDown:9,ArrowLeft:-1,ArrowRight:1};
      if(e.key in ds){e.preventDefault();let j=i+ds[e.key];while(j>=0&&j<81){if((e.key==='ArrowLeft'||e.key==='ArrowRight')&&Math.floor(j/9)!==Math.floor(i/9))break;if(!PUZZLE[j]){this.selected=j;this.focused=null;this.render();this.grid.querySelector(`[data-index="${j}"]`).focus();break;}j+=ds[e.key];}}
      else if(/^[1-9]$/.test(e.key)){e.preventDefault();this.enter(Number(e.key));}
      else if(e.key==='Backspace'||e.key==='Delete'){e.preventDefault();this.erase();}
    });
    this.render();
  }
  start(){if(!this.started){this.started=true;track('sudoku_trial_start');}}
  hideClear(){this.root.querySelector('.xp-clear').hidden=true;this.grid.classList.remove('xp-board-complete');this.overlay.replaceChildren();}
  enter(value){
    if(this.selected===null||PUZZLE[this.selected]||complete(this.board))return;
    this.start();
    if(SOLUTION[this.selected]!==value){
      this.say(`${position(this.selected)}の${value}は正解と一致しません。ほかの候補を調べてみましょう。`);
      const cell=this.grid.querySelector(`[data-index="${this.selected}"]`);cell.classList.remove('xp-error');void cell.offsetWidth;cell.classList.add('xp-error');return;
    }
    if(this.board[this.selected]===value)return;
    this.history.push([...this.board]);const i=this.selected;this.apply(i,value);
    if(complete(this.board)){this.say('正解です。すべてのマスが埋まりました！');track('sudoku_trial_complete');}
    else this.say(`${position(i)}に${value}を入れました。残り${this.board.filter(v=>!v).length}マスです。`);
  }
  erase(){
    if(this.selected===null||PUZZLE[this.selected]||!this.board[this.selected]){this.say('消したい入力済みのマスを選んでください。');return;}
    this.history.push([...this.board]);this.board[this.selected]=0;this.hideClear();this.render();this.say(`${position(this.selected)}の数字を消しました。`);
  }
}
for(const element of document.querySelectorAll('[data-demo]'))new Demo(element);
for(const element of document.querySelectorAll('[data-game]'))new Game(element);
