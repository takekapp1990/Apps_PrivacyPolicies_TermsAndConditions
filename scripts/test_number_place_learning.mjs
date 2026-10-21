import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';
import { key, isCorrect, describeSolution } from '../NumberPlaceHint/ja/learn/practice-engine.mjs';
const data = JSON.parse(readFileSync(new URL('../NumberPlaceHint/ja/learn/practice-data.json', import.meta.url)));
let count = 0;
for (const puzzles of Object.values(data)) for (const p of puzzles) {
  const s = p.acceptedSolutions[0];
  const expected = new Set(p.answerType === 'placeValue' ? [key(s.cell.row, s.cell.col, s.value)] : s.eliminations.map(e => key(e.row, e.col, e.candidate)));
  assert.equal(isCorrect(p, expected), true);
  assert.equal(isCorrect(p, new Set()), false);
  assert.equal(isCorrect(p, new Set([...expected, '99,99,9'])), false, 'Extra eliminations must be rejected');
  for (const entry of expected) {
    const [r,c,n] = entry.split(',').map(Number);
    assert.equal(p.values[r][c], 0);
    assert.ok(p.notes[`${r},${c}`].includes(n));
  }
  if (p.answerType === 'placeValue') {
    assert.deepEqual(p.notes[`${s.cell.row},${s.cell.col}`], [s.value]);
  } else {
    const digits = s.explanationData.patternCandidates;
    assert.equal(digits.length, 2);
    assert.equal(s.patternCells.length, 2);
    const [a,b] = s.patternCells;
    for (const cell of s.patternCells) assert.deepEqual(p.notes[`${cell.row},${cell.col}`], digits);
    for (const e of s.eliminations) {
      assert.ok(!s.patternCells.some(c => c.row === e.row && c.col === e.col));
      assert.ok(digits.includes(e.candidate));
      const sameUnit = (a.row === b.row && a.row === e.row) || (a.col === b.col && a.col === e.col) || (Math.floor(a.row/3) === Math.floor(b.row/3) && Math.floor(a.col/3) === Math.floor(b.col/3) && Math.floor(a.row/3) === Math.floor(e.row/3) && Math.floor(a.col/3) === Math.floor(e.col/3));
      assert.ok(sameUnit, 'Elimination must share a unit with the pair');
    }
    // Independently enumerate all direct eliminations, including shared blocks.
    const all = new Set();
    for (const [coord, notes] of Object.entries(p.notes)) {
      const [r,c] = coord.split(',').map(Number);
      if (s.patternCells.some(x=>x.row===r&&x.col===c)) continue;
      const shared = (a.row===b.row&&a.row===r)||(a.col===b.col&&a.col===c)||(Math.floor(a.row/3)===Math.floor(b.row/3)&&Math.floor(a.col/3)===Math.floor(b.col/3)&&Math.floor(a.row/3)===Math.floor(r/3)&&Math.floor(a.col/3)===Math.floor(c/3));
      if (shared) for(const d of digits) if(notes.includes(d)) all.add(key(r,c,d));
    }
    assert.deepEqual(expected,all);
    assert.equal(isCorrect(p, new Set([key(a.row,a.col,digits[0])])),false,'Pair candidates must not be removed');
  }
  // Verify uniqueness and that every retained candidate list contains the true solution.
  const grid=p.values.map(row=>[...row]); let solutions=0, solution;
  const candidates=(r,c)=>Array.from({length:9},(_,i)=>i+1).filter(n=>!grid[r].includes(n)&&!grid.some(row=>row[c]===n)&&!grid.slice(Math.floor(r/3)*3,Math.floor(r/3)*3+3).some(row=>row.slice(Math.floor(c/3)*3,Math.floor(c/3)*3+3).includes(n)));
  function solve(){
    if(solutions>1)return;
    let best=null;
    for(let r=0;r<9;r++)for(let c=0;c<9;c++)if(!grid[r][c]){const ns=candidates(r,c);if(!ns.length)return;if(!best||ns.length<best.ns.length)best={r,c,ns};}
    if(!best){solutions++;solution=grid.map(row=>[...row]);return;}
    for(const n of best.ns){grid[best.r][best.c]=n;solve();grid[best.r][best.c]=0;}
  }
  solve(); assert.equal(solutions,1,'Practice grid must have exactly one solution');
  for(const [coord,notes] of Object.entries(p.notes)) { const [r,c]=coord.split(',').map(Number); assert.ok(notes.includes(solution[r][c]),'Notes must retain solution digit'); }
  for(const entry of expected){const[r,c,n]=entry.split(',').map(Number);assert.equal(solution[r][c]===n,p.answerType==='placeValue');}
  assert.ok(describeSolution(p).reason.length > 20); count++;
}
assert.equal(count, 4);
console.log(`PASS: ${count} practice grids, unique solutions, candidate integrity, exact answers, invalid answers, and pair eliminations.`);
