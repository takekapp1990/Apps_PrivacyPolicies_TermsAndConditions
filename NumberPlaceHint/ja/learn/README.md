# ナンプレ学習ページの保守

## 範囲

入口ページ、楽しみ方・脳トレの記事、固定問題の体験版、解説5本、裸のシングルと裸のペアの各2問。記事本文・図解は静的HTMLで、JavaScriptがなくても読めます。問題データはアプリから4問だけを抽出し、開始時のvalues・notes・givensと受理解を維持しています。全問題データや汎用ソルバーは配信しません。解説を見る操作は練習完了として計測しません。

## 編集・再生成

### 日本語のアプリ紹介LP

`../landing_page_ja.html`、`../landing-page.css`、`../landing-page.js` は直接編集します。
LPはKV・画面カルーセル・課題・機能・おすすめ・解説ガイド・ダウンロードの順です。
カルーセルは横スクロール・ドット・矢印キーに対応し、自動では切り替わりません。ドットは画面幅に応じて到達できる表示位置ごとに生成し、現在位置と連動します。
書体は `../../fonts/README.md` のZen Kaku Gothic Newをサイト内から読み込みます。
LPの `#learning` はガイドへの入口を保ち、折りたたみ内の `#lp-demo` に一手だけを試す独立したデモを置いています。
初期盤面は `experience-data.mjs` の `PUZZLE` と同じです。5行5列の候補が5だけであることを、
`sudoku-engine.mjs` の `candidates` で確認できます。ヒント表示、5の入力、リセットの3操作で、
自動再生や演出設定はありません。JSが無効でも盤面と解説が読めます。
`landing-page.js` の `sudoku_lp_hint_view` と `sudoku_lp_step_complete` は、一手デモの操作を計測します。
体験版1問のクリアを表す `sudoku_trial_complete` とは区別してください。
LPの実画面画像の出典は `../../images/lp/ja/README.md` に記載しています。全22言語版の再生成は `scripts/build_number_place_landing.py --app-root /path/to/number_place_hint`、検証は `scripts/validate_number_place_landing.py` です。日本語の文言を変える際は、`scripts/number_place_lp_ja.json` と `scripts/number_place_lp_translations.py` の対応する項目も更新してください。画像は各言語の実画面素材から取得し、デモの動的メッセージも各ページのJSONから読み込みます。

記事本文、共通ページ構造、図解、サンプル抽出ルールは `scripts/build_number_place_learning.py` にあります。HTMLはその生成結果です。本文は生成スクリプトを編集してから再生成してください。CSSとJSはこのディレクトリ内で直接編集します。

リポジトリ直下で実行：

```sh
python3 scripts/build_number_place_learning.py --app-root /path/to/number_place_hint
python3 scripts/validate_number_place_learning.py
node scripts/test_number_place_learning.mjs
node scripts/test_number_place_experience.mjs
```

生成スクリプトはアプリ側を読み取るだけです。アプリの問題データが変わると抽出結果も変わるため、再生成後は問題の一意性、候補、回答を必ず検証してください。Web独自の問題に替える場合も、同じJSON形式と検証を維持します。正解データはブラウザに配信されます。学習用の例題であり、競技用の秘匿性はありません。

記事を追加するときは生成スクリプトのarticles・diagramsに追記し、一覧へのリンク、関連記事、canonical、パンくず、sitemap.xmlも確認します。既存LPの入口は `../landing_page_ja.html` の `#learning` です。サンプルは開始局面で候補削除済みの場合があるため、valuesだけからnotesを再計算しないでください。

## 練習UI

マスを選んで数字ボタン（または数字キー）で回答します。シングルは1つの配置、ペアは直接削除できる候補の集合が回答です。ペアの候補を選んだだけでは正解になりません。矢印キーは次の空きマスへ移動します。チェック・解説表示後は盤面を固定し、「やり直す」か問題選択で再開できます。

## 計測

既存GA4 `G-0VCS46ZTHC` と `/js/app_store_analytics.js` を利用します。

- `technique_practice_start`：各問題の最初の操作
- `technique_practice_complete`：正答したときだけ
- `technique_practice_solution_view`：正答前に解説を表示したとき
- 共通パラメータ：`article_id`、`technique_id`、`puzzle_id`
- `app_store_click`：既存のストアリンク計測。`link_position=learning_footer`

「やり直す」は新しい試行として開始・完了イベントが再度発火します。ページ再訪でも再度発火するので、ユニークユーザー数やインストール数としては扱わないでください。GA4側で必要に応じてカスタムディメンションと探索レポートを設定します。

## ローカル確認

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

`http://127.0.0.1:8765/NumberPlaceHint/ja/learn/` を開きます。サーバー停止はCtrl+C。HTMLを直接開くfile://のプレビューでも、デモ・体験版・手筋練習が動作します。

公開・広告導入は含みません。AdSenseを導入するときは操作領域と広告を離し、ドメイン全体の審査・プライバシー表示も別途確認してください。


## 文章のセルフレビュー

文章を追加・変更したら、生成スクリプトだけでなく、出力したHTMLと練習画面の文言も読み直します。

- 抽象的なコピーが続いていないか確認します。「気づき」「発見」「次の一手」などを並べるより、扱う手筋やできる操作を書きます。
- 本文では主語・述語のつながりを確かめ、体言止めや短い断片を続けないようにします。見出し・ボタン名は、読み取りやすい短さを優先します。
- 語順を不自然に入れ替えたり、読点や改行で過剰に間を作ったりしていないか確認します。
- 「当店」「当サイト」「私たち」など、運営側を指す言葉を不要に繰り返しません。商品説明では、必要な箇所でアプリ名を示します。
- 「学びましょう」「確かめましょう」と繰り返し呼びかける代わりに、読者が知りたい条件・理由・手順を説明します。
- やさしい表現に直した結果、手筋の成立条件や候補を消せる範囲が曖昧になっていないか、図と例題を照らし合わせます。

