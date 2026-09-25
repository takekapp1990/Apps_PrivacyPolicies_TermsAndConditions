#!/usr/bin/env python3
"""Apply repeatable SEO maintenance to the static TakeKApp site.

The script intentionally limits itself to mechanical, repository-wide fixes:
canonical URLs, missing descriptions/language declarations, reciprocal hreflang
clusters, SoftwareApplication JSON-LD, image loading hints, known broken local
references, analytics tags on public landing pages, and retired duplicate blog
URLs.
"""

from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://takekapp.com"
GA_MEASUREMENT_ID = "G-0VCS46ZTHC"

ANALYTICS_EXTRA_PAGES = {
    "AwaAwaPon/ja/tournament_202507_ja.html",
    "VersaMemo/en/index.html",
    "VersaMemo/ja/index.html",
}

RETIRED_URLS = {
    "blog/posts/dev/ja/2025-01-30-development-diary-starts.html":
        "blog/posts/dev/ja/2025-11-22-development-diary-starts.html",
    "blog/posts/dev/ja/2025-02-15-casual-game-failure.html":
        "blog/posts/dev/ja/2025-11-23-casual-game-failure.html",
    "blog/posts/dev/en/2025-01-30-development-diary-starts.html":
        "blog/posts/dev/en/2025-11-22-development-diary-starts.html",
    "blog/posts/dev/en/2025-02-15-casual-game-failure.html":
        "blog/posts/dev/en/2025-11-23-casual-game-failure.html",
    "FunTopics/ja/app_introduction.html":
        "LearningStatistics/ja/app_introduction.html",
}

LANG_ALIASES = {
    "zh_CN": "zh-Hans",
    "zh_TW": "zh-Hant",
    "zh_Hans": "zh-Hans",
    "zh_Hant": "zh-Hant",
    "pt_BR": "pt-BR",
    "pt_PT": "pt-PT",
    "pt-BR": "pt-BR",
    "pt-PT": "pt-PT",
}

GAME_APPS = {
    "AwaAwaPon",
    "FlagMemoryAwaAwaPon",
    "KanjiAwaAwaPon",
    "Meiro25MojiQuiz",
    "TimesTablesMemoryAwaAwaPon",
}
EDUCATION_APPS = {"LearningStatistics", "NumberPlaceHint"}
FINANCE_APPS = {"LoanManagement"}
MULTIMEDIA_APPS = {"MemoWinkAlbum", "TapAlbum"}


def iter_html() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.html")
        if ".git" not in path.parts and "_private_docs" not in path.parts
    )


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def canonical_url(path: Path) -> str:
    relative = rel(path)
    if relative == "index.html":
        return f"{BASE_URL}/"
    if relative.endswith("/index.html"):
        return f"{BASE_URL}/{relative[:-10]}"
    return f"{BASE_URL}/{relative}"


def language_for(path: Path) -> str:
    parts = path.relative_to(ROOT).parts
    candidates = list(reversed(parts[:-1]))
    stem = path.stem
    match = re.search(
        r"_(zh_Hans|zh_Hant|zh_CN|zh_TW|pt_BR|pt_PT|pt-BR|pt-PT|[a-z]{2})$",
        stem,
    )
    if match:
        candidates.insert(0, match.group(1))
    for candidate in candidates:
        if candidate in LANG_ALIASES:
            return LANG_ALIASES[candidate]
        if re.fullmatch(r"[a-z]{2}", candidate):
            return candidate
    return "ja" if path.name in {"index.html", "about.html", "privacy_policy.html"} else "en"


