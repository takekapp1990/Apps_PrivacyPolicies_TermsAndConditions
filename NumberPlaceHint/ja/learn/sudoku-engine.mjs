export const related = (a,b) => Math.floor(a/9)===Math.floor(b/9)||a%9===b%9||(Math.floor(a/27)===Math.floor(b/27)&&Math.floor(a%9/3)===Math.floor(b%9/3));
export function candidates(board,index) {
  if(board[index])return [];
  return [1,2,3,4,5,6,7,8,9].filter(n=>!board.some((v,i)=>v===n&&related(i,index)));
}
export const units = [
  ...Array.from({length:9},(_,r)=>Array.from({length:9},(_,c)=>r*9+c)),
  ...Array.from({length:9},(_,c)=>Array.from({length:9},(_,r)=>r*9+c)),
  ...Array.from({length:9},(_,b)=>Array.from({length:9},(_,p)=>Math.floor(b/3)*27+(b%3)*3+Math.floor(p/3)*9+p%3)),
];
export const position = i => `${Math.floor(i/9)+1}行${i%9+1}列`;
export function nextStep(board) {
  for(let i=0;i<81;i++)if(!board[i]){
    const ns=candidates(board,i);
    if(ns.length===1)return {index:i,value:ns[0],type:'naked-single',reason:`${position(i)}は、同じ行・列・ブロックにある数字を除くと、候補が${ns[0]}だけになります。`};
  }
  for(let u=0;u<units.length;u++)for(let n=1;n<=9;n++){
    if(units[u].some(i=>board[i]===n))continue;
    const positions=units[u].filter(i=>candidates(board,i).includes(n));
    if(positions.length===1){
      const label=u<9?`${u+1}行目`:u<18?`${u-8}列目`:`${u-17}番目のブロック`;
      return {index:positions[0],value:n,type:'hidden-single',reason:`${label}で${n}を置けるのは${position(positions[0])}だけです。`};
    }
  }
  return null;
}
export function completedUnits(before,after) {
  return units.filter(u=>u.some(i=>!before[i])&&u.every(i=>after[i]));
}
export const complete = board => board.length===81&&units.every(u=>new Set(u.map(i=>board[i])).size===9&&u.every(i=>board[i]>=1&&board[i]<=9));
