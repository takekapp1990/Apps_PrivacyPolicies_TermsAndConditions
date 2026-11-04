const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../language-router.js'), 'utf8');
const entry = fs.readFileSync(path.join(__dirname, '../index.html'), 'utf8');
const inline = entry.match(/<script id="locale-entry">\n([\s\S]*?)\n<\/script>/)?.[1];
assert.equal(inline, source.trim());
assert.ok(entry.indexOf('<script id="locale-entry">') < entry.indexOf('<style>'));
assert.doesNotMatch(entry, /<link[^>]+rel="stylesheet"|<script[^>]+src=/);
assert.match(entry, /<noscript><meta http-equiv="refresh" content="3;url=\.\/en\/index\.html"><\/noscript>/);
assert.equal((entry.match(/data-language="/g) || []).length, 20);
function run(languages, saved, blocked = false, entry = true, failFirst = false) {
  const destinations = [];
  let stored;
  let fallback;
  let delay;
  const context = {
    window: {
      location: {search:'?ref=store', hash:'#features', replace: value => {
        destinations.push(value);
        if (failFirst && destinations.length === 1) throw Error('navigation blocked');
      }},
      setTimeout: (callback, milliseconds) => { fallback = callback; delay = milliseconds; }
    },
    navigator: { languages, language: languages[0] },
    localStorage: { getItem: () => { if(blocked) throw Error('blocked'); return saved; }, setItem: (key,value)=>stored=value },
    document: { documentElement: {hasAttribute:()=>entry}, addEventListener:()=>{} }
  };
  vm.runInNewContext(source, context);
  return {api:context.window.NemuCueLocale, destination:destinations[0], destinations, stored, fallback, delay};
}
const cases = [
  [['fr-CA','en'],'fr'], [['de-DE'],'de'], [['en-GB','ja'],'en'], [['xx','ko-KR'],'ko'],
  [['zh-TW'],'zh-Hant'], [['zh-HK'],'zh-Hant'], [['zh-MO'],'zh-Hant'], [['zh-CN'],'zh-Hans'],
  [['zh-SG'],'zh-Hans'], [['zh'],'zh-Hans'], [['zh-Hant-CN'],'zh-Hant'], [['zh-Hans-HK'],'zh-Hans'],
  [['pt-PT'],'pt-BR'], [['pt-BR'],'pt-BR'], [['ar-SA'],'ar'], [['hi-IN'],'hi'],
  [['es-MX'],'es'], [['uk-UA'],'uk'], [['vi-VN'],'vi'], [['th-TH'],'th'], [['xx'],'en'], [[], 'en']
];
for (const [languages, expected] of cases) {
  assert.equal(run(languages).destination, `./${expected}/index.html?ref=store#features`);
}
assert.equal(run(['ja'],'fr').destination,'./fr/index.html?ref=store#features');
assert.equal(run(['ja'],'../../bad').destination,'./ja/index.html?ref=store#features');
assert.equal(run(['ja'],'fr',true).destination,'./ja/index.html?ref=store#features');
const stalled = run(['ja']);
assert.equal(stalled.delay, 3000);
stalled.fallback();
assert.deepEqual(stalled.destinations, ['./ja/index.html?ref=store#features', './en/index.html?ref=store#features']);
const failed = run(['ja'], null, false, true, true);
failed.fallback();
assert.deepEqual(failed.destinations, ['./ja/index.html?ref=store#features', './en/index.html?ref=store#features']);
const localePage = run(['fr'], null, false, false);
assert.equal(localePage.destination, undefined); // Direct locale URLs are never redirected.
assert.equal(localePage.fallback, undefined);
assert.equal(run(['en']).api.match('enough'),null);
assert.equal(run(['en']).api.match('zh_Hant_TW'),'zh-Hant');
console.log('Locale routing and early entry redirect: checks passed.');