def strip_markup(value: str) -> str:
    value = re.sub(r"<(script|style|nav|footer)[^>]*>.*?</\1>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def title_from(source: str) -> str:
    match = re.search(r"<title[^>]*>(.*?)</title>", source, flags=re.I | re.S)
    return strip_markup(match.group(1)) if match else "TakeKApp"


def description_for(path: Path, source: str) -> str:
    custom = {
        "index.html": "TakeKAppは、毎日を少し楽しくするモバイルアプリを個人開発しています。ゲーム、学習、日記、仕事効率化など、Android・iOS向けアプリを紹介します。",
        "blog/index.html": "TakeKAppのアプリ開発日記。Flutterでの個人開発、リリース後の学び、AI・統計学・プロダクト設計について、実体験をもとに発信しています。",
    }
    if rel(path) in custom:
        return custom[rel(path)]

    body = re.search(r"<body[^>]*>(.*?)</body>", source, flags=re.I | re.S)
    body_source = body.group(1) if body else source
    paragraphs = re.findall(r"<p\b[^>]*>(.*?)</p>", body_source, flags=re.I | re.S)
    ignored = (
        "日本語", "English", "Last updated", "Effective", "最終更新", "お問い合わせ",
        "Copyright", "©", "All rights reserved",
    )
    for paragraph in paragraphs:
        text = strip_markup(paragraph)
        if len(text) >= 35 and not any(text.startswith(prefix) for prefix in ignored):
            return text[:155].rstrip(" ,、。") + ("。" if language_for(path) == "ja" else "")

    title = title_from(source)
    fallback = f"{title}についての公式情報を掲載しています。" if language_for(path) == "ja" else f"Official information about {title}."
    return fallback[:155]


def insert_before_head_end(source: str, block: str) -> str:
    return re.sub(r"\s*</head>", f"\n{block}\n</head>", source, count=1, flags=re.I)


def upsert_lang(source: str, language: str) -> str:
    if re.search(r"<html\b[^>]*\blang=", source, flags=re.I):
        return source
    return re.sub(r"<html\b", f'<html lang="{language}"', source, count=1, flags=re.I)


def add_basic_metadata(path: Path, source: str) -> str:
    if "noindex" in source.lower():
        return source

    source = upsert_lang(source, language_for(path))
    additions: list[str] = []
    if not re.search(r"<meta\b[^>]*\bname=[\"']description[\"']", source, flags=re.I):
        description = html.escape(description_for(path, source), quote=True)
        additions.append(f'    <meta name="description" content="{description}">')
    if not re.search(r"<link\b[^>]*\brel=[\"'][^\"']*canonical", source, flags=re.I):
        additions.append(f'    <link rel="canonical" href="{canonical_url(path)}">')
    if additions:
        source = insert_before_head_end(source, "\n".join(additions))
    return source


def add_analytics(path: Path, source: str) -> str:
    relative = rel(path)
    is_landing_page = "landing_page_" in path.name or path.name == "app_introduction.html"
    if not (is_landing_page or relative in ANALYTICS_EXTRA_PAGES):
        return source
    if "noindex" in source.lower() or GA_MEASUREMENT_ID in source:
        return source

    block = f'''    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('js', new Date());
        gtag('config', '{GA_MEASUREMENT_ID}');
    </script>'''
    return insert_before_head_end(source, block)


def clamp_description(value: str, language: str) -> str:
    terminal = ".!?。！？…"
    if len(value) <= 160 and (len(value) < 150 or value.rstrip('"\'”’）)]').endswith(tuple(terminal))):
        return value

    shortened = value[:155].rstrip()
    if language.startswith(("ja", "zh")):
        last_stop = max(shortened.rfind(mark) for mark in "。！？")
        if last_stop >= 80:
            return shortened[: last_stop + 1]
        return shortened.rstrip("、。，． ") + "…"

    last_space = shortened.rfind(" ")
    if last_space >= 110:
        shortened = shortened[:last_space]
    return shortened.rstrip(" ,;:.-") + "…"


def normalize_description(path: Path, source: str) -> str:
    pattern = re.compile(
        r"(?P<prefix><meta\b[^>]*\bname=[\"']description[\"'][^>]*\bcontent=)(?P<quote>[\"'])(?P<value>.*?)(?P=quote)",
        flags=re.I,
    )
    match = pattern.search(source)
    if not match:
        return source
    old_value = html.unescape(match.group("value"))
    new_value = clamp_description(old_value, language_for(path))
    if new_value == old_value:
        return source
    escaped = html.escape(new_value, quote=True)
    source = source[:match.start("value")] + escaped + source[match.end("value"):]
    source = source.replace(
        f'"description": {json.dumps(old_value, ensure_ascii=False)}',
        f'"description": {json.dumps(new_value, ensure_ascii=False)}',
    )
    return source


def local_path_for_image(page: Path, src: str) -> Path | None:
    parsed = urlparse(src)
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc not in {"takekapp.com", "www.takekapp.com"}:
            return None
        return ROOT / parsed.path.lstrip("/")
    if src.startswith(("data:", "//")):
        return None
    return (ROOT / src.lstrip("/")) if src.startswith("/") else (page.parent / src)


def optimize_images(path: Path, source: str) -> str:
    image_number = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal image_number
        tag = match.group(0)
        image_number += 1
        if "decoding=" not in tag.lower():
            tag = tag[:-1].rstrip() + ' decoding="async">'
        if image_number > 1 and "loading=" not in tag.lower():
            tag = tag[:-1].rstrip() + ' loading="lazy">'
        return tag

    return re.sub(r"<img\b[^>]*>", replace, source, flags=re.I)


def application_category(path: Path) -> str:
    app = path.relative_to(ROOT).parts[0]
    if app in GAME_APPS:
        return "GameApplication"
    if app in EDUCATION_APPS:
        return "EducationalApplication"
    if app in FINANCE_APPS:
        return "FinanceApplication"
    if app in MULTIMEDIA_APPS:
        return "MultimediaApplication"
    return "UtilitiesApplication"


def add_software_schema(path: Path, source: str) -> str:
    relative = rel(path)
    is_landing = "landing_page_" in path.name or path.name == "app_introduction.html"
    is_versamemo_home = relative in {"VersaMemo/en/index.html", "VersaMemo/ja/index.html"}
    if not (is_landing or is_versamemo_home) or "noindex" in source.lower():
        return source
    if re.search(r'"@type"\s*:\s*"(?:SoftwareApplication|MobileApplication)"', source):
        return source

    description_match = re.search(
        r"<meta\b[^>]*\bname=[\"']description[\"'][^>]*\bcontent=[\"']([^\"']*)",
        source,
        flags=re.I,
    )
    description = html.unescape(description_match.group(1)) if description_match else description_for(path, source)
    name = re.split(r"\s+[|—–-]\s+", title_from(source), maxsplit=1)[0].strip()
    schema = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": name,
        "url": canonical_url(path),
        "description": description,
        "applicationCategory": application_category(path),
        "operatingSystem": "Android, iOS",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "JPY" if language_for(path) == "ja" else "USD",
        },
        "publisher": {"@type": "Organization", "name": "TakeKApp", "url": f"{BASE_URL}/"},
    }
    payload = json.dumps(schema, ensure_ascii=False, indent=2)
    block = f'    <script type="application/ld+json">\n{payload}\n    </script>'
    return insert_before_head_end(source, block)


