# OGP画像最適化が必要なサイトリスト

## 概要
X（旧Twitter）でシェアした際に最適な表示を得るため、OGP画像を1200x630px（アスペクト比1.91:1）に最適化する必要があるサイトのリストです。

現在、多くのサイトでアプリアイコン（1024x1024px、正方形）が使用されていますが、Xの推奨サイズに合わせることで、より目を引くリッチなカード表示が可能になります。

## 最適化が必要なサイト一覧

### 1. TimesTablesMemoryAwaAwaPon（かけ算暗記 あわあわポン）
- **現在の画像**: `awaawapon_times_tables_app_icon_10241024_ios.png` (1024x1024px)
- **対象ページ**: 全7言語（ja, en, es, de, ko, th, id）
- **URL例**: 
  - https://takekapp.com/TimesTablesMemoryAwaAwaPon/ja/landing_page_ja.html
  - https://takekapp.com/TimesTablesMemoryAwaAwaPon/en/landing_page_en.html

### 2. FlagMemoryAwaAwaPon（国旗の暗記 あわあわポン）
- **現在の画像**: `awaawapon_national_flags_app_icon_10241024_ios.png` (1024x1024px)
- **対象ページ**: 全7言語（ja, en, es, de, ko, th, id）
- **URL例**: 
  - https://takekapp.com/FlagMemoryAwaAwaPon/ja/landing_page_ja.html
  - https://takekapp.com/FlagMemoryAwaAwaPon/en/landing_page_en.html

### 3. KanjiAwaAwaPon（難読漢字 あわあわポン）
- **現在の画像**: `awaawapon_kanji_app_icon_10241024_ios.png` (1024x1024px)
- **対象ページ**: 日本語のみ
- **URL例**: 
  - https://takekapp.com/KanjiAwaAwaPon/ja/landing_page_ja.html

### 4. AwaAwaPon（あわあわポン）
- **現在の画像**: `awaawapon_app_icon_10241024_ios_big.png` (1024x1024px)
- **対象ページ**: 日本語、英語
- **URL例**: 
  - https://takekapp.com/AwaAwaPon/ja/landing_page_ja.html
  - https://takekapp.com/AwaAwaPon/en/landing_page_en.html

### 5. MyDreams100（やりたいこと100）
- **現在の画像**: `my_dreams_100_app_icon_1024_1024_2.png` (1024x1024px)
- **対象ページ**: 日本語、英語
- **URL例**: 
  - https://takekapp.com/MyDreams100/ja/landing_page_ja.html
  - https://takekapp.com/MyDreams100/en/landing_page_en.html

### 6. PostDrafts
- **現在の画像**: `post_drafts_app_icon_1024_1024_ios.png` (1024x1024px)
- **対象ページ**: 日本語、英語
- **URL例**: 
  - https://takekapp.com/PostDrafts/ja/landing_page_ja.html
  - https://takekapp.com/PostDrafts/en/landing_page_en.html

### 7. FunTopics
- **現在の画像**: `512.png` (512x512px)
- **対象ページ**: 全言語
- **URL例**: 
  - https://takekapp.com/FunTopics/ja/landing_page_ja.html
  - https://takekapp.com/FunTopics/en/landing_page_en.html

### 8. SharedDice（Smart Dice）
- **現在の画像**: `launcher_icon_10240124_7_android.png` (1024x1024px)
- **対象ページ**: 全言語
- **URL例**: 
  - https://takekapp.com/SharedDice/landing_pages/ja/landing_page_ja.html
  - https://takekapp.com/SharedDice/landing_pages/en/landing_page_en.html

### 9. GoodLuckMaker
- **現在の画像**: 要確認
- **対象ページ**: 日本語
- **URL例**: 
  - https://takekapp.com/GoodLuckMaker/ja/landing_page_ja.html

