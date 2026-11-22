#!/usr/bin/env python3
"""
make.fun bounty: Sum up 22 November's world news in one image
https://make.fun/bounty/news-image-20261122

Renders a 1024x1024 news front page to output/entry.png
(and to /output/entry.png when that directory exists, as in the
make.fun grading sandbox).

Deterministic: no network, no random, no clock, no environment
dependence. The same code + the bundled fonts always produce the
same PNG bytes. Run twice and compare hashes to verify.

Python 3.13, Pillow only. Fonts are bundled in fonts/ so the
render is identical on any machine; system DejaVu paths are
only a fallback.
"""

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------- fonts
def load_font(name, size):
    candidates = [
        ROOT / "fonts" / name,
        Path("/usr/share/fonts/truetype/dejavu") / name,
        Path("/usr/share/fonts/truetype/liberation") / name,
    ]
    for path in candidates:
        if path.is_file():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default(size)


TITLE_FONT = lambda s: load_font("DejaVuSerif-Bold.ttf", s)
BOLD = lambda s: load_font("DejaVuSans-Bold.ttf", s)
REG = lambda s: load_font("DejaVuSans.ttf", s)

# ---------------------------------------------------------------- colours
INK = (17, 17, 17)
GREY = (85, 85, 85)
LIGHT_GREY = (238, 238, 238)
RED = (176, 0, 32)
WHITE = (255, 255, 255)
RULE = (200, 200, 200)

# ---------------------------------------------------------------- content
# All stories are the verified 22 Nov 2026 stories from the brief.
# Nothing is invented. Headlines are short and factual; each
# summary is one line of verified fact.
LEAD = {
    "tag": "WAR  •  UKRAINE",
    "headline": "Ukraine hit by largest attack of the year",
    "summary": (
        "110 missiles and 400+ drones in one night. "
        "Zelenskyy called Putin a \u201ckiller\u201d. "
        "A Russian missile violated Polish airspace."
    ),
    "fact": "Lviv strike: at least 2 killed, 10 injured",
}

GRID = [
    {
        "tag": "MIDDLE EAST",
        "headline": "Iran hits US assets; Houthis strike Riyadh",
        "summary": (
            "Iran targeted US military assets and Patriot radars "
            "in Bahrain. Three Houthi ballistic missiles aimed "
            "at Riyadh were intercepted."
        ),
    },
    {
        "tag": "GAZA",
        "headline": "Four nations urge aid into flooded Gaza",
        "summary": (
            "Australia, Canada, Italy and the UK call on Israel "
            "to let aid reach Gaza as flooding worsens."
        ),
    },
    {
        "tag": "POLITICS",
        "headline": "Eisenkot tapped to form Israel government",
        "summary": (
            "President Herzog asked Gadi Eisenkot to form a "
            "government, bypassing Prime Minister Netanyahu."
        ),
    },
    {
        "tag": "ECONOMY",
        "headline": "EU\u2013Indonesia deal ends 10-year wait",
        "summary": (
            "The trade deal eliminates 98.5% of tariffs "
            "after a decade of talks."
        ),
    },
    {
        "tag": "CLIMATE",
        "headline": "COP31 talks deadlocked on fossil fuels",
        "summary": (
            "Climate negotiations stall over fossil fuels "
            "and finance."
        ),
    },
    {
        "tag": "WORLD",
        "headline": "Magnitude 6.8 quake shakes Peru",
        "summary": (
            "A 6.8 earthquake struck the central Andes "
            "and was felt in Lima."
        ),
    },
]

ALSO = [
    {
        "headline": "Google puts Duplex into Gemini Tasks",
        "summary": "AWS launches a KV Cache skill.",
    },
    {
        "headline": "FinCEN flags MEXC over laundering",
        "summary": "Binance may freeze MEXC deposits.",
    },
    {
        "headline": "Norway voids disputed oil licences",
        "summary": "France protests enter a 4th weekend.",
    },
]