def replace_known_broken_references(path: Path, source: str) -> str:
    relative = rel(path)

    if relative.startswith("SharedDice/landing_pages/"):
        language = language_for(path)
        policy_language = "ja" if language == "ja" else "en"
        source = re.sub(
            r"href=[\"']\.\./[^/]+/(terms_and_conditions|privacy_policy)_[^\"']+\.html[\"']",
            lambda m: f'href="../../{policy_language}/{m.group(1)}_{policy_language}.html"',
            source,
        )

    if relative.startswith("Tificat/") and "/en/" not in f"/{relative}" and "/ja/" not in f"/{relative}":
        source = source.replace('href="terms_and_conditions_en.html"', 'href="../en/terms_and_conditions_en.html"')
        source = source.replace('href="privacy_policy_en.html"', 'href="../en/privacy_policy_en.html"')

    if relative.startswith("blog/posts/"):
        source = source.replace('href="../../index.html"', 'href="/blog/index.html"')

    if relative in {"LoanManagement/ja/privacy_policy_ja.html", "LoanManagement/ja/terms_and_conditions_ja.html"}:
        source = source.replace('href="../favicon.ico"', 'href="../images/app_icon/icon_loan_management_1024_1024_ios.png"')

    if relative.startswith("MemoWinkAlbum/"):
        source = re.sub(
            r"Download_on_the_App_Store_Badge_(?:CN|HK|DE|KR|FR|ES)_RGB_blk_100317\.svg",
            "Download_on_the_App_Store_Badge_US-UK_RGB_blk_092917.svg",
            source,
        )

    if relative.startswith("FunTopics/") and "landing_page_" in path.name:
        language = language_for(path)
        image_language = language if (ROOT / "FunTopics/images/screen_shots/phone" / language).is_dir() else "en"
        image_dir = ROOT / "FunTopics/images/screen_shots/phone" / image_language
        available = sorted(image_dir.glob("*.png"))
        preferred = available[-3:] if len(available) >= 3 else available
        references = list(re.finditer(
            r"(?P<quote>[\"'])(?P<src>images/screen_shots/phone/[^/]+/[^\"']+\.png)(?P=quote)",
            source,
        ))
        replacement_index = 0
        for match in references:
            if not preferred:
                break
            image_source = match.group("src")
            if (path.parent / image_source).exists():
                continue
            replacement = (
                f'{match.group("quote")}../images/screen_shots/phone/{image_language}/'
                f'{preferred[replacement_index % len(preferred)].name}{match.group("quote")}'
            )
            source = source.replace(match.group(0), replacement, 1)
            replacement_index += 1
        if language not in {"ja", "en"}:
            source = re.sub(r"href=[\"'](?:privacy_policy|terms_and_conditions)_[^\"']+\.html[\"']",
                            lambda m: 'href="../en/privacy_policy_en.html"' if "privacy" in m.group(0)
                            else 'href="../en/terms_and_conditions_en.html"', source)

    return source


