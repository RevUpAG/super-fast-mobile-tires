# Super Fast Mobile Tires: growth proposal + website preview

Private preview. Every page is `noindex, nofollow`.

| Path | What it is |
|---|---|
| `/` | Audit + growth proposal (hand-written `index.html`) |
| `/website/` | New website, English |
| `/website/es/` | New website, Spanish |
| `/website/<city>/` | City pages: boca-raton, delray-beach, boynton-beach, west-palm-beach, fort-lauderdale, coral-springs |
| `/404.html` | Branded 404 |

## Editing the website

The website pages are generated. Don't edit `website/**/index.html` by hand.

- Copy (EN + ES): `build.py`
- Styles / scripts: `src/site.css`, `src/site.js`
- City intros: `src/cities.json`

Then run:

```
python3 build.py
```

## Photos needed

Put these in `/assets/` with these exact names, then run `python3 build.py`. A missing photo shows a dark tire-tread pattern, never a broken image.

| File | Status | Used for |
|---|---|---|
| `logo.png` | ✅ from their current app (cropped) | Header logo |
| `van-hero.jpg` | ✅ from their current app (side shot) | Website hero |
| `van-side.jpg` | ✅ from their current app | "This is our truck" band |
| `tech-1.jpg` | ❌ needed: tech working on a tire | "This is our truck" band |
| `tech-2.jpg` | ❌ needed: tech working on a tire | "This is our truck" band |
| `current-site.png` | ✅ screenshot of their current homepage | Proposal hero phone |

Also used: `van-rear.jpg` (rear shot from their app), plus `.webp` copies of the photos above.
When you replace a photo, delete its `.webp` copy (e.g. `van-hero-*.webp`, `van-side.webp`) or the old version keeps showing.

## TODOs before sending

- Reviews: paste real Google reviews at `<!-- REVIEW 2/3/4 -->` in `build.py`, then rebuild.
- Google profile link: replace `href="#reviews"` on the "5.0 on Google" badge in `build.py` (marked `TODO`).
- Contact slot: add the sender's WhatsApp/phone at `<!-- CONTACT -->` in `index.html`.
- At launch: remove the `.preview-only` "Back to proposal" link (one element in `build.py`) and the `noindex` tags, and add tracking at `<!-- TRACKING -->`.
