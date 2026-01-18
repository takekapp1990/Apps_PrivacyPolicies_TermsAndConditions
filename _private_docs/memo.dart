import 'package:freezed_annotation/freezed_annotation.dart';
import 'tag.dart';
import 'hashtag.dart';

part 'memo.freezed.dart';
part 'memo.g.dart';

/// メモのデータモデル
///
/// SNS投稿用のメモを管理するためのクラス
@freezed
class Memo with _$Memo {
  const factory Memo({
    /// メモのID（データベースの主キー）
    int? id,

    /// メモのタイトル
    @Default('') String title,

    /// メモの内容
    @Default('') String content,

    /// 文字数制限（デフォルトはXの280文字）
    @Default(280) int charLimit,

    /// 投稿済みフラグ
    @Default(false) bool isPosted,

    /// 作成日時
    required DateTime createdAt,

    /// 更新日時
    required DateTime updatedAt,

    /// 関連するタグのリスト
    @Default([]) List<Tag> tags,

    /// 関連するハッシュタグのリスト
    @Default([]) List<Hashtag> hashtags,
  }) = _Memo;

  factory Memo.fromJson(Map<String, dynamic> json) => _$MemoFromJson(json);
}

/// メモの編集モード
enum MemoEditMode {
  /// 新規作成
  create,

  /// 編集
  edit,

  /// 表示のみ
  view,

  /// コピー
  copy,
}

/// メモの文字数カウント結果
class MemoCharCount {
  /// 現在の文字数
  final int currentCount;

  /// 文字数制限
  final int limit;

  /// 残り文字数
  int get remainingCount => limit - currentCount;

  /// 制限を超えているか
  bool get isOverLimit => currentCount > limit;

  /// 制限の80%を超えているか（警告表示用）
  bool get isNearLimit => currentCount > (limit * 0.8);

  /// 制限の90%を超えているか（注意表示用）
  bool get isCloseToLimit => currentCount > (limit * 0.9);

  const MemoCharCount({
    required this.currentCount,
    required this.limit,
  });

  /// 選択されたテキストの文字数をカウント
  static int countSelectedText(String selectedText,
      {String charCountMethod = 'x_standard'}) {
    if (charCountMethod == 'simple') {
      return _countSimple(selectedText);
    } else {
      return _countXStandard(selectedText);
    }
  }

  /// X標準の文字数カウント
  static int _countXStandard(String text) {
    int count = 0;

    // URLを検出して23文字としてカウント
    final urlRegex = RegExp(r'https?://[^\s]+');
    final urls = urlRegex.allMatches(text);
    count += urls.length * 23;

    // URLを除去したテキストを取得
    final textWithoutUrls = text.replaceAll(urlRegex, '');

    // 絵文字を検出して2文字としてカウント（X仕様準拠）
    // 主要な絵文字範囲をカバーする簡潔な正規表現
    final emojiRegex = RegExp(
        r'[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F1E0}-\u{1F1FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]|[\u{1F900}-\u{1F9FF}]',
        unicode: true);
    final emojis = emojiRegex.allMatches(textWithoutUrls);
    count += emojis.length * 2;

    // 絵文字を除去したテキストを取得
    final textWithoutEmojis = textWithoutUrls.replaceAll(emojiRegex, '');

    // 各文字をカウント
    for (final rune in textWithoutEmojis.runes) {
      final char = String.fromCharCode(rune);

      if (char == '\n') {
        // 改行は1文字
        count += 1;
      } else if (_isCJK(char)) {
        // CJK文字は2文字
        count += 2;
      } else {
        // その他の文字は1文字
        count += 1;
      }
    }

    return count;
  }

  /// 単純カウント（1文字=1文字）
  static int _countSimple(String text) {
    return text.length;
  }

  /// 連続した改行3つで分割された各セクションの文字数をカウント
  static List<SectionCharCount> countSections(String content, int limit,
      {String charCountMethod = 'x_standard'}) {
    // 連続した改行3つ以上で分割
    final sections = content.split(RegExp(r'\n\s*\n\s*\n'));

    return sections.map((section) {
      final trimmedSection = section.trim();
      final charCount =
          count(trimmedSection, limit, charCountMethod: charCountMethod);
      return SectionCharCount(
        content: trimmedSection,
        charCount: charCount.currentCount,
        limit: limit,
      );
    }).toList();
  }