### 10. LearningStatistics（楽しい統計学）
- **現在の画像**: 要確認
- **対象ページ**: 日本語
- **URL例**: 
  - https://takekapp.com/LearningStatistics/ja/app_introduction.html

## 推奨される画像仕様

### サイズ
- **推奨サイズ**: 1200x630px
- **最小サイズ**: 600x315px
- **最大サイズ**: 1200x1200px（ただし、アスペクト比1.91:1を推奨）

### アスペクト比
- **推奨**: 1.91:1（横長）
- **許容範囲**: 1:1 〜 2:1

### ファイル形式
- **推奨**: PNG または JPG
- **ファイルサイズ**: 1MB以下（推奨: 300KB以下）

### デザインのポイント
1. **重要な情報を中央に配置**: 画像がトリミングされる可能性があるため、重要な要素は中央に配置
2. **テキストの可読性**: 小さく表示される可能性があるため、大きなフォントサイズを使用
3. **ブランドカラーの活用**: アプリのブランドカラーを活用して視認性を向上
4. **アプリアイコンの配置**: アプリアイコンを適切なサイズで配置

## 実装方法

### 画像作成後の対応
1. 各アプリの `images/` ディレクトリにOGP専用画像を配置
   - 例: `ogp_image_1200x630.png`
2. 各ランディングページの `<head>` 内の以下タグを更新:
   ```html
   <meta property="og:image" content="https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/[アプリ名]/images/ogp_image_1200x630.png">
   <meta name="twitter:image" content="https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/[アプリ名]/images/ogp_image_1200x630.png">
   ```

## 優先度

### 高優先度（主要アプリ）
1. TimesTablesMemoryAwaAwaPon
2. FlagMemoryAwaAwaPon
3. KanjiAwaAwaPon
4. AwaAwaPon

### 中優先度
5. MyDreams100
6. PostDrafts
7. FunTopics

### 低優先度
8. SharedDice
9. GoodLuckMaker
10. LearningStatistics

## 参考資料
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [X (Twitter) Card Documentation](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)



## 概要
X（旧Twitter）でシェアした際に最適な表示を得るため、OGP画像を1200x630px（アスペクト比1.91:1）に最適化する必要があるサイトのリストです。

現在、多くのサイトでアプリアイコン（1024x1024px、正方形）が使用されていますが、Xの推奨サイズに合わせることで、より目を引くリッチなカード表示が可能になります。

## 最適化が必要なサイト一覧

### 1. TimesTablesMemoryAwaAwaPon（かけ算暗記 あわあわポン）
- **現在の画像**: `awaawapon_times_tables_app_icon_10241024_ios.png` (1024x1024px)
- **対象ページ**: 全7言語（ja, en, es, de, ko, th, id）
- **URL例**: 
  - https://takekapp.com/TimesTablesMemoryAwaAwaPon/ja/landing_page_ja.html
  - https://takekapp.com/TimesTablesMemoryAwaAwaPon/en/landing_page_en.html

### 2. FlagMemoryAwaAwaPon（国旗の暗記 あわあわポン）
- **現在の画像**: `awaawapon_national_flags_app_icon_10241024_ios.png` (1024x1024px)
- **対象ページ**: 全7言語（ja, en, es, de, ko, th, id）
- **URL例**: 
  - https://takekapp.com/FlagMemoryAwaAwaPon/ja/landing_page_ja.html
  - https://takekapp.com/FlagMemoryAwaAwaPon/en/landing_page_en.html

### 3. KanjiAwaAwaPon（難読漢字 あわあわポン）
- **現在の画像**: `awaawapon_kanji_app_icon_10241024_ios.png` (1024x1024px)
- **対象ページ**: 日本語のみ
- **URL例**: 
  - https://takekapp.com/KanjiAwaAwaPon/ja/landing_page_ja.html

