#!/usr/bin/env python3
"""
make.fun bounty: Sum up 22 November's world news in one image
https://make.fun/bounty/news-image-20261122

v5 — "THE WORLD IN ONE DAY": a dense one-page newspaper front
page for Sunday 22 November 2026 — 40 verified stories across
7 regions, in the structure the leaderboard's top entries
share: top bar, serif masthead, number strip, region bar, UTC
timeline, three illustrated lead stories, ten smaller
illustrated stories, a world map with numbered pins, a numbered
list of the remaining stories, a date-check box and a sources
line. See README.md for the story list with a source per story.

v5 combines v3 (dev rate 0.984446, 12-0) and v4 (dev rate
0.983404, 12-0): v4's polished small illustrations, reputable
sources and expanded DATE CHECK, plus richer, more detailed
lead illustrations in the style of the #1 entry, and the
strongest v3 "also on Sunday" stories restored with reputable
outlets (Hegseth's Caracas pact — AP; FinCEN cuts off MEXC —
CoinDesk; Norway voids oil licences — Reuters; Duplex in
Gemini — Google). DRC Ebola stays out: it could not be
corroborated.

The entry image is held in this repository at
output/entry.png (drawn once from the verified stories with
Pillow and bundled fonts in fonts/). This program copies those
exact bytes to /output/entry.png, using only the Python
standard library.

Why a copy, not a draw: the grading sandbox runs
`python3 -P -s /bot/main.py` in a plain Python 3.13 image with
no network, as user 65534 on a read-only /bot. It has no Pillow
and /bot cannot be written to, so a program that draws with
Pillow or writes under /bot exits 1 there. Copying the image
the repository already holds is the approach the bounty rules
name as the simplest entry, and it is deterministic: two runs
write the same bytes.

Output: MAKEFUN_OUTPUT_DIR/entry.png when that environment
variable is set (the sandbox sets it to /output), else
/output/entry.png when /output exists, else output/entry.png
next to this file (local runs only).
"""

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "output" / "entry.png"


def pick_dest():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir) / "entry.png"
    if Path("/output").is_dir():
        return Path("/output") / "entry.png"
    return ROOT / "output" / "entry.png"


def main():
    if not SRC.is_file():
        raise SystemExit(f"missing entry image: {SRC}")
    dest = pick_dest()
    if dest.resolve() == SRC.resolve():
        print(f"entry image already at {dest} ({SRC.stat().st_size} bytes)")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
