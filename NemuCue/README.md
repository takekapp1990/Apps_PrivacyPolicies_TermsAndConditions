# NemuCue landing pages

20 localized LPs: `<language>/index.html`.
Shared LP styles: `landing.css`. Edit `content/landing-copy.json`, then run `python3 NemuCue/tools/build_landing.py` from the website repository root. The generated static HTML has no runtime build dependency. The build also copies `language-router.js` into the shared entry page's inline script.
The existing `styles.css` belongs to privacy, terms and support pages.

## Copy sources (2026-11-04)

- Japanese headline: **変な振動で、起こします。** — uploaded store listing, `nemu_cue/store_creatives/listing/ja.json` (upload/readback recorded on 2026-10-31).
- Japanese audience: **仮眠や寝かしつけで、そのまま寝てしまう人へ。** — app introduction `msg0785` in `localization/source_messages.json`.
- The app introduction uses the longer headline **変な振動パターンで、起こしにいきます。** (`msg0786`). The LP uses the short store version with the same meaning; no new unrelated slogan.
- Vibration heading: **短い。長い。連打。次が読めない振動。** — existing Japanese store screenshot copy.
- English headline: **Wake up to unusual vibrations.** — uploaded English store listing.
- Function descriptions and free/Premium boundaries follow the store listing. Monthly and one-time purchase are both supported. No fixed prices are embedded.

The latest local app changes repeat scheduling from fixed initial times to scheduling the next alarm after stopping. The LP deliberately describes only the behavior shared by both versions. Its diagram illustrates the number of reminders, without promising specific times. Confirm the released build before adding a detailed timing example.

## Images

`images/lp/<language>/` contains optimized 640px-wide JPEGs derived from the app's existing iPhone screenshot inputs, not fabricated web UI. The source screenshots are from the iPhone app.

Originals in the Flutter repository:

`store_creatives/nemu_cue/input_screenshots/ios/iPhone/{ja,en-US}/slot_*.png`

Mapping: `01` alarm, `02` vibration, `03` ringing, `04` math, `05` sequence, `06` light, `07` night.
The screenshot input files may be updated independently; compare against the shipping app before replacing these assets.

## Publication (2026-11-07)

The app has been released. The LP App Store and Google Play links both returned HTTP 200 and resolved to NemuCue listings on 2026-11-07. The localized LPs are indexable and included in the site sitemap. The shared `/NemuCue/` language router retains `noindex, follow` so search results use the language-specific canonical URLs. The homepage already links to NemuCue and both stores.

- App Store: `https://apps.apple.com/jp/app/id6827425453` (English page uses `/us/`).
- Google Play: `https://play.google.com/store/apps/details?id=com.takekapp1990.nemucue` with the page language in `hl`.
- Badge assets are shared with other app LPs in `commonImages/badgeiOSAppStore/` and `commonImages/badgeAndroid/`.

After an LP update, regenerate the localized pages, update the 20 NemuCue canonical URLs in the site sitemap, run the checks below, and confirm the published pages and store links. Compare screenshots and the repeat-alarm description with the released build before changing those claims.

## Preview

From the website repository root:

```sh
python3 -m http.server 8793 --bind 127.0.0.1
```

Open `http://127.0.0.1:8793/NemuCue/ja/index.html`.
No external fonts, analytics or build step are required. The header uses the same native disclosure dropdown as VersaMemo, with all 20 app language choices and a checkmark for the current language. `landing.js` adds outside-click, Escape and focus-out dismissal. Language links and FAQ disclosures also work without JavaScript. Reduced-motion preferences are supported.

The KV cycles through alarm setup, ringing alarm, vibration settings, calculation and Night Screen every four seconds with a short crossfade. Arrows, screen selectors, keyboard arrows and horizontal touch swipes select a screen and pause automatic rotation. The pause/resume button controls automatic rotation; hovering, keyboard focus, leaving the viewport and a hidden browser tab temporarily suspend it. Reduced-motion settings disable automatic rotation and transitions. Without JS, the first screenshot remains visible and controls stay hidden. The phone frame reserves the same space for every slide. The KV has no floating time label or platform footnote.

