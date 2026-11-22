#!/usr/bin/env python3
"""
make.fun bounty: Sum up 22 November's world news in one image
https://make.fun/bounty/news-image-20261122

The entry image is the 1024x1024 news front page for Sunday
22 November 2026 — 40 verified stories in a dense grid — held
in this repository at output/entry.png (rendered from the
verified stories listed in README.md). This program copies
those exact bytes to /output/entry.png, using only the Python
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
