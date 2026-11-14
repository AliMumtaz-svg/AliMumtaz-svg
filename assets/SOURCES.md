# Asset sources and licences

All five SVGs in this folder are self-contained. Each one embeds its fonts as base64 WOFF2 data URIs, uses only CSS for motion, and makes no network requests when rendered. The SVGs contain no scripts, no SMIL and no nested HTML.

## Fonts (embedded)

| Role | Family | Version / source | Licence |
|---|---|---|---|
| Display (weight 700) | Space Grotesk | `@fontsource/space-grotesk` 5.3.0 (latin subset, WOFF2) | SIL Open Font License 1.1. Copyright 2020 The Space Grotesk Project Authors. |
| Mono (weight 400) | JetBrains Mono | `@fontsource/jetbrains-mono` 5.3.0 (latin subset, WOFF2) | SIL Open Font License 1.1. Copyright 2020 The JetBrains Mono Project Authors. |

The licence texts ship in `profile-design/licenses/`.

## Tech and social icons

| Icon | Source | Licence | Notes |
|---|---|---|---|
| Python, TypeScript, React, Next.js, Node.js, PostgreSQL, Docker, Git, Linux, Tailwind CSS | Simple Icons (`simple-icons` npm package) | CC0 1.0 | Each icon's title was checked against its requested label. |
| YouTube | Simple Icons | CC0 1.0 | |
| Instagram | Simple Icons | CC0 1.0 | |
| LinkedIn | **Not from Simple Icons.** Simple Icons no longer ships a LinkedIn mark. | Trademark of LinkedIn Corporation | The current file uses a monogram ("in"), not the official mark. See below. |
| Topmate | **Not from Simple Icons.** No mark is listed there. | Trademark of its owner | The current file uses a monogram ("T"), not the official mark. See below. |

Brand marks are trademarks of their owners. Simple Icons' CC0 licence covers the icon files only.

### LinkedIn: official mark (still to be added)

- Official guidelines: https://www.brand.linkedin.com/in-logo
- Official download page: https://www.brand.linkedin.com/downloads (the `[in]` logo zip is linked there)
- Terms: use only the approved blue, black or white variations. Do not modify the colour or shape.

I located the official page and download link. I could not retrieve the zip into this build environment, so the monogram stays until you add the SVG. To swap it in, extract `in-logo` from the zip, then replace the monogram group in `connect.svg` with the official path.

### Topmate: official mark (still to be added)

I did not find an official Topmate brand asset in my search. The monogram "T" is a placeholder. To replace it, obtain the mark from Topmate's own brand or press resources and record its URL here.

## Images (you supply)

- `id.png`: the portrait, which appears in `hero.svg` and `id-dashboard.svg`.
- `right_pointing.png`: the pointing character, which appears in `connect.svg`.

Run `python3 inline_images.py` from this folder after adding them. The script embeds each PNG unchanged as a base64 data URI, so alpha is preserved.
