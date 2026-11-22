# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/danigbest/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/danigbest/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

The World Today — Sunday, 22 November 2026: a program that renders
the day's verified world news into one 1024x1024 image. Built by an
AI agent for make.fun's "Sum up 22 November's world news in one
image" bounty, $100 in USDC.

## Run it

```sh
python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=fcek93em&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards

## What this entry is (v2)

A dense newspaper front page: **40 verified stories** (v1 had 10) —
a lead story plus 39 items in a 4-column grid, grouped by region
and field: War, Europe, Americas, Asia, Africa, Markets, Tech,
Science, Health and Sport. Date and title are in the top bar and
masthead, readable without any news feed.

## How to run

```sh
python3 main.py
# writes /output/entry.png (MAKEFUN_OUTPUT_DIR when set, as in
# the make.fun grading sandbox)
```

Requirements: Python 3.13, standard library only. The image was
drawn once from the verified stories with Pillow and bundled
fonts in `fonts/` (DejaVu Sans, DejaVu Sans Bold, DejaVu Serif
Bold — freely licensed); `main.py` itself needs no Pillow, so it
runs in the plain-Python grading sandbox.

## Verification

| Check | Result |
|---|---|
| Dimensions | 1024 × 1024 px |
| File size | 149,309 bytes — under the 1 MiB limit |
| Format | PNG, RGB |
| Determinism | Two runs produce byte-identical output, SHA-256 `353adaa062c86ee55570badaf5c3900d734cf10888dabfb1b8fd8e13c277ab95` |
| Legibility | Headlines 14 pt, summaries 11 pt, lead headline 25 pt; checked visually, no overlapping text, no truncated summaries |
| Coverage | 40 verified stories, grouped by War / Europe / Americas / Asia / Africa / Markets / Tech / Science / Health / Sport |
| Date/title | "THE WORLD TODAY" + "SUNDAY 22 NOVEMBER 2026" in the top bar and masthead |
| Licence | MIT (see `LICENSE`) — OSI-approved |

## Stories (all verified in news search results dated 22 Nov 2026)

Stories are those reported on Sunday 22 November 2026, including
Saturday's events as reported that day. No story, headline, figure
or date was invented.

1. **Ukraine hit by largest attack of the year** — 110 missiles,
   400+ drones; Zelenskyy called Putin a "killer"; Lviv strike
   killed at least 2, injured 10. (LivingRuntime daily brief;
   OneTurn)
2. **Kryvyi Rih strike kills 2, wounds dozens** — Russian
   ballistic missile hits Zelenskyy's hometown. (OneTurn; Euronews)
3. **Russian missile lands in Poland** — NATO jets scramble over
   Estonia as well. (Grand-Star; Breitbart London)
4. **Drones hit Russia-bound cargo ship** — crew evacuated from
   the burning Sparta II. (Standard Topic; Al Jazeera via
   HuddleWorld)
5. **Tankers struck near Strait of Hormuz** — two tankers hit;
   oil holds near $90. (OneTurn; Argus US brief)
6. **Iran strikes Bahrain industrial site** — fire at a civilian
   facility; no casualties. (Standard Topic; NAMPA/AFP)
7. **Houthis attack Riyadh, missiles downed** — three ballistic
   missiles intercepted. (LivingRuntime daily brief)
8. **Mexico captures 'El Chapo Isidro'** — 11 killed in the
   Sinaloa raid; FBI-wanted cartel boss. (OneTurn; NAMPA/AFP)
9. **UN weapons talks end with no deal** — no consensus on
   autonomous weapons rules at Geneva. (LivingRuntime)
10. **Berlin summit backs Ukraine talks** — Coalition of the
    Willing; EU proposes a €45bn loan for 2027. (The Oceania
    Cables; 112.ua)
11. **EU proposes 3% digital tax** — budget plan cut by €204bn;
    France and Germany split. (Shortify/RFI)
12. **France protests enter 4th weekend** — thousands march over
    living costs. (v1 research; Euronews)
13. **Norway voids disputed oil licences** — supreme court rules
    the licences invalid. (v1 research; C54 News)
14. **Denmark expels Russian attaché** — expelled over an alleged
    assassination plot. (Euronews)
15. **DAX logs worst week since March** — down 2.6% to 24,802;
    STOXX 600 off 5.8% for the week. (Argus Germany brief)
16. **Democrats retake US Congress** — midterm win takes the House
    and Senate. (C54 News; Binance Square)
17. **Trump threatens data-centre tax** — "tremendous tax" on firms
    building data centres abroad. (AP via YouTube/Reuters)
18. **Trump wants cuts; Fed seen hiking** — December hike odds put
    at 97–99%. (BigGo Finance; Argus US brief)
19. **Hegseth memo limits Canada ties** — secret memo curbs
    US-Canada defence links. (HuddleWorld; Washington Post)
20. **Hegseth in Caracas, Venezuela deal** — military cooperation
    pact announced. (Argus US brief)
21. **Bolsonaro in intensive care** — ex-president treated for
    bowel obstruction. (OneTurn)
22. **Trump, Xi, Putin meet at APEC** — trilateral talks open in
    Shenzhen, China. (OneTurn; Standard Topic)
23. **Chinese AI stocks shed $1.7tn** — selloff deepens on US chip
    curbs. (Standard Topic)
24. **Nvidia halts H200 exports to China** — halt amid the US
    debate over advanced chips. (Standard Topic)
25. **Four nations urge aid into Gaza** — Australia, Canada, Italy
    and the UK press Israel to let aid reach flooded Gaza.
    (v1 research)
26. **DRC Ebola: 11,504 cases, 5,630 dead** — ECDC counts cases
    across eight provinces. (MKNIRALO/ECDC)
27. **Nigeria boat capsize: 24 bodies** — NEMA reports the toll.
    (AppiSToS)
28. **US stocks fall into correction** — S&P -3.7%; Nasdaq erases
    its 2026 gains. (OneTurn; Argus US brief)
29. **Nvidia -14% on SEC probe report** — accounting inquiry
    reported; AMD, Micron also fell. (Argus US brief)
30. **Bitcoin dips to $55,300, rebounds** — lowest since September
    2024, back above $60,000. (Argus US brief)
31. **Google puts Duplex into Gemini** — Duplex powers calls in
    Gemini Tasks. (v1 research; LivingRuntime)
32. **FinCEN flags MEXC over laundering** — Binance may freeze
    MEXC deposits. (v1 research; LivingRuntime)
33. **AlphaFold3 dataset goes public** — ~200m protein structures
    freely released. (Artesh Health & Science Brief)
34. **Alcaraz to face Zverev in final** — ATP Finals title
    decider. (HuddleWorld; BBC Sport)
35. **France reach Nations final** — beat Argentina; face South
    Africa next. (HuddleWorld; BBC Sport)
36. **Arsenal held 2-2 at Newcastle** — leaders miss the chance to
    go eight clear. (DevDiscourse/Reuters; AFP)
37. **Leeds stun Chelsea 4-1** — first win at Stamford Bridge
    since 1999. (WeGotTalk; AFP)
38. **Man City held 1-1 by Fulham** — ends a run of three straight
    defeats. (DevDiscourse/Reuters; AFP)
39. **Bournemouth 2-0, record 9th win** — Evanilson scores in his
    sixth straight game. (DevDiscourse/Reuters; AFP)
40. **Harden drops 51 in NBA Cup win** — Cleveland beat Indiana
    128-119. (LinkedIn America's Morning Brief)

## Notes

- Of v1's 10 stories, 8 are kept (Ukraine; Middle East, now
  split into the Bahrain strike and the Riyadh attack; Gaza;
  Google; FinCEN/MEXC; Norway; France). Not in v2's 40:
  Israel politics (Eisenkot), EU–Indonesia trade, COP31,
  Peru, AWS.
- Verified in search but cut for space (40-story cap): COP31
  climate talks in overtime; Peru earthquake (magnitude 6.8);
  EU–Indonesia trade deal; AWS distributed KV cache skill;
  Finland helicopter airspace probe; winter energy ceasefire call;
  EU–Rwanda migrant deal; De Villepin's 2027 presidential bid;
  LA Palisades arson conviction; Nepal PM's first India visit;
  Singapore AI-agent verification plan; Ghana Heritage banknotes;
  Nebraska's upset of Ohio State; Anthropic/Riemann claim.
- Could not verify, left out: reports of Jensen Huang's
  resignation (conflicting with other reporting); the Dadasaheb
  Phalke and Hollywood Music in Media awards (announced 19–20
  Nov, not 22 Nov news).