2026年10月21日の見直しでは、冒頭を「ナンプレの解き方を、図と例題で学べます。」に変更しました。「ひとつの気づきが、次の一手に」「読むだけで終わらない」などのコピーは、解説内容や練習の案内に置き換えています。


## 体験版・自動解答デモ（2026年10月21日追加）

入口は `index.html`、楽しみ方は `enjoy.html`、脳トレと研究の説明は `brain-training.html`、通常プレイの体験版は `play.html` です。記事・共通デモHTML・固定問題のソースは `scripts/number_place_experience_content.py` にあり、既存の生成スクリプトから呼び出します。既存LPの `#learning` にもデモを配置しています。デモHTMLを変更した場合は、このLP埋め込みも更新してください。

`experience-data.mjs` は固定問題1問・その解・デモの開始局面を生成したものです。デモは数字30個・空きマス51個の最初の盤面から、実際の候補を調べて順番に確定します。体験版のヒントは裸のシングルと隠れたシングルを検出します。この固定問題は全51マスを対応手筋で解けること、一意解であることをテストしています。任意盤面の入力や問題生成はありません。

`experience.js` は候補表示、数字入力、取り消し、ヒント、デモの再生・停止・一手進行・速度変更を扱います。デモは盤面の25%以上が画面に表示されると自動再生します。画面外や別タブでは停止し、表示を戻すと続きから再開します。利用者が一時停止・一手進行で止めた場合は、表示が変わっても勝手に再開しません。全マス完成後は4秒待って最初から繰り返します。`prefers-reduced-motion` では演出と初期の自動再生を無効にします。明示的な再生や一手進行は利用できます。音は使いません。体験版の数字は入力時に正解と照合し、誤答を盤面に残しません。途中保存はありません。

演出はアプリの `lib/widgets/game_effect_burst_overlay.dart` と `lib/styles/sudoku_cell_style_config.dart` を参考に、CSSとDOMで再現しています。アプリ既定のarcade強度を参考に、入力620ms・18粒、範囲完成1150ms・46粒、全完成1800ms・74粒を使い、4スタイルの配色も合わせています。Flutterの描画コードをそのまま動かすものではないため、粒子の軌道・形状やバウンスには差があります。

追加イベント：`sudoku_demo_start` / `sudoku_demo_complete`、`sudoku_trial_start` / `sudoku_trial_hint` / `sudoku_trial_complete`。体験版ではヒントを見てもクリアを計測せず、全マスが正しく埋まったときだけ完了とします。取り消し後の再クリアでも完了イベントが発火するので、ユニーク人数として扱わないでください。

脳トレの記事は2019年の観察研究（PMID:30746778）を出典とし、頻度と課題成績の関連と、因果関係・アプリ固有の効果を区別しています。能力向上・認知症予防・脳年齢の数値を訴求文に使わないでください。


### 直接HTMLを開くプレビュー

生成スクリプトは `experience-browser.js` と `learning-browser.js` も出力します。モジュールのコードと少数の固定データを通常のスクリプトにまとめることで、file://でもデモ・体験版・手筋練習を利用できます。追加のビルド依存はありません。これら2ファイルは生成物です。`experience.js`・`sudoku-engine.mjs`・`learning.js`・`practice-engine.mjs`を編集したら、ページ生成スクリプトを実行して更新してください。HTTP経由のプレビューも公開サイトと同じパスで確認できます。


### デモの表示と盤面サイズ

自動再生は数字の入力を中心に進み、候補を見せるための待ち時間は8手に1回だけ設けています。ヒントの理由は入力後の説明でも確認できます。盤面には縦横9本の均等なトラックを明示し、候補メモはセル内に絶対配置しています。候補・確定数字の切り替えで、行や盤面の高さが変わらないようにしてください。


## 全言語への展開

現在のLPに合わせた22言語・各9ページ（計198ページ）を生成します。日本語の本文・表示は既存のソースを維持し、言語切り替えと相互のhreflangを追加しています。中国語はURLディレクトリをzh_CN / zh_TWのまま保ち、HTMLとhreflangではzh-Hans / zh-Hantを使います。

- `scripts/number_place_translations.py`：Web向け紹介文、脳トレ記事、ボタン、動的メッセージの翻訳。
- `scripts/build_number_place_international.py`：アプリの各言語ARBから手筋の既存訳を読み、各言語のページ・LP入口・サイトマップを生成。
- `scripts/number_place_runtime_i18n.py`：日本語版の動作を保ったまま各言語の通常スクリプトを生成。未翻訳の日本語が残る場合や元コードの差し込み箇所が変わった場合は失敗させます。
- `NumberPlaceHint/learning-locales/`：共通の表示調整・言語切り替え・対応言語情報。

再生成コマンドはこれまでと同じです。記事本文・動的UIに英語へ自動で逃がすフォールバックはありません。翻訳キーと差し込み変数の対応を検証してから生成します。各言語の法的文書は、既存LPと同様に英語版へ案内し、リンクにEnglishと明記しています。アラビア語の文章はRTL、盤面と数字キーは全言語でLTRを維持します。

```sh
python3 scripts/build_number_place_learning.py --app-root /path/to/number_place_hint
python3 scripts/validate_number_place_international.py
```

日本語版のCSSと演出・問題ロジックを共用します。各言語の出力HTMLやbrowser.jsを直接編集せず、ソースと翻訳データを更新してください。LP内の追加部分はsudoku-learningのコメントで囲み、再生成時にこの範囲だけを差し替えます。その他の既存編集は保持します。
