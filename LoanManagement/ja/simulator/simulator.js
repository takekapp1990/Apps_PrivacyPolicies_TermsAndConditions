(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const yen = value => `${Math.round(value).toLocaleString('ja-JP')}円`;
  const man = value => `${(Math.round(value / 1000) / 10).toLocaleString('ja-JP')}万円`;
  const period = months => months === 0 ? '今すぐ完済' : `${Math.floor(months / 12) ? `${Math.floor(months / 12)}年` : ''}${months % 12 ? `${months % 12}か月` : ''}`;
  const duration = months => months === 0 ? '0か月' : period(months);
  const rateLabel = value => Number(value.toFixed(3)).toLocaleString('ja-JP', { maximumFractionDigits: 3 });
  const moneyChange = (value, baseline, prefix = '月々') => {
    const difference = Math.round(value - baseline);
    if (difference === 0) return `${prefix} 変わらない`;
    return `${prefix ? `${prefix} ` : ''}${yen(Math.abs(difference))}${difference > 0 ? '増' : '減'}`;
  };
  const periodChange = (value, baseline) => {
    const difference = value - baseline;
    if (difference === 0) return '完済時期 変わらない';
    return `完済時期 ${duration(Math.abs(difference))}${difference > 0 ? '延長' : '短縮'}`;
  };
  const interestChange = (value, baseline) => {
    const difference = Math.round(value - baseline);
    if (difference === 0) return '残りの利息総額 変わらない';
    return `残りの利息総額 ${yen(Math.abs(difference))}${difference > 0 ? '増' : '減'}`;
  };
  const currentMoneyChange = (value, baseline) => {
    const difference = Math.round(value - baseline);
    if (difference === 0) return '現状と変わらない';
    return `現状から${yen(Math.abs(difference))}${difference > 0 ? '増加' : '減少'}`;
  };
  const currentPeriodChange = (value, baseline) => {
    const difference = value - baseline;
    if (difference === 0) return '現状と変わらない';
    return `現状から${duration(Math.abs(difference))}${difference > 0 ? '延長' : '短縮'}`;
  };
  const currentInterestChange = (value, baseline) => {
    const difference = Math.round(value - baseline);
    if (difference === 0) return '現状と変わらない';
    return `現状から約${man(Math.abs(difference))}${difference > 0 ? '増加' : '減少'}`;
  };
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const placeholder = $('result-content').innerHTML;
  const drafts = { current: { balance: '', payment: '', rate: '' }, new: { balance: '', rate: '' } };
  let mode = 'prepayment';
  let hasResult = false;
  let example = false;
  const started = new Set();
  const ratePresets = {
    gradual: { label: 'ゆるやか', deltas: [[12, .25], [36, .5], [60, .75]] },
    standard: { label: '標準', deltas: [[12, .5], [36, 1], [60, 1.5]] },
    strong: { label: '大きめ', deltas: [[12, 1], [36, 2], [60, 3]] }
  };
  const copy = {
    prepayment: {intro:'現在の状況と契約期間から、繰上げ効果を比較。', scope:'返済開始月と当初期間から残り期間を計算します。5年ルールでは見直し基準月の残債と残期間から返済額を再計算します。', cta:'繰上げ返済後の毎月の変化まで、詳しく。', description:'アプリなら繰上げ返済前後の返済明細を月ごとに確認できます。元金・利息・返済後残高を見ながら、時期や金額を変えて計画を比べられます。'},
    rate: {intro:'現在の契約期間で、金利が上がった先を比較。', scope:'現在の金利から残り期間を逆算せず、契約期間を使います。5年ルールでは見直し時点の残債と残期間から返済額を再計算します。', cta:'金利が上がった後の返済明細まで、詳しく。', description:'アプリなら残債や金利の変更を記録し、複数の将来シナリオを比較できます。各ケースの月々の返済額・元金・利息・残高も確認できます。'},
    new: {intro:'借入額を共通に、金利・期間・返済方式を比較。', scope:'入力条件を基準に、選んだ金利差・期間差・返済方式を比較します。諸費用は含みません。', cta:'借りた後の毎月の返済も、見える化。', description:'アプリなら借入条件を保存し、毎月の返済額・元金・利息・返済後残高を返済明細で確認できます。残債や完済予定もまとめて管理できます。'}
  };
  const now = new Date();
  const currentMonth = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;
  $('repayment-start').max = currentMonth;
  for (const id of ['original-term-years', 'years', 'new-custom-years']) {
    for (let year = 1; year <= 50; year++) {
      const option = document.createElement('option');
      option.value = String(year); option.textContent = `${year}年`;
      $(id).append(option);
    }
    $(id).value = '35';
  }
  for (const id of ['bonus-month-1', 'bonus-month-2', 'new-bonus-month-1', 'new-bonus-month-2']) {
    for (let month = 1; month <= 12; month++) {
      const option = document.createElement('option');
      option.value = String(month); option.textContent = `${month}月`;
      $(id).append(option);
    }
  }
  $('bonus-month-1').value = '6'; $('bonus-month-2').value = '12';
  $('new-bonus-month-1').value = '6'; $('new-bonus-month-2').value = '12';
  $('new-start').value = currentMonth;
  function track(event) {
    if (typeof window.gtag === 'function') window.gtag('event', event, { simulator_type: mode, example_input: example });
  }
  function clearError() {
    $('form-error').hidden = true;
    document.querySelectorAll('[aria-invalid]').forEach(el => el.removeAttribute('aria-invalid'));
  }
  function markChanged() {
    example = false;
    clearError();
    if (!started.has(mode)) { started.add(mode); track('simulator_start'); }
    if (hasResult) {
      $('stale-note').hidden = false;
      $('result-area').classList.add('result-stale');
      $('result-badge').textContent = '再計算が必要です';
    }
  }
  function switchMode(next, updateHash = true) {
    if (!copy[next]) return;
    const previousGroup = mode === 'new' ? 'new' : 'current';
    const nextGroup = next === 'new' ? 'new' : 'current';
    if (previousGroup !== nextGroup) {
      for (const key of Object.keys(drafts[previousGroup])) drafts[previousGroup][key] = $(key).value;
      for (const key of Object.keys(drafts[nextGroup])) $(key).value = drafts[nextGroup][key];
    }
    mode = next;
    tabs.forEach(tab => {
      const selected = tab.dataset.mode === mode;
      tab.setAttribute('aria-selected', String(selected));
      tab.tabIndex = selected ? 0 : -1;
      const panel = $(`panel-${tab.dataset.mode}`);
      panel.hidden = !selected;
      panel.querySelectorAll('input,select').forEach(el => { el.disabled = !selected; });
    });
    $('payment-field').hidden = mode === 'new';
    $('payment').disabled = mode === 'new';
    $('current-bonus-section').hidden = mode === 'new';
    $('current-term-fields').hidden = mode === 'new';
    $('current-term-fields').querySelectorAll('input,select').forEach(el => { el.disabled = mode === 'new'; });
    $('contract-details').hidden = mode === 'new';
    $('contract-details').querySelectorAll('input,select').forEach(el => { el.disabled = mode === 'new' || (el.closest('#five-year-fields') && !$('five-year-rule').checked); });
    updateContractFields();
    updateCustomRateFields();
    updateNewFields();
    $('balance-label').textContent = mode === 'new' ? '借りたい金額' : '今の残債';
    $('balance-hint').textContent = mode === 'new' ? '頭金を差し引いた借入額（1〜100,000万円）' : '現在のローン残高（1〜100,000万円）';
    $('rate-label').textContent = mode === 'new' ? '借入金利（年利）' : '現在の適用金利（年利）';
    $('rate-hint').textContent = mode === 'new' ? '新たに借り入れる際の年利を入力してください。' : '現在の返済に適用されている年利（0〜10%）を入力してください。';
    $('form-intro').textContent = copy[mode].intro;
    $('scope-note').textContent = copy[mode].scope;
    $('app-title').textContent = copy[mode].cta;
    $('app-description').textContent = copy[mode].description;
    $('result-content').innerHTML = placeholder;
    $('result-badge').textContent = '入力すると表示';
    $('result-badge').classList.remove('ready');
    $('stale-note').hidden = true;
    $('result-area').classList.remove('result-stale');
    $('result-announcement').textContent = '';
    hasResult = false; example = false; clearError();
    if (updateHash) history.replaceState(null, '', `#${mode}`);
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => switchMode(tab.dataset.mode));
    tab.addEventListener('keydown', event => {
      let target;
      if (event.key === 'ArrowRight') target = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') target = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') target = 0;
      if (event.key === 'End') target = tabs.length - 1;
      if (target !== undefined) { event.preventDefault(); switchMode(tabs[target].dataset.mode); tabs[target].focus(); }
    });
  });
  $('loan-form').addEventListener('input', markChanged);
  $('loan-form').addEventListener('change', markChanged);
  function updateContractFields() {
    const fiveYear = $('five-year-rule').checked;
    const bonus = $('bonus-enabled').checked;
    $('five-year-fields').hidden = !fiveYear;
    $('five-year-fields').querySelectorAll('input,select').forEach(el => { el.disabled = !fiveYear || mode === 'new'; });
    $('bonus-fields').hidden = !bonus;
    $('bonus-fields').querySelectorAll('input,select').forEach(el => { el.disabled = !bonus || mode === 'new'; });
    if (!fiveYear) $('cap-rule').checked = false;
  }
  function updateCustomRateFields() {
    const enabled = $('custom-rate-enabled').checked;
    $('custom-rate-fields').hidden = !enabled;
    $('custom-rate-fields').querySelectorAll('input,select').forEach(el => { el.disabled = !enabled || mode !== 'rate'; });
  }
  function updateNewFields() {
    const customEnabled = $('new-custom-enabled').checked;
    const bonusEnabled = $('new-bonus-enabled').checked;
    $('new-custom-fields').hidden = !customEnabled;
    $('new-custom-fields').querySelectorAll('input,select').forEach(el => { el.disabled = !customEnabled || mode !== 'new'; });
    $('new-bonus-fields').hidden = !bonusEnabled;
    $('new-bonus-fields').querySelectorAll('input,select').forEach(el => { el.disabled = !bonusEnabled || mode !== 'new'; });
  }
  $('five-year-rule').addEventListener('change', updateContractFields);
  $('bonus-enabled').addEventListener('change', updateContractFields);
  $('custom-rate-enabled').addEventListener('change', updateCustomRateFields);
  $('new-custom-enabled').addEventListener('change', updateNewFields);
  $('new-bonus-enabled').addEventListener('change', updateNewFields);
  document.querySelectorAll('[data-extra]').forEach(button => button.addEventListener('click', () => {
    $('extra').value = button.dataset.extra; markChanged(); $('extra').focus();
  }));
  $('example').addEventListener('click', () => {
    $('balance').value = mode === 'new' ? '3500' : '3000';
    $('payment').value = '10'; $('rate').value = mode === 'new' ? '1' : '0.8';
    if (mode === 'prepayment') { $('extra').value = '100'; $('prepayment-after').value = '0'; }
    if (mode === 'rate') {
      document.querySelectorAll('[data-rate-scenario]').forEach(input => { input.checked = input.dataset.rateScenario === 'standard'; });
      $('custom-rate-enabled').checked = false;
      for (let i = 1; i <= 3; i++) $('custom-rate-' + i).value = '';
      updateCustomRateFields();
    }
    if (mode === 'new') {
      $('years').value = '35';
      document.querySelectorAll('[data-new-scenario]').forEach(input => { input.checked = ['higher-rate','shorter','principal'].includes(input.dataset.newScenario); });
      $('new-custom-enabled').checked = false;
      $('new-custom-rate').value = ''; $('new-custom-years').value = '35';
      $('new-bonus-enabled').checked = false; $('new-bonus-principal').value = '';
      $('new-start').value = currentMonth;
      updateNewFields();
    }
    if (mode !== 'new') {
      const exampleStart = new Date(now.getFullYear() - 5, now.getMonth(), 1);
      $('repayment-start').value = `${exampleStart.getFullYear()}-${String(exampleStart.getMonth() + 1).padStart(2, '0')}`;
      $('original-term-years').value = '35';
      $('five-year-rule').checked = true; $('cap-rule').checked = true;
      $('payment-review-base-month').value = '10';
      $('term-payment-update').checked = false;
      $('bonus-enabled').checked = false; updateContractFields();
    }
    markChanged(); example = true; $('loan-form').requestSubmit();
  });
  function number(id, label, min, max, multiplier = 1, integer = false) {
    const field = $(id);
    const normalized = field.value.normalize('NFKC').trim().replace(/,/g, '');
    const value = Number(normalized);
    const scaled = value * multiplier;
    if (!/^\d+(?:\.\d+)?$/.test(normalized) || !Number.isFinite(value) || value < min || value > max ||
      ((integer || multiplier > 1) && Math.abs(scaled - Math.round(scaled)) > 1e-6)) {
      field.setAttribute('aria-invalid', 'true'); field.focus();
      throw new Error(`${label}は${min.toLocaleString('ja-JP')}〜${max.toLocaleString('ja-JP')}の範囲で${integer ? '整数で' : ''}入力してください。${multiplier > 1 ? '金額は円単位まで入力できます。' : ''}`);
    }
    return multiplier > 1 ? Math.round(scaled) : value;
  }
  function readRequest() {
    const request = { mode, balance: number('balance', mode === 'new' ? '借入額（万円）' : '残債（万円）', 1, 100000, 10000), rate: number('rate', mode === 'new' ? '借入金利（年利）' : '現在の適用金利（年利）', 0, mode === 'new' ? 20 : 10) };
    if (mode === 'new') {
      const years = number('years', '返済期間（年）', 1, 50, 1, true);
      request.months = years * 12;
      request.newScenarios = [{ id:'baseline', label:`入力条件（年${rateLabel(request.rate)}%・${years}年）`, rate:request.rate, months:request.months, equalPrincipal:false }];
      document.querySelectorAll('[data-new-scenario]:checked').forEach(input => {
        const type = input.dataset.newScenario;
        if (type === 'lower-rate') {
          if (request.rate < .25) throw new Error('金利が0.25ポイント低い条件は0%未満になるため比較できません。');
          request.newScenarios.push({ id:type, label:`金利低め（年${rateLabel(request.rate-.25)}%）`, rate:request.rate-.25, months:request.months, equalPrincipal:false });
        }
        if (type === 'higher-rate') {
          if (request.rate > 19.5) throw new Error('金利が0.5ポイント高い条件は20%を超えるため比較できません。');
          request.newScenarios.push({ id:type, label:`金利高め（年${rateLabel(request.rate+.5)}%）`, rate:request.rate+.5, months:request.months, equalPrincipal:false });
        }
        if (type === 'shorter') {
          if (years <= 5) throw new Error('5年短い返済期間を比較するには、基準の返済期間を6年以上にしてください。');
          request.newScenarios.push({ id:type, label:`期間短め（${years-5}年）`, rate:request.rate, months:(years-5)*12, equalPrincipal:false });
        }
        if (type === 'longer') {
          if (years > 45) throw new Error('5年長い返済期間は50年を超えるため比較できません。');
          request.newScenarios.push({ id:type, label:`期間長め（${years+5}年）`, rate:request.rate, months:(years+5)*12, equalPrincipal:false });
        }
        if (type === 'principal') request.newScenarios.push({ id:type, label:'元金均等（入力条件）', rate:request.rate, months:request.months, equalPrincipal:true });
      });
      if ($('new-custom-enabled').checked) {
        const customRate = number('new-custom-rate', '独自条件の金利（年利）', 0, 20);
        const customYears = number('new-custom-years', '独自条件の返済期間（年）', 1, 50, 1, true);
        request.newScenarios.push({ id:'custom-new', label:`独自条件（年${rateLabel(customRate)}%・${customYears}年）`, rate:customRate, months:customYears*12, equalPrincipal:false });
      }
      if ($('new-bonus-enabled').checked) {
        request.newBonusPrincipal = number('new-bonus-principal', 'ボーナス返済に割り当てる元本（万円）', .0001, 100000, 10000);
        if (request.newBonusPrincipal >= request.balance) { $('new-bonus-principal').setAttribute('aria-invalid','true'); $('new-bonus-principal').focus(); throw new Error('ボーナス返済に割り当てる元本は、借入額より小さくしてください。'); }
        request.newBonusMonth1 = Number($('new-bonus-month-1').value); request.newBonusMonth2 = Number($('new-bonus-month-2').value);
        if (request.newBonusMonth1 === request.newBonusMonth2) { $('new-bonus-month-2').setAttribute('aria-invalid','true'); $('new-bonus-month-2').focus(); throw new Error('ボーナス返済月は異なる月を選んでください。'); }
        const startMatch = /^(\d{4})-(\d{2})$/.exec($('new-start').value);
        if (!startMatch) { $('new-start').setAttribute('aria-invalid','true'); $('new-start').focus(); throw new Error('返済開始月を入力してください。'); }
        request.newStartYear = Number(startMatch[1]); request.newStartMonth = Number(startMatch[2]);
      }
    }
    else {
      request.payment = number('payment', '現在の月々の返済額（万円）', 0.0001, 1000, 10000);
      request.asOfYear = now.getFullYear(); request.asOfMonth = now.getMonth() + 1;
      const match = /^(\d{4})-(\d{2})$/.exec($('repayment-start').value);
      if (!match) { $('repayment-start').setAttribute('aria-invalid', 'true'); $('repayment-start').focus(); throw new Error('返済開始月を入力してください。'); }
      request.repaymentStartYear = Number(match[1]); request.repaymentStartMonth = Number(match[2]);
      request.originalTermMonths = number('original-term-years', '当初の返済期間（年）', 1, 50, 1, true) * 12;
      request.applyFiveYearRule = $('five-year-rule').checked;
      request.apply125PercentCap = $('cap-rule').checked;
      request.paymentReviewBaseMonth = Number($('payment-review-base-month').value);
      if ($('bonus-enabled').checked) {
        request.bonusPayment = number('bonus-payment', 'ボーナス月の追加返済額（万円）', 0.0001, 100000, 10000);
        request.bonusMonth1 = Number($('bonus-month-1').value); request.bonusMonth2 = Number($('bonus-month-2').value);
        if (request.bonusMonth1 === request.bonusMonth2) { $('bonus-month-2').setAttribute('aria-invalid', 'true'); $('bonus-month-2').focus(); throw new Error('ボーナス返済月は異なる月を選んでください。'); }
      }
      const annualPayment = request.payment * 12 + (request.bonusPayment || 0) * (request.bonusPayment ? 2 : 0);
      if (!request.applyFiveYearRule && annualPayment <= request.balance * request.rate / 100) {
        $('rate').setAttribute('aria-invalid', 'true'); $('rate').focus();
        throw new Error('現在の適用金利に対して返済額が利息以下になります。金利・月々の返済額・ボーナス返済額を確認してください。');
      }
      if (mode === 'prepayment') {
        request.afterMonths = Number($('prepayment-after').value);
        request.extra = number('extra', '繰上げ返済額（万円）', 0.0001, 100000, 10000);
        request.recalculateTermPayment = $('term-payment-update').checked;
      }
      if (mode === 'rate') {
        request.afterMonths = 0;
        request.rateScenarios = [];
        document.querySelectorAll('[data-rate-scenario]:checked').forEach(input => {
          const preset = ratePresets[input.dataset.rateScenario];
          const steps = preset.deltas.map(([afterMonths, delta]) => ({ afterMonths, rate: request.rate + delta }));
          if (steps.some(step => step.rate > 20)) throw new Error(`${preset.label}シナリオでは年利20%を超えます。独自シナリオで入力してください。`);
          request.rateScenarios.push({ id: input.dataset.rateScenario, label: `${preset.label}シナリオ`, steps });
        });
        if ($('custom-rate-enabled').checked) {
          const steps = [];
          for (let i = 1; i <= 3; i++) {
            if (!$('custom-rate-' + i).value.trim()) continue;
            steps.push({ afterMonths: Number($('custom-rate-after-' + i).value), rate: number('custom-rate-' + i, `${i}段階目の年利（%）`, 0, 20) });
          }
          if (!steps.length) throw new Error('独自シナリオの金利を1段階以上入力してください。');
          request.rateScenarios.push({ id: 'custom', label: '独自シナリオ', steps });
        }
        if (!request.rateScenarios.length) throw new Error('比較する金利上昇シナリオを1つ以上選んでください。');
      }
    }
    return request;
  }
  function graph(plans, principal) {
    const colors = ['#8596a9','#197767','#c08036','#5578b8','#915f9d','#b54c5f','#467c9d'];
    const maxMonths = Math.max(...plans.map(p => p.months));
    const x = month => 62 + month / maxMonths * 478;
    const y = amount => 173 - amount / principal * 142;
    let grid = '';
    for (let i = 0; i <= 2; i++) {
      const value = principal * i / 2;
      grid += `<line x1="62" y1="${y(value)}" x2="540" y2="${y(value)}" stroke="#e5ebf1"/><text x="53" y="${y(value)+4}" text-anchor="end" font-size="10" fill="#596b7d">${Math.round(value/10000).toLocaleString('ja-JP')}</text>`;
    }
    for (const month of [...new Set([0,Math.round(maxMonths / 2),maxMonths])]) {
      grid += `<text x="${x(month)}" y="195" text-anchor="middle" font-size="10" fill="#596b7d">${month === 0 ? '現在' : `${(month / 12).toFixed(1)}年後`}</text>`;
    }
    const lines = plans.map((p, index) => {
      let points = p.balances.map((balance, month) => `${x(month).toFixed(2)},${y(balance).toFixed(2)}`);
      if (p.months < maxMonths) points.push(`${x(maxMonths)},${y(0)}`);
      return `<polyline points="${points.join(' ')}" fill="none" stroke="${colors[index]}" stroke-width="${index === 0 ? 2 : 2.5}" ${index === 0 ? 'stroke-dasharray="5 4"' : ''} stroke-linejoin="round"/>`;
    }).join('');
    return `<div class="result-block"><h3>これからの残債の推移</h3><div class="legend">${plans.map((p,i) => `<span><i style="--color:${colors[i]}"></i>${escape(p.label)}</span>`).join('')}</div><svg class="chart" viewBox="0 0 560 212" role="img" aria-label="比較条件ごとの残債の推移。数値は上の比較表に記載しています。"><text x="13" y="16" font-size="10" fill="#596b7d">万円</text>${grid}${lines}</svg></div>`;
  }
  function table(plans, request) {
    const isNew = request.mode === 'new';
    const baseline = plans[0];
    const rows = plans.map((p, i) => {
      const difference = i === 0 ? '<span class="difference-base">比較の基準</span>' : `<span>${moneyChange(p.monthly,baseline.monthly)}</span><span>${periodChange(p.months,baseline.months)}</span><span>${interestChange(p.interest,baseline.interest)}</span>`;
      return `<tr class="${i === 0 ? 'baseline' : 'accent-row'}"><th scope="row">${escape(p.label)}</th><td>${yen(p.monthly)}</td><td>${period(p.months)}</td><td>${yen(p.interest)}</td><td class="difference-cell">${difference}</td></tr>`;
    }).join('');
    const totalRows = plans.map(p => `<tr><th scope="row">${escape(p.label)}</th><td>${yen(p.total)}</td></tr>`).join('');
    const monthlyHeading = isNew ? '通常月／初回' : request.mode === 'rate' ? '通常月の最大額' : '通常月の返済額';
    const monthlyNote = request.mode === 'rate' ? '表示額はボーナス加算分を除く通常月返済額のうち、試算期間内で最も高い金額です。' : '表示額はボーナス加算分を除く通常月の返済額です。';
    return `<div class="result-block"><h3>${isNew ? '同じ借入額で比較' : '同じ条件で比較'}</h3><div class="table-scroll" tabindex="0" role="region" aria-label="返済額と利息の比較表。横にスクロールできます。"><table class="comparison-table"><thead><tr><th scope="col">返済プラン</th><th scope="col">${monthlyHeading}</th><th scope="col">${isNew ? '返済期間' : '今から完済まで'}</th><th scope="col">${isNew ? '利息総額' : '残りの利息総額'}</th><th scope="col">${isNew ? '入力条件との差' : 'いまのままとの差'}</th></tr></thead><tbody>${rows}</tbody></table></div><p class="result-note">${isNew ? '元利均等は通常月の返済額がほぼ一定です。元金均等の欄は初回の通常月返済額で、その後徐々に減ります。差分は入力条件を基準にしています。' : `${monthlyNote} 差分は「いまのまま」を基準にしています。`} 最終回の返済額は調整されます。</p><details class="result-note"><summary>元本を含む${isNew ? '' : '今後の'}支払総額を見る</summary><table class="comparison-table"><thead><tr><th scope="col">返済プラン</th><th scope="col">支払総額</th></tr></thead><tbody>${totalRows}</tbody></table>${request.mode === 'prepayment' ? '<p>支払総額には繰上げ返済額を含みます。</p>' : ''}</details></div>`;
  }
  function render(result, request) {
    const [base, ...others] = result.plans;
    let highlight, cards, notes;
    const when = request.afterMonths === 0 ? '次回の返済前' : `${duration(request.afterMonths)}分の通常返済の後`;
    if (request.mode === 'prepayment') {
      const [term, payment] = others;
      const planMetric = (label, value, change) => `<div><dt>${label}</dt><dd><b class="plan-change">${change}</b><small class="plan-value">試算後 ${value}</small></dd></div>`;
      const planCard = (title, caption, plan) => `<section class="prepayment-plan-card"><div class="plan-card-heading"><h4>${title}</h4><p>${caption}</p></div><dl>${planMetric('残りの利息総額',yen(plan.interest),currentInterestChange(plan.interest,base.interest))}${planMetric('月々の返済額',yen(plan.monthly),currentMoneyChange(plan.monthly,base.monthly))}${planMetric('今から完済まで',period(plan.months),currentPeriodChange(plan.months,base.months))}</dl></section>`;
      highlight = `<div class="prepayment-highlight-head"><div><p class="eyebrow">2つの方法を同じ基準で比較</p><h3>${when}に<strong>${man(request.extra)}</strong>を繰上げ返済した場合</h3></div><button class="plan-info-button" type="button" data-open-prepayment-info aria-haspopup="dialog"><span aria-hidden="true">i</span> 2つの方式の違い</button></div><div class="prepayment-plan-cards">${planCard('期間短縮型',request.recalculateTermPayment ? '繰上げ時に返済額を再計算' : '繰上げ時の返済額は据え置き',term)}${planCard('返済額軽減型','契約上の完済時期を維持',payment)}</div><p class="highlight-sub">差分は「いまのまま」を基準にしています。手数料・住宅ローン控除の影響は含みません。</p>`;
      cards = '';
      const termPaymentPolicy = request.recalculateTermPayment ? '期間短縮型は、繰上げ時点で短縮後の期間に合わせて通常月の返済額も再計算します。' : '期間短縮型は、繰上げ時点では通常月の返済額を据え置きます。';
      notes = `繰上げ時点の残債は${yen(result.balanceAtChange)}の見込み。繰上げ返済後も年${rateLabel(request.rate)}%が続く前提です。${termPaymentPolicy}${request.applyFiveYearRule ? ` 5年ルールに基づき、${request.paymentReviewBaseMonth}月を5回経過した時点の残債・残期間から返済額を再計算します。` : ' 5年ルールは適用していません。'}${request.apply125PercentCap ? ' 見直し後の通常月返済額には、直前額の125%上限を適用します。' : ''}${request.bonusPayment ? ` ボーナス月は年2回、通常返済に${yen(request.bonusPayment)}を加算します。` : ''}${request.extra === result.balanceAtChange ? '今回は全額返済のため、両方式の結果は同じです。' : ''}`;
    } else if (request.mode === 'rate') {
      const target = others.find(p => p.id === 'standard') || others[0];
      const monthlyDelta = target.monthly-base.monthly;
      const reviewTiming = target.reviewAfterMonths == null ? '見直しなし' : target.reviewAfterMonths === 0 ? '次回の返済から' : `${duration(target.reviewAfterMonths)}後`;
      const comparisonBasis = request.applyFiveYearRule ? '「いまのまま」の通常月最大額より' : '現在の返済額より';
      const ratePath = target.steps.map(step => `${step.afterMonths === 0 ? '次回から' : `${duration(step.afterMonths)}後`} 年${rateLabel(step.rate)}%`).join(' → ');
      highlight = `<p class="eyebrow">${escape(target.label)}｜${escape(ratePath)}</p><h3>通常月の返済額は最大で <strong>${yen(target.monthly)}</strong></h3><p class="highlight-sub">${comparisonBasis} ${moneyChange(target.monthly,base.monthly,'')}。契約上の完済時期を維持して再計算しています。</p>`;
      cards = `<div class="metric-card"><h3>残りの利息総額の変化</h3><p>約${man(Math.abs(target.interest-base.interest))}${target.interest < base.interest ? '減' : '増'}</p><small>${escape(target.label)}との比較</small></div><div class="metric-card"><h3>最初に返済額を見直す時期</h3><p>${reviewTiming}</p><small>${request.applyFiveYearRule ? `${request.paymentReviewBaseMonth}月を5回経過後、3か月後から反映` : '各金利上昇の時点で再計算'}</small></div>`;
      notes = `<strong>${others.length}件の上昇シナリオを比較しています。${escape(target.label)}は ${escape(ratePath)} の想定です。</strong> ${request.applyFiveYearRule ? `5年ルールを反映し、${request.paymentReviewBaseMonth}月を5回経過するまでは現在の返済額を据え置き、反映直前の残債・その時点の適用金利・残期間から新返済額を計算して3か月後から反映します。「いまのまま」も同じ見直し日に現在金利で再計算します。` : '各段階で通常月の返済額を見直します。'}${request.apply125PercentCap ? ' 見直し額には直前の通常月返済額の125%上限を適用します。最終回に残額を精算する場合があります。' : ''}${request.bonusPayment ? ` ボーナス月は通常返済に${yen(request.bonusPayment)}を加算します。` : ''}`;
    } else {
      const bonusText = base.firstBonusMonthPayment == null ? '' : `／ボーナス月 ${yen(base.firstBonusMonthPayment)}`;
      highlight = `<p class="eyebrow">入力条件｜元利均等返済</p><h3>通常月の返済額は <strong>${yen(base.monthly)}</strong></h3><p class="highlight-sub">借入${man(request.balance)}・年${rateLabel(request.rate)}%・${period(request.months)}返済${bonusText}</p>`;
      cards = `<div class="metric-card"><h3>初年度の返済額</h3><p>約${man(base.firstYearPayment)}</p><small>${request.newBonusPrincipal ? '年2回のボーナス返済を含む' : '通常月の返済額を12か月分'}</small></div><div class="metric-card"><h3>入力条件の利息総額</h3><p>約${man(base.interest)}</p><small>支払総額 ${yen(base.total)}</small></div>`;
      notes = `<strong>入力条件を基準に${others.length}件の条件を比較しています。</strong> 各条件の金利は完済まで一定と仮定します。${request.newBonusPrincipal ? `すべての条件で、借入元本のうち${man(request.newBonusPrincipal)}を${request.newBonusMonth1}月・${request.newBonusMonth2}月のボーナス返済分に割り当てます。` : 'ボーナス返済は含めていません。'} 手数料・保証料等は含みません。`;
    }
    const summary = `${example ? '入力例での試算です。' : ''}${request.mode === 'new' ? `借入${man(request.balance)}を、入力条件と選択した比較条件で試算しています。` : `残債${man(request.balance)}・通常月${yen(request.payment)}・年${rateLabel(request.rate)}%。返済開始月と当初期間から、契約上の残り期間は${period(result.estimatedMonths)}です。`}`;
    const comparisonTable = request.mode === 'prepayment' ? '' : table(result.plans,request);
    $('result-content').innerHTML = `<p class="result-summary">${summary}</p><div class="highlight">${highlight}</div>${cards ? `<div class="comparison-cards">${cards}</div>` : ''}${comparisonTable}${graph(result.plans,request.balance)}<p class="condition-note">${notes}</p><a class="result-cta" href="#app-next">この先の返済計画を、アプリで管理する ↓</a>`;
    $('result-badge').textContent = example ? '入力例の結果' : '入力した条件での概算';
    $('result-badge').classList.add('ready');
    $('stale-note').hidden = true;
    $('result-area').classList.remove('result-stale');
    $('result-announcement').textContent = request.mode === 'prepayment' ? '試算が完了しました。2つの方式の結果と残債グラフを表示しています。' : '試算が完了しました。結果の比較表とグラフを表示しています。';
    hasResult = true;
    $('result-area').focus({preventScroll:true});
    if (window.matchMedia('(max-width:700px)').matches) $('result-area').scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block:'start'});
  }
  $('loan-form').addEventListener('submit', event => {
    event.preventDefault(); clearError();
    try {
      const request = readRequest();
      if (typeof window.loanSimulatorCalculate !== 'function') throw new Error('計算機能を読み込めませんでした。ページを再読み込みしてください。');
      const response = JSON.parse(window.loanSimulatorCalculate(JSON.stringify(request)));
      if (!response.ok) throw new Error(response.error);
      render(response.result,request); track('simulator_complete');
    } catch (error) {
      $('form-error').textContent = error.message;
      $('form-error').hidden = false;
      if (hasResult) {
        $('stale-note').hidden = false; $('result-area').classList.add('result-stale');
        $('result-badge').textContent = '再計算が必要です';
      }
      if (!$('loan-form').querySelector('[aria-invalid=true]')) $('form-error').scrollIntoView({block:'nearest'});
    }
  });
  const prepaymentInfoDialog = $('prepayment-info-dialog');
  document.addEventListener('click', event => {
    if (event.target.closest('[data-open-prepayment-info]')) {
      if (typeof prepaymentInfoDialog.showModal === 'function') prepaymentInfoDialog.showModal();
      else prepaymentInfoDialog.setAttribute('open', '');
    }
    if (event.target.closest('[data-close-prepayment-info]')) prepaymentInfoDialog.close();
  });
  prepaymentInfoDialog.addEventListener('click', event => {
    if (event.target === prepaymentInfoDialog) prepaymentInfoDialog.close();
  });
  window.addEventListener('hashchange', () => { const hash = location.hash.slice(1); if (copy[hash] && hash !== mode) switchMode(hash,false); });
  updateContractFields();
  updateCustomRateFields();
  updateNewFields();
  switchMode(copy[location.hash.slice(1)] ? location.hash.slice(1) : 'prepayment',false);
})();
