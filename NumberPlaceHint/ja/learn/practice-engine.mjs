// Pure answer logic, shared by the browser UI and the Node validation script.
export function key(row, col, candidate) { return `${row},${col},${candidate}`; }
export function isCorrect(puzzle, selected) {
  return puzzle.acceptedSolutions.some(solution => {
    const expected = puzzle.answerType === 'placeValue'
      ? [key(solution.cell.row, solution.cell.col, solution.value)]
      : solution.eliminations.map(e => key(e.row, e.col, e.candidate));
    return expected.length === selected.size && expected.every(value => selected.has(value));
  });
}
export function describeSolution(puzzle) {
  const s = puzzle.acceptedSolutions[0];
  if (puzzle.answerType === 'placeValue') {
    return { reason: `${s.cell.row + 1}行${s.cell.col + 1}列の候補は${s.value}だけです。ほかの数字は候補から除かれているため、このマスは${s.value}と確定できます。`, effect: `回答：${s.cell.row + 1}行${s.cell.col + 1}列に${s.value}を入れます。` };
  }
  const coords = s.patternCells.map(c => `${c.row + 1}行${c.col + 1}列`).join('と');
  const digits = s.explanationData.patternCandidates.join('・');
  const u = s.explanationData.primaryUnit;
  const unit = u.type === 'row' ? `${u.index + 1}行目` : u.type === 'column' ? `${u.index + 1}列目` : `${u.index + 1}番目のブロック`;
  const eliminations = s.eliminations.map(e => `${e.row + 1}行${e.col + 1}列の${e.candidate}`).join('、');
  return { reason: `${coords}は、候補がどちらも${digits}だけです。この2マスには${digits}が1つずつ入るため、${unit}のほかのマスからは、この2つの数字を候補から外せます。`, effect: `削除できる候補：${eliminations}。ペアのどちらにどの数字が入るかは、まだ決まりません。` };
}
