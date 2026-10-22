"""Cache official Google Fonts shards needed by the Japanese LP.

All text inspection happens locally. No LP text or source code is sent to Google.
Run again after editing copy to include shards for any newly used characters.
"""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
import re
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'NumberPlaceHint/fonts'
SOURCES = [ROOT / 'NumberPlaceHint/ja' / name for name in
           ['landing_page_ja.html', 'landing-page.js']]
SOURCES.append(ROOT / 'NumberPlaceHint/language_switcher.js')
# Local comparison only: the source text is never used in a request.
codepoints = {ord(c) for path in SOURCES for c in path.read_text()}
codepoints.update(range(32, 127))
CSS_URL = ('https://fonts.googleapis.com/css2?'
           'family=Zen+Kaku+Gothic+New:wght@400;500;700;900&display=swap')
AGENT = ('Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) '
         'Chrome/130.0.0.0 Safari/537.36')


def download(url):
    assert urlparse(url).hostname in {
        'fonts.googleapis.com', 'fonts.gstatic.com', 'raw.githubusercontent.com'}
    with urlopen(Request(url, headers={'User-Agent': AGENT}), timeout=30) as response:
        return response.read()


def needed(ranges):
    if not ranges:
        return True
    for item in ranges.split(','):
        bounds = item.strip().removeprefix('U+').split('-')
        low = int(bounds[0].replace('?', '0'), 16)
        high = int(bounds[-1].replace('?', 'F'), 16)
        if any(low <= point <= high for point in codepoints):
            return True
    return False


css = download(CSS_URL).decode()
OUT.mkdir(parents=True, exist_ok=True)
faces = []
files = {}
for face in re.findall(r'@font-face\s*\{(.*?)\}', css, re.S):
    ranges = re.search(r'unicode-range:\s*([^;]+)', face)
    if not needed(ranges.group(1) if ranges else ''):
        continue
    match = re.search(r'url\((https://[^)]+)\)\s*format\([\'"]?woff2[\'"]?\)', face)
    assert match and urlparse(match.group(1)).hostname == 'fonts.gstatic.com'
    url = match.group(1)
    filename = f'zen-kaku-{sha256(url.encode()).hexdigest()[:16]}.woff2'
    files[filename] = url
    faces.append('@font-face {' + face.replace(url, './' + filename) + '}')
assert faces, 'Expected official WOFF2 font faces.'


def cache(item):
    filename, url = item
    path = OUT / filename
    if path.exists():
        return path.stat().st_size
    data = download(url)
    assert data[:4] == b'wOF2', 'Expected a WOFF2 font.'
    path.write_bytes(data)
    return len(data)


with ThreadPoolExecutor(max_workers=8) as pool:
    sizes = list(pool.map(cache, files.items()))
(OUT / 'fonts.css').write_text('\n'.join(faces) + '\n')
(OUT / 'OFL.txt').write_bytes(download(
    'https://raw.githubusercontent.com/google/fonts/main/ofl/zenkakugothicnew/OFL.txt'))
print(f'Cached {len(files)} official font shards ({sum(sizes):,} bytes).')
