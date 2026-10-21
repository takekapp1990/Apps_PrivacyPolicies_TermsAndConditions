import { key, isCorrect, describeSolution } from './practice-engine.mjs';

function track(name, details) {
  if (typeof window.gtag === 'function') window.gtag('event', name, { article_id: document.body.dataset.article, ...details });
}
const section = document.querySelector('[data-technique]');
if (section) initializePractice(section).catch(() => {
  const mount = section.querySelector('.practice-mount');
  mount.replaceChildren();
  const message = document.createElement('p');
  message.textContent = '練習盤面を読み込めませんでした。通信状態をご確認のうえ、ページを再読み込みしてください。';
  mount.append(message);
});

async function initializePractice(section) {
  const response = await fetch(new URL('./practice-data.json', import.meta.url));
  if (!response.ok) throw new Error('Practice data unavailable');
  const data = await response.json();
  const technique = section.dataset.technique;
  const puzzles = data[technique];
  let index = 0, selectedCell = null, selected = new Set(), revealed = false, started = false, completed = false;
  const mount = section.querySelector('.practice-mount');
  mount.innerHTML = `<div class="practice-toolbar"><label>問題 <select aria-label="練習問題を選ぶ">${puzzles.map((_, i) => `<option value="${i}">例題 ${i + 1} / ${puzzles.length}</option>`).join('')}</select></label><label><input type="checkbox" checked class="notes-toggle">候補を表示</label></div><p class="board-help">行は上から、列は左から数えます。マスを選び、下の数字ボタンで答えを入力します。矢印キーで移動し、数字キー1〜9でも操作できます。</p><div class="board" role="group" aria-label="練習用ナンプレ盤面、9行9列"></div><p class="selection-label" aria-live="polite"></p><div class="keypad" role="group" aria-label="回答する数字"></div><div class="practice-actions"><button class="button check" type="button">回答を確認</button><button class="small-button clear" type="button">選択を消す</button><button class="small-button reset" type="button">やり直す</button><button class="small-button reveal" type="button">解説を見る</button></div><p class="practice-status" role="status" aria-live="polite"></p><div class="solution" hidden><h3>この一手の根拠</h3><p class="reason"></p><p class="effect"></p><p>青い枠で囲んだマスが、この手筋の根拠です。取り消し線を付けた候補は消せます。</p><div class="practice-actions"><button class="small-button next" type="button">次の例題へ →</button><a href="#continue">アプリで練習を続ける →</a></div></div>`;
  const board = mount.querySelector('.board'), label = mount.querySelector('.selection-label'), status = mount.querySelector('.practice-status'), solution = mount.querySelector('.solution'), selector = mount.querySelector('select'), keypad = mount.querySelector('.keypad');
  const puzzle = () => puzzles[index];
  const markStarted = () => { if (!started) { started = true; track('technique_practice_start', { technique_id: technique, puzzle_id: puzzle().id }); } };
  function setStatus(message, kind = '') { status.textContent = message; status.className = `practice-status ${kind}`; }
  function draw() {
    const p = puzzle(), s = p.acceptedSolutions[0];
    const focusedCell = board.contains(document.activeElement) ? document.activeElement.dataset.cell : null;
    board.replaceChildren();
    for (let row = 0; row < 9; row++) for (let col = 0; col < 9; col++) {
      const coord = `${row},${col}`, value = p.values[row][col], notes = p.notes[coord] || [];
      const cell = document.createElement(value ? 'span' : 'button');
      if (!value) cell.type = 'button';
      cell.dataset.cell = coord;
      cell.className = `cell ${value ? (p.givens[row][col] ? 'given' : 'entered') : ''}`;
      if (selectedCell === coord) cell.classList.add('selected');
      if (revealed && s.patternCells.some(c => c.row === row && c.col === col)) cell.classList.add('pattern');
      let description = `${row + 1}行${col + 1}列、`;
      if (value) { cell.textContent = value; description += `${value}、確定済み`; }
      else {
        description += `候補${notes.join('・')}`;
        const ns = document.createElement('span'); ns.className = 'notes'; ns.setAttribute('aria-hidden', 'true');
        for (let digit = 1; digit <= 9; digit++) {
          const n = document.createElement('span');
          n.textContent = notes.includes(digit) ? digit : '';
          if (selected.has(key(row, col, digit))) { n.classList.add('chosen'); description += `、回答${digit}`; }
          if (revealed && s.eliminations?.some(e => e.row === row && e.col === col && e.candidate === digit)) n.classList.add('eliminated');
          ns.append(n);
        }
        cell.append(ns);
        const placed = [...selected].find(k => k.startsWith(`${coord},`));
        if (p.answerType === 'placeValue' && (placed || (revealed && s.cell.row === row && s.cell.col === col))) {
          const digit = revealed ? s.value : placed.split(',')[2];
          const overlay = document.createElement('span'); overlay.className = 'placement'; overlay.textContent = digit; overlay.setAttribute('aria-hidden', 'true'); cell.append(overlay);
        }
        cell.setAttribute('aria-pressed', String(selectedCell === coord));
        cell.addEventListener('click', () => { if (revealed) return; markStarted(); selectedCell = coord; draw(); });
      }
      cell.setAttribute('aria-label', description);
      board.append(cell);
    }
    if (focusedCell) board.querySelector(`[data-cell="${focusedCell}"]`)?.focus();
    const notes = selectedCell ? p.notes[selectedCell] || [] : [];
    label.textContent = revealed ? '解説を表示中です。「やり直す」で、もう一度回答できます。' : selectedCell ? `${Number(selectedCell.split(',')[0]) + 1}行${Number(selectedCell.split(',')[1]) + 1}列を選んでいます。${p.answerType === 'placeValue' ? '入る数字を1つ選びます。' : '消す候補を選びます。再度押すと解除できます。'} 回答数：${selected.size}` : 'まず空きマスを選んでください。';
    for (const button of keypad.children) {
      const digit = Number(button.dataset.digit);
      button.disabled = revealed || !selectedCell || !notes.includes(digit);
      button.setAttribute('aria-pressed', String(!!selectedCell && selected.has(`${selectedCell},${digit}`)));
    }
    mount.querySelector('.check').disabled = revealed;
    mount.querySelector('.clear').disabled = revealed || selected.size === 0;
    mount.querySelector('.reveal').disabled = revealed;
  }
  function answer(digit) {
    if (!selectedCell || revealed || !(puzzle().notes[selectedCell] || []).includes(digit)) return;
    markStarted();
    const k = `${selectedCell},${digit}`;
    if (selected.has(k)) selected.delete(k);
    else { if (puzzle().answerType === 'placeValue') selected.clear(); selected.add(k); }
    setStatus('回答を選択しました。「回答を確認」を押してください。');
    draw();
  }
  for (let n = 1; n <= 9; n++) {
    const b = document.createElement('button'); b.type = 'button'; b.textContent = n; b.dataset.digit = n; b.setAttribute('aria-label', `${n}を回答として選択・解除`); b.addEventListener('click', () => answer(n)); keypad.append(b);
  }
  board.addEventListener('keydown', e => {
    const origin = e.target.closest('[data-cell]');
    if (!origin || revealed) return;
    const [r, c] = origin.dataset.cell.split(',').map(Number);
    const delta = { ArrowUp: [-1, 0], ArrowDown: [1, 0], ArrowLeft: [0, -1], ArrowRight: [0, 1] }[e.key];
    if (delta) {
      e.preventDefault(); let nr = r + delta[0], nc = c + delta[1];
      while (nr >= 0 && nr < 9 && nc >= 0 && nc < 9) {
        if (!puzzle().values[nr][nc]) { selectedCell = `${nr},${nc}`; markStarted(); draw(); board.querySelector(`[data-cell="${selectedCell}"]`).focus(); break; }
        nr += delta[0]; nc += delta[1];
      }
    } else if (/^[1-9]$/.test(e.key)) { e.preventDefault(); selectedCell = origin.dataset.cell; answer(Number(e.key)); }
  });
  function showSolution() {
    revealed = true;
    const text = describeSolution(puzzle());
    mount.querySelector('.reason').textContent = text.reason;
    mount.querySelector('.effect').textContent = text.effect;
    solution.hidden = false;
    const next = mount.querySelector('.next'); next.hidden = index === puzzles.length - 1;
    draw();
  }
  mount.querySelector('.check').addEventListener('click', () => {
    markStarted();
    if (!selected.size) { setStatus('まだ回答がありません。マスを選んでから数字を選んでください。', 'error'); return; }
    if (isCorrect(puzzle(), selected)) {
      if (!completed) { completed = true; track('technique_practice_complete', { technique_id: technique, puzzle_id: puzzle().id }); }
      setStatus('正解です。下の解説で理由を確認できます。', 'success'); showSolution();
    } else setStatus('正解ではありません。選んだマスや数字を見直してください。消す候補を答える問題では、選び忘れや選びすぎがないかも確認しましょう。', 'error');
  });
  mount.querySelector('.reveal').addEventListener('click', () => { markStarted(); selected.clear(); track('technique_practice_solution_view', { technique_id: technique, puzzle_id: puzzle().id }); setStatus('解説を表示しました。「やり直す」を押すと、同じ問題にもう一度回答できます。'); showSolution(); });
  function reset() {
    selectedCell = null; selected.clear(); revealed = false; started = false; completed = false;
    solution.hidden = true;
    setStatus(puzzle().answerType === 'placeValue' ? '候補が1つのマスを探しましょう。' : '同じ2候補だけを持つ2マスを探し、消せる候補を選びましょう。'); draw();
  }
  mount.querySelector('.clear').addEventListener('click', () => { selected.clear(); setStatus('回答の選択をすべて消しました。'); draw(); });
  mount.querySelector('.reset').addEventListener('click', reset);
  mount.querySelector('.next').addEventListener('click', () => { index++; selector.value = String(index); reset(); selector.focus(); });
  selector.addEventListener('change', () => { index = Number(selector.value); reset(); });
  mount.querySelector('.notes-toggle').addEventListener('change', e => { board.classList.toggle('notes-hidden', !e.target.checked); });
  reset();
}
