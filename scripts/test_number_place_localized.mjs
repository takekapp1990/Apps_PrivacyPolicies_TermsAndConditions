import {readFileSync} from 'node:fs';
import {runInNewContext} from 'node:vm';
import assert from 'node:assert/strict';
const root=new URL('../',import.meta.url);
const locales=JSON.parse(readFileSync(new URL('NumberPlaceHint/learning-locales/locales.json',root)));
const examples=JSON.parse(readFileSync(new URL('NumberPlaceHint/ja/learn/practice-data.json',root)));
let moves=0,answers=0;
for(const code of Object.keys(locales.languages)){
 const base=`NumberPlaceHint/${code}/learn/`;
 const context={window:{matchMedia:()=>({matches:false,addEventListener(){}})},document:{querySelectorAll:()=>[],querySelector:()=>null},setTimeout,clearTimeout};
 const xp=readFileSync(new URL(base+'experience-browser.js',root),'utf8');
 const instrumented=xp.replace(/\}\)\(\);\s*$/,'globalThis.result={nextStep,complete,DEMO,SOLUTION};})();');
 runInNewContext(instrumented,context,{timeout:1000});
 const engine=context.result;let board=[...engine.DEMO],count=0;
 while(!engine.complete(board)){
  const step=engine.nextStep(board);assert.ok(step,code);assert.equal(step.value,engine.SOLUTION[step.index]);
  assert.ok(step.reason.length>5);assert.ok(!/\{(?:cell|value|row|col)\}/.test(step.reason),code);
  board[step.index]=step.value;count++;assert.ok(count<=51);
 }
 assert.equal(count,51,code);moves+=count;
 const learning=readFileSync(new URL(base+'learning-browser.js',root),'utf8');
 const pc={...context};runInNewContext(learning.replace(/\}\)\(\);\s*$/,'globalThis.practice={isCorrect,describeSolution};})();'),pc,{timeout:1000});
 for(const puzzles of Object.values(examples))for(const puzzle of puzzles){
  const s=puzzle.acceptedSolutions[0];const selected=new Set(puzzle.answerType==='placeValue'?[`${s.cell.row},${s.cell.col},${s.value}`]:s.eliminations.map(e=>`${e.row},${e.col},${e.candidate}`));
  assert.equal(pc.practice.isCorrect(puzzle,selected),true,code);assert.equal(pc.practice.isCorrect(puzzle,new Set()),false,code);
  const description=pc.practice.describeSolution(puzzle);assert.ok(description.reason.length>5);assert.ok(!/\{\w+\}/.test(description.reason+description.effect),code);answers++;
 }
}
console.log(`PASS: ${moves} localized logical demo steps; ${answers} correct and incorrect practice answers; no unresolved dynamic variables.`);
