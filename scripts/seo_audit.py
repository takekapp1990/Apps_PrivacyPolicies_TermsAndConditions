#!/usr/bin/env python3
"""Read-only SEO checks for the public TakeKApp static site.

This script intentionally inspects repository files only. It does not use
credentials, Search Console data, App Store analytics, or Play Console data.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
BASE_HOSTS = {"takekapp.com", "www.takekapp.com"}
LARGE_ASSET_BYTES = 2 * 1024 * 1024


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.images = 0
        self.images_without_dimensions = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {name.lower(): value for name, value in attrs if value is not None}
        for attribute in ("href", "src", "poster"):
            if attribute in attributes:
                self.links.append((attribute, attributes[attribute]))
        if tag.lower() == "img":
            self.images += 1
            if "width" not in attributes or "height" not in attributes:
                self.images_without_dimensions += 1


def iter_html() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.html")
        if ".git" not in path.parts and "_private_docs" not in path.parts
    )


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def first_match(pattern: str, source: str) -> str | None:
    match = re.search(pattern, source, flags=re.I | re.S)
    return html.unescape(match.group(1).strip()) if match else None


def local_target(page: Path, raw_url: str) -> Path | None:
    raw_url = html.unescape(raw_url.strip())
    if not raw_url or raw_url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None

    parsed = urlparse(raw_url)
    if parsed.scheme in {"http", "https"}:
        if parsed.hostname not in BASE_HOSTS:
            return None
        target = ROOT / unquote(parsed.path.lstrip("/"))
    elif parsed.scheme or raw_url.startswith("//"):
        return None
    elif parsed.path.startswith("/"):
        target = ROOT / unquote(parsed.path.lstrip("/"))
    else:
        target = page.parent / unquote(parsed.path)

    if not parsed.path or parsed.path.endswith("/"):
        target = target / "index.html"
    return target.resolve()


def sitemap_urls() -> set[str]:
    tree = ET.parse(ROOT / "sitemap.xml")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return {
        element.text.strip()
        for element in tree.findall("s:url/s:loc", namespace)
        if element.text
    }


def audit(strict: bool) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    canonical_pages: dict[str, list[str]] = {}
    referenced_assets: set[Path] = set()
    image_count = 0
    images_without_dimensions = 0

    for path in iter_html():
        rel = relative(path)
        source = path.read_text(encoding="utf-8", errors="ignore")
        noindex = bool(re.search(r'<meta\b[^>]*name=["\']robots["\'][^>]*content=["\'][^"\']*noindex', source, re.I))

        title = first_match(r"<title[^>]*>(.*?)</title>", source)
        description = first_match(
            r'<meta\b[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']',
            source,
        )
        canonical = first_match(
            r'<link\b[^>]*rel=["\'][^"\']*canonical[^"\']*["\'][^>]*href=["\'](.*?)["\']',
            source,
        )

        if not title:
            errors.append(f"{rel}: missing <title>")
        if not noindex and not description:
            errors.append(f"{rel}: missing meta description")
        if not noindex and not canonical:
            errors.append(f"{rel}: missing canonical URL")
        if not noindex and canonical:
            canonical_pages.setdefault(canonical, []).append(rel)

        for match in re.finditer(
            r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
            source,
            flags=re.I | re.S,
        ):
            try:
                json.loads(html.unescape(match.group(1)))
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD ({exc.msg}, line {exc.lineno})")

        parser = PageParser()
        parser.feed(source)
        image_count += parser.images
        images_without_dimensions += parser.images_without_dimensions
        for attribute, url in parser.links:
            target = local_target(path, url)
            if target is None:
                continue
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                warnings.append(f"{rel}: {attribute} escapes repository: {url}")
                continue
            if not target.exists():
                warnings.append(f"{rel}: missing local target: {url}")
            elif attribute in {"src", "poster"} and target.is_file():
                referenced_assets.add(target)

    for canonical, pages in canonical_pages.items():
        if len(pages) > 1:
            warnings.append(f"duplicate canonical {canonical}: {', '.join(pages)}")

    listed_urls = sitemap_urls()
    expected_urls = set(canonical_pages)
    for url in sorted(expected_urls - listed_urls):
        errors.append(f"sitemap missing canonical URL: {url}")
    for url in sorted(listed_urls - expected_urls):
        warnings.append(f"sitemap URL has no indexable canonical page: {url}")

    for asset in sorted(referenced_assets):
        size = asset.stat().st_size
        if size > LARGE_ASSET_BYTES:
            warnings.append(f"large referenced asset ({size / 1024 / 1024:.1f} MiB): {relative(asset)}")

    print(
        f"Audited {len(iter_html())} HTML files; "
        f"{len(canonical_pages)} canonical URLs; {image_count} images."
    )
    if images_without_dimensions:
        warnings.append(
            f"{images_without_dimensions}/{image_count} images do not declare both width and height"
        )

    if errors:
        print("\nErrors:")
        for message in errors:
            print(f"  - {message}")
    if warnings:
        counts = Counter(message.split(":", 1)[0] for message in warnings)
        print(f"\nWarnings ({len(warnings)} total across {len(counts)} files/categories):")
        for message in warnings[:100]:
            print(f"  - {message}")
        if len(warnings) > 100:
            print(f"  - ... {len(warnings) - 100} more warning(s)")

    if errors or (strict and warnings):
        return 1
    print("\nSEO audit passed.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings, such as missing local assets, as failures.",
    )
    args = parser.parse_args()
    sys.exit(audit(strict=args.strict))


if __name__ == "__main__":
    main()