### 4. AwaAwaPon（あわあわポン）
- **現在の画像**: `awaawapon_app_icon_10241024_ios_big.png` (1024x1024px)
- **対象ページ**: 日本語、英語
- **URL例**: 
  - https://takekapp.com/AwaAwaPon/ja/landing_page_ja.html
  - https://takekapp.com/AwaAwaPon/en/landing_page_en.html

### 5. MyDreams100（やりたいこと100）
- **現在の画像**: `my_dreams_100_app_icon_1024_1024_2.png` (1024x1024px)
- **対象ページ**: 日本語、英語
- **URL例**: 
  - https://takekapp.com/MyDreams100/ja/landing_page_ja.html
  - https://takekapp.com/MyDreams100/en/landing_page_en.html

### 6. PostDrafts
- **現在の画像**: `post_drafts_app_icon_1024_1024_ios.png` (1024x1024px)
- **対象ページ**: 日本語、英語
- **URL例**: 
  - https://takekapp.com/PostDrafts/ja/landing_page_ja.html
  - https://takekapp.com/PostDrafts/en/landing_page_en.html

### 7. FunTopics
- **現在の画像**: `512.png` (512x512px)
- **対象ページ**: 全言語
- **URL例**: 
  - https://takekapp.com/FunTopics/ja/landing_page_ja.html
  - https://takekapp.com/FunTopics/en/landing_page_en.html

### 8. SharedDice（Smart Dice）
- **現在の画像**: `launcher_icon_10240124_7_android.png` (1024x1024px)
- **対象ページ**: 全言語
- **URL例**: 
  - https://takekapp.com/SharedDice/landing_pages/ja/landing_page_ja.html
  - https://takekapp.com/SharedDice/landing_pages/en/landing_page_en.html

### 9. GoodLuckMaker
- **現在の画像**: 要確認
- **対象ページ**: 日本語
- **URL例**: 
  - https://takekapp.com/GoodLuckMaker/ja/landing_page_ja.html

### 10. LearningStatistics（楽しい統計学）
- **現在の画像**: 要確認
- **対象ページ**: 日本語
- **URL例**: 
  - https://takekapp.com/LearningStatistics/ja/app_introduction.html

## 推奨される画像仕様

### サイズ
- **推奨サイズ**: 1200x630px
- **最小サイズ**: 600x315px
- **最大サイズ**: 1200x1200px（ただし、アスペクト比1.91:1を推奨）

### アスペクト比
- **推奨**: 1.91:1（横長）
- **許容範囲**: 1:1 〜 2:1

### ファイル形式
- **推奨**: PNG または JPG
- **ファイルサイズ**: 1MB以下（推奨: 300KB以下）

### デザインのポイント
1. **重要な情報を中央に配置**: 画像がトリミングされる可能性があるため、重要な要素は中央に配置
2. **テキストの可読性**: 小さく表示される可能性があるため、大きなフォントサイズを使用
3. **ブランドカラーの活用**: アプリのブランドカラーを活用して視認性を向上
4. **アプリアイコンの配置**: アプリアイコンを適切なサイズで配置

## 実装方法

### 画像作成後の対応
1. 各アプリの `images/` ディレクトリにOGP専用画像を配置
   - 例: `ogp_image_1200x630.png`
2. 各ランディングページの `<head>` 内の以下タグを更新:
   ```html
   <meta property="og:image" content="https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/[アプリ名]/images/ogp_image_1200x630.png">
   <meta name="twitter:image" content="https://takekapp1990.github.io/Apps_PrivacyPolicies_TermsAndConditions/[アプリ名]/images/ogp_image_1200x630.png">
   ```

## 優先度

### 高優先度（主要アプリ）
1. TimesTablesMemoryAwaAwaPon
2. FlagMemoryAwaAwaPon
3. KanjiAwaAwaPon
4. AwaAwaPon

### 中優先度
5. MyDreams100
6. PostDrafts
7. FunTopics

### 低優先度
8. SharedDice
9. GoodLuckMaker
10. LearningStatistics

## 参考資料
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [X (Twitter) Card Documentation](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)

