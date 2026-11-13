#!/usr/bin/env python3
"""Add localized discovery modules to existing app legal pages.

Run from any directory: python3 scripts/build_app_discovery.py [--check]
Optional: --apps SharedDice FunTopics
Copy and recommendation profiles live in app_discovery.json. Redirects, legacy
documents and the unpublished PartyAmida draft are intentionally excluded.
Only marked navigation modules are regenerated; legal text is never translated.
"""

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((Path(__file__).with_name("app_discovery.json")).read_text())
LANG_NAMES = {"ja": "日本語", "en": "English", "ko": "한국어", "zh-Hans": "简体中文", "zh-Hant": "繁體中文"}
HUB_LANGS = {"zh-Hans": "zh_CN", "zh-Hant": "zh_TW"}
LANG_ALIASES = {"zh-CN": "zh-Hans", "zh-TW": "zh-Hant", "zh_CN": "zh-Hans", "zh_TW": "zh-Hant"}


class Metadata(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.lang = ""
        self.redirect = False
        self.main = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang", "")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.redirect = True
        if tag == "main":
            self.main = True


@dataclass
class Page:
    path: Path
    app: str
    lang: str
    kind: str


def module(name, content):
    content = "\n".join(line.rstrip() for line in content.splitlines())
    return f"<!-- takekapp-discovery:{name}:start -->\n{content}\n<!-- takekapp-discovery:{name}:end -->"


def replace_module(source, name, content):
    pattern = rf"<!-- takekapp-discovery:{name}:start -->.*?<!-- takekapp-discovery:{name}:end -->"
    return re.sub(pattern, lambda _: module(name, content), source, flags=re.S)


def landing_pages(app):
    directory = ROOT / app
    candidates = set(directory.glob("*/landing_page_*.html"))
    candidates.update(directory.glob("landing_pages/*/landing_page_*.html"))
    candidates.update(p for p in directory.glob("*/index.html") if p.parent.name in DATA["ui"])
    candidates.update(directory.glob("*/app_introduction.html"))
    pages = {}
    for path in sorted(candidates):
        meta = Metadata(path.read_text())
        if meta.lang and not meta.redirect:
            pages[LANG_ALIASES.get(meta.lang, meta.lang)] = "/" + path.relative_to(ROOT).as_posix()
    return pages


LANDINGS = {app: landing_pages(app) for app in DATA["profiles"]}


def legal_pages():
    result = []
    for app in DATA["profiles"]:
        for path in sorted((ROOT / app).rglob("*.html")):
            if not path.name.startswith(("privacy", "terms")) or "legacy" in path.name:
                continue
            meta = Metadata(path.read_text())
            if meta.redirect or meta.lang not in DATA["ui"]:
                continue
            result.append(Page(path, app, meta.lang, "privacy" if path.name.startswith("privacy") else "terms"))
    return result


def hub(lang):
    return f"/?lang={HUB_LANGS.get(lang, lang)}#apps"


def tracked_link(url, text, app, position, css=""):
    class_attr = f' class="{css}"' if css else ""
    return (f'<a{class_attr} href="{escape(url, quote=True)}" data-cross-app="{app}" '
            f'data-cross-app-position="{position}">{text}</a>')


def related(page, pages):
    # Platform-specific documents only link to their matching document variant.
    variant = "ios" if page.path.stem.endswith("_ios") else "default"
    return [other for other in pages if other.app == page.app and
            ("ios" if other.path.stem.endswith("_ios") else "default") == variant]


def header(page, pages, styled=False):
    ui = DATA["ui"][page.lang]
    own_lang = next((lang for lang in [page.lang, "en", "ja"] if lang in LANDINGS[page.app]), None)
    own = ""
    if own_lang:
        suffix = f' ({LANG_NAMES.get(own_lang, own_lang)})' if own_lang != page.lang else ""
        own = f'<a href="{LANDINGS[page.app][own_lang]}" lang="{own_lang}">{ui["own"]}{suffix}</a>'
    languages = []
    for other in related(page, pages):
        if other.lang == page.lang or other.kind != page.kind:
            continue
        url = "/" + other.path.relative_to(ROOT).as_posix()
        languages.append(f'<a class="discovery-nav__language" href="{url}" lang="{other.lang}" hreflang="{other.lang}">{LANG_NAMES[other.lang]}</a>')
    brand = tracked_link(hub(page.lang), '<img src="/commonImages/fabicons/favicon_circle.png" alt="" width="32" height="32">TakeKApp', "takekapp", "header_brand", "discovery-brand")
    more = tracked_link(hub(page.lang), ui["more"], "takekapp", "header_more_apps")
    if styled:
        # The app's original header already contains its home, support and locale links.
        own = ""
        languages = []
    compact = " discovery-header--compact" if styled else ""
    skip = f'<a class="discovery-skip" href="#legal-content">{ui["skip"]}</a>\n' if not styled else ""
    return skip + f'''<header class="discovery-header{compact}" data-takekapp-discovery>
    <div class="discovery-shell discovery-header__inner">
        {brand}
        <nav class="discovery-nav" aria-label="{ui['nav']}">
            {own}
            {more}
            {''.join(languages)}
        </nav>
    </div>
</header>'''


def recommendations(page):
    candidates = DATA["recommendations"][DATA["profiles"][page.app]]
    # Prefer actual localized LPs. If needed, an English fallback is labeled.
    selected = []
    for lang in dict.fromkeys([page.lang, "en"]):
        for app in candidates:
            if app == page.app or any(app == chosen[0] for chosen in selected):
                continue
            if lang in DATA["apps"][app]["copy"] and lang in LANDINGS[app]:
                selected.append((app, lang))
                if len(selected) == 3:
                    return selected
    raise ValueError(f"Not enough recommendation targets for {page.path}")


def footer(page, pages, styled):
    ui = DATA["ui"][page.lang]
    cards = []
    for app, lang in recommendations(page):
        info = DATA["apps"][app]
        copy = info["copy"][lang]
        fallback = f'<span class="discovery-app__language">{ui["english"]}</span>' if lang != page.lang else ""
        contents = f'''<img src="{info['icon']}" alt="" width="56" height="56" loading="lazy" decoding="async">
                <h3 lang="{lang}">{escape(copy['name'])}</h3>
                <p lang="{lang}">{escape(copy['description'])}</p>
                {fallback}
                <span class="discovery-app__cta">{ui['cta']}<span aria-hidden="true">→</span></span>'''
        cards.append(tracked_link(LANDINGS[app][lang], contents, app, "footer_card", "discovery-app"))
    all_apps = tracked_link(hub(page.lang), ui["all"] + ' <span aria-hidden="true">→</span>', "takekapp", "footer_all_apps", "discovery-all-apps")
    section = f'''<section id="more-apps" class="discovery-recommendations" data-takekapp-discovery aria-labelledby="more-apps-title">
    <div class="discovery-shell">
        <p class="discovery-recommendations__eyebrow">MORE BY TAKEKAPP</p>
        <h2 id="more-apps-title">{ui['heading']}</h2>
        <p class="discovery-recommendations__intro">{ui['intro']}</p>
        <div class="discovery-apps">
            {''.join(cards)}
        </div>
        {all_apps}
    </div>
</section>'''
    if styled:
        return section
    links = []
    for other in related(page, pages):
        if other.lang != page.lang:
            continue
        url = "/" + other.path.relative_to(ROOT).as_posix()
        current = ' aria-current="page"' if other.path == page.path else ""
        links.append(f'<a href="{url}"{current}>{ui[other.kind]}</a>')
    return section + f'''
<footer class="discovery-footer" data-takekapp-discovery>
    <div class="discovery-shell discovery-footer__inner">
        <small>© TakeKApp</small>
        <nav aria-label="{ui['legal_nav']}">{''.join(links)}</nav>
    </div>
</footer>'''


CSS_VERSION = hashlib.sha256((ROOT / "css/legal_navigation.css").read_bytes()).hexdigest()[:12]
ASSETS = f'''<link rel="stylesheet" href="/css/legal_navigation.css?v={CSS_VERSION}">
<script defer src="/js/cross_app_analytics.js"></script>'''


def migrate_pilot(source):
    """Convert the original four-page prototype to the shared generator once."""
    if 'class="legal-page" data-app="SharedDice"' not in source:
        return source
    content = re.search(r'<main\b[^>]*>\s*<p class="legal-document__label">.*?</p>(.*?)</main>', source, re.S).group(1)
    source = re.sub(r'<body\b[^>]*>.*?</body>', lambda _: "<body>" + content + "</body>", source, count=1, flags=re.S)
    source = re.sub(r'^[ \t]*<(?:link rel="stylesheet" href="/css/legal_navigation.css"|script defer src="/js/cross_app_analytics.js")[^\n]*\n', "", source, flags=re.M)
    return source


def render(page, pages):
    source = page.path.read_text()
    if "<!-- takekapp-discovery:assets:start -->" in source:
        styled = 'data-discovery-layout="existing"' in source
        # Migrate an earlier generated skip link into the header module.
        source = re.sub(r'(?<=<!-- takekapp-discovery:header:end -->)\s*<a class="discovery-skip".*?</a>', "\n", source)
        source = replace_module(source, "assets", ASSETS)
        source = replace_module(source, "header", header(page, pages, styled))
        source = replace_module(source, "footer", footer(page, pages, styled))
        return re.sub(r"(?m)^[ \t]+$", "", source)

    source = migrate_pilot(source)
    styled = Metadata(source).main
    body = re.search(r'<body\b([^>]*)>(.*?)</body>', source, re.I | re.S)
    if not body:
        raise ValueError(f"Missing body in {page.path}")
    attrs, original = body.groups()
    attrs += f' data-app="{page.app}" data-page-type="{page.kind}" data-discovery-layout="{"existing" if styled else "document"}"'
    if not styled:
        if re.search(r'\bclass=', attrs):
            attrs = re.sub(r'\bclass=([\'"])(.*?)\1', lambda m: f'class="{m[2]} discovery-page"', attrs)
        else:
            attrs += ' class="discovery-page"'
        name = DATA["apps"].get(page.app, {}).get("copy", {}).get(page.lang, {}).get("name", "TakeKApp")
        original = f'<main id="legal-content" class="discovery-shell discovery-document" tabindex="-1">\n<p class="discovery-document__label">{escape(name)} · LEGAL</p>\n' + original + '\n</main>'
    bottom = module("footer", footer(page, pages, styled))
    if styled and re.search(r'<footer\b', original, re.I):
        original = re.sub(r'<footer\b', lambda _: bottom + '\n<footer', original, count=1, flags=re.I)
    else:
        original += '\n' + bottom
    replacement = f'<body{attrs}>\n' + module("header", header(page, pages, styled)) + '\n' + original + '</body>'
    source = source[:body.start()] + replacement + source[body.end():]
    source = re.sub(r'</head>', lambda _: module("assets", ASSETS) + '\n</head>', source, count=1, flags=re.I)
    return re.sub(r"(?m)^[ \t]+$", "", source)


def validate(page, source):
    class Check(HTMLParser):
        def __init__(self):
            super().__init__()
            self.ids = []
            self.cards = 0

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if "id" in attrs:
                self.ids.append(attrs["id"])
            if attrs.get("class") == "discovery-app":
                self.cards += 1
                assert attrs["data-cross-app"] != page.app, f"Self recommendation: {page.path}"
            if tag not in ("a", "img", "link", "script"):
                return
            if tag == "link" and attrs.get("rel") != "stylesheet":
                return
            url = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
            if not url or not url.startswith("/"):
                return
            target = ROOT / urlsplit(url).path.lstrip("/")
            assert target.exists(), f"Broken local link on {page.path}: {url}"

    check = Check()
    check.feed(source)
    assert check.cards == 3, f"Expected three recommendations: {page.path}"
    assert len(check.ids) == len(set(check.ids)), f"Duplicate ids: {page.path}"
    for name in ["assets", "header", "footer"]:
        assert source.count(f"<!-- takekapp-discovery:{name}:start -->") == 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apps", nargs="+", choices=sorted(DATA["profiles"]))
    parser.add_argument("--check", action="store_true", help="Validate generated modules without writing files")
    args = parser.parse_args()
    pages = legal_pages()
    chosen = [page for page in pages if not args.apps or page.app in args.apps]
    updates = []
    for page in chosen:
        updated = render(page, pages)
        validate(page, updated)
        if updated != page.path.read_text():
            updates.append((page.path, updated))
    if args.check and updates:
        for path, _ in updates:
            print(f"Out of date: {path.relative_to(ROOT)}")
        raise SystemExit(1)
    for path, updated in updates:
        path.write_text(updated)
    print(f"{'Checked' if args.check else 'Built'} {len(chosen)} legal pages across {len({p.app for p in chosen})} apps / {len({p.lang for p in chosen})} languages; {len(updates)} updates.")


if __name__ == "__main__":
    main()
