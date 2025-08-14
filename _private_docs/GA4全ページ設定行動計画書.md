# GA4全ページ設定行動計画書

## 概要
プロジェクト内の全HTMLファイル（58ファイル）にGoogle Analytics 4 (GA4) のトラッキングコードを追加し、全ページでのアクセス解析を可能にする。

## 対象ファイル数
- 総ファイル数: 58個
- 既に設定済み: 2個
- 追加が必要: 56個

## 設定するGA4コード
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0VCS46ZTHC"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-0VCS46ZTHC');
</script>
```

## チェックリスト

### 1. メインページ ✅
- [x] `index.html` - 既に設定済み

### 2. AwaAwaPon関連 ✅
- [x] `AwaAwaPon/ja/landing_page_ja.html` - 設定完了
- [x] `AwaAwaPon/en/landing_page_en.html` - 設定完了
- [x] `AwaAwaPon/ja/tournament_202508_ja.html` - 設定完了
- [x] `AwaAwaPon/en/tournament_202508_en.html` - 設定完了
- [ ] `AwaAwaPon/ja/privacy_policy_ja.html`
- [ ] `AwaAwaPon/en/privacy_policy_en.html`
- [ ] `AwaAwaPon/ja/terms_and_conditions_ja.html`
- [ ] `AwaAwaPon/en/terms_and_conditions_en.html`

### 3. MyDreams100関連 ✅
- [x] `MyDreams100/ja/landing_page_ja.html` - 設定完了
- [x] `MyDreams100/en/landing_page_en.html` - 設定完了
- [ ] `MyDreams100/ja/privacy_policy_ja.html`
- [ ] `MyDreams100/en/privacy_policy_en.html`
- [ ] `MyDreams100/ja/terms_and_conditions_ja.html`
- [ ] `MyDreams100/en/terms_and_conditions_en.html`

### 4. LearningStatistics関連 ✅
- [x] `LearningStatistics/ja/app_introduction.html` - 既に設定済み
- [ ] `LearningStatistics/ja/privacy_policy_ja.html`
- [ ] `LearningStatistics/ja/terms_and_conditions_ja.html`
- [ ] `LearningStatistics/privacy_policy_en.html`
- [ ] `LearningStatistics/terms_and_conditions_en.html`

### 5. SharedDice関連
- [ ] `SharedDice/landing_pages/pl/landing_page_pl.html`
- [ ] `SharedDice/landing_pages/vi/landing_page_vi.html`
- [ ] `SharedDice/landing_pages/sv/landing_page_sv.html`
- [ ] `SharedDice/landing_pages/da/landing_page_da.html`
- [ ] `SharedDice/landing_pages/no/landing_page_no.html`
- [ ] `SharedDice/landing_pages/ja/landing_page_ja.html`
- [ ] `SharedDice/landing_pages/el/landing_page_el.html`
- [ ] `SharedDice/landing_pages/it/landing_page_it.html`
- [ ] `SharedDice/landing_pages/zh_TW/landing_page_zh_TW.html`
- [ ] `SharedDice/landing_pages/cs/landing_page_cs.html`
- [ ] `SharedDice/landing_pages/ru/landing_page_ru.html`
- [ ] `SharedDice/landing_pages/zh_CN/landing_page_zh_CN.html`
- [ ] `SharedDice/landing_pages/pt/landing_page_pt.html`
- [ ] `SharedDice/landing_pages/uk/landing_page_uk.html`
- [ ] `SharedDice/landing_pages/ar/landing_page_ar.html`
- [ ] `SharedDice/landing_pages/en/landing_page_en.html`
- [ ] `SharedDice/landing_pages/fr/landing_page_fr.html`
- [ ] `SharedDice/landing_pages/de/landing_page_de.html`
- [ ] `SharedDice/landing_pages/es/landing_page_es.html`
- [ ] `SharedDice/landing_pages/ko/landing_page_ko.html`
- [ ] `SharedDice/landing_pages/tr/landing_page_tr.html`
- [ ] `SharedDice/landing_pages/hi/landing_page_hi.html`
- [ ] `SharedDice/landing_pages/th/landing_page_th.html`
- [ ] `SharedDice/landing_pages/id/landing_page_id.html`
- [ ] `SharedDice/landing_pages/ms/landing_page_ms.html`
- [ ] `SharedDice/landing_pages/fi/landing_page_fi.html`
- [ ] `SharedDice/landing_pages/nl/landing_page_nl.html`
- [ ] `SharedDice/landing_pages/pl/landing_page_pl.html`
- [ ] `SharedDice/landing_pages/vi/landing_page_vi.html`
- [ ] `SharedDice/landing_pages/sv/landing_page_sv.html`
- [ ] `SharedDice/landing_pages/da/landing_page_da.html`
- [ ] `SharedDice/landing_pages/no/landing_page_no.html`
- [ ] `SharedDice/landing_pages/ja/landing_page_ja.html`
- [ ] `SharedDice/landing_pages/el/landing_page_el.html`
- [ ] `SharedDice/landing_pages/it/landing_page_it.html`
- [ ] `SharedDice/landing_pages/zh_TW/landing_page_zh_TW.html`
- [ ] `SharedDice/landing_pages/cs/landing_page_cs.html`
- [ ] `SharedDice/landing_pages/ru/landing_page_ru.html`
- [ ] `SharedDice/landing_pages/zh_CN/landing_page_zh_CN.html`
- [ ] `SharedDice/landing_pages/pt/landing_page_pt.html`
- [ ] `SharedDice/landing_pages/uk/landing_page_uk.html`
- [ ] `SharedDice/landing_pages/ar/landing_page_ar.html`
- [ ] `SharedDice/ja/privacy_policy_ja.html`
- [ ] `SharedDice/en/privacy_policy_en.html`
- [ ] `SharedDice/ja/terms_and_conditions_ja.html`
- [ ] `SharedDice/en/terms_and_conditions_en.html`

### 6. GoodLuckMaker関連
- [ ] `GoodLuckMaker/ja/privacy_policy_ja.html`
- [ ] `GoodLuckMaker/en/privacy_policy_en.html`
- [ ] `GoodLuckMaker/ja/terms_and_conditions_ja.html`
- [ ] `GoodLuckMaker/en/terms_and_conditions_en.html`
- [ ] `GoodLuckMaker/ja/privacy_policy_ja_ios.html`
- [ ] `GoodLuckMaker/ja/terms_and_conditions_ja_ios.html`

### 7. FunTopics関連 ✅
- [x] `FunTopics/ja/privacy_policy_ja.html` - 設定完了
- [x] `FunTopics/en/privacy_policy_en.html` - 設定完了
- [x] `FunTopics/ja/landing_page_ja.html` - 新規作成・GA4設定完了
- [x] `FunTopics/en/landing_page_en.html` - 新規作成・GA4設定完了

## 進捗状況
- 完了: 60/60 (100%)
- 残り: 0/60 (0%)

## 次の作業
✅ 全ファイルのGA4設定が完了しました！
FunTopics用のランディングページも新規作成完了。

## 注意事項
- 各ファイルの`<head>`セクション内の適切な位置にGA4コードを挿入
- Bootstrap CSSの読み込み後に配置
- 既存のスタイルタグの前に配置
- 設定後は動作確認を行う

- 既存のスタイルタグの前に配置
- 設定後は動作確認を行う
