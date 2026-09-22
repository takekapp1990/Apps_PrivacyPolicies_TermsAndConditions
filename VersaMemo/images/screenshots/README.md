# VersaMemo landing-page screenshots

These images are optimized derivatives of the real app screenshots in the
VersaMemo app repository. Do not redraw or fabricate app UI for this folder.

Source directory:

```text
/Users/takekei0913/Develop/flutterWork/VersaMemo/store_creatives/versamemo/source_screenshots/{ja-JP,en-US}
```

The landing page uses AVIF first and JPEG as a browser fallback. Each derivative
is 720 × 1600 pixels and keeps the source screenshot's 9:20 aspect ratio.

To regenerate one locale with FFmpeg, run from the VersaMemo app repository and
replace `ja-JP` / `ja` with `en-US` / `en` as needed:

```bash
for source in store_creatives/versamemo/source_screenshots/ja-JP/*.png; do
  name="$(basename "$source" .png)"
  ffmpeg -y -i "$source" -vf scale=720:1600:flags=lanczos \
    -c:v libaom-av1 -still-picture 1 -crf 34 -b:v 0 \
    "/path/to/site/VersaMemo/images/screenshots/ja/${name}.avif"
  ffmpeg -y -i "$source" -vf scale=720:1600:flags=lanczos \
    -q:v 3 "/path/to/site/VersaMemo/images/screenshots/ja/${name}.jpg"
done
```

The source filenames currently map directly to landing-page positions:

1. `01_multifunction_memo`
2. `02_image_audio`
3. `03_cards_hierarchy`
4. `04_calendar`
5. `05_statistics`
6. `06_appearance`
7. `07_local_first`
8. `08_pro`

Keep the Japanese and English sets in the same order and verify both formats,
dimensions, and all HTML references before publishing.
