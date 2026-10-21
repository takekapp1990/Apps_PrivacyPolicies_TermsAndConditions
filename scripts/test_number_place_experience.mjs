import assert from 'node:assert/strict';
import {PUZZLE,SOLUTION,DEMO} from '../NumberPlaceHint/ja/learn/experience-data.mjs';
import {candidates,nextStep,completedUnits,complete,units} from '../NumberPlaceHint/ja/learn/sudoku-engine.mjs';
assert.equal(PUZZLE.length,81);assert.equal(new Set(units.map(u=>u.join(','))).size,27);
assert.ok(complete(SOLUTION));assert.equal(complete(PUZZLE),false);
const invalid=[...SOLUTION];invalid[0]=invalid[1];assert.equal(complete(invalid),false);
for(const initial of [PUZZLE,DEMO]) {
 let board=[...initial],fills=0,unitCount=0;
 while(!complete(board)){
  const step=nextStep(board);assert.ok(step,'Trial and demo must be solvable with supported logical hints');
  assert.equal(board[step.index],0);assert.ok(candidates(board,step.index).includes(step.value));assert.equal(step.value,SOLUTION[step.index]);
  const before=[...board];board[step.index]=step.value;unitCount+=completedUnits(before,board).length;
  assert.ok(step.reason.includes(String(step.value)));assert.ok(++fills<=81);
 }
 assert.deepEqual(board,SOLUTION);
 assert.equal(fills,initial.filter(v=>!v).length);
 assert.equal(nextStep(board),null);
 assert.equal(completedUnits(board,board).length,0);
 assert.equal(unitCount,units.filter(u=>u.some(i=>!initial[i])).length);
 for(let i=0;i<81;i++)if(initial[i])assert.equal(initial[i],SOLUTION[i]);
 console.log(`PASS: ${fills} valid logical steps; unit completion counts verified.`);
}
assert.equal(DEMO.filter(v=>!v).length,51);
assert.deepEqual(DEMO,PUZZLE);
let solutions=0;
function solve(board){
 if(solutions>1)return;
 let best=null;
 for(let i=0;i<81;i++)if(!board[i]){const ns=candidates(board,i);if(!ns.length)return;if(!best||ns.length<best.ns.length)best={i,ns};}
 if(!best){assert.ok(complete(board));solutions++;return;}
 for(const n of best.ns){board[best.i]=n;solve(board);board[best.i]=0;}
}
solve([...PUZZLE]);assert.equal(solutions,1);
// Hidden single path: this valid puzzle has no naked singles at the start.
const hidden='030000000002105000000000507800001000000003001003920000001500084200010000040086070'.split('').map(Number);
const hs=nextStep(hidden);assert.ok(hs);assert.equal(hs.type,'hidden-single');
assert.deepEqual(PUZZLE,'530070000600195000098000060800060003400803001700020006060000280000419005000080079'.split('').map(Number));
console.log('PASS: unique trial solution, hidden single hints, complete/invalid grids, immutable initial data.');
