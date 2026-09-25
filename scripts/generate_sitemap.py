
import subprocess
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

BASE_URL = "https://takekapp.com"
ROOT = Path(__file__).resolve().parents[1]


def canonical_url(path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    if relative == "index.html":
        return f"{BASE_URL}/"
    if relative.endswith("/index.html"):
        return f"{BASE_URL}/{relative[:-10]}"
    return f"{BASE_URL}/{relative}"


def last_modified(path: Path) -> str:
    relative = str(path.relative_to(ROOT))
    dirty = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", relative],
        cwd=ROOT,
        check=False,
    )
    if dirty.returncode == 1:
        return date.today().isoformat()
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", relative],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() or date.today().isoformat()


def generate_sitemap() -> None:
    pages: dict[str, Path] = {}
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts or "_private_docs" in path.parts:
            continue
        source = path.read_text(encoding="utf-8", errors="ignore")
        if "noindex" in source.lower():
            continue
        url = canonical_url(path)
        pages.setdefault(url, path)

    ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset = ET.Element("{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")
    for url, path in sorted(pages.items()):
        entry = ET.SubElement(urlset, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        ET.SubElement(entry, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text = url
        ET.SubElement(entry, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod").text = last_modified(path)

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    with (ROOT / "sitemap.xml").open("a", encoding="utf-8") as stream:
        stream.write("\n")
    print(f"Successfully generated sitemap.xml with {len(pages)} canonical URLs.")

if __name__ == "__main__":
    generate_sitemap()
