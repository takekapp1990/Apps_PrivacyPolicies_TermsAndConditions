# SEO・LLM対策実行計画書

## 📋 概要
TakeKApp公式サイトのSEO（検索エンジン最適化）とLLM（大規模言語モデル）対策を実施し、検索順位の向上とAIによる情報取得の最適化を図る。

## 🎯 目標
- 検索エンジンでの露出向上
- ユーザビリティの改善
- AIによる正確な情報取得の促進
- ブランド認知度の向上

---

## 📊 現状分析

### 現在の状況
✅ **実装済み**
- OGP設定（index.html）
- 多言語対応（日本語・英語）
- レスポンシブデザイン
- Google Analytics設定
- 構造化されたHTML
- 構造化データ（JSON-LD）: Organization、WebSite、FAQ、SoftwareApplicationスキーマ
- robots.txt: 検索エンジンクローラー向け設定
- sitemap.xml: サイト構造の最適化
- llms.txt: AIクローラー向けポリシー設定
- 画像alt属性: アクセシビリティとSEO向上
- セマンティックHTML: 説明文の追加
- ページタイトルの最適化
- メタディスクリプション

✅ **Phase 1-3 完了済み**
- 基本SEO対策（Phase 1）
- LLM対策（Phase 2）
- パフォーマンス最適化（Phase 3）

❌ **未実装・改善が必要**
- 内部リンク構造の最適化
- ページ読み込み速度の詳細測定
- 継続的な監視と改善

---

## 🚀 実行計画

### ✅ Phase 1: 基本SEO対策（完了）

#### 1.1 メタ情報の最適化
- [x] 各ページのメタディスクリプション追加
- [x] ページタイトルの最適化
- [x] キーワード密度の調整

#### 1.2 構造化データ（JSON-LD）の実装
- [x] Organization（組織）スキーマ
- [x] WebSite（ウェブサイト）スキーマ
- [x] FAQスキーマ
- [x] SoftwareApplication（ソフトウェア）スキーマ（2アプリ分）

#### 1.3 技術的SEO
- [x] robots.txtの作成・最適化
- [x] sitemap.xmlの作成・更新
- [x] 画像のalt属性追加
- [x] 内部リンク構造の最適化

### ✅ Phase 2: LLM対策（完了）

#### 2.1 構造化情報の強化
- [x] FAQスキーマの実装
- [x] アプリ詳細情報の構造化
- [x] 会社情報の構造化

#### 2.2 LLM向けファイル作成
- [x] llms.txtファイルの作成・配置
- [x] AIクローラー向けのポリシー設定
- [x] レート制限・エラーハンドリング設定
- [x] コンテンツ利用条件の明記

#### 2.3 コンテンツ最適化
- [x] LLM向けの明確な情報構造
- [x] キーワードの自然な配置
- [x] コンテンツの階層化

### ✅ Phase 3: パフォーマンス最適化（完了）

#### 3.1 読み込み速度の改善
- [x] 画像のalt属性最適化
- [x] セマンティックHTML改善
- [x] 構造化データの最適化

#### 3.2 ユーザビリティ向上
- [x] ナビゲーションの改善
- [x] セマンティックHTMLの改善
- [x] アクセシビリティの向上

### Phase 4: コンテンツ戦略（優先度：中）

#### 4.1 コンテンツ拡充
- [ ] アプリ詳細ページの充実
- [ ] ブログ・ニュースセクション
- [ ] ユーザーガイド・ヘルプ

#### 4.2 多言語コンテンツ
- [ ] 他言語ページの最適化
- [ ] 言語別SEO対策

---

## 📝 詳細実装項目

### 1. 構造化データ（JSON-LD）実装計画

#### Organization スキーマ
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "TakeKApp",
  "url": "https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/",
  "logo": "https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/SharedDice/images/icon_512512_app_store.png",
  "description": "あなたの毎日が少しだけ楽しくなるようなアプリを開発しています",
  "sameAs": [
    "https://github.com/takekapp1990",
    "https://x.com/takekapp"
  ]
}
```

#### WebSite スキーマ
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "TakeKApp アプリコレクション",
  "url": "https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/",
  "description": "あなたの毎日が少しだけ楽しくなるようなアプリを開発しています"
}
```

#### SoftwareApplication スキーマ（各アプリ用）
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "多機能サイコロ",
  "applicationCategory": "GameApplication",
  "operatingSystem": "Android, iOS",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "JPY"
  }
}
```

### 2. robots.txt 実装計画
```
User-agent: *
Allow: /

# Sitemap
Sitemap: https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/sitemap.xml

# Disallow
Disallow: /app_store_text/
```

### 3. llms.txt 実装計画
```
user-agent: *

# License and AI Training Policy
x-content-license: "(c) TakeKApp. All rights reserved."
x-ai-training-policy: "allowed"

