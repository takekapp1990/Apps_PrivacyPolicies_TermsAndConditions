# 日本語LPの書体

Zen Kaku Gothic New（400 / 500 / 700 / 900）を使用しています。
Google Fonts公式のWOFF2を同じサイトから配信し、外部CSSの接続状況に依存せず表示します。
ライセンスは同梱の `OFL.txt` です。

出典：<https://github.com/google/fonts/tree/main/ofl/zenkakugothicnew>

必要なUnicode範囲のファイルだけを保存しています。コピーを変更したら、リポジトリ直下で
`python3 scripts/update_number_place_lp_fonts.py` を実行すると新しい文字の範囲を追加できます。
文字の判定はローカルで行い、HTML・JavaScriptやページの文章は外部へ送信しません。
生成されるCSSが参照するWOFF2とライセンスを一緒に公開してください。