  /// 文字数カウントを実行
  ///
  /// Xの文字数カウントルールに準拠：
  /// - 絵文字：2文字（twemojiサポート絵文字）
  /// - CJK文字（中国語・日本語・韓国語）：2文字
  /// - その他の文字：1文字
  /// - URL：23文字としてカウント
  /// - 改行：1文字としてカウント
  static MemoCharCount count(String content, int limit,
      {String charCountMethod = 'x_standard'}) {
    int count = 0;

    if (charCountMethod == 'simple') {
      count = _countSimple(content);
    } else {
      count = _countXStandard(content);
    }

    return MemoCharCount(
      currentCount: count,
      limit: limit,
    );
  }

  /// CJK文字（中国語・日本語・韓国語）かどうかを判定
  static bool _isCJK(String char) {
    if (char.isEmpty) return false;

    final codeUnit = char.codeUnitAt(0);

    // CJK文字の範囲をチェック
    return (
        // ひらがな (U+3040-U+309F)
        (codeUnit >= 0x3040 && codeUnit <= 0x309F) ||
            // カタカナ (U+30A0-U+30FF)
            (codeUnit >= 0x30A0 && codeUnit <= 0x30FF) ||
            // CJK統合漢字 (U+4E00-U+9FFF)
            (codeUnit >= 0x4E00 && codeUnit <= 0x9FFF) ||
            // CJK統合漢字拡張A (U+3400-U+4DBF)
            (codeUnit >= 0x3400 && codeUnit <= 0x4DBF) ||
            // CJK記号・句読点 (U+3000-U+303F)
            (codeUnit >= 0x3000 && codeUnit <= 0x303F) ||
            // 全角英数字 (U+FF10-U+FF19, U+FF21-U+FF3A, U+FF41-U+FF5A)
            (codeUnit >= 0xFF10 && codeUnit <= 0xFF19) || // 全角数字
            (codeUnit >= 0xFF21 && codeUnit <= 0xFF3A) || // 全角大文字
            (codeUnit >= 0xFF41 && codeUnit <= 0xFF5A) || // 全角小文字
            // 全角記号 (U+FF01-U+FF0F, U+FF1A-U+FF20, U+FF3B-U+FF40, U+FF5B-U+FF60)
            (codeUnit >= 0xFF01 && codeUnit <= 0xFF0F) ||
            (codeUnit >= 0xFF1A && codeUnit <= 0xFF20) ||
            (codeUnit >= 0xFF3B && codeUnit <= 0xFF40) ||
            (codeUnit >= 0xFF5B && codeUnit <= 0xFF60) ||
            // その他の全角記号
            (codeUnit >= 0xFFE0 && codeUnit <= 0xFFE6) ||
            (codeUnit >= 0xFFE8 && codeUnit <= 0xFFEE));
  }
}

/// 区切り線で分割されたセクションの文字数カウント
class SectionCharCount {
  /// セクションの内容
  final String content;

  /// 文字数
  final int charCount;

  /// 文字数制限
  final int limit;

  /// 残り文字数
  int get remainingCount => limit - charCount;

  /// 制限を超えているか
  bool get isOverLimit => charCount > limit;

  /// 制限の80%を超えているか（警告表示用）
  bool get isNearLimit => charCount > (limit * 0.8);

  /// 制限の90%を超えているか（注意表示用）
  bool get isCloseToLimit => charCount > (limit * 0.9);

  const SectionCharCount({
    required this.content,
    required this.charCount,
    required this.limit,
  });
}

/// メモの検索条件
class MemoSearchCondition {
  /// 検索クエリ
  final String? query;

  /// タグでフィルタ
  final List<String>? tagNames;

  /// 投稿済みフラグでフィルタ
  final bool? isPosted;

  /// 作成日時範囲（開始）
  final DateTime? createdAtFrom;

  /// 作成日時範囲（終了）
  final DateTime? createdAtTo;

  const MemoSearchCondition({
    this.query,
    this.tagNames,
    this.isPosted,
    this.createdAtFrom,
    this.createdAtTo,
  });

  /// 検索条件が空かどうか
  bool get isEmpty =>
      (query == null || query!.isEmpty) &&
      (tagNames == null || tagNames!.isEmpty) &&
      isPosted == null &&
      createdAtFrom == null &&
      createdAtTo == null;
}
