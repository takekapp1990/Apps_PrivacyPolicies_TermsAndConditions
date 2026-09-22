# VersaMemo Open Graph images

`ja.svg` and `en.svg` are the editable, deterministic sources for the 1200 × 630
social preview images. They reuse the current app icon and localized real-screen
card-view capture; no app UI is redrawn.

Because the SVG files contain relative image references, render them through a
local HTTP server from the website repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --hide-scrollbars --disable-gpu \
  --window-size=1200,630 \
  --screenshot=VersaMemo/images/og/ja.png \
  http://127.0.0.1:8765/VersaMemo/images/og/ja.svg

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --hide-scrollbars --disable-gpu \
  --window-size=1200,630 \
  --screenshot=VersaMemo/images/og/en.png \
  http://127.0.0.1:8765/VersaMemo/images/og/en.svg
```

After regeneration, verify both PNGs are exactly 1200 × 630 and visually check
the icon, text, and real-screen crop before publishing.
