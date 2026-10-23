# VersaMemo website

Release-site update: 2026-10-23.

## Public routes and deployment

- Japanese landing page: `https://takekapp.com/VersaMemo/ja/`
- English landing page: `https://takekapp.com/VersaMemo/en/`
- Each locale includes `privacy.html`, `terms.html`, and `support.html`.
- `/VersaMemo/`, `/VersaMemo/privacy/`, `/VersaMemo/terms/`, and
  `/VersaMemo/support/` select Japanese or English. Their `noindex` is intentional;
  localized landing pages have indexable canonical URLs and hreflang links.
- GitHub Pages publishes the repository root from `main`. Do not create a second
  hosting project or change existing public routes for routine updates.

## Release content

Both landing pages describe the released app and include App Store and Google
Play links at the top and bottom. The TakeKApp home page has Japanese and English
VersaMemo cards. Basic note-taking is free; eligible Pro categories have two
trials and a one-time store purchase. Use the in-app store price rather than
hard-coding a launch price here.

App and memo locks control access; they do not encrypt the local database,
attachments, automatic backups, or widgets. External backup and portable ZIPs
can separately use an optional password of at least eight characters and
AES-256. Passwords are not saved or recoverable. Keep this distinction consistent
in the landing pages, FAQs, privacy policies, terms, and support pages.

## Assets and verification

- Use real app screenshots. See `images/screenshots/README.md` for source paths
  and the AVIF/JPEG generation workflow.
- Social preview PNGs are 1200 × 630. See `images/og/README.md` for editable SVG
  sources. They do not contain pre-release copy and need no release-status edit.
- Preview the repository through a local HTTP server and check both locales at
  phone, tablet, and desktop widths, including the Pro section and bottom CTA.
- Check links, local assets, unique IDs, JSON-LD, sitemap entries, and
  `git diff --check` before publishing. `python3 scripts/seo_audit.py` is the
  repository-wide read-only SEO check; unrelated pre-existing warnings should
  be reviewed separately.

## Measurement and search

The existing GA4 property receives `app_store_click`. The shared
`/js/app_store_analytics.js` sends `store_name`, `app_name`, `lp_path`,
`link_url`, and `link_position`. Landing-page positions are `hero` and
`availability`; home-page links explicitly identify `VersaMemo` and use
`app_list_versamemo_ja` / `app_list_versamemo_en`. A click is an outbound store
visit, not a verified install or purchase. Do not inject synthetic production
events to validate the code.

Search Console already has the `takekapp.com` domain property and a successful
site sitemap submission. URL Inspection confirmed both Japanese and English
landing pages are already indexed on 2026-10-23. Both localized landing pages are listed in
`sitemap.xml`; update only the lastmod values of pages that actually change.
Request recrawling only after the deployed pages have been verified. Indexing
and search-result changes are controlled by Google and may take time.

The landing-page footer links to the website privacy policy separately from
the app privacy policy. The app's no-advertising/no-first-party-analytics
statement describes the app, not the website's GA4 measurement.
