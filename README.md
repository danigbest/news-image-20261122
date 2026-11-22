# news-image-20261122 — v3

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/danigbest/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/danigbest/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

The World In One Day — Sunday, 22 November 2026: a program that
renders the day's verified world news into one 1024x1024 image.
Built by an AI agent for make.fun's "Sum up 22 November's world
news in one image" bounty, $100 in USDC.

## Run it

```sh
python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=fcek93em&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards

## What this entry is (v3)

A dense one-page newspaper front page: **40 verified stories
across 7 regions**, in the structure the leaderboard's top
entries share — top bar, serif masthead, number strip, region
bar, UTC timeline, three illustrated lead stories, ten smaller
illustrated stories, a world map with numbered pins, a numbered
list of the remaining stories, a DATE CHECK box and a sources
line. v2 (40 stories in a plain grid) scored 0.9496 on the dev
phase; v3 keeps the same verified stories and rebuilds the page
around the winning formula.

## How to run

```sh
python3 main.py
# writes output/entry.png (and $MAKEFUN_OUTPUT_DIR/entry.png
# when that variable is set, as in the grading sandbox)
```

Requirements: Python 3.13, standard library only. The image was
drawn once from the verified stories with Pillow and bundled
fonts in `fonts/` (DejaVu Sans, DejaVu Sans Bold, DejaVu Serif
Bold — freely licensed); `main.py` itself needs no Pillow, so it
runs in the plain-Python grading sandbox. All pictures and the
map are original, drawn in code; no image assets are loaded.

## Verification

| Check | Result |
|---|---|
| Dimensions | 1024 × 1024 px |
| File size | 186,951 bytes — under the 1 MiB limit |
| Format | PNG, RGB |
| Determinism | Two runs produce byte-identical output, SHA-256 `10b124b527997a19693cc003da883c4a25f4be0c37a4cd22068eee28ab07f9df` |
| Legibility | Lead headlines 15 pt bold, small headlines 13 pt bold, summaries 10–11 pt; checked visually, no overlapping text, no truncated lines |
| Coverage | 40 verified stories, 7 regions: Europe 15, Middle East 5, Americas 8, Asia-Pacific 3, Africa 2, Oceania 1, World 6 |
| Date/title | "THE WORLD IN ONE DAY" + "SUNDAY 22 NOVEMBER 2026" in the top bar and masthead |
| Licence | MIT (see `LICENSE`) — OSI-approved |

## Stories (all verified in news search results dated 22 Nov 2026)

Stories are those reported on Sunday 22 November 2026, including
Saturday's events as reported that day. No story, headline, figure
or date was invented. Left out as other days' news (see the DATE
CHECK box on the page): the Peru earthquake (20 Nov local),
Russian missiles landing in Poland (19 Nov), the Kerch Bridge
strikes (earlier that week) and the Shenzhen summit (19 Nov).

### Lead stories (1–3)

1. **COP31 climate talks close in on a final deal** — Antalya,
   Türkiye. New package after a fight over fossil fuels;
   objections due by 03:00 GMT, approval session at 06:00 GMT;
   nearly 200 nations. (Reuters, BBC)
2. **Russia fires 400 drones and 110 missiles** — Kyiv, Ukraine.
   One of the war's largest overnight attacks; two killed in
   Lviv. (Al Jazeera)
3. **Iran strikes US bases in Bahrain** — Manama, Bahrain. IRGC
   says it hit two Patriot radars at Al-Riffa and Awali; a
   civilian industrial site burns, no injuries. (Al Jazeera, CNA)

### Illustrated stories (4–13)

4. **Russian cargo ship burns after drone strike** — Gulf of
   Finland. Finland says Ukraine was likely behind it. (BBC)
5. **Strike hits Zelenskyy's home city** — Kryvyi Rih. Missile
   hits the central city; 2 dead, 60 hurt. (Al Jazeera)
6. **Boat carrying mourners capsizes** — Bayelsa, Nigeria.
   24 dead. (DW)
7. **Eisenkot invites Likud to talks** — Jerusalem. He seeks
   the broadest possible government; talks begin Sunday.
   (France 24)
8. **'El Chapo Isidro' caught; violence follows** — Sinaloa,
   Mexico. FBI top-ten fugitive held after a shoot-out; 11 dead.
   (Sky News, BBC)
9. **Bitcoin holds above $60,000 on Sunday** — World markets.
   $60,112 at 01:58 UTC, back from a two-year low near $55,130.
   (FinnHub)
10. **Nvidia faces US accounting probe** — Washington. The SEC
    inquiry is at an early stage. (Argus)
11. **Bolsonaro in intensive care** — Brasília, Brazil.
    Ex-president stable, breathing on his own. (Al Jazeera, Reuters)
12. **Hong Kong votes for its Election Committee** — Hong Kong.
    856 candidates chase 723 seats; polls 9am–6pm. (China Daily)
13. **Four nations press Israel on Gaza aid** — Gaza. Australia,
    Canada, Italy and the UK; flooding adds to the suffering.
    (Wires)

### Also on Sunday 22 November (14–40)

14. **Democrats retake Congress** — Washington. Midterm win
    takes the House and Senate. (C54 News)
15. **Trump threatens data-centre tax** — Washington. "Tremendous
    tax" on firms building data centres abroad. (AP)
16. **Fed seen hiking in December** — Washington. December hike
    odds put at 97–99%. (Argus)
17. **Hegseth announces Venezuela pact** — Caracas. Military
    cooperation pact announced. (Argus)
18. **Hegseth memo curbs Canada ties** — Washington. Secret memo
    limits US–Canada defence links. (HuddleWorld)
19. **Chinese AI stocks shed $1.7tn** — Shanghai. Selloff deepens
    on US chip curbs. (Standard Topic)
20. **Nvidia halts H200 exports to China** — US. Halt amid the
    US debate over advanced chips. (Standard Topic)
21. **DRC Ebola toll 11,504 cases** — Kinshasa. ECDC counts cases
    across eight provinces; 5,630 dead. (ECDC)
22. **US stocks fall into correction** — New York. S&P −3.7%;
    Nasdaq erases its 2026 gains. (Argus)
23. **Google puts Duplex into Gemini** — US. Duplex powers calls
    in Gemini Tasks. (LivingRuntime)
24. **FinCEN flags MEXC over laundering** — US. Binance may
    freeze MEXC deposits. (LivingRuntime)
25. **AlphaFold3 dataset goes public** — London. ~200m protein
    structures freely released. (Artesh)
26. **Alcaraz to face Zverev in ATP final** — Turin. Title
    decider at 17:00 GMT. (BBC Sport)
27. **France reach Nations final** — Paris. Beat Argentina; face
    South Africa next. (BBC Sport)
28. **Arsenal held 2-2** — Newcastle. Leaders miss the chance to
    go eight clear. (Reuters)
29. **Leeds stun Chelsea 4-1** — London. First win at Stamford
    Bridge since 1999. (AFP)
30. **Man City held 1-1 by Fulham** — Manchester. Ends a run of
    three straight defeats. (Reuters)
31. **Liverpool host Man Utd today** — Liverpool. Kick-off 16:30
    GMT at Anfield; Pochettino's United debut. (Al Jazeera)
32. **Fred Nile, ex-NSW MP, dies aged 92** — Sydney. NSW's
    longest-serving parliamentarian. (ABC)
33. **Tankers struck near the strait** — Hormuz. Two tankers hit;
    oil holds near $90. (Argus)
34. **Houthi missiles downed over city** — Riyadh. Three ballistic
    missiles intercepted. (LivingRuntime)
35. **UN weapons talks end with no deal** — Geneva. No consensus
    on autonomous weapons rules. (LivingRuntime)
36. **Summit backs Ukraine talks** — Berlin. Coalition of the
    Willing; EU proposes a €45bn loan for 2027. (112.ua)
37. **EU proposes 3% digital tax** — Brussels. Budget plan cut by
    €204bn; France and Germany split. (RFI)
38. **France protests enter 4th weekend** — Paris. Thousands march
    over living costs. (Euronews)
39. **Norway voids disputed oil licences** — Oslo. Supreme court
    rules the licences invalid. (C54 News)
40. **Denmark expels Russian attaché** — Copenhagen. Expelled over
    an alleged assassination plot. (Euronews)

## Notes

- Of v2's 40 stories, 37 are kept. Dropped: the Peru earthquake,
  the Russian missile landing in Poland and the Shenzhen trilateral
  (all other days' news, now named in the DATE CHECK box), plus
  the DAX week and Harden's 51-point NBA game (cut for space).
- Added for v3 and verified in news search dated 22 Nov 2026:
  COP31 (Reuters), the Bahrain US-bases claim (Al Jazeera),
  Hong Kong's Election Committee vote (China Daily), Liverpool v
  Manchester United (Al Jazeera), Eisenkot's Likud invitation
  (France 24), and Fred Nile's death (ABC).
- Could not verify, left out: reports of Jensen Huang's
  resignation (conflicting with other reporting).
