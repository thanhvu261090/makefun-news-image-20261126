#!/usr/bin/env python3
"""Draw 'The World Today' front page for Thursday 26 November 2026.

One deterministic program: fixed headlines, fixed DejaVu fonts, no
network, no clock, no randomness. Two runs write byte-identical PNGs.
The image goes to $MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png),
with a best-effort copy beside this file for local runs.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
if not os.path.isdir(OUT_DIR):
    OUT_DIR = HERE
OUT = os.path.join(OUT_DIR, "entry.png")

W, H = 1024, 1024
M = 46                      # page margin
R = W - M                   # right edge
PAPER = (247, 242, 230)
INK = (18, 18, 18)
RED = (158, 22, 22)
GREY = (104, 98, 88)
FAINT = (196, 188, 172)
NAVY = (24, 42, 64)
BLUE = (36, 84, 138)
GOLD = (168, 122, 30)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy wrap of text to the given pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if not cur or draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, width, text, fnt, leading, fill=INK):
    """Draw a wrapped paragraph; return the y just below it."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, weight=1, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=weight)


def centred(draw, y, text, fnt, fill=INK):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size + 4


def image_summary(img):
    """Return a short report on the finished front page."""
    return f"{img.size[0]}x{img.size[1]} {img.mode}"


def tariff_bars(draw, x, y, width):
    """Horizontal bars: the tariff rates at the heart of the lead story."""
    rows = [("INDIA — AS PROPOSED", 25, RED),
            ("INDIA — IF A DEAL IS STRUCK", 17, BLUE),
            ("CHINA — AS PROPOSED", 40, INK)]
    lab = font(SANS_B, 13)
    val = font(SANS_B, 15)
    for label, pct, colour in rows:
        draw.text((x, y), label, font=lab, fill=GREY)
        bar_x = x
        bar_y = y + 20
        bar_w = int(width * pct / 45.0)
        draw.rectangle([bar_x, bar_y, bar_x + width, bar_y + 16],
                       outline=FAINT, width=1)
        draw.rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + 16], fill=colour)
        draw.text((bar_x + bar_w + 8, bar_y - 1), "%d%%" % pct,
                  font=val, fill=colour)
        y = bar_y + 30
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- top strip -------------------------------------------------------
    y = 30
    small = font(SANS_B, 12)
    d.text((M, y), "WORLD NEWS IN ONE PAGE", font=small, fill=GREY)
    tag = "No. 26  ·  PRICE: ONE IMAGE"
    d.text((R - d.textlength(tag, font=small), y), tag, font=small, fill=GREY)
    y += 22
    rule(d, M, R, y, 3)
    y += 10

    # --- masthead --------------------------------------------------------
    y = centred(d, y, "THE WORLD TODAY", font(SERIF_B, 86))
    y -= 2
    rule(d, M, R, y, 1)
    y += 8
    y = centred(d, y, "T H U R S D A Y   2 6   N O V E M B E R   2 0 2 6",
                font(SANS_B, 17), fill=RED)
    y += 2
    rule(d, M, R, y, 3)
    y += 16

    # --- lead story ------------------------------------------------------
    kick = font(SANS_B, 15)
    d.text((M, y), "TRADE  —  THE LEAD STORY", font=kick, fill=RED)
    y += 24
    y = para(d, M, y, R - M, "AMERICA'S NEW TARIFF WALL",
             font(SERIF_B, 52), 58)
    y += 4
    y = para(d, M, y, R - M,
             "Washington unveils a sweeping new tariff plan: duties of up to "
             "25% on Indian goods — cut to 17% if a trade deal is struck — "
             "and as high as 40% on China, redrawing the map of world trade "
             "in a single morning.",
             font(SERIF, 19), 26)
    y += 12
    y = tariff_bars(d, M, y, R - M)
    y += 6
    rule(d, M, R, y, 1)
    y += 14

    # --- two middle stories ----------------------------------------------
    col_w = (R - M - 28) // 2
    d.text((M, y), "BEIJING'S SHANGHAI SHOCK", font=font(SANS_B, 17), fill=INK)
    d.text((M + col_w + 28, y), "THE HUMAN TOLL, COUNTED",
           font=font(SANS_B, 17), fill=INK)
    y += 26
    y1 = para(d, M, y, col_w,
              "China opens a graft investigation into Chen Jining, the "
              "Politburo member who runs Shanghai — a probe that upends the "
              "usual path to the top of Chinese power.",
              font(SERIF, 16), 22)
    y2 = para(d, M + col_w + 28, y, col_w,
              "Russia's own figures show it has lost nearly 500,000 people "
              "in the war in Ukraine — the starkest official toll yet of a "
              "war now deep into its fifth year.",
              font(SERIF, 16), 22)
    y = max(y1, y2) + 12
    rule(d, M, R, y, 1)
    y += 14

    # --- three short stories ----------------------------------------------
    box_w = (R - M - 2 * 24) // 3
    shorts = [
        ("MINES IN THE STRAIT", RED,
         "Oil tankers hit naval mines near the Strait of Hormuz as the "
         "US-Israel-Iran standoff grinds on; India condemns the attack on "
         "a Riyadh tower that injured two Indians."),
        ("A PAY RISE AT LAST", NAVY,
         "Bangladesh raises the minimum wage for garment workers by 36% "
         "after weeks of protests — a win for the millions who stitch the "
         "world's clothes, though many say it is still not enough."),
        ("HOSTAGES FREED", GOLD,
         "Colombian police storm a supermarket and free 20 people held "
         "hostage for 17 hours — ending a siege that gripped the city "
         "through the night."),
    ]
    tops = []
    for i, (head, colour, text) in enumerate(shorts):
        x = M + i * (box_w + 24)
        d.text((x, y), head, font=font(SANS_B, 15), fill=colour)
        tops.append(para(d, x, y + 24, box_w, text, font(SERIF, 14), 19))
    y = max(tops) + 12
    rule(d, M, R, y, 1)
    y += 12

    # --- also today --------------------------------------------------------
    d.text((M, y), "ALSO TODAY", font=font(SANS_B, 15), fill=RED)
    y += 24
    briefs = [
        "A Pakistani astronaut joins China's Shenzhou-24 crew — the first "
        "foreigner aboard the Tiangong space station.",
        "North Korea orders Switzerland to close its newly opened diplomatic "
        "office in Pyongyang.",
        "Nearly 2,000 migrants reach Spain's Canary Islands in a single day — "
        "a record arrival.",
        "India marks Constitution Day; Gukesh plays for the World Chess crown.",
    ]
    for b in briefs:
        y = para(d, M + 16, y, R - M - 16, "•  " + b, font(SERIF, 14), 19)
        y += 2
    y += 4
    rule(d, M, R, y, 1, fill=FAINT)
    y += 8
    foot = font(SANS, 11)
    note = ("Sources: Reuters, AP, SCMP, Manila Times — 26 November 2026.  •  "
            "THE WORLD TODAY is a one-page summary of the day's world news.")
    centred(d, y, note, foot, fill=GREY)

    img.save(OUT, "PNG", optimize=True)
    print("wrote", OUT, image_summary(img))
    if OUT_DIR != HERE:
        try:
            img.save(os.path.join(HERE, "entry.png"), "PNG", optimize=True)
            print("copy", os.path.join(HERE, "entry.png"))
        except OSError:
            pass


if __name__ == "__main__":
    main()
