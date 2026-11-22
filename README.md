# Sum up 22 November's world news in one image

make.fun bounty: **Sum up 22 November's world news in one image**
https://make.fun/bounty/news-image-20261122

- Prize: $100, 50 places paid — 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20
- Ends: Tue, Nov 24, 2026, 12:00 AM UTC
- Entry: a program that writes one image to `/output/entry.png`.
  An AI judge that can see images compares entries two at a time and
  picks the one that best sums up the day's world news. The judge has
  no news feed — it judges by what the image itself shows.

## What this entry is

A one-page newspaper front page for **Sunday 22 November 2026**,
rendered as a 1024×1024 PNG by `main.py` (Python 3.13, Pillow only,
no network, no randomness, no clock).

- Lead story, biggest: **Ukraine** — largest attack of the year
  (110 missiles, 400+ drones; Zelenskyy called Putin a "killer";
  Russian missile violated Polish airspace; Lviv strike killed at
  least 2, injured 10).
- Grid of 6 more stories: Middle East escalation (Iran / Bahrain /
  Houthi–Riyadh), Gaza aid call (Australia, Canada, Italy, UK),
  Israel politics (Herzog taps Eisenkot, bypassing Netanyahu),
  EU–Indonesia trade deal (98.5% of tariffs eliminated after
  10 years), COP31 deadlock (fossil fuels / finance), Peru
  earthquake (magnitude 6.8, felt in Lima).
- "Also today" strip: Google Duplex into Gemini Tasks / AWS KV
  Cache skill; FinCEN flags MEXC / Binance may freeze MEXC
  deposits; Norway voids disputed oil licences / France protests
  enter a 4th weekend.

That is 10 verified stories in total: 1 lead + 6 in the grid + 3 in
the "Also today" strip. No story was invented; every headline and
summary comes from the verified 22 Nov 2026 news list in the brief.

## How to run

```bash
python3 main.py
# writes output/entry.png (and /output/entry.png when that
# directory exists, as in the make.fun grading sandbox)
```

Requirements: Python 3.13, Pillow. Fonts are bundled in `fonts/`
(DejaVu Sans, DejaVu Sans Bold, DejaVu Serif Bold — freely
licensed), so rendering is identical on any machine; system DejaVu
paths are only a fallback.

## News sources used

The 10 stories above, as verified in the 22 Nov 2026 news search
for this bounty (Ukraine war, Middle East escalation, Gaza aid,
Israel politics, EU–Indonesia trade, COP31, Peru earthquake,
Google/AWS tech, FinCEN/MEXC crypto, Norway/France). No other
stories were added, and no figures were invented.

## Grading self-check

| Check | Result |
|---|---|
| Dimensions | 1024 × 1024 px (verified with Pillow) |
| File size | 111 KB — under the 1 MiB limit (re-check after any edit) |
| Format | PNG, RGB |
| Legibility | Large sans-serif/serif text; title 62 pt, lead headline 34 pt, grid headlines 21 pt, grid summaries 16 pt. No overlapping text; checked visually. |
| Coverage | 10 verified stories, grouped by War / Middle East / Gaza / Politics / Economy / Climate / World / Tech / Crypto |
| Date/title | "THE WORLD TODAY" + "SUNDAY 22 NOVEMBER 2026" in the top bar and masthead — readable without any news feed |
| Determinism | `main.py` run twice produces byte-identical output (same SHA-256, verified with `cmp`). No network, no `random`, no time/date calls |
| Watermark/logos | None |
| Licence | MIT (see `LICENSE`) — OSI-approved |

## What the user still needs to do to submit (not done here)

1. Create a make.fun account (if you don't have one).
2. Create a **public GitHub repo** yourself, owned by your own
   GitHub account, created after the competition opened, and push
   this code into it (with the MIT licence). Do not use anyone
   else's account.
3. Upload the AI session transcripts with each submission, as the
   bounty requires.
4. Submit via make.fun before Tue, Nov 24, 2026, 12:00 AM UTC.
   At most 10 submissions/day, 20 total; the last submission
   before the deadline is final.

This repo was built locally only. No make.fun skill kit was
installed or run, no wallet was created, no seed phrase was sent,
and nothing was submitted to make.fun or GitHub from here.
