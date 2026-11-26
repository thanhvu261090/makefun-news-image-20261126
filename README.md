# The World Today — Thursday 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/thanhvu261090/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/thanhvu261090/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

A one-page newspaper front page summing up the world news of
**Thursday 26 November 2026**, rendered as a single 1024×1024 image.

## What is in the picture

- **Lead story — "America's New Tariff Wall":** Washington unveils a
  sweeping new tariff plan — duties of up to 25% on Indian goods, cut to
  17% if a trade deal is struck, and as high as 40% on China. A bar chart
  in the page shows the three rates at a glance.
- **Beijing:** China opens a graft investigation into Chen Jining, the
  Politburo member who runs Shanghai — a probe that upends the usual path
  to the top of Chinese power.
- **The human toll:** Russia's own figures show it has lost nearly
  500,000 people in the war in Ukraine.
- **The Strait:** Oil tankers hit naval mines near the Strait of Hormuz
  as the US-Israel-Iran standoff grinds on; India condemns the attack on
  a Riyadh tower that injured two Indians.
- **A pay rise at last:** Bangladesh raises the minimum wage for garment
  workers by 36% after weeks of protests.
- **Hostages freed:** Colombian police storm a supermarket and free 20
  people held hostage for 17 hours.
- **Also today:** a Pakistani astronaut joins China's Shenzhou-24 crew
  aboard the Tiangong station; North Korea orders Switzerland to close
  its Pyongyang office; nearly 2,000 migrants reach Spain's Canary
  Islands in a single day; India marks Constitution Day; Gukesh plays
  for the World Chess crown.

## How the page is laid out

Masthead first, then the lead story with its tariff bar chart, two
middle stories side by side, three short stories in columns, and a
briefs column at the foot — the shape of a real broadsheet front page,
squeezed onto one square image. Every headline and figure on the page
is a real story from 26 November 2026, checked against the day's
reporting before the page was drawn.

## Run it

```sh
python3 main.py
```

`main.py` draws the front page with Pillow and the DejaVu fonts, using
fixed text only — no network, no clock, no randomness. It writes
`entry.png` (1024×1024, PNG) to `$MAKEFUN_OUTPUT_DIR` (or `/output`,
or the repository directory when neither exists), and two runs write
byte-identical files.

## Entry

- Competition: [news-image-20261126](https://make.fun/bounty/news-image-20261126)
  — "Sum up 26 November's world news in one image", $100 shared by the
  top 50 entries.
- Program: `main.py` (Python 3.13, standard library plus Pillow).
- Output: `entry.png`, 1024×1024 PNG, 118,743 bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=thanhvu261090&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