def build_hreflang_clusters(paths: list[Path]) -> dict[Path, list[Path]]:
    clusters: dict[str, list[Path]] = defaultdict(list)
    for path in paths:
        relative = rel(path)
        if "noindex" in path.read_text(encoding="utf-8", errors="ignore").lower():
            continue
        if "landing_page_" in path.name:
            app = path.relative_to(ROOT).parts[0]
            clusters[f"app:{app}"].append(path)
        elif relative in {"VersaMemo/en/index.html", "VersaMemo/ja/index.html"}:
            clusters["app:VersaMemo"].append(path)
        elif relative.startswith("blog/posts/"):
            slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.name)
            clusters[f"blog:{slug}"].append(path)

    result: dict[Path, list[Path]] = {}
    for members in clusters.values():
        distinct_languages = {language_for(member) for member in members}
        if len(distinct_languages) < 2:
            continue
        for member in members:
            result[member] = members
    return result


def add_hreflang(path: Path, source: str, members: list[Path]) -> str:
    source = re.sub(
        r"\s*<link\b[^>]*\brel=[\"']alternate[\"'][^>]*\bhreflang=[\"'][^\"']+[\"'][^>]*>",
        "",
        source,
        flags=re.I,
    )
    by_language: dict[str, Path] = {}
    for member in sorted(members, key=lambda item: rel(item)):
        by_language.setdefault(language_for(member), member)
    lines = [
        f'    <link rel="alternate" hreflang="{language}" href="{canonical_url(member)}">'
        for language, member in sorted(by_language.items())
    ]
    default = by_language.get("en") or by_language.get("ja") or next(iter(by_language.values()))
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{canonical_url(default)}">')
    return insert_before_head_end(source, "\n".join(lines))


def write_redirects() -> None:
    for old_relative, new_relative in RETIRED_URLS.items():
        old_path = ROOT / old_relative
        target = f"{BASE_URL}/{new_relative}"
        language = language_for(old_path)
        label = "ページは新しいURLへ移動しました。" if language == "ja" else "This page has moved to a new URL."
        document = f'''<!doctype html>
<html lang="{language}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex,follow">
    <link rel="canonical" href="{target}">
    <meta http-equiv="refresh" content="0;url={target}">
    <title>{html.escape(label)}</title>
    <script>location.replace({json.dumps(target)} + location.search + location.hash);</script>
</head>
<body><p>{html.escape(label)} <a href="{target}">{html.escape(target)}</a></p></body>
</html>
'''
        old_path.write_text(document, encoding="utf-8")


def main() -> None:
    write_redirects()
    paths = iter_html()
    clusters = build_hreflang_clusters(paths)
    changed = 0
    for path in paths:
        before = path.read_text(encoding="utf-8", errors="ignore")
        source = replace_known_broken_references(path, before)
        source = add_basic_metadata(path, source)
        source = add_analytics(path, source)
        source = normalize_description(path, source)
        source = add_software_schema(path, source)
        if path in clusters:
            source = add_hreflang(path, source, clusters[path])
        source = optimize_images(path, source)
        if source != before:
            path.write_text(source, encoding="utf-8")
            changed += 1
    print(f"Updated {changed} HTML files.")


if __name__ == "__main__":
    main()
