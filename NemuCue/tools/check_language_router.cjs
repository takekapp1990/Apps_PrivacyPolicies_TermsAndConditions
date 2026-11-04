const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const source = fs.readFileSync(path.join(__dirname, '../language-router.js'), 'utf8');
function run(languages, saved, blocked = false, entry = true) {
  let destination;
  let stored;
  const context = {
    window: { location: {search:'?ref=store', hash:'#features', replace: value => destination=value} },
    navigator: { languages, language: languages[0] },
    localStorage: { getItem: () => { if(blocked) throw Error('blocked'); return saved; }, setItem: (key,value)=>stored=value },
    document: { documentElement: {hasAttribute:()=>entry}, addEventListener:()=>{} }
  };
  vm.runInNewContext(source, context);
  return {api:context.window.NemuCueLocale, destination, stored};
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
assert.equal(run(['fr'],null,false,false).destination,undefined); // Direct locale URLs are never redirected.
assert.equal(run(['en']).api.match('enough'),null);
assert.equal(run(['en']).api.match('zh_Hant_TW'),'zh-Hant');
console.log('Locale routing: 28 checks passed.');