The vibration section explains unfamiliar rhythms as a cue to notice the alarm and wake up, without claiming measured effectiveness. A dedicated sounds and light section follows Night Screen usage, using the actual light controls screenshot. Its copy covers the three sound choices, the fade before the first reminder, and screen light colors and brightness.

## Languages and routing (2026-11-04)

The app and uploaded store listing support 20 locales: ja, en, zh-Hans, zh-Hant, ko, es, pt-BR, fr, de, it, nl, ru, uk, pl, tr, ar, hi, id, vi and th. This set comes from the app's `localization/locales.json` and `store_creatives/nemu_cue/locales.json`. Store text upload and verification is recorded in `output/store-listing-upload-2026-10-31/status.json`; this record verifies localized metadata, not current public availability. The current store API could not be queried in this environment because its authentication configuration was unavailable.

The 18 added translations reuse the corresponding uploaded store headline, feature descriptions, purchase terms and app introduction, plus localized navigation and the vibration-benefit explanation. Release-specific fixed alarm timing is omitted. Each locale uses its own existing iPhone screenshot set. Arabic uses `dir="rtl"` with matching layout rules. Added-language FAQs cover iPhone use, sounds/light and free functions. Japanese and English retain their existing five questions. Legal/support content remains at the existing Japanese and English URLs; added LPs explicitly label their English destinations. Official English store badges are reused outside Japanese.

`/NemuCue/` is the shared entry URL. Its router runs inline in the document head, before any stylesheet or external script, and immediately redirects to a locale page. No LP stylesheet is fetched for the entry page. It selects a saved manual choice first, then the first supported language from `navigator.languages`, and finally English. Chinese script tags take precedence over region: Hant or TW/HK/MO uses Traditional Chinese, otherwise Hans. Portuguese variants use pt-BR. Query parameters and the hash are retained. Storage errors are tolerated. If the page remains open after three seconds, JavaScript retries with the English page. A `noscript` refresh also moves to English after three seconds when JavaScript is disabled. Language-specific URLs never auto-redirect, so shared links and explicit selections stay in that language. The dropdown remains on each LP and remembers explicit choices when browser storage is available. If redirecting is unavailable, the shared entry provides links to all 20 LPs.

Validation:

```sh
python3 NemuCue/tools/check_landing.py
node NemuCue/tools/check_language_router.cjs
node --check NemuCue/language-router.js
node --check NemuCue/landing.js
```

Each KV screenshot has a localized sentence explaining its use or benefit. Captions use 16px desktop / 15px mobile text. All five captions participate in one CSS grid cell, reserving the height of the longest caption at the current width so the page stays still when slides change. Image alt text and selector names retain concise screen labels.

## OGP images

`images/ogp/<locale>.jpg` contains browser screenshots of each localized KV at 1200×800. The 3:2 image ratio and centered capture layout keep the headline, real app screen, app name and store badges together. The capture fills a 1100px-wide area with a 300px phone, a 78px Japanese headline (60px in other locales), 22px audience text and a larger app name to stay readable in thumbnails. The copy is inset toward the phone by 20–44px per locale while preserving its line breaks; RTL Arabic uses a negative horizontal offset. These are deterministic screenshots of the first carousel slide, not generated illustrations. The shared `/NemuCue/` entry uses the Japanese image so social crawlers do not depend on JavaScript; language-specific pages use their own image. Open Graph dimensions, image alt text and Twitter large-image tags are set explicitly.

The live desktop KV is limited to 1000px with a 24px column gap to bring the copy and phone closer to the center. Mobile retains its existing single-column layout. The stylesheet URL includes a content hash for cache refresh.

To refresh images after editing the LP, run `python3 NemuCue/tools/build_landing.py`, then `python3 NemuCue/tools/prepare_ogp_capture.py`. Serve the repository locally, open `/NemuCue/_ogp/<locale>.html` with a browser viewport of exactly 1200×800, wait for the actual app screenshot to load, and save a viewport JPEG to `NemuCue/images/ogp/<locale>.jpg`. `_ogp/` is an ignored temporary preview directory and is not part of the published source.