# ---------------------------------------------------------------- helpers
def wrap(draw, text, font, max_width):
    """Greedy word wrap measured with the real font. Deterministic."""
    words, lines, current = text.split(), [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, x, y, text, font, max_width, fill, line_h,
                 max_lines=None):
    lines = wrap(draw, text, font, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_h
    return y


def text_h(font):
    ascent, descent = font.getmetrics()
    return ascent + descent


# ---------------------------------------------------------------- render
def render():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    mx = 36                      # side margin
    cw = W - 2 * mx              # content width = 952

    # --- top red bar -------------------------------------------------
    d.rectangle([0, 0, W, 56], fill=RED)
    d.text((mx, 14), "WORLD NEWS", font=BOLD(28), fill=WHITE)
    date = "SUNDAY 22 NOVEMBER 2026"
    d.text((W - mx - d.textlength(date, font=BOLD(22)), 17),
           date, font=BOLD(22), fill=WHITE)

    # --- masthead ----------------------------------------------------
    title = "THE WORLD TODAY"
    tf = TITLE_FONT(62)
    d.text((mx, 72), title, font=tf, fill=INK)
    d.text((mx, 142),
           "The day's world news in one page",
           font=REG(21), fill=GREY)
    d.line([(mx, 176), (W - mx, 176)], fill=INK, width=3)

    # --- lead story: Ukraine ----------------------------------------
    lx, ly, lw, lh = mx, 190, cw, 178
    d.rectangle([lx, ly, lx + lw, ly + lh], outline=INK, width=2)
    d.rectangle([lx, ly, lx + 10, ly + lh], fill=RED)
    px = lx + 26
    y = ly + 14
    d.text((px, y), LEAD["tag"], font=BOLD(18), fill=RED)
    y += 28
    y = draw_wrapped(d, px, y, LEAD["headline"], BOLD(34), lw - 52,
                     INK, 42, max_lines=2)
    y += 4
    y = draw_wrapped(d, px, y, LEAD["summary"], REG(20), lw - 52,
                     INK, 26, max_lines=3)
    d.text((px, ly + lh - 34), LEAD["fact"], font=BOLD(19), fill=RED)

    # --- grid: 2 columns x 3 rows ------------------------------------
    gx, gy = mx, 384
    gutter, row_gap = 20, 14
    cell_w = (cw - gutter) // 2
    cell_h = 150
    for i, story in enumerate(GRID):
        col, row = i % 2, i // 2
        x = gx + col * (cell_w + gutter)
        y = gy + row * (cell_h + row_gap)
        d.line([(x, y), (x + cell_w, y)], fill=INK, width=2)
        y += 10
        d.text((x, y), story["tag"], font=BOLD(15), fill=RED)
        y += 24
        y = draw_wrapped(d, x, y, story["headline"], BOLD(21),
                         cell_w, INK, 26, max_lines=2)
        y += 2
        draw_wrapped(d, x, y, story["summary"], REG(16), cell_w,
                     GREY, 21, max_lines=3)

    # --- also today ---------------------------------------------------
    ax, ay, aw, ah = mx, 878, cw, 104
    d.rectangle([ax, ay, ax + aw, ay + ah], fill=LIGHT_GREY)
    d.text((ax + 16, ay + 8), "ALSO TODAY", font=BOLD(16), fill=RED)
    col_w = (aw - 32 - 2 * 24) // 3
    for i, item in enumerate(ALSO):
        x = ax + 16 + i * (col_w + 24)
        y = ay + 32
        y = draw_wrapped(d, x, y, item["headline"], BOLD(16), col_w,
                         INK, 20, max_lines=2)
        draw_wrapped(d, x, y, item["summary"], REG(15), col_w,
                     GREY, 19, max_lines=2)

    # --- source line --------------------------------------------------
    src = "Sources: verified news reports, 22 November 2026"
    d.text(((W - d.textlength(src, font=REG(14))) // 2, 996),
           src, font=REG(14), fill=GREY)

    return img


def main():
    img = render()
    out_local = ROOT / "output" / "entry.png"
    out_local.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_local, format="PNG", optimize=True)
    # Grading sandbox path, when it exists: write the same bytes.
    sandbox = Path("/output")
    if sandbox.is_dir():
        img.save(sandbox / "entry.png", format="PNG", optimize=True)
    print(f"Wrote {out_local} ({W}x{H})")


if __name__ == "__main__":
    main()