# Rate Limits
crawl-delay: 1
x-rate-limit: 60
x-rate-limit-window: 60
x-rate-limit-policy: "strict"
x-rate-limit-retry: "no-retry"
x-rate-limit-description: "Maximum 60 requests per 60 seconds. If rate limit is exceeded, do not retry and move on to next request."

# Concurrency Limits
x-concurrency-limit: 3
x-concurrency-limit-description: "Please limit concurrent requests to a maximum of 3. This helps us manage server load."

# Error Handling and Retry Policy
x-error-retry-policy: "exponential-backoff"
x-error-retry-policy-description: "For transient errors (5xx except 429), implement exponential backoff with initial wait of 2 seconds, doubling on each retry, with maximum 5 retries."
x-rate-limit-exceeded-policy: "wait-and-retry"
x-rate-limit-exceeded-policy-description: "When receiving HTTP 429 (Too Many Requests), do not retry immediately. Wait at least 60 seconds before attempting the request again."
x-max-retries: 5
x-retry-status-codes:
  - 500
  - 502
  - 503
  - 504
x-no-immediate-retry-status-codes:
  - 429
x-no-retry-status-codes:
  - 403
  - 404

# Canonical URL
x-canonical-url-policy: "strict"
x-canonical-url: "https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/"
x-canonical-url-description: "Access via other FQDNs or IP addresses is invalid. Use only the specified URL as the base URL."

# Site Structure
x-site-type: "app-collection"
x-site-description: "TakeKApp official website featuring mobile applications that make daily life more enjoyable"
x-app-pattern: "/SharedDice/landing_pages/*/landing_page_*.html"
x-app-type: "mobile-application"
x-app-description: "Mobile applications for Android and iOS platforms"
```

### 4. sitemap.xml 実装計画
- メインページ（index.html）
- 各アプリのランディングページ
- プライバシーポリシー・利用規約ページ
- 多言語ページ

### 5. LLM向け最適化項目
- FAQセクションの追加
- アプリ詳細情報の構造化
- 会社情報の明確化
- キーワードの自然な配置
- llms.txtファイルの実装

---

## 📅 実行スケジュール

### ✅ Week 1: Phase 1 基本SEO対策（完了）
- Day 1-2: 構造化データ（JSON-LD）実装 ✅
- Day 3-4: robots.txt・sitemap.xml作成 ✅
- Day 5: メタ情報最適化 ✅

### ✅ Week 2: Phase 2 LLM対策（完了）
- Day 1-3: 構造化情報強化 ✅
- Day 4-5: コンテンツ最適化 ✅

### ✅ Week 3: Phase 3 パフォーマンス最適化（完了）
- Day 1-3: 読み込み速度改善 ✅
- Day 4-5: ユーザビリティ向上 ✅

### 🔄 Week 4: Phase 4 コンテンツ戦略（未実装）
- Day 1-3: コンテンツ拡充
- Day 4-5: 多言語最適化

---

## 📈 成功指標（KPI）

### SEO指標
- 検索順位の向上
- オーガニックトラフィックの増加
- ページビューの増加
- 直帰率の改善

### LLM指標
- AIによる正確な情報取得
- 構造化データの認識率
- コンテンツの理解度

### ユーザビリティ指標
- ページ読み込み速度
- モバイルユーザビリティ
- アクセシビリティ

---

## 🔧 実装ツール・リソース

### 必要なツール
- Google Search Console
- Google PageSpeed Insights
- Schema.org Validator
- Google Rich Results Test

### 参考リソース
- Schema.org ドキュメント
- Google SEO ガイドライン
- Web.dev パフォーマンスガイド

---

## 📋 チェックリスト

### Phase 1 完了チェック
- [x] 構造化データ実装完了
- [x] robots.txt作成完了
- [x] sitemap.xml作成完了
- [x] メタ情報最適化完了

### Phase 2 完了チェック
- [x] FAQスキーマ実装完了
- [x] アプリ情報構造化完了
- [x] llms.txtファイル実装完了
- [x] コンテンツ最適化完了

### Phase 3 完了チェック
- [x] 画像最適化完了
- [x] セマンティックHTML改善完了
- [x] ユーザビリティ向上完了

### Phase 4 完了チェック
- [ ] コンテンツ拡充完了
- [ ] 多言語最適化完了

---

## 🎯 次のステップ

1. **✅ Phase 1-3 完了済み**
2. **📊 効果測定の実施**
   - Google Search Consoleでの登録・確認
   - Google PageSpeed Insightsでのパフォーマンス測定
   - Schema.org Validatorでの構造化データ検証
3. **🔄 継続的な監視と改善**
   - 検索順位の監視
   - トラフィック分析
   - ユーザビリティの改善
4. **📈 必要に応じて追加対策の実施**

---

*作成日: 2024年*
*更新日: 2024年12月19日*
*担当: AI Assistant*
*状況: Phase 1-3 完了* 